
import pandas as pd


def extract_excel(file_path):
    df_extraction = pd.read_excel(file_path)
    return df_extraction


def extract_excel(file_path):
    try:
         
        df_extraction = pd.read_excel(file_path)

        if df_extraction.empty:
            raise ValueError(
                "O DataFrame extraído está vazio. Verifique o arquivo de entrada."
            )
        colunas_esperadas = {
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "UnitPrice",
            "CustomerID",
            "Country"
        }

        colunas_encontradas = set(df_extraction.columns)

        colunas_faltantes = colunas_esperadas - colunas_encontradas
        if colunas_faltantes:
            raise ValueError(
                f"Colunas faltantes no DataFrame extraído: {colunas_faltantes}"
            )
        return df_extraction

    except FileNotFoundError as erro:
        raise FileNotFoundError(
            f"Arquivo não encontrado durante a extração: {file_path}"
        ) from erro