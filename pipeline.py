from src.extract import extract_excel
from src.transform import transform_data
from src.load import load_parquet



def main():
    # Extract data from Excel
    excel_file_path = "data/raw/Online-Retail.xlsx"
    dados_extraidos = extract_excel(excel_file_path)

    # Transform the extracted data
    dados_transformados = transform_data(dados_extraidos)

    # Load the transformed data into Parquet format
    parquet_file_path = "data/processed/online_retail.parquet"
    load_parquet(dados_transformados, parquet_file_path)

if __name__ == "__main__":
    main()