import pandas as pd
import numpy as np


df = pd.read_csv('../datasets/cleanData/workingDataset.csv')

numeric_cols = ['pPrice', 'rScore']

df.columns = df.columns.str.strip()
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
df[numeric_cols] = df[numeric_cols].astype(float)

df_price = df['pPrice']
df_summary = df['rSummary']
df_summary_text = df['rText']

df_price_lten = df.loc[(df['pPrice'] > 0) & (df['pPrice'] < 9.99), ['pPrice']]
price_arr_lten = np.array(df_price_lten)
sum_price_lten = np.sum(price_arr_lten)

df_price_lten_score = df.loc[(df['pPrice'] > 0) & (df['pPrice'] < 9.99), ['rScore']]
df_pltens = pd.concat([df_price_lten, df_price_lten_score], axis=1)
df_summary_text = pd.concat([df_summary, df_summary_text], axis=1)

prods_lten = len(df_price_lten)

if __name__ == "__main__":
    print(df.columns.tolist())
    print(df_pltens.tail())
    print(df_summary_text.tail())
    print(price_arr_lten)
    print(round(sum_price_lten, 2))
    print(df_price_lten.shape)
    print(prods_lten)