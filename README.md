# End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
Analyze car insurance data to identify low-risk segments, perform A/B hypothesis testing, and build predictive models for claim severity and premium optimization. Includes EDA, statistical testing, machine learning, SHAP explainability, and DVC-based version control

## ✅ Task 1: Git, GitHub & Exploratory Data Analysis (EDA)

### Goals:
- Set up a version-controlled repo with a proper Git branching strategy.
- Understand and summarize key insurance features using EDA.
- Provide statistical insights and visual summaries for actionable decision-making.

### Methodology:
- 📁 Created a GitHub repository with a dedicated `task-1` branch and frequent, descriptive commits.
- 🧪 Used `pandas`, `matplotlib`, and `seaborn` to perform:
  - Descriptive statistics on features like `TotalClaims`, `TotalPremium`, `CustomValueEstimate`.
  - Histograms, bar charts, and box plots to examine distributions and detect outliers.
- 📊 Investigated:
  - Loss Ratio (`TotalClaims / TotalPremium`) segmented by `Province`, `VehicleType`, and `Gender`.
  - Temporal patterns over 18 months and auto make/model effects on claims.
  - Detected skewness, extreme outliers, and claim seasonality.
- ✅ Produced 3 high-impact, visually creative plots summarizing these insights.

---

## ✅ Task 2: Reproducible Data Pipeline with DVC
## 📦 Data Version Control (DVC)

- Project uses DVC to version raw and processed datasets.
- Tracked files:
  - `data/raw/insurance_cleaned.csv`
  - `data/clean/insurance_cleaned_final.csv`
- Data is excluded from Git using `.gitignore` and stored in a local DVC cache.

### Goals:
- Set up **DVC** to version-control datasets and ensure full auditability.
- Configure a local remote storage system for backing up datasets.
## Setup DVC and pull data
!pip install dvc
dvc init
dvc remote add -d localstorage `C:\Users\ABC\Desktop\10Acadamy\week 3\End-to-End-Insurance-Risk-Analytics-Predictive-Modelin\data\dvc_file`
dvc add data/raw/insurance_cleaned.csv
dvc add data/clean/insurance_cleaned_final.csv
git add insurance_cleaned.csv.dvc insurance_cleaned_final.csv.dvc .gitignore
git commit -m "Restart project cleanly: Removed DVC cache and restored source files"
dvc push
### Methodology:
- 🛠️ Installed and initialized `dvc` within the project.
- 🗂️ Created a DVC remote at `C:\Users\ABC\Desktop\10Acadamy\week 3\End-to-End-Insurance-Risk-Analytics-Predictive-Modelin\data\dvc_file`.
- 📥 Tracked datasets via `dvc add`, pushed them with `dvc push`, and committed `.dvc` files to Git.
- 🔁 This ensured that anyone cloning the repo could reproduce the entire workflow via `dvc pull`.

---

## ✅ Task 3: Hypothesis Testing – Validating Risk Drivers

### Goals:
- Statistically validate or reject assumptions about segmentation risk factors and margin differences.
- Guide the future risk segmentation strategy.

### Hypotheses Tested:
1. **H₀: No risk difference across provinces**
2. **H₀: No risk difference between zip codes**
3. **H₀: No margin difference across zip codes**
4. **H₀: No risk difference between Women and Men**

### Methodology:
- 📊 Selected key metrics:
  - **Claim Frequency**: Proportion of policies with at least one claim.
  - **Claim Severity**: Average claim amount (if a claim occurred).
  - **Margin**: `TotalPremium - TotalClaims`
- 🔍 Segmented data using client attributes ensuring comparability.
- 🧠 Performed:
  - `t-test` for numerical comparisons (claim severity, margin).
  - `chi-square` test for categorical proportions (claim frequency).
- 📈 Analyzed p-values and interpreted:
  - Significant differences found in Gender and Province-based risk profiles.
  - Some zip codes had outlier margins and claim behaviors warranting re-segmentation.

---

## ⚙️ CI/CD – GitHub Actions

- Implemented GitHub Actions workflow to validate notebook execution and maintain reproducibility.

---

## 📈 Key Skills Demonstrated

- ✅ Git & GitHub Workflow
- ✅ EDA and data storytelling
- ✅ Statistical testing and hypothesis validation
- ✅ Reproducibility with DVC
- ✅ Automation with GitHub Actions

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
│ └── AB_Hypothesis_Testing.ipynb # Exploratory Data Analysis,A/B testing and stastical analysis
│
├── src/
│ ├── visualization.py # All modular plots
│ ├── LossRatio.py # Loss Ratio calculation utils
│ └── temporal_trends.py # Time-based claim analysis
│ └──stastical_methods.py # Tests
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

