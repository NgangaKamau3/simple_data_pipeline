import pandas as pd
import os

input_path = os.path.join("/data", "Medicaldataset.csv")
output_path  = os.path.join("/data", "CleanedMedicalData.csv")

def extract_path(path):
	df = pd.read_csv(path)
	print("Data Extraction complete")
	return df

def transform_data(df):
	df_cleaned =df.dropna()
	df_cleaned.columns = [col.strip().lower().replace(" ", "_")]
	print("Data Preparation Complete")
	return df_cleaned

def load_data(df, output_path):
	df.to_csv(output_path, index=False)
	print("Data Loading completed.")

def run_pipeline():
	df_raw = extract_path(input_path)
	df_cleaned = transform_data(df_raw)
	load_data(df_cleaned, output_path)
	print("Data pipeline completed successfully.")

if __name__ == "__main":
	run_pipeline()
