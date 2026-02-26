# %%
from parsers import PARSERS_PERSONEN, parse_field, clean_field
import pandas as pd


personen_df = pd.read_excel(
    "data/Herrnhuter NaturkundlerInnen.xlsx",
    sheet_name="Personen",
    dtype=str,
    keep_default_na=False,  # do not insert NaN, keep ""
)

# filter and rename cols
personen_df = personen_df.rename(
    columns=lambda c: c.replace("*", "").split("\n")[0].strip()
).filter(items=list(PARSERS_PERSONEN.keys()))

# only eval test persons
test_ids = ["P0010000"]
test_ids = ["P0010000", "P0170000", "P0220000"]
personen_df = personen_df[
    personen_df["ID"].isin(test_ids)
]  # drops rows with matching IDs


def parse_table(df: pd.DataFrame, specs: dict):

    parsed_data = {}
    errors = []
    for row_idx, row in df.iterrows():  # ignore first data row
        person_id = row.get("ID", f"ROW_{row_idx}")
        person_surname = row.get("Name - Nachname(n)", "<unknown>")

        parsed_data[person_id] = {}
        for col_name, spec in specs.items():
            # col_name with spec has to exist in df cols
            if col_name not in df.columns:
                continue

            raw = str(row[col_name])
            clean_raw = clean_field(raw)

            # skip if empty after cleaning
            if not clean_raw:
                continue
            try:
                # codelist = set(spec.codelist) if spec.codelist else None

                parsed_field = parse_field(
                    str(clean_raw),
                    parser=spec.parser,
                    is_list=spec.is_list,
                    codelist=spec.codelist,
                )

                # break col names at "-" and translate into json hierarchy

                keys = [k.strip() for k in col_name.split("-")]

                current_level = parsed_data

                # Traverse/create nested dictionaries
                for key in keys[:-1]:
                    if key not in current_level:
                        current_level[key] = {}
                    current_level = current_level[key]

                # Assign final value
                current_level[keys[-1]] = parsed_field

            except Exception as e:
                error = f"__{person_id} ({person_surname})__, _{col_name}_:\n {e}"
                # print(f"ERROR {error}")
                errors.append(f"- [ ] {error}\n")

    return parsed_data, errors


# --- run  ---
personen, person_errors = parse_table(personen_df, PARSERS_PERSONEN)
with open("todo/person_errors.md", "w", encoding="utf-8") as f:
    f.write("# Parsing Errors\n\n")
    for err in person_errors:
        f.write(err)
# %%
