"""
Yuva Intern Task 2: Hands-On Data Lab Implementation
Student Performance Analysis using Python, Pandas, NumPy and Matplotlib.

Dataset is synthetic practice data generated for this project; it is NOT real student data.
Run from this folder:
    python -m pip install -r requirements.txt
    python main.py
Outputs are saved in the outputs/ folder.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "student_performance_raw.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def load_and_clean(path):
    data = pd.read_csv(path)
    original_rows = len(data)
    missing_before = data.isna().sum()
    # Convert impossible attendance values to missing; then impute numeric columns by median.
    data.loc[~data["attendance_percent"].between(0, 100), "attendance_percent"] = np.nan
    numeric = data.select_dtypes(include="number").columns
    for col in numeric:
        data[col] = data[col].fillna(data[col].median())
    # Keep score and attendance values within valid limits.
    data["attendance_percent"] = data["attendance_percent"].clip(0, 100)
    data["final_score"] = data["final_score"].clip(0, 100)
    return data, original_rows, missing_before

def save_charts(data):
    plt.figure(figsize=(8, 5))
    plt.hist(data["final_score"], bins=12, edgecolor="black")
    plt.title("Distribution of Final Scores")
    plt.xlabel("Final score")
    plt.ylabel("Number of students")
    plt.tight_layout()
    plt.savefig(OUT / "01_score_distribution.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(data["hours_studied"], data["final_score"], alpha=0.75)
    z = np.polyfit(data["hours_studied"], data["final_score"], 1)
    x = np.linspace(data["hours_studied"].min(), data["hours_studied"].max(), 100)
    plt.plot(x, np.poly1d(z)(x))
    plt.title("Study Hours vs Final Score")
    plt.xlabel("Hours studied")
    plt.ylabel("Final score")
    plt.tight_layout()
    plt.savefig(OUT / "02_study_hours_vs_score.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(data["attendance_percent"], data["final_score"], alpha=0.75)
    z = np.polyfit(data["attendance_percent"], data["final_score"], 1)
    x = np.linspace(data["attendance_percent"].min(), data["attendance_percent"].max(), 100)
    plt.plot(x, np.poly1d(z)(x))
    plt.title("Attendance vs Final Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Final score")
    plt.tight_layout()
    plt.savefig(OUT / "03_attendance_vs_score.png", dpi=160)
    plt.close()

    corr = data.select_dtypes(include="number").corr()
    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar(label="Correlation")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=35, ha="right")
    plt.yticks(range(len(corr.columns)), corr.columns)
    for i in range(len(corr)):
        for j in range(len(corr)):
            plt.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", fontsize=8)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig(OUT / "04_correlation_matrix.png", dpi=160)
    plt.close()

    data["attendance_group"] = pd.cut(
        data["attendance_percent"], bins=[0, 60, 75, 90, 100],
        labels=["Below 60", "60-75", "75-90", "90-100"], include_lowest=True
    )
    group_means = data.groupby("attendance_group", observed=False)["final_score"].mean()
    plt.figure(figsize=(8, 5))
    group_means.plot(kind="bar", edgecolor="black")
    plt.title("Average Final Score by Attendance Group")
    plt.xlabel("Attendance group (%)")
    plt.ylabel("Average final score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUT / "05_attendance_group_comparison.png", dpi=160)
    plt.close()
    return corr, group_means

def main():
    data, row_count, missing_before = load_and_clean(DATA)
    data.to_csv(OUT / "student_performance_cleaned.csv", index=False)
    stats = data[["hours_studied","attendance_percent","assignments_completed","previous_score","final_score"]].describe().round(2)
    stats.to_csv(OUT / "descriptive_statistics.csv")
    corr, group_means = save_charts(data)
    report = [
        "YUVA INTERN TASK 2 - HANDS-ON DATA LAB RESULTS",
        "Dataset: synthetic practice data (not real student records)",
        f"Rows analysed: {len(data)}",
        f"Rows in source file: {row_count}",
        f"Missing values before cleaning: {int(missing_before.sum())}",
        f"Missing values after cleaning: {int(data.isna().sum().sum())}",
        "",
        "DESCRIPTIVE STATISTICS",
        stats.to_string(),
        "",
        "CORRELATION WITH FINAL SCORE",
        corr["final_score"].sort_values(ascending=False).round(3).to_string(),
        "",
        "AVERAGE FINAL SCORE BY ATTENDANCE GROUP",
        group_means.round(2).to_string(),
        "",
        "Interpretation: Correlation describes association, not proof of causation."
    ]
    (OUT / "analysis_summary.txt").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))
    print("\\nSUCCESS: cleaned data, statistics, summary and five charts saved in outputs/")

if __name__ == "__main__":
    main()
