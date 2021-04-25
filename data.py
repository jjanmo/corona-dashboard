import pandas as pd

conditions = ["confirmed", "deaths", "recovered"]

daily_df = pd.read_csv('data/daily_report.csv')

# 전세계 누적 확진자/사망자/완치자
totals_df = daily_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
totals_df = totals_df.rename(columns={'index': 'condition'})

# 나라별 누적 확진자/사망자/완치자
countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()


# 전세계 날짜별 누적 확진자/사망자/완치자 데이터
def make_global_df():
    def make_df(_condition):
        _df = pd.read_csv(f'data/time_{_condition}.csv')
        _df = _df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name=_condition)
        _df = _df.rename(columns={"index": "date"})
        return _df

    final_df = None
    for condition in conditions:
        df = make_df(condition)
        if final_df is None:
            final_df = df
        else:
            final_df = final_df.merge(df)
    return final_df


# 전세계 날짜별 + 국가별 누적 확진자/사망자/완치자 데이터
def make_country_df(country):
    def make_df(_condition):
        _df = pd.read_csv(f'data/time_{_condition}.csv')
        _df = _df.loc[_df["Country/Region"] == country]
        _df = _df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name=_condition)
        _df = _df.rename(columns={"index": "date"})
        return _df

    final_df = None
    for condition in conditions:
        df = make_df(condition)
        if final_df is None:
            final_df = df
        else:
            final_df = final_df.merge(df)
    return final_df
