import pandas as pd

def consolidate_reports(dataframes):
    """ merges all monthly reports into one dataframe."""
    final_df=pd.concat(dataframe,ignore_index=True)

    return final_df
