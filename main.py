import pandas as pd

daily_df = pd.read_csv('data/daily_report.csv')

# get totals data of confirmed, deaths, recovered
totals_df = daily_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
totals_df = totals_df.rename(columns={'index': 'condition'})

# get totals of countries of confirmed, deaths, recovered
countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()
