import pandas as pd
import numpy as np
from numpy import nan
from future.builtins.misc import isinstance
from fastjsonschema import indent

file_path = '../UT_data/program_Ford_DCME_metric.xlsx'
new_file_path = '../UT_data/Data_002_temp1.xlsx'
sheet_name = 'HIS (Routines)'

df = pd.read_excel(file_path, sheet_name=sheet_name)

UT_req = [1]

df_fil1 = df[df.iloc[:, 2].isin(UT_req)]
df_fil1 = df_fil1.iloc[:, :2]

df_fil1['C0']='xyz'
df_fil1['C1']='xyz'
df_fil1['CTE']='Not Created'
df_fil1['Code Coverage Status']='abc'
df_fil1['Report Generated']='Not Done'
df_fil1['Backup Saved']='Not Done'

# Drop duplicates and keep the first occurrence
df_fil1['Metric name'] = df_fil1['Metric name'].where(~df_fil1.duplicated(subset=['Metric name']), nan)

# Function to add empty rows
def add_empty_rows(df):
    new_df = pd.DataFrame(columns=df.columns)
    for i in range(len(df)):
        if not pd.isna(df.iloc[i, 0]):
            empty_row = pd.DataFrame([[np.nan] * len(df.columns)], columns=df.columns)
            new_df = pd.concat([new_df, empty_row], ignore_index=True)
            new_df = pd.concat([new_df, empty_row], ignore_index=True)
        new_df = pd.concat([new_df, df.iloc[[i]]], ignore_index=True)
    return new_df

# Apply the function
new_df = add_empty_rows(df_fil1)

for i in range((len(new_df) - 1)):
    new_df.iloc[i,0] = new_df.iloc[(i + 1),0]

for i in range(len(new_df)):
    if isinstance(new_df.iloc[i,0],str):
        ind = 1
    elif i + 1 < len(new_df) and isinstance(new_df.iloc[i + 1, 0], str):
        ind = 0
    else:
        new_df.iloc[i,0] = ind
        ind +=1

new_df.to_excel(new_file_path, index=False)
print("script run completed")
