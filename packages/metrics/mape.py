import numpy as np
import pandas as pd

def mean_absolute_percentage_error(y_test, y_pred):
    """Calculate the mean absolute percentage error.

    Args:
        y_test (array-like): The actual values.
        y_pred (array-like): The predicted values.

    Returns:
        float: The mean absolute percentage error.
    """
        
    if all([isinstance(y_pred,np.ndarray),isinstance(y_test,np.ndarray)]):
        y_pred = y_pred.reshape(-1)
        y_test = y_test.reshape(-1)

        mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
        return mape
    else: 
        y_pred = np.asarray(y_pred).reshape(-1)
        y_test = np.asarray(y_test).reshape(-1)

        mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
        return mape