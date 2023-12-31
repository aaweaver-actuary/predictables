import pandas as pd
from .BaseLookup import BaseLookup
from dataclasses import dataclass


@dataclass
class date_lookup(BaseLookup):
    super().__init__()

    df: pd.DataFrame = None
    name: str = "date"
    description: str = "A lookup table for dates"
    id_column: str = "date_id"
