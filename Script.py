import os
import pandas as pd
from datetime import datetime, timedelta
import calendar
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to process CSV files
def process_csv(csv_path, existing_table=None):
    try:
        # Read CSV file
        csv_data = pd.read_csv(csv_path)
        csv_data['Agent Name'] = csv_data['Agent Name'].str.strip()

        # Find the row containing "From:" in the first column
        from_row = csv_data[csv_data.iloc[:, 0].str.contains('From:', na=False)]

        # Extract date from the column next to "From:"
        from_date_str = from_row.iloc[0, 1]  # Assuming "From:" is in the first column
        from_date = pd.to_datetime(from_date_str, format='%m/%d/%Y %I:%M %p')

        # Read existing XLSX table as a template if it doesn't exist
        if existing_table is None:
            template_path = os.path.join(os.path.dirname(csv_path), 'template.xlsx')
            template_data = pd.read_excel(template_path)
        else:
            template_data = existing_table.copy()

        # Get the current month and corresponding month name
        current_month = datetime.now().month
        month_name = calendar.month_name[current_month]

        # Check if the current month has 31 days
        if current_month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif current_month in [4, 6, 9, 11]:
            max_days = 30
        else:
            # February: Check for leap year
            year = datetime.now().year
            if calendar.isleap(year):
                max_days = 29
            else:
                max_days = 28

        # Find columns with day numbers greater than the maximum days of the month
        columns_to_delete = [col for col in template_data.columns if 'Date' in str(col) and int(col.split()[-1]) > max_days]

        # Delete columns with day numbers greater than the maximum days of the month
        new_table = template_data.drop(columns=columns_to_delete)

        # Update column headers to correspond to the current month day numbers
        new_column_names = []
        for col in new_table.columns:
            if 'Date' in str(col):
                day_number = int(col.split()[-1])  # Extract day number from the column header
                new_date = f"{month_name} {day_number}"
                new_column_names.append(new_date)
            else:
                new_column_names.append(col)

        # Update column names in the new table
        new_table.columns = new_column_names

        # Iterate over rows in the CSV file and update Total Handled values in the existing table
        for _, row in csv_data.iterrows():
            agent_name = row['Agent Name']
            total_handled = row['Total Handled']
            callback_handled = row['Callback Handled']
            
            # Find the row index corresponding to the agent name in the existing table
            agent_row_index = template_data.index[template_data['Agent Name'] == agent_name]
            
            if not agent_row_index.empty:
                agent_row_index = agent_row_index[0]
                # Update Total Handled value for the corresponding date column
                date_column = f"{month_name} {from_date.day}"
                if date_column in new_table.columns:
                    new_value = float(total_handled) + float(callback_handled)
                    new_table.loc[agent_row_index, date_column] = new_value

        return new_table
    except Exception as e:
        messagebox.showerror("Error", f"Error processing CSV file: {e}")
        return None

# Function to process all CSV files in a directory
def process_csv_directory(csv_directory):
    try:
        # List all files in the directory
        file_names = os.listdir(csv_directory)

        # Filter out CSV files
        csv_files = [file for file in file_names if file.endswith('.csv')]

        # Process each CSV file and concatenate the results
        result_table = None
        for csv_file in csv_files:
            csv_path = os.path.join(csv_directory, csv_file)
            result_table = process_csv(csv_path, existing_table=result_table)

        return result_table
    except Exception as e:
        messagebox.showerror("Error", f"Error processing CSV directory: {e}")
        return None

# Function to handle GUI button click event
def browse_directory():
    try:
        global input_directory
        input_directory = filedialog.askdirectory()
        entry_input.delete(0, tk.END)
        entry_input.insert(0, input_directory)
    except Exception as e:
        messagebox.showerror("Error", f"Error browsing directory: {e}")

def generate_result():
    try:
        if not input_directory:
            messagebox.showerror("Error", "Please select input directory.")
            return
        
        result_table = process_csv_directory(input_directory)
        
        if result_table is None:
            messagebox.showinfo("Information", "No data processed.")
            return
        
        result_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if result_path:
            result_table.to_excel(result_path, index=False)
            messagebox.showinfo("Information", "Result table saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error generating result: {e}")

# Create GUI window
root = tk.Tk()
root.title("CSV Processor")

# Create input directory selection widgets
label_input = tk.Label(root, text="Input Directory:")
label_input.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_input = tk.Entry(root, width=50)
entry_input.grid(row=0, column=1, padx=10, pady=5)

button_browse = tk.Button(root, text="Browse", command=browse_directory)
button_browse.grid(row=0, column=2, padx=5, pady=5)

# Create process button
button_process = tk.Button(root, text="Generate Result", command=generate_result)
button_process.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start GUI event loop
root.mainloop()

