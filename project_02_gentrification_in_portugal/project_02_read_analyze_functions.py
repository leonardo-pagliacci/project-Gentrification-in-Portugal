# Functions

def main(file_path, file_format='csv'):
    """
    Main function to read a CSV or Excel file into a DataFrame and perform analysis.

    Parameters:
    - file_path (str): The path to the file.
    - file_format (str, optional): The file format, either 'csv' or 'excel'. Defaults to 'csv'.

    The function extracts the file name from the path without the extension, reads the file into a
    DataFrame with the same name as the file (without extension), analyzes the DataFrame, and displays
    the standard head of the DataFrame.

    Note: Using the file name as a variable name might lead to confusion, especially if there are spaces
    or special characters in the file name. It's generally recommended to use a more standardized variable name if possible.
    """
    
    # Validate file_format
    if file_format not in ['csv', 'excel']:
        raise ValueError("Invalid file_format. Please choose 'csv' or 'excel'.")

    # Extract the file name from the path without the extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Read the file into a DataFrame with the same name as the file
    if file_format == 'csv':
        globals()[file_name] = pd.read_csv(file_path)
    elif file_format == 'excel':
        globals()[file_name] = pd.read_excel(file_path)
    else:
        raise ValueError("Invalid file_format. Please choose 'csv' or 'excel'.")
    
    # Print the name of the database
    print(f'The database is stored on the "{file_name}" variable')
    print('\n')
    
    # Standardize head
    standard_head(globals()[file_name])

    # Analyze the DataFrame
    analyze_dataframe(globals()[file_name])

def standard_head(df):
    ''' This function modifies the column names: convert to lowercase and replace spaces with underscores'''
    cols = []

    for i in range(len(df.columns)):
        cols.append(df.columns[i].lower().replace(' ','_'))
    df.columns = cols
    
    return df

def analyze_dataframe(df):
    """
    Analyzes a DataFrame by printing unique values for each column,
    checking for null values, and displaying data types.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to be analyzed.
    """

    # Unique values
    for col in df.columns:
        unique_values = df[col].unique()
        print(f"Unique values for {col}:\n{unique_values}\n")

    # Null values
    null_values = df.isnull().sum()
    print("Null values:\n", null_values)

    # Data types
    print("\nData types:")
    display(df.dtypes)

