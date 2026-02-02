import pandas as pd

def format_time(df):
    df = df.copy()
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.strftime('%H:%M')
    return df
