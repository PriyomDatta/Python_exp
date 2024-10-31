import pandas as pd
import os

# Load the Excel file
excel_file = '../UT_data/Data_002_temp1.xlsx'
new_file_path = '../UT_data/Test_Report.pdbx'
#.................................. Functios ..................................
# Define function Seperate_Sheet_Calls
def Seperate_Sheet_Calls(df, sheet_name):
    print(f"Processing sheet: {sheet_name}")
    #Cleaning data
    df = df.iloc[:,:2]
    df_1clean = df.dropna(subset=[df.columns[0],df.columns[1]],how='all')
    folders = ''
    fun_list = []
    for index, row in df_1clean.iterrows():
        if '/' in str(row.iloc[0]):
            formatting_and_saving(folders,fun_list)
            fun_list =[]
            path_string = str(row.iloc[0])
            folders = path_string.split('/')
        else:
            fun_list.append(str(row.iloc[1]))
    
    formatting_and_saving(folders,fun_list)

    #if(sheet_name == 'E_abchjk'):
    #    print(df_1clean)

def formatting_and_saving(folders,fun_list):
    print(folders)
    if os.path.exists(new_file_path):
        nested_structure = build_folder_structure(folders, fun_list)
        with open(new_file_path, 'a') as f:  
            f.write(nested_structure)
    else:
        nested_structure = build_folder_structure(folders, fun_list)
        with open(new_file_path, 'w') as f:  
            f.write(nested_structure)

# Step 4: Recursive function to create the nested folder structure
def build_folder_structure(folders, test_data=None):
    if not folders:
        # When we reach the deepest folder, add the test data if provided
        if test_data:
            test_elements = ''.join([f'<Test = "{data}"/>\n' for data in test_data])
            return test_elements  # Add test data inside the deepest folder
        return ''  # Base case: no more folders to process
    
    current_folder = folders[0]
    rest_folders = folders[1:]  # Remaining folders

    # Create current folder and recursively add the rest as nested folders
    return f'<folder = "{current_folder}">\n' + \
           build_folder_structure(rest_folders, test_data) + \
           f'</folder>\n'
#.................................. Program Starts ..................................

# Use the ExcelFile object to load all sheet names
xls = pd.ExcelFile(excel_file)

# Create a dictionary to store the DataFrames
dfs = {}
# List to store sheet names
sheet_names = []

# Loop through each sheet name and read it into a DataFrame
for sheet_name in xls.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    dfs[sheet_name] = df
    sheet_names.append(sheet_name)
    # Call function Seperate_Sheet_Calls with DataFrame and sheet name
    Seperate_Sheet_Calls(df, sheet_name)

# Now you have a dictionary of DataFrames and a list of sheet names
#print(sheet_names)
