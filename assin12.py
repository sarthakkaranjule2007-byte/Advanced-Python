import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# 1. Read the Customer Churn Dataset
# -----------------------------------------

df = pd.read_csv("customer_churn.csv")

print("First 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)


# -----------------------------------------
# 2. Check for Missing Values
# -----------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# -----------------------------------------
# 3. Handle Missing Values
# -----------------------------------------

# Convert TotalCharges to numeric
# Invalid/blank values become NaN
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )

# Fill missing numerical values with median
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])


# -----------------------------------------
# 4. Remove Duplicate Records
# -----------------------------------------

print("\nNumber of duplicate records:",
      df.duplicated().sum())

df = df.drop_duplicates()


# -----------------------------------------
# 5. Summary Statistics
# -----------------------------------------

print("\nSummary Statistics:")
print(df.describe())


# -----------------------------------------
# 6. Churn Analysis
# -----------------------------------------

if "Churn" in df.columns:

    print("\nCustomer Churn Count:")
    print(df["Churn"].value_counts())

    print("\nCustomer Churn Percentage:")
    print(df["Churn"].value_counts(normalize=True) * 100)


# -----------------------------------------
# 7. NumPy Statistical Analysis
# -----------------------------------------

if "MonthlyCharges" in df.columns:

    charges = df["MonthlyCharges"].to_numpy()

    print("\nMonthly Charges Analysis:")
    print("Mean     :", np.mean(charges))
    print("Median   :", np.median(charges))
    print("Minimum  :", np.min(charges))
    print("Maximum  :", np.max(charges))
    print("Std Dev  :", np.std(charges))


# -----------------------------------------
# 8. Visualization: Churn Distribution
# -----------------------------------------

if "Churn" in df.columns:

    df["Churn"].value_counts().plot(
        kind="bar",
        title="Customer Churn Distribution"
    )

    plt.xlabel("Churn Status")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 9. Visualization: Monthly Charges
# -----------------------------------------

if "MonthlyCharges" in df.columns:

    plt.hist(
        df["MonthlyCharges"],
        bins=20
    )

    plt.title("Distribution of Monthly Charges")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 10. Tenure vs Churn
# -----------------------------------------

if "Tenure" in df.columns and "Churn" in df.columns:

    df.groupby("Churn")["Tenure"].mean().plot(
        kind="bar",
        title="Average Tenure by Churn Status"
    )

    plt.xlabel("Churn Status")
    plt.ylabel("Average Tenure")
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 11. Monthly Charges vs Churn
# -----------------------------------------

if "MonthlyCharges" in df.columns and "Churn" in df.columns:

    df.groupby("Churn")["MonthlyCharges"].mean().plot(
        kind="bar",
        title="Average Monthly Charges by Churn Status"
    )

    plt.xlabel("Churn Status")
    plt.ylabel("Average Monthly Charges")
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# 12. Correlation Analysis
# -----------------------------------------

numeric_data = df.select_dtypes(include=np.number)

print("\nCorrelation Matrix:")
print(numeric_data.corr())


print("\nEDA Completed Successfully!")