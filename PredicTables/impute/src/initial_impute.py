from typing import Union

import pandas as pd
import polars as pl

from PredicTables.impute.src.impute_with_median import impute_with_median
from PredicTables.impute.src.impute_with_mode import impute_with_mode
from PredicTables.util import to_pl_lf


def initial_impute(
    df: Union[pl.DataFrame, pd.DataFrame, pl.LazyFrame, pd.Series, pl.Series]
) -> pl.LazyFrame:
    """
    Loop through all the columns in a dataframe and impute missing values with the median or mode depending on the column type.

    Parameters
    ----------
    df : Union[pl.DataFrame, pd.DataFrame, pl.LazyFrame, pd.Series, pl.Series]
        A dataframe. Will be coerced to a polars lazy frame.

    Returns
    -------
    pl.LazyFrame
        A dataframe with missing values imputed with the median or mode from each column.
    """
    df = to_pl_lf(df)

    # Loop through each column and impute with the median or mode
    df = impute_with_median(df)
    df = impute_with_mode(df)
    return df
