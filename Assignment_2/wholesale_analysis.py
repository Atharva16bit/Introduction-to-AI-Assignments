import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
def display(value):
    print(value.to_string() if hasattr(value, "to_string") else value)

dataset = Path("Wholesale customers data.csv")
if not dataset.exists():
    from google.colab import files
    uploaded = files.upload()
    dataset = Path(next(name for name in uploaded if name.lower().endswith(".csv")))
df = pd.read_csv(dataset)

sns.set_theme(style="whitegrid")

display(df.head())

print("Rows and columns:", df.shape)
print("\nColumn names:", df.columns.tolist())

df.info()

display(df.tail())
display(df.describe())

products = [
    "Fresh", "Milk", "Grocery",
    "Frozen", "Detergents_Paper", "Delicassen"
]

print("Missing values before cleaning:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

df[products] = df[products].fillna(df[products].median())
df = df.dropna(subset=["Channel", "Region"]).copy()

print("\nMissing values after cleaning:")
print(df.isna().sum())

display(df[["Milk", "Grocery"]].head())

display(df.iloc[:5, :4])

display(df.loc[df.index[:5], ["Channel", "Fresh", "Milk"]])

display(df[df["Fresh"] > 20000].head())

display(df.query("Milk > 10000 and Grocery > 10000").head())

display(df.sort_values("Fresh").head())

display(df.sort_values("Fresh", ascending=False).head())

spending = np.array(df[products], dtype=float)

summary = pd.DataFrame({
    "Product": products,
    "Total": np.sum(spending, axis=0),
    "Mean": np.mean(spending, axis=0),
    "Median": np.median(spending, axis=0),
    "Std_dev": np.std(spending, axis=0, ddof=1),
    "Minimum": np.min(spending, axis=0),
    "Maximum": np.max(spending, axis=0)
})

display(summary.round(2))

print("Channel codes:", np.unique(df["Channel"]))
print("Region codes:", np.unique(df["Region"]))

# Total spending for each customer
df["Total_Spending"] = np.sum(spending, axis=1)

highest = np.argmax(df["Total_Spending"].to_numpy())
lowest = np.argmin(df["Total_Spending"].to_numpy())

print("\nCustomer row with highest total spending:")
display(df.iloc[[highest]])

print("Customer row with lowest total spending:")
display(df.iloc[[lowest]])

milk = df["Milk"].to_numpy()
grocery = df["Grocery"].to_numpy()

operations = pd.DataFrame({
    "Milk": milk,
    "Grocery": grocery,
    "Combined": np.add(milk, grocery),
    "Grocery_minus_Milk": np.subtract(grocery, milk),
    "Milk_after_10_percent_increase": np.multiply(milk, 1.10)
})

display(operations.head())

print("Average spending by channel:")
display(df.groupby("Channel")[products].mean().round(2))

print("Average spending by region:")
display(df.groupby("Region")[products].mean().round(2))

print("Channel summary:")
display(
    df.groupby("Channel").agg(
        Customers=("Channel", "size"),
        Average_Total=("Total_Spending", "mean"),
        Total_Spending=("Total_Spending", "sum")
    ).round(2)
)

print("Average grocery spending by region and channel:")
display(
    df.pivot_table(
        values="Grocery",
        index="Region",
        columns="Channel",
        aggfunc="mean"
    ).round(2)
)

average_spending = df[products].mean()

plt.figure(figsize=(9, 4))
plt.bar(average_spending.index, average_spending.values, color="steelblue")

plt.title("Average Spending by Product")
plt.xlabel("Product")
plt.ylabel("Average spending")
plt.xticks(rotation=25)
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

sns.countplot(data=df, x="Channel", ax=axes[0])
axes[0].set_title("Customers by Channel")

sns.histplot(data=df, x="Fresh", bins=30, ax=axes[1])
axes[1].set_title("Distribution of Fresh Spending")

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

sns.scatterplot(
    data=df,
    x="Grocery",
    y="Detergents_Paper",
    hue="Channel",
    palette="Set1",
    ax=axes[0]
)
axes[0].set_title("Grocery and Detergents/Paper Spending")

sns.boxplot(data=df, x="Channel", y="Grocery", ax=axes[1])
axes[1].set_title("Grocery Spending by Channel")

plt.tight_layout()
plt.show()

correlation = df[products].corr()

plt.figure(figsize=(8, 5))
sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Between Product Spending")
plt.tight_layout()
plt.show()