import pandas as pd

df = pd.read_csv(r"C:/Users/HP/Desktop/INTERNSHIP TASK/project 1/hourly_raw.csv")
print(df.columns.tolist())
print(df.head())

# hour कॉलम datetime मध्ये रूपांतर
df["hour"] = pd.to_datetime(df["hour"], errors="coerce")



# नवीन कॉलम्स तयार कर
df["day_of_week"] = df["hour"].dt.dayofweek   # 0=Monday … 6=Sunday
df["hour_of_day"] = df["hour"].dt.hour
df["month"] = df["hour"].dt.month

print(df["hour"].head(10))

df["day_of_week"] = df["hour"].dt.dayofweek   # 0=Monday … 6=Sunday
df["hour_of_day"] = df["hour"].dt.hour

pivot = df.pivot_table(
    index="day_of_week",       # rows = weekdays
    columns="hour_of_day",     # columns = hours
    values="demand_kwh",       # aggregate value
    aggfunc="mean"             # average demand
)
print(pivot.head())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,6))
sns.heatmap(pivot, cmap="YlGnBu", annot=False)
plt.title("Average Demand (kWh) by Weekday & Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week (0=Mon ... 6=Sun)")
plt.show()

# Example: Line plot of hourly demand
plt.figure(figsize=(10,5))
df.groupby("hour_of_day")["demand_kwh"].mean().plot(kind="line")
plt.title("Average Demand per Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Avg Demand (kWh)")
plt.show()

import matplotlib.pyplot as plt

# Line chart: Hour of day vs Average demand
line_data = df.groupby("hour_of_day")["demand_kwh"].mean()

plt.figure(figsize=(10,5))
plt.plot(line_data.index, line_data.values, marker="o", linestyle="-", color="b")
plt.title("Average Demand (kWh) by Hour of Day")
plt.xlabel("Hour of Day (0–23)")
plt.ylabel("Average Demand (kWh)")
plt.grid(True)
plt.show()



