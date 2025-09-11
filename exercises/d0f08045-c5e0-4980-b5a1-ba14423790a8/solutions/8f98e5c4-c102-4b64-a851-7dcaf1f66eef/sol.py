import pandas as pd
import numpy as np
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/.tmp"

def applying(path):
    # TODO this is what you need to complete
    df = pd.read_csv(path)

    # --- helpers ---
    def pct_to_float(s):
        return pd.to_numeric(
            s.astype(str)
            .str.replace('%', '', regex=False)
            .str.replace(',', '', regex=False)
            .str.strip(),
            errors='coerce'
        )

    def money_to_num(s):
        return pd.to_numeric(
            s.astype(str).str.replace(r'[^0-9.\-]', '', regex=True),
            errors='coerce'
        )

    # 2) Clean numeric columns
    change_cols = ['1h', '24h', '7d', '30d']
    for c in change_cols:
        if c in df.columns:
            df[c] = pct_to_float(df[c])

    money_cols = ['Price', '24h Volume', 'Market Cap']
    for c in money_cols:
        if c in df.columns:
            df[c] = money_to_num(df[c])

    # Circulating Supply can include text like "BTC"
    if 'Circulating Supply' in df.columns:
        df['Circulating Supply'] = money_to_num(df['Circulating Supply'])

    # 3) Fill missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna("Unknown")

    # 4) Feature engineering
    if {'24h Volume', 'Market Cap'}.issubset(df.columns):
        denom = df['Market Cap'].replace(0, np.nan)
        df['Daily_Volume_to_MarketCap'] = (df['24h Volume'] / denom).replace([np.inf, -np.inf], np.nan)

    if '30d' in df.columns:
        df['Return_30d'] = df['30d'].astype(float)

    if {'24h Volume', 'Circulating Supply'}.issubset(df.columns):
        denom = df['Circulating Supply'].replace(0, np.nan)
        df['Liquidity_Index'] = (df['24h Volume'] / denom).replace([np.inf, -np.inf], np.nan)

    # Optional: final numeric imputation for engineered columns
    for col in ['Daily_Volume_to_MarketCap', 'Liquidity_Index']:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    return df


############## DO NOT TOUCH AREA: START #################
def save_df(df):
    file_path = 'ml_crypto_1_' + str(np.random.randint(1000)) + '.csv'
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == '__main__':
    inp = input()
    df = applying(inp)
    path = save_df(df)
    print(path)
############## DO NOT TOUCH AREA: END ###################
