# End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
Analyze car insurance data to identify low-risk segments, perform A/B hypothesis testing, and build predictive models for claim severity and premium optimization. Includes EDA, statistical testing, machine learning, SHAP explainability, and DVC-based version control

---

## ✅ Task 1: Data Cleaning & EDA

**Goals**:
- Remove inconsistencies in date and numeric fields
- Handle missing values in key vehicle and claim columns
- Explore claim distribution, claim frequency, and top-risk segments

**Methods Used**:
- Histograms & boxplots to visualize outliers
- Group-by aggregations on transaction date
- Missing value % computation
- Identification of top/bottom claim models

📝 See: `notebooks/task1_eda.ipynb`

---

## ✅ Task 2: DVC Integration & Modularization

**Goals**:
- Version-control cleaned datasets with DVC
- Modularize visualizations and aggregation logic
- Improve project reproducibility and structure

**Highlights**:
- Created `.dvc` metafiles for raw and cleaned data
- Moved EDA plotting logic into `src/visualization.py`
- Added utility modules like `LossRatio.py` and `temporal_trends.py`

📦 Run `dvc repro` to regenerate the cleaned dataset pipeline if raw files change.

---

## 🧰 Technologies

- Python 3.10+
- Pandas, Seaborn, Matplotlib
- DVC (Data Version Control)
- Git & GitHub


## 🔍 Project Objective

To build a reliable pipeline for analyzing auto insurance claim data:
- Clean and validate raw insurance datasets
- Explore temporal and financial claim patterns
- Track data versions using DVC
- Prepare the data for future modeling and risk prediction

---

## 📁 Project Structure
End-to-End-Insurance-Risk-Analytics-Predictive-Modelin/
│
├── data/
│ ├── raw/ # Original input data
│ └── clean/ # Cleaned/preprocessed datasets
│ |── .dvc/ # DVC metadata folder
├── notebooks/
│ ├── data_convert_load.ipynb # Initial data loading & conversion
│ └── task1_eda.ipynb # Exploratory Data Analysis
│
├── src/
│ ├── visualization.py # All modular plots
│ ├── LossRatio.py # Loss Ratio calculation utils
│ └── temporal_trends.py # Time-based claim analysis
│
├
├── .gitignore
├── README.md
└── requirements.txt

## 🚀 How to Reproduce

```bash
# Step 1: Clone this repo
git clone https://github.com/sumeyaaaa/End-to-End-Insurance-Risk-Analytics-Predictive-Modelin.git
cd End-to-End-Insurance-Risk-Analytics-Predictive-Modelin

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Pull data with DVC
dvc pull

# Step 4: Launch analysis
jupyter notebook notebooks/task1_eda.ipynb

