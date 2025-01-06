#pip install pandas openpyxl
import pandas as pd

# Function to read the Excel file and print the data in tabular form
def read_excel(file_path):
    try:
        # Read the Excel file
        data = pd.read_excel(file_path)
        
        # Print the data in tabular form
        print("Data from Excel file:")
        print(data)
        
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'example.xlsx' with the path to your Excel file
file_path = 'D:\\2024-25\\even sem\\PPFSD\\Python_practical\\set2.xlsx'
read_excel(file_path)

