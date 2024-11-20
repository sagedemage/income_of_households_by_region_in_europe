"""Perform data cleaning on the original dataset to generate a dataset"""

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

INCOME_OF_HOUSEHOLDS_DATASET = "original_dataset/nama_10r_2hhinc_linear.csv"
PPS_DATASET = "dataset/europe_purchasing_power_standard.csv"
COUNTRY_CODES = "codes/country_geo_codes.csv"

# HU: Hungary
GEO_CODES = ["DE", "ES", "FR"]
UNIT_MEASURE = "PPS_EU27_2020_HAB"
# B5N: Balance of primary incomes/national income, net
NATIONAL_ACCOUNTS_INDICATOR = "B5N"


def get_country_name(df_country_geo_codes: DataFrame, geo_code: str):
    rows = df_country_geo_codes.loc[df_country_geo_codes["Code"] == geo_code]
    row = rows.iloc[0]
    return row["Country"]


def main():
    # 1. Read CSV file
    df_data = pd.read_csv(INCOME_OF_HOUSEHOLDS_DATASET)

    df_country_geo_codes = pd.read_csv(COUNTRY_CODES)

    # 2. Set columns for the written data
    write_data = {
        "Year": [],
        "Purchasing_Power_Standard_B5N": [],
        "Country": [],
    }

    # 3. Filter the data by country and unit measure
    for _, row in df_data.iterrows():
        geo = row["geo"]
        unit = row["unit"]
        year = row["TIME_PERIOD"]
        value = row["OBS_VALUE"]
        na_item = row["na_item"]
        if (
            geo in GEO_CODES
            and unit == UNIT_MEASURE
            and na_item == NATIONAL_ACCOUNTS_INDICATOR
        ):
            country = get_country_name(df_country_geo_codes, geo)
            write_data["Year"].append(year)
            write_data["Country"].append(country)
            write_data["Purchasing_Power_Standard_B5N"].append(value)

    # 4. Write the data to a CSV file
    df_write_data = pd.DataFrame(write_data)
    df_write_data.to_csv(PPS_DATASET, index=False)

    print(f"Written the CSV file to {PPS_DATASET}")


if __name__ == "__main__":
    main()
