# ------------------------------------------------------------
# Step 1: Import libraries
# ------------------------------------------------------------
import csv
import pandas as pd
from tabulate import tabulate

# ------------------------------------------------------------
# Step 2: Define data for each image
# ------------------------------------------------------------
data = [
    [r"C:\Users\lafor\OneDrive\Module 2\MASK_Sk658 Llobe ch010017.jpg", 45, 0.6571054458618164],
    [r"C:\Users\lafor\OneDrive\Module 2\MASK_Sk658 Llobe ch010018.jpg", 60, 0.8045673370361328],
    [r"C:\Users\lafor\OneDrive\Module 2\MASK_Sk658 Llobe ch010019.jpg", 80, 0.7469892501831055],
    [r"C:\Users\lafor\OneDrive\Module 2\MASK_Sk658 Llobe ch010021.jpg", 570, 0.5698204040527344],
    [r"C:\Users\lafor\OneDrive\Module 2\MASK_Sk658 Llobe ch010022.jpg", 955, 0.7903814315795898],
    [r"C:\Users\lafor\OneDrive\Module 2\MASK_Sk658 Llobe ch010023.jpg", 2800, 0.8942604064941406]
]

# ------------------------------------------------------------
# Step 3: Create a DataFrame with proper column headers
# ------------------------------------------------------------
df = pd.DataFrame(data, columns=["Filenames", "Depths", "White percents"])

# ------------------------------------------------------------
# Step 4: Save as a CSV file
# ------------------------------------------------------------
csv_filename = "Percent_White_Pixels.csv"
df.to_csv(csv_filename, index=False)

# ------------------------------------------------------------
# Step 5: Print a neatly formatted table to the terminal
# ------------------------------------------------------------
print("\n✅ CSV file created successfully: 'Percent_White_Pixels.csv'\n")
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
