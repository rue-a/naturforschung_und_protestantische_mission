import pandas as pd
import json

from parsers import clean_field, parse_field


class DomainEncoder(json.JSONEncoder):
    """Automatically serialize domain objects."""

    def default(self, obj):
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        return super().default(obj)


class TableParser:
    def __init__(self, sheet_name, parser_specs, excel_file):
        self.sheet_name = sheet_name
        self.specs = parser_specs
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

            for col_name, spec in self.specs.items():
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

                    keys = [k.strip() for k in col_name.split("-")]

                    level = current_row

                    for key in keys[:-1]:
                        level = level.setdefault(key, {})

                    level[keys[-1]] = parsed_value

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
