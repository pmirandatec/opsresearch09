from tabulate import tabulate

jss_data = 'InputPog'
time_limit = '22'
# Generating the table output using tabulate
input_settings = [
    ["Input Instance", "Time Limit"],
    [jss_data, time_limit]
]

# Print the formatted output (just for reference)
print(" \n" + "=" * 25 + "INPUT SETTINGS" + "=" * 25)
print(tabulate(input_settings, headers="firstrow"))

# Create a new Excel workbook and add a worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Input Settings"

# Add the title to the worksheet
ws.append(["", "=" * 25 + "INPUT SETTINGS" + "=" * 25])

# Write the table headers
for row in input_settings:
    ws.append(row)

# Save the workbook to a file
excel_filename = "input_settings.xlsx"
wb.save(excel_filename)

print(f"Data written to {excel_filename}")