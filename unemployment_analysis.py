import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print(df.head())

# ======================
# State-wise Analysis
# ======================

state_data = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print(state_data.sort_values(ascending=False).head(10))

# ======================
# Graph 1
# ======================

plt.figure(figsize=(10,8))
state_data.sort_values().plot(kind='barh')
plt.title("Average Unemployment Rate by State")
plt.xlabel("Unemployment Rate (%)")
plt.show()

# ==========================
# COVID ANALYSIS
# ==========================

before_covid = df[df['Date'] < '2020-03-01']
during_covid = df[df['Date'] >= '2020-03-01']

before_avg = before_covid['Estimated Unemployment Rate (%)'].mean()
during_avg = during_covid['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Before Covid:", round(before_avg, 2))
print("Average Unemployment During Covid:", round(during_avg, 2))

# ==========================
# GRAPH 2 - COVID IMPACT
# ==========================

plt.figure(figsize=(6,5))
plt.bar(
    ['Before Covid', 'During Covid'],
    [before_avg, during_avg]
)

plt.title("Impact of Covid on Unemployment")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ==========================
# GRAPH 3 - TOP 10 STATES
# ==========================

top10 = state_data.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top10.plot(kind='bar')

plt.title("Top 10 States with Highest Unemployment")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ==========================
# GRAPH 4 - DISTRIBUTION
# ==========================

plt.figure(figsize=(8,5))
plt.hist(df['Estimated Unemployment Rate (%)'], bins=20)

plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY")