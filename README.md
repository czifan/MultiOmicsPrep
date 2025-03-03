# Multi-Omics Preprocessing Pipeline for Clinical Data

Currently, open-source codebases for prognostic multimodal models (e.g., [MCAT](https://github.com/mahmoodlab/MCAT) and [PORPOISE](https://github.com/mahmoodlab/PORPOISE)) provide preprocessed multi-omics data. However, they do not offer the preprocessing scripts to convert raw data into these processed formats. This omission can make it challenging to adapt these methods to other datasets. This project aims to fill that gap by providing end-to-end preprocessing code that converts raw multi-omics data (including CNV, Mutations, and RNA-Seq) into a form ready for downstream clinical task modeling.

## Data Preparation

Using the TCGA-BRCA dataset as an example, the molecular profile data (mutation status, copy number variation, and RNA-Seq abundance) was downloaded from [cBioPortal](https://www.cbioportal.org/datasets) via this [URL](https://cbioportal-datahub.s3.amazonaws.com/brca_tcga.tar.gz).

## CNV Data Processing

For CNV data, the process uses the `data_cna.txt` file from the downloaded directory. The script `cnv_to_csv.py` is used to process the data. The key steps include:

- **Merging duplicate genes/cases**: using the mean value.
- **Filtering genes with missing expression values**.
- **Saving the processed data as a CSV file**: rows represent cases, and columns represent genes.

The CNV gene data will be saved with the naming format `{gene}_cnv`. Note that this procedure yields over ten thousand genes, whereas prior works (e.g., MCAT and PORPOISE) typically have around two thousand genes—likely due to additional filtering steps such as high-variance gene selection. Contributions to refine this filtering are welcome.

### Usage

```bash
RAW_CNV_FILE=<path_to_data_cna.txt>
SAVE_CNV_FILE=<path_to_save_csv_file>
python cnv_to_csv.py --raw_file $RAW_CNV_FILE --save_file $SAVE_CNV_FILE
```

## RNA-Seq Data Processing

For RNA-Seq data, the pipeline uses the file `data_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt` from the download. The script `mrnaseq_to_csv.py` processes the data with the following steps:

- **Merging duplicate genes/cases**: using the mean value.
- **Filtering out genes with missing expression**.
- **Saving the processed data as a CSV file**: rows represent cases, and columns represent genes.

The RNA Seq data will be saved with the naming format `{gene}_rnaseq`. 

### Usage

```bash
RAW_MRNA_FILE=<path_to_data_mrna_seq_v2_rsem_zscores_ref_diploid_samples.txt>
SAVE_MRNA_FILE=<path_to_save_csv_file>
python mrnaseq_to_csv.py --raw_file $RAW_MRNA_FILE --save_file $SAVE_MRNA_FILE
```

## Mutations Data Processing

At this time, a robust method for processing mutation data has not been identified. Contributions and suggestions from experienced users are highly encouraged to complete this part of the pipeline.

## Acknowledgments

- [MCAT](https://github.com/mahmoodlab/MCAT) 
- [PORPOISE](https://github.com/mahmoodlab/PORPOISE)