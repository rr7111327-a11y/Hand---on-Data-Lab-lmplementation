# Yuva Intern Task 2 - Hands-On Data Lab Implementation

## Project overview
This project demonstrates a beginner-friendly Data Science workflow using a **synthetic student performance dataset**. It covers data loading, inspection, cleaning, transformation, descriptive statistics, grouping/aggregation and five visualizations.

## Tools
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook (optional)

## Folder structure
- `main.py` - complete runnable analysis
- `data/student_performance_raw.csv` - practice dataset with intentional missing values and a duplicate
- `data_lab.ipynb` - notebook version of the workflow
- `requirements.txt` - required Python libraries
- `outputs/` - generated cleaned data, statistics, summaries, findings and charts (created when you run the program)
- `REPORT_GUIDE.md` - report content and evidence checklist

## Run in VS Code (Windows)
1. Install Python 3.10 or newer and VS Code.
2. Extract this ZIP file.
3. Open VS Code -> File -> Open Folder -> select `Yuva_Intern_Task_2_Hands_On_Data_Lab`.
4. Open Terminal -> New Terminal.
5. Create a virtual environment (recommended): `py -m venv .venv`
6. Activate it: `.venv\\Scripts\\activate`
7. Install libraries: `py -m pip install -r requirements.txt`
8. Run: `py main.py`
9. Wait until `TASK COMPLETED` appears. Open the `outputs` folder to see the generated evidence.

If `py` is not recognized, try `python` in the same commands. If activation is blocked, you can skip activation and run `python -m pip install -r requirements.txt` followed by `python main.py`.

## Notebook
To open the notebook, run `py -m jupyter notebook` in the project terminal and open `data_lab.ipynb`. Select the Python kernel and run cells from top to bottom. The Python script is the reliable alternative if Jupyter is not installed.

## Important
The included dataset is synthetic and intended only for practice. Do not describe it as real institutional student data. Verify the script runs on your own computer and include your actual screenshots in the submission.
