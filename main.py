import pandas as pd

daily_df = pd.read_csv('data/daily_report.csv')

# get totals data of confirmed, deaths, recovered
totals_df = daily_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
totals_df = totals_df.rename(columns={'index': 'condition'})

# get totals of countries of confirmed, deaths, recovered
countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()

# get global totals according to countries
conditions = ["confirmed", "deaths", "recovered"]
final_df = None


def make_global_df(_condition):
    _df = pd.read_csv(f'data/time_{_condition}.csv')
    _df = _df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name=_condition)
    _df = _df.rename(columns={"index": "date"})
    return _df


for condition in conditions:
    df = make_global_df(condition)
    if final_df is None:
        final_df = df
    else:
        final_df = final_df.merge(df)

