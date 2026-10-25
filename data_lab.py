"""
Yuva Intern - Hands-On Data Lab Implementation
Run: python data_lab.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "student_performance.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def main():
    print("=== Hands-On Data Lab Implementation ===")
    df = pd.read_csv(DATA)
    print("\n1) Raw dataset preview:")
    print(df.head())
    print("\nRaw shape:", df.shape)
    print("\nMissing values before cleaning:\n", df.isna().sum())

    # Remove exact duplicate records and duplicate student IDs (keep first).
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=["Student_ID"], keep="first")

    # Fill missing numeric values using each column's median.
    for col in ["Study_Hours", "Attendance_Percent", "Previous_Score", "Final_Score"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    # Basic data-quality validation.
    df["Attendance_Percent"] = df["Attendance_Percent"].clip(0, 100)
    for col in ["Previous_Score", "Final_Score"]:
        df[col] = df[col].clip(0, 100)
    df["Study_Hours"] = df["Study_Hours"].clip(lower=0)

    print("\n2) Cleaned data preview:")
    print(df.head())
    print("\nCleaned shape:", df.shape)
    print("\nMissing values after cleaning:\n", df.isna().sum())

    # Pandas and NumPy examples.
    df["Score_Change"] = df["Final_Score"] - df["Previous_Score"]
    print("\n3) Average final score:", round(df["Final_Score"].mean(), 2))
    print("Median study hours:", round(df["Study_Hours"].median(), 2))
    print("\nDescriptive statistics:\n", df[["Study_Hours", "Attendance_Percent", "Previous_Score", "Final_Score"]].describe().round(2))
    print("\nCorrelation matrix:\n", df[["Study_Hours", "Attendance_Percent", "Previous_Score", "Final_Score"]].corr().round(2))
    print("\nStudents grouped by department:\n", df.groupby("Department")["Final_Score"].agg(["count", "mean"]).round(2))

    sns.set_theme(style="whitegrid")
    plots = [
        ("bar_average_score_by_department.png", "bar"),
        ("line_student_scores.png", "line"),
        ("hist_final_score.png", "hist"),
        ("scatter_study_vs_score.png", "scatter"),
        ("box_final_score_department.png", "box"),
    ]
    # Bar chart
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="Department", y="Final_Score", errorbar=None, color="steelblue")
    plt.title("Average Final Score by Department")
    plt.tight_layout()
    plt.savefig(OUT / plots[0][0], dpi=150)
    plt.close()

    # Line chart
    plt.figure(figsize=(8, 5))
    ordered = df.sort_values("Student_ID")
    plt.plot(ordered["Student_ID"].astype(str), ordered["Final_Score"], marker="o")
    plt.title("Final Score by Student ID")
    plt.xlabel("Student ID")
    plt.ylabel("Final Score")
    plt.tight_layout()
    plt.savefig(OUT / plots[1][0], dpi=150)
    plt.close()

    # Histogram
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="Final_Score", bins=6, kde=True, color="steelblue")
    plt.title("Distribution of Final Scores")
    plt.tight_layout()
    plt.savefig(OUT / plots[2][0], dpi=150)
    plt.close()

    # Scatter plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Study_Hours", y="Final_Score", hue="Department", s=90, palette="deep")
    plt.title("Study Hours vs Final Score")
    plt.tight_layout()
    plt.savefig(OUT / plots[3][0], dpi=150)
    plt.close()

    # Box plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Department", y="Final_Score", color="steelblue")
    plt.title("Final Score Spread by Department")
    plt.tight_layout()
    plt.savefig(OUT / plots[4][0], dpi=150)
    plt.close()

    df.to_csv(OUT / "cleaned_student_performance.csv", index=False)
    print("\n4) Saved five charts and cleaned dataset in the outputs/ folder.")
    print("\n5) Key observations:")
    print("- The department means above show differences in average final scores.")
    print("- The scatter plot helps inspect the relationship between study hours and final score.")
    print("- The correlation matrix summarizes linear relationships; correlation does not prove causation.")
    print("- Missing numeric values were filled with medians, and duplicate student IDs were removed.")
    print("\nProject completed successfully.")

if __name__ == "__main__":
    main()
