# 📊 Development of an Automated Exploratory Data Analysis & Visualization Dashboard

An interactive, dynamic web-based Data Analytics Portal built with **Streamlit** to streamline data ingestion, preprocessing, and exploratory data analysis (EDA). Developed as part of the **KPITB AI/ML Internship Capstone Framework**, this production-ready tool automates manual data profiling workflows and provides instantaneous visual insights into structured student data.

🚀 **Live Production Link:** [View Dashboard](https://app-data-analysis-tool-hyurro4pwuzfexnwf5hcj7.streamlit.app/)

---

## 🛠️ Core Functional Architecture

*   **Dynamic Data Ingestion:** Supports automated structural parsing for multiple data file extensions (`.csv`, `.xlsx`, `.json`, `.txt`).
*   **Programmatic Data Profiling:** One-click generation of statistical summaries, feature dimension mappings (`df.shape`), and structural metadata types (`df.dtypes`).
*   **Algorithmic Data Wrangling:** Automated data cleaning routines including immediate removal of duplicate rows and dynamic handle filtration for missing values (`df.dropna()`).
*   **Interactive Visual Analytics:** Integrated real-time plotting subsystem using Matplotlib allowing on-the-fly toggling between Bar Charts, Line Plots, Scatter Plots, and Histograms across continuous numeric attributes.

---

## 💻 Technical Stack

*   **Language:** Python 3.10+
*   **Web Framework:** Streamlit
*   **Data Processing:** Pandas, NumPy
*   **Visualization Engine:** Matplotlib

---

## 📂 Project Organization Matrix

```text
├── app.py                   # Main backend application engine and Streamlit layout code
├── student_performance.csv  # Standardized 300-row testing evaluation dataset
├── requirements.txt         # Explicit dependency configuration file 
└── README.md                # Technical project overview and documentation
```
