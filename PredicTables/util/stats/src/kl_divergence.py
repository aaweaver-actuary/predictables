from typing import Union

import numpy as np
import pandas as pd
import polars as pl

from PredicTables.util import to_pd_s


def kl_divergence(
    observed: Union[list, pd.Series, pl.Series, np.ndarray],
    modeled: Union[list, pd.Series, pl.Series, np.ndarray],
) -> float:
    """Calculate the KL divergence between two distributions. This function is a wrapper for scipy.stats.entropy.

    Parameters
    ----------
    observed : Union[list, pd.Series, pl.Series, np.ndarray]
        Observed values. Must be the same length as modeled values.
    modeled : Union[list, pd.Series, pl.Series, np.ndarray]
        Modeled values. Must be the same length as observed values.

    Returns
    -------
    float
        KL divergence between the two distributions
    """
    from scipy.stats import entropy

    # Convert to pandas Series
    observed = to_pd_s(observed)
    modeled = to_pd_s(modeled)

    # Calculate KL divergence directly from observed and modeled averages
    return entropy(observed, modeled)
