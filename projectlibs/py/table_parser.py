import pandas as pd
import json

from projectlibs.py.parsers import clean_field, parse_field, flatten_parser_specs


class DomainEncoder(json.JSONEncoder):
    """Automatically serialize domain objects."""

    def default(self, obj):
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        return super().default(obj)


def serialize_typed_value(value):
    if hasattr(value, "to_dict"):
        return value.to_dict()

    if isinstance(value, bool):
        return {
            "type": "Boolean",
            "value": value,
        }

    if isinstance(value, str):
        return {
            "type": "String",
            "value": value,
        }

    if isinstance(value, int):
        return {
            "type": "Integer",
            "value": value,
        }

    if isinstance(value, float):
        return {
            "type": "Decimal",
            "value": value,
        }

    if value is None:
        return {
            "type": "Null",
            "value": None,
        }

    if isinstance(value, (list, tuple)):
        return {
            "type": "List",
            "value": [serialize_typed_value(item) for item in value],
        }

    if isinstance(value, dict):
        if set(value.keys()) == {"values", "source"}:
            return {
                "type": "ComplexType",
                "value": {
                    "values": [serialize_typed_value(item) for item in value["values"]],
                    "source": serialize_typed_value(value["source"]),
                },
            }

        return {
            "type": "Object",
            "value": {key: serialize_typed_value(item) for key, item in value.items()},
        }

    raise TypeError(f"Cannot serialize typed value of type {type(value)!r}")


class TableParser:
    def __init__(self, sheet_name, parser_specs, excel_file):
        self.sheet_name = sheet_name
        self.specs = flatten_parser_specs(parser_specs)
        self.excel_file = excel_file

    # ---------- Loading ----------

    def load(self):

        df = pd.read_excel(
            self.excel_file,
            sheet_name=self.sheet_name,
            dtype=str,
            keep_default_na=False,
        )

        df = df.rename(columns=lambda c: c.replace("*", "").split("\n")[0].strip())

        df = df.filter(items=list(self.specs.keys()))

        return df

    # ---------- Parsing ----------

    def parse(self, df):

        parsed_data = {}
        errors = []

        for row_idx, row in df.iterrows():
            row_id = row.get("ID", f"ROW_{row_idx}")

            parsed_data[row_id] = {}
            current_row = parsed_data[row_id]

            for col_name, (path, spec) in self.specs.items():
                if col_name not in df.columns:
                    continue

                raw = str(row[col_name])
                clean_raw = clean_field(raw)

                if not clean_raw:
                    continue

                try:
                    parsed_value = parse_field(
                        clean_raw,
                        parser=spec.parser,
                        is_list=spec.is_list,
                        codelist=spec.codelist,
                    )

                    level = current_row

                    for key in path[:-1]:
                        level = level.setdefault(key, {})

                    level[path[-1]] = {
                        "excel-column-name": spec.excel_column_name,
                        "label": spec.label,
                        "value": serialize_typed_value(parsed_value),
                    }

                except Exception as e:
                    error = f"__{row_id}, {col_name}__:\n _{e}_"

                    errors.append(
                        f"- [ ] {error}\n> {raw[:250].replace(chr(10), chr(10) + '> ')}\n\n"
                    )

        return parsed_data, errors

    # ---------- Pipeline ----------

    def run(self, output_json, error_file, test_ids=None):

        df = self.load()

        if test_ids:
            df = df[df["ID"].isin(test_ids)]

        parsed, errors = self.parse(df)

        # write errors
        with open(error_file, "w", encoding="utf-8") as f:
            f.write("# Parsing Errors\n\n")
            for err in errors:
                f.write(err)

        # write JSON
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(parsed, f, ensure_ascii=False, indent=4, cls=DomainEncoder)

        return parsed
