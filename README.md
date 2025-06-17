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

- 🔁 Pushed tracked datasets via `dvc push` and committed `.dvc` files.

---

## ✅ Task 3: Hypothesis Testing – Validating Risk Drivers

### Goals:
- Quantify the statistical impact of features on claim metrics.
- Confirm or reject segmentation strategies using hypothesis testing.

### Methodology:
- 📊 Metrics analyzed:
- **Claim Frequency** = % of policyholders with ≥1 claim.
- **Claim Severity** = Avg claim value for claimants.
- **Margin** = `TotalPremium - TotalClaims`
- 🧪 Statistical Tests:
- `t-test`, `z-test` for margin/severity
- `chi-square` for claim frequency comparisons
- 🧩 Null Hypotheses Tested:
1. No risk difference across provinces ✅ Rejected
2. No risk difference between zip codes ✅ Mixed outcomes
3. No margin difference across zip codes ✅ Rejected for outliers
4. No risk difference between Women and Men ✅ Rejected (p = 0.03)

### Business Insights:
- Gauteng and Western Cape show significant loss ratio differences → pricing should reflect regional risk.
- Gender-based segmentation might enhance profitability.
- Zip codes with high margins or claims require individualized treatment in pricing.

---

## ✅ Task 4: Statistical Modeling & Risk-Based Premium Optimization

### Goals:
1. **Risk Model** – Predict claim amount (`TotalClaims`) for policies with claims.
2. **Pricing Model** – Predict risk-adjusted premium using customer, car, and location features.

### Models Implemented:
- 🔍 **Regression Models**:
- Linear Regression
- Decision Tree
- Random Forest
- XGBoost

- 🧪 **Evaluation Metrics**:
- RMSE & R² (for claim severity)
- Accuracy, Precision, Recall, F1 (for binary classification of claim occurrence)

| Model             | RMSE   | R²      |
|------------------|--------|---------|
| XGBoost          | 680.85 | 0.8888  |
| Random Forest    | 620.35 | 0.9077  |
| Decision Tree    | 719.16 | 0.8759  |

- ✅ **Best Model:** Random Forest Regressor (lowest RMSE)

### Model Interpretability:
- Used **SHAP** to identify key drivers of claim amount and premium:
- 🔼 `CustomValueEstimate`, `CapitalOutstanding`, and `Vehicle Model` strongly influence predictions.
- 👤 Gender and province impact binary classification of claim occurrence.
- 💡 Insight: SHAP showed older vehicles = higher expected claims → support age-based pricing.

---

## ⚙️ CI/CD – GitHub Actions

- GitHub Actions pipeline runs notebook validation on push to ensure reproducibility and proper formatting.

---

## 📈 Key Skills Demonstrated

- ✅ Git & GitHub Workflow
- ✅ Exploratory Data Analysis
- ✅ Hypothesis Testing
- ✅ Predictive Modeling & ML Evaluation
- ✅ SHAP Explainability
- ✅ Reproducibility via DVC
- ✅ CI/CD Integration

---

## 🧰 Technologies

- Python 3.10+
- Pandas, Seaborn, Matplotlib
- Scikit-learn, XGBoost, SHAP
- DVC (Data Version Control)
- Git & GitHub

---

## 🔍 Project Objective

To build a reliable pipeline for analyzing auto insurance claim data:
- Understand risk patterns via EDA and testing
- Predict financial risk and recommend optimized premiums
- Deliver actionable insights for marketing and pricing strategies

---

## 📁 Project Structure
\`\`\`
End-to-End-Insurance-Risk-Analytics-Predictive-Modelin/
│
├── data/
│   ├── raw/                     # Original input data
│   └── clean/                   # Cleaned/preprocessed datasets
│   └── .dvc/                    # DVC metadata
├── notebooks/
  ├──task-1 and 2
│   ├── data_convert_load.ipynb   
  ├──task 3          # Initial data loading & transformation
│   ├── AB_Hypothesis_Testing.ipynb 
  ├──task 4        # Statistical Testing and Risk Segmentation
│   └── predicitive_models.ipynb       # choosing features to use in the model
    └── claim_pridiction.ipynb       # Modeling and SHAP Explainability
├── src/
│   ├── visualization.py         # EDA and plot utilities
│   ├── LossRatio.py             # Loss ratio calculator
│   ├── temporal_trends.py       # Monthly trend analysis
│   ├── statistical_methods.py   # t-test, chi-square, etc.
│   └── predictive_models.py        # for prediciton model
├── .gitignore
├── requirements.txt
└── README.md
└── dvc.yml!
└── dvcignore

\`\`\`

---

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
jupyter notebook notebooks/data_convert_load.ipynb
\`\`\`
"""

# Save as README.md
readme_path = Path("/mnt/data/README.md")
readme_path.write_text(readme_content.strip())
readme_path.name

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



