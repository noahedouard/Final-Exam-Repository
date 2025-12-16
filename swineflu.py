## LOAD YOUR DATASET HERE.
import pandas as pd
import matplotlib.pyplot as plt
from main_functions import convert_cumulative_to_SIR   # or wherever your function lives

# 1. Read your Mexican swine flu cumulative case data
df = pd.read_csv("swine_flu_mexico_data_2009_cumulative.csv")

# Ensure date is datetime
df["date"] = pd.to_datetime(df["date"])

# Ensure cumulative column is named correctly for the SIR function
df.rename(columns={"confirmed_cases": "cumulative_cases"}, inplace=True)

# 2. Convert cumulative cases → S, I, R using DAILY infectious period
mexico_population_2009 = 112_000_000       # approx Mexico pop. 2009
infectious_period_days = 8                 # typical H1N1 infectious period (7–9 days)

sir_df = convert_cumulative_to_SIR(
    df,
    date_col="date",
    cumulative_col="cumulative_cases",
    population=mexico_population_2009,
    infectious_period=infectious_period_days
)

print(sir_df.head())

# 3. Plot I(t) alone
plt.figure(figsize=(10, 6))
plt.plot(sir_df["date"], sir_df["I_est"], label="Estimated Infectious I(t)")
plt.xlabel("Date")
plt.ylabel("Estimated Number Infectious")
plt.title("Estimated Infectious Population I(t) for Mexican H1N1 Swine Flu (2009)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

