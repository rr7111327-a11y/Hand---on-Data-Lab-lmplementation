"""
Yuva Intern Task 2: Hands-On Data Lab Implementation
Run from this folder: python main.py
Dataset is synthetic practice data, not real student records.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "student_performance_raw.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def main():
    print("=" * 65)
    print("YUVA INTERN TASK 2 - HANDS-ON DATA LAB IMPLEMENTATION")
    print("=" * 65)

    df = pd.read_csv(DATA)
    print(f"\n1. DATA LOADED: {df.shape[0]} rows, {df.shape[1]} columns")
    print(df.head().to_string(index=False))

    print("\n2. DATA QUALITY CHECK")
    print("Missing values before cleaning:\n", df.isna().sum())
    duplicate_count = int(df.duplicated().sum())
    print("Duplicate rows before cleaning:", duplicate_count)

    # Remove duplicate records and normalize numeric columns.
    df = df.drop_duplicates().copy()
    numeric_cols = ["Age", "Study_Hours", "Attendance_Percent",
                    "Math_Score", "Science_Score", "English_Score"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fill missing numeric values with the column median.
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Keep values in realistic ranges for this practice dataset.
    df["Attendance_Percent"] = df["Attendance_Percent"].clip(0, 100)
    for col in ["Math_Score", "Science_Score", "English_Score"]:
        df[col] = df[col].clip(0, 100)

    df["Average_Score"] = df[["Math_Score", "Science_Score", "English_Score"]].mean(axis=1).round(2)
    df["Performance_Level"] = np.select(
        [df["Average_Score"] >= 85, df["Average_Score"] >= 70],
        ["Excellent", "Good"], default="Needs Improvement"
    )

    cleaned_path = OUT / "student_performance_cleaned.csv"
    df.to_csv(cleaned_path, index=False)
    print("\n3. CLEANING COMPLETE")
    print(f"Removed duplicate rows: {duplicate_count}")
    print("Missing numeric values filled using column medians.")
    print("Cleaned dataset saved to:", cleaned_path)

    print("\n4. DESCRIPTIVE STATISTICS")
    stats = df[numeric_cols + ["Average_Score"]].describe().round(2)
    stats.to_csv(OUT / "descriptive_statistics.csv")
    print(stats.to_string())

    print("\n5. GROUPING AND AGGREGATION")
    grouped = df.groupby("Performance_Level").agg(
        Student_Count=("Student_ID", "count"),
        Mean_Average_Score=("Average_Score", "mean"),
        Mean_Attendance=("Attendance_Percent", "mean")
    ).round(2)
    grouped.to_csv(OUT / "performance_summary.csv")
    print(grouped.to_string())

    # Visualizations
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Average_Score"], bins=8, kde=True, color="steelblue")
    plt.title("Distribution of Student Average Scores")
    plt.xlabel("Average score")
    plt.tight_layout()
    plt.savefig(OUT / "01_score_distribution.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="Performance_Level", y="Average_Score",
                order=["Needs Improvement", "Good", "Excellent"], errorbar=None, color="steelblue")
    plt.title("Average Score by Performance Level")
    plt.xlabel("Performance level")
    plt.ylabel("Average score")
    plt.tight_layout()
    plt.savefig(OUT / "02_performance_level.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Study_Hours", y="Average_Score", hue="Performance_Level")
    plt.title("Study Hours vs Average Score")
    plt.tight_layout()
    plt.savefig(OUT / "03_study_hours_vs_score.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    corr = df[["Study_Hours", "Attendance_Percent", "Math_Score",
               "Science_Score", "English_Score", "Average_Score"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(OUT / "04_correlation_heatmap.png", dpi=150)
    plt.close()

    subject_means = df[["Math_Score", "Science_Score", "English_Score"]].mean().reset_index()
    subject_means.columns = ["Subject", "Mean_Score"]
    plt.figure(figsize=(8, 5))
    sns.barplot(data=subject_means, x="Subject", y="Mean_Score", errorbar=None, color="steelblue")
    plt.title("Mean Score by Subject")
    plt.ylabel("Mean score")
    plt.tight_layout()
    plt.savefig(OUT / "05_subject_average.png", dpi=150)
    plt.close()

    # A concise evidence file for the report.
    with open(OUT / "key_findings.txt", "w", encoding="utf-8") as f:
        f.write("KEY FINDINGS - SYNTHETIC PRACTICE DATA\n")
        f.write(f"Cleaned student records: {len(df)}\n")
        f.write(f"Average score across all students: {df['Average_Score'].mean():.2f}\n")
        f.write(f"Average attendance: {df['Attendance_Percent'].mean():.2f}%\n")
        f.write(f"Average study hours: {df['Study_Hours'].mean():.2f}\n")
        f.write(f"Top performance level count: {(df['Performance_Level']=='Excellent').sum()}\n")
        f.write("\nThese are descriptive observations from a synthetic learning dataset, not causal conclusions.\n")

    print("\n6. CHARTS CREATED")
    for p in sorted(OUT.glob("*.png")):
        print(" -", p.name)
    print("\n7. TASK COMPLETED. Check the outputs folder for CSV files, charts and findings.")
    print("=" * 65)

if __name__ == "__main__":
    main()
