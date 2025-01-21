import pandas as pd 

df = pd.read_csv("weather_forecast_data.csv")
df.columns = [i.strip() for i in df.columns]
df["Rain"] = df["Rain"].apply(lambda a: 1 if a.strip().lower()=='rain' else 0)

df.to_excel("Cleaned_data.xlsx",index=False)
print(df.columns)