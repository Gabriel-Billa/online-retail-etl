
import pandas as pd
from pathlib import Path


def load_parquet(df: pd.DataFrame, file_path: str) -> None:


    destino = Path(file_path)

    destino.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(
        destino,
        engine="pyarrow",
        index=False
    )

    print(f"Arquivo Parquet salvo em: {destino}")
