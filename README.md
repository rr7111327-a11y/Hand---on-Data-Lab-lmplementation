# Yuva Intern Task 2 — Hands-On Data Lab Implementation

**Student:** Ramesh Singh  
**Course:** BCA 5th Semester  
**College:** Bhupal Nobles University, Udaipur  

## Project objective
Perform a complete, reproducible data-analysis lab on student-performance practice data using Python, Pandas, NumPy and Matplotlib.

## Dataset note
`data/student_performance_raw.csv` is a synthetic learning dataset generated for this project. It contains 120 fictional records and deliberately includes a few missing/impossible values so the cleaning process can be demonstrated. It is not collected from real students.

## Folder structure
- `main.py` — complete executable analysis program
- `data/student_performance_raw.csv` — source practice dataset
- `outputs/` — generated cleaned data, descriptive statistics, text summary and five charts
- `report/Task2_Report_Ramesh_Singh.docx` — project report

## Run in VS Code
1. Install Python 3.10 or newer.
2. Open this project folder in VS Code.
3. Open Terminal → New Terminal.
4. Run: `python -m pip install -r requirements.txt`
5. Run: `python main.py`
6. Confirm the terminal prints `SUCCESS` and check the `outputs` folder.

On Windows, if `python` does not work, try `py -m pip install -r requirements.txt` and `py main.py`.

## Analysis performed
- Data inspection and missing-value detection
- Invalid attendance-value handling
- Median imputation for missing numeric values
- Descriptive statistics (count, mean, standard deviation, quartiles, min and max)
- Correlation analysis
- Attendance-group comparison
- Five labelled visualizations

## Important interpretation note
Correlation indicates association only. It does not establish that one variable causes a change in another.

## Evidence to add before resubmission
Capture your own screenshots from your computer after running the project:
1. VS Code showing `main.py` and the project folder.
2. Terminal showing the command `python main.py` and the final `SUCCESS` message.
3. `outputs` folder showing all five PNG charts and generated CSV/TXT files.
4. Open each chart (or at least the correlation matrix and two scatter plots) and capture readable screenshots.
5. GitHub repository page showing the uploaded files.

Do not claim screenshots were captured if you have not captured them. Add the screenshots to a folder named `evidence/` in your GitHub repository.
