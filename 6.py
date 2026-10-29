
import pandas as pd
import os

# Step 1: Read the dataset
file_path = input("Enter CSV or Excel file path: ")

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith((".xls", ".xlsx")):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file format!")
    exit()

print("\nOriginal Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# Step 2: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Handle missing values
for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            mode = df[col].mode()
            if not mode.empty:
                df[col] = df[col].fillna(mode[0])
            else:
                df[col] = df[col].fillna("Unknown")

# Step 4: Remove duplicate rows
df = df.drop_duplicates()

# Step 5: Clean column names
df.columns = (
    df.columns.astype(str)
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Step 6: Display cleaned dataset
print("\nPreprocessed Dataset:")
print(df.head())

print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())

print("\nFinal Dataset Shape:", df.shape)

# Step 7: Save cleaned dataset
output_file = "cleaned_data.csv"
df.to_csv(output_file, index=False)

print("\nPreprocessed data saved to:", os.path.abspath(output_file))
