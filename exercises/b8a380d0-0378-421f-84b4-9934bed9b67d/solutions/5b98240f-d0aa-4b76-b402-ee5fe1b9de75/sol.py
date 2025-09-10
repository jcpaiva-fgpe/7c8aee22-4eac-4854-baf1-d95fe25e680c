import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def applying(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)

    # 2) Handle missing data
    numeric_cols = [
        "Avg Temperature (°C)", "CO2 Emissions (Tons/Capita)", "Sea Level Rise (mm)",
        "Rainfall (mm)", "Population", "Renewable Energy (%)",
        "Extreme Weather Events", "Forest Area (%)"
    ]
    # Fill only for columns that actually exist (avoids KeyErrors)
    for col in [c for c in numeric_cols if c in df.columns]:
        df[col] = df[col].fillna(df[col].median())

    # Drop rows with missing Country or Year
    df = df.dropna(subset=["Country", "Year"])

    # 3) Feature engineering
    df["CO2_per_Person"] = df["CO2 Emissions (Tons/Capita)"] * df["Population"]
    df["Sustainability_Index"] = (df["Renewable Energy (%)"] + df["Forest Area (%)"]) / 2

    # 4) Select only the important columns
    df = df[[
        "Country", "Year",
        "Avg Temperature (°C)", "CO2 Emissions (Tons/Capita)", "Population",
        "CO2_per_Person", "Sustainability_Index", "Renewable Energy (%)"
    ]]
    return df


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
