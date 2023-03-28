import numpy as np
import pandas as pd

def ensure_array_order(func):
    def wrapper(y_true, y_pred):
        if isinstance(y_true, pd.DataFrame):
            y_true = y_true.values
        if isinstance(y_pred, pd.DataFrame):
            y_pred = y_pred.values

        return func(y_true, y_pred)

    return wrapper

@ensure_array_order
def mean_absolute_percentage_error2(y_true, y_pred):
    """Calculate the mean absolute percentage error.

    Args:
        y_true (array-like): The actual values.
        y_pred (array-like): The predicted values.

    Returns:
        float: The mean absolute percentage error.
    """
        
    if all([isinstance(y_pred,np.ndarray),isinstance(y_true,np.ndarray)]):
        y_pred = y_pred.reshape(-1)
        y_true = y_true.reshape(-1)

        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        return mape
    else: 
        y_pred = np.asarray(y_pred).reshape(-1)
        y_true = np.asarray(y_true).reshape(-1)

        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        return mape