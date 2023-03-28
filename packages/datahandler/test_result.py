class TestResult:
    """
    A class to store the results of model prediction on test data.

    Args:
        raw_df (pd.DataFrame): The raw dataset. (Not encoded)
        y_pred (dictionay, array-like): The predicted values.
        idx (pd.core.indexes.numeric.Int64Index): The index values for the predicted values.

    Raises:
        ValueError: If the length of `raw_df` and `y_pred` are not equal.
    """

    def __init__(self, raw_df, idx, y_pred):

        self.raw_df = raw_df
        self.y_pred = y_pred
        self.idx = idx


    def to_decode_dataframe(self):

        if isinstance(self.y_pred,dict): 
            test_df = self.raw_df.loc[self.idx].copy()
            for k,val in self.y_pred.items(): 
                test_df[k] = val
            return test_df 
        else: 
            test_df = self.raw_df.loc[self.idx].copy()
            test_df['y_pred'] = self.y_pred 
        
            return test_df 

if __name__ == "__main__":
   print('run main')
