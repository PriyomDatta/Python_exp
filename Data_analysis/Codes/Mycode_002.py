import pandas as pd
import numpy as np
from numpy import nan
from future.builtins.misc import isinstance
from openpyxl import load_workbook
import os

file_path = '../Data/Data_002.xlsx'
new_file_path = '../Data/Data_002_output.xlsx'
sheet_name = 'HIS (Routines)'

#............................. Functions .............................
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

def extract_prefix(s):
    return s.split('/')[0]

def formatting_and_save(df_fil1: pd.DataFrame,chec_string: str) -> pd.DataFrame:
    #Adding extra data as per requirement if MCDC change required
    df_fil1.loc[:,'C0']='xyz'
    df_fil1.loc[:,'C1']='xyz'
    df_fil1.loc[:,'CTE']='Not Created'
    df_fil1.loc[:,'Code Coverage Status']='abc'
    df_fil1.loc[:,'Report Generated']='Not Done'
    df_fil1.loc[:,'Backup Saved']='Not Done'

    # Drop duplicates and keep the first occurrence
    df_fil1['Metric name'] = df_fil1['Metric name'].where(~df_fil1.duplicated(subset=['Metric name']), nan)

    # Apply the function
    new_df = add_empty_rows(df_fil1)

    #Upshift first column
    for i in range((len(new_df) - 1)):
        new_df.iloc[i,0] = new_df.iloc[(i + 1),0]

    #formatting the last [last,0] element
    el_last = len(new_df) - 1
    new_df.iloc[el_last, 0] = np.nan

    #Adding the Si. No.
    for i in range(len(new_df)):
        if isinstance(new_df.iloc[i,0],str):
            ind = 1
        elif i + 1 < len(new_df) and isinstance(new_df.iloc[i + 1, 0], str):
            ind = 0
        else:
            new_df.iloc[i,0] = ind
            ind +=1

    #new_df.to_excel(new_file_path,sheet_name=chec_string, index=False)
    # Check if the file exists
    if os.path.exists(new_file_path):
        print(chec_string)
        append_new_sheet_to_excel(new_df,chec_string)
        print(chec_string)

    else:
        new_df.to_excel(new_file_path, sheet_name=chec_string, index=False)
        print(type(chec_string))
        

def append_new_sheet_to_excel(df: pd.DataFrame, sheet_name: str,):
    try:
        # Open the existing workbook with openpyxl
        book = load_workbook(new_file_path)
        
        # Use pandas ExcelWriter with openpyxl engine, and don't overwrite the existing file
        with pd.ExcelWriter(new_file_path, mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
            writer._book = book  # Use the internal book assignment method
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"Successfully added a new sheet '{sheet_name}' to {file_path}.")
    
    except Exception as e:
        print(f"Error while adding new sheet: {e}")



#............................. Program Starts .............................

df = pd.read_excel(file_path, sheet_name=sheet_name)

UT_req = [1]

df_fil1 = df[df.iloc[:, 2].isin(UT_req)]
df_fil1 = df_fil1.iloc[:, :2]

#Module specific implementation
#Change abc with module name, one at a time
#df_fil1 = df_fil1[df_fil1['Metric name'].str.startswith('abc')]

prefixes = df_fil1['Metric name'].apply(extract_prefix)
prefixes = prefixes.drop_duplicates()

for i in range(len(prefixes)):
    chec_string = prefixes.iloc[i]  # Access the ith element of prefixes
    grouped_data = df_fil1[df_fil1['Metric name'].str.startswith(chec_string)]
    formatting_and_save(grouped_data,chec_string)

#print(grouped_data)
#print(prefixes)

print("script run completed")
