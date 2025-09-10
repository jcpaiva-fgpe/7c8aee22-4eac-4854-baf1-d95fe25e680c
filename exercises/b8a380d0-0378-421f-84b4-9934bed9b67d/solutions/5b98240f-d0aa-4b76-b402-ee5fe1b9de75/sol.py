import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def applying(path):
    # TODO this is what you need to complete
    # TODO this is what you need to complete
    df = pd.read_csv(path)

    num_cols = [
        "Avg Temperature (°C)", "CO2 Emissions (Tons/Capita)", "Sea Level Rise (mm)",
        "Rainfall (mm)", "Population", "Renewable Energy (%)",
        "Extreme Weather Events", "Forest Area (%)"
    ]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df = df.dropna(subset=["Country", "Year"])
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df.dropna(subset=["Year"])
    df["Year"] = df["Year"].astype(int)

    df[num_cols] = df[num_cols].apply(lambda s: s.fillna(s.median()))

    df["CO2_per_Person"] = df["CO2 Emissions (Tons/Capita)"] * df["Population"]
    df["Sustainability_Index"] = (df["Renewable Energy (%)"] + df["Forest Area (%)"]) / 2

    grouped = (
        df.groupby(["Country", "Year"], as_index=False)
          .mean(numeric_only=True)
    )

    grouped = grouped.sort_values(["Country", "Year"]).reset_index(drop=True)
    return grouped


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'ml_climate_1_' + str(np.random.randint(1000)) + '.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = input()
    df = applying(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
