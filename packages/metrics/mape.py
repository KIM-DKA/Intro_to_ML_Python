import numpy as np

def mean_absolute_percentage_error(y_test, y_pred):
    """Calculate the mean absolute percentage error"""
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    return mape