import pandas as pd

from .cts_cts import calc_continuous_continuous_corr
from .cts_bin import calc_continuous_binary_corr
from .cts_cat import calc_continuous_categorical_corr
from .bin_bin import calc_binary_binary_corr
from .bin_cat import calc_binary_categorical_corr
from .cat_cat import calc_categorical_categorical_corr

from PredicTables.util import get_column_dtype, to_pd_df, to_pd_s
from tqdm import tqdm


def predictor_target_corr(X, y):
    X, y = to_pd_df(X), to_pd_s(y)
    X_dtype = [get_column_dtype(X[x0]) for x0 in X.columns.tolist()]
    y_dtype = get_column_dtype(y)

    df = pd.concat([X, y], axis=1)

    output = []
    x_cols = []
    for i, col in tqdm(enumerate(X.columns.tolist()[:10])):
        col = f"{col}_target_corr"
        if X_dtype[i] == "continuous" and y_dtype == "continuous":
            x_cols.append(col)
            output.append(calc_continuous_continuous_corr(df)["target"])
        elif X_dtype[i] == "continuous" and y_dtype == "binary":
            x_cols.append(col)
            output.append(calc_continuous_binary_corr(df)["target"])
        elif X_dtype[i] == "continuous" and y_dtype == "categorical":
            x_cols.append(col)
            output.append(calc_continuous_categorical_corr(df)["target"])
        elif X_dtype[i] == "binary" and y_dtype == "binary":
            x_cols.append(col)
            output.append(calc_binary_binary_corr(df)["target"])
        elif X_dtype[i] == "binary" and y_dtype == "categorical":
            x_cols.append(col)
            output.append(calc_binary_categorical_corr(df)["target"])
        elif X_dtype[i] == "categorical" and y_dtype == "categorical":
            x_cols.append(col)
            output.append(calc_categorical_categorical_corr(df)["target"])
        else:
            print(
                f"Skipping {col} because it is not a valid predictor, having dtype={X_dtype[i]}"
            )

    output = pd.concat(output, axis=1)
    output.columns = x_cols
    output = output.reset_index(drop=True)

    return output
