#!/bin/bash

# # mrnaseq to csv
# RAW_MRNA_FILE="/gpfs/share/home/2201213258/czifan/MCT-Bench/DATA/TCGA-BRCA/brca_tcga/data_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt"
# SAVE_MRNA_FILE="/gpfs/share/home/2201213258/czifan/MCT-Bench/PREPROCESS/PREPROCESSED_DATA/TCGA-BRCA/GENOMIC/mrna.csv"
# python mrnaseq_to_csv.py --raw_file $RAW_MRNA_FILE --save_file $SAVE_MRNA_FILE

# # # cnv to csv
# RAW_CNV_FILE="/gpfs/share/home/2201213258/czifan/MCT-Bench/DATA/TCGA-BRCA/brca_tcga/data_cna.txt"
# SAVE_CNV_FILE="/gpfs/share/home/2201213258/czifan/MCT-Bench/PREPROCESS/PREPROCESSED_DATA/TCGA-BRCA/GENOMIC/cnv.csv"
# python cnv_to_csv.py --raw_file $RAW_CNV_FILE --save_file $SAVE_CNV_FILE 

# mutation to csv
RAW_MUT_FILE="/gpfs/share/home/2201213258/czifan/MCT-Bench/DATA/TCGA-BRCA/brca_tcga/data_mutations.txt"
SAVE_MUT_FILE="/gpfs/share/home/2201213258/czifan/MCT-Bench/PREPROCESS/PREPROCESSED_DATA/TCGA-BRCA/GENOMIC/mutation.csv"
python mutation_to_csv.py --raw_file $RAW_MUT_FILE --save_file $SAVE_MUT_FILE
