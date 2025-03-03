import pandas as pd 
import numpy as np 
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument("--raw_file", type=str, default="None")
parser.add_argument("--save_file", type=str, default="None")
args = parser.parse_args()

data_mrna_seq = pd.read_csv(args.raw_file, sep="\t")
columns = data_mrna_seq.values[:, 0]
my_sample_data_column_names = ["case_id",]
for column in columns:
    my_sample_data_column_names.append(f"{column.upper()}_rnaseq")
my_sample_data = []
for case_id in data_mrna_seq.columns.values[2:]:
    case_sample_data = data_mrna_seq[case_id].values 
    my_sample_data.append([case_id[:-3], *case_sample_data])   
my_sample_data = pd.DataFrame(my_sample_data, columns=my_sample_data_column_names)
my_sample_data = my_sample_data.groupby('case_id').mean()
my_sample_data = my_sample_data.reset_index()

vis_columns = []
duplicate_columns = []
for column in my_sample_data.columns:
    if column in vis_columns:
        duplicate_columns.append(column)
    else:
        vis_columns.append(column)
for column in list(set(duplicate_columns)):
    column_sample_data = my_sample_data[column].values
    my_sample_data = my_sample_data.drop(columns=[column])
    my_sample_data[column] = column_sample_data.mean(axis=1)

missing_value_ratio = my_sample_data.isna().mean()
columns_to_keep = missing_value_ratio[missing_value_ratio <= 0.0].index
my_sample_data = my_sample_data[columns_to_keep]

os.makedirs(os.path.dirname(args.save_file), exist_ok=True)
print(my_sample_data.head())
my_sample_data.to_csv(args.save_file, index=False)