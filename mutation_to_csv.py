import pandas as pd 
import numpy as np 
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument("--raw_file", type=str, default="None")
parser.add_argument("--save_file", type=str, default="None")
args = parser.parse_args()

mutdata = pd.read_csv(args.raw_file, sep="\t")

case_ids = [case_id[:-3] for case_id in list(set(mutdata["Tumor_Sample_Barcode"].values))]
genes = [f"{gene}_mut" for gene in list(set(mutdata["Hugo_Symbol"].values))]

mut_matrix = pd.DataFrame(0, index=case_ids, columns=genes)
mut_matrix.index.name = "case_id"
for idx, row in mutdata.iterrows():
    case_id = row["Tumor_Sample_Barcode"][:-3]
    gene = row["Hugo_Symbol"]+"_mut"
    mut_matrix.loc[case_id, gene] = 1

os.makedirs(os.path.dirname(args.save_file), exist_ok=True)
print(mut_matrix.head())
mut_matrix.to_csv(args.save_file)