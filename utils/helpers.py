# utils/helpers.py
import pandas as pd

def format_time(df):
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.strftime('%H:%M:%S IST')
    return df
