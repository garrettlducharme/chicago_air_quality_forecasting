import numpy as np

def log_trans(y):
    y = np.array(y)
    return np.log10(y + 1)

def inv_log_trans(y):
    y = np.array(y)
    return 10**y - 1

def df_shift(df, n_lags=1, n_obs=1):
    """
    Returns a dataframe with n_lags for all variables and n_obs for the sample value
    """
    n_vars = df.shape[1]
    cols, col_names = [], []
    # lags
    for i in range(n_lags, 0, -1):
        cols.append(df.shift(i))
        col_names += [f'{col} (t-{i})' for col in df.columns]
    # observations
    for i in range(0, n_obs):
        cols.append(df['Sample Value'].shift(-i))
        if i == 0:
            col_names.append('Sample Value (t)')
        else:
            col_names.append(f'Sample Value (t+{i})')
            
    shifted_df = pd.concat(cols, axis=1)
    shifted_df.columns = col_names
    shifted_df.dropna(inplace=True)
    
    return shifted_df

