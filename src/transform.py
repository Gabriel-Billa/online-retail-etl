import pandas as pd
import pathlib as path



def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove linhas completamente duplicadas de um DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que será tratado.

    Returns:
        pd.DataFrame: DataFrame sem registros duplicados.
    """

    quantidade_antes = len(df)

    quantidade_duplicados = df.duplicated().sum()

    df_limpo = df.drop_duplicates().copy()

    quantidade_depois = len(df_limpo)

    print(f"Registros antes: {quantidade_antes}")
    print(f"Duplicados encontrados: {quantidade_duplicados}")
    print(f"Registros depois: {quantidade_depois}")

    return df_limpo

def define_cancelamento(df: pd.DataFrame) -> pd.DataFrame:
    """ Identifica registros cancelados no DataFrame a partir do prefixo "C" no campo "InvoiceNo".
    rgs:
        df (pd.DataFrame): DataFrame que será tratado.

    Returns:
        pd.DataFrame: DataFrame com a coluna is_cancelled.
    """
    df= df.copy()
    df["cancelado"] = (
        df["InvoiceNo"]
        .astype(str)
        .str.startswith("C")
    )
    quantidade_cancelados = df["cancelado"].sum()
    print(f"Quantidade de registros cancelados: {quantidade_cancelados}")
    return df

def define_ajuste_estoque(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["ajuste_estoque"] = (
        (df["Quantity"] <0)
        & (df["cancelado"] == False)
        & (df["UnitPrice"] == 0)
    )
    quantidade_ajustes = df["ajuste_estoque"].sum()
    print(f"Quantidade de registros de ajuste de estoque: {quantidade_ajustes}")
    return df

def define_tipo_transacao(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["tipo_transacao"] = "VENDA"

    # identificar cancelamentos
    df.loc[df["cancelado"], "tipo_transacao"] = "CANCELAMENTO"

    # identificar ajustes de estoque
    df.loc[df["ajuste_estoque"], "tipo_transacao"] = "AJUSTE_DE_ESTOQUE"

    # mostrar quantidade de cada categoria
    print(f"Quantidade de vendas: {df[df['tipo_transacao'] == 'VENDA'].shape[0]}")
    print(f"Quantidade de cancelamentos: {df[df['tipo_transacao'] == 'CANCELAMENTO'].shape[0]}")
    print(f"Quantidade de ajustes de estoque: {df[df['tipo_transacao'] == 'AJUSTE_DE_ESTOQUE'].shape[0]}")

    return df

def calcula_valor_total(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["valor_total"] = df["Quantity"] * df["UnitPrice"]
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = remove_duplicates(df)
    df = define_cancelamento(df)
    df = define_ajuste_estoque(df)
    df = define_tipo_transacao(df)
    df = calcula_valor_total(df)

    return df