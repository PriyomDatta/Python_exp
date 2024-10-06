import pandas as pd

file_path = '../Data/Data_002.xlsx'
new_file_path = '../Data/Data_002_output.xlsx'
sheet_name = 'HIS (Routines)'

df = pd.read_excel(file_path,sheet_name = sheet_name)

#print(df)

UT_req = [1]
empty_row = []

df_fil1 = df[df.iloc[:,2].isin(UT_req)]
df_fil1 = df_fil1.iloc[:,:2]

#print('new data is')
#print(df_fil1)
#We have first two column sorted

# Drop duplicates and keep the first occurrence
df_fil1['metric name'] = df_fil1['metric name'].where(~df_fil1.duplicated(subset=['metric name']), '')


print(df_fil1)

df_fil1.to_excel(new_file_path,index=False)
