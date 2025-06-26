import pandas as pd

def clean_csv(input_file, output_file):
    # Load the CSV file
    df = pd.read_csv(input_file)

    # Drop rows with missing values
    cleaned_df = df.dropna()

    # Save cleaned data to a new CSV
    cleaned_df.to_csv(output_file, index=False)

    print("Cleaning complete. Saved to", output_file)

# Example use
# clean_csv("dirty_data.csv", "clean_data.csv")
