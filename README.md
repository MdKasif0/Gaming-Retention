# AI-Based Online Gaming Player Retention Prediction Using Random Forest

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Connected-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An end-to-end Machine Learning system developed for college AI/ML curriculum submission and viva defense. This project analyzes player telemetry and demographics from 40,034 gaming records to forecast player retention risk using an ensemble **Random Forest Classifier** wrapped in a **Streamlit AI web dashboard**.

---

## 📑 Table of Contents
1. [Project Title & Overview](#-project-title--overview)
2. [Problem Statement](#-problem-statement)
3. [Project Objectives](#-project-objectives)
4. [Dataset Description](#-dataset-description)
5. [Discovered Features & Data Dictionary](#-discovered-features--data-dictionary)
6. [Methodology & Retention Proxy Formulation](#-methodology--retention-proxy-formulation)
7. [Data Preprocessing & Leakage Prevention](#-data-preprocessing--leakage-prevention)
8. [Random Forest Algorithm Architecture](#-random-forest-algorithm-architecture)
9. [Hyperparameter Optimization](#-hyperparameter-optimization)
10. [Comprehensive Model Evaluation](#-comprehensive-model-evaluation)
11. [Web Application Architecture & Features](#-web-application-architecture--features)
12. [How to Run the Project](#-how-to-run-the-project)
13. [Limitations & Methodological Disclaimers](#-limitations--methodological-disclaimers)
14. [Future Improvements](#-future-improvements)

---

## 🎮 Project Title & Overview
**"AI-Based Online Gaming Player Retention Prediction Using Random Forest"**

Player retention is the central operational metric in the modern multi-billion-dollar video game and Free-to-Play (F2P) live-service industry. Acquiring a new gamer costs up to **5× to 7× more** than retaining an existing player. This project provides an automated, data-driven framework to intercept disengaged players *before* they permanently churn.

---

## ❓ Problem Statement
Modern video games generate high-velocity telemetry streams capturing session durations, login frequencies, microtransactions, and in-game achievements. However, raw telemetry alone cannot alert community managers and game developers to imminent player drop-off until the player has already abandoned the title. 

Game studios require an interpretable machine learning model that can ingest cross-sectional player telemetry, classify players into **`Retained`** vs. **`At Risk`** cohorts, and quantify the behavioral drivers contributing to churn risk.

---

## 🎯 Project Objectives
1. **Automated Data Discovery:** Scan and ingest the benchmark *Online Gaming Behavior Dataset* dynamically across local and cloud environments (Google Colab).
2. **Operational Target Formulation:** Define and document a scientifically rigorous **Retention Proxy** based on player engagement tiers.
3. **Leakage-Free Feature Engineering:** Construct an scikit-learn `ColumnTransformer` pipeline that handles imputation and categorical encoding exclusively on training splits.
4. **Ensemble Optimization:** Train and tune a **Random Forest Classifier** using 5-Fold Stratified `RandomizedSearchCV` optimized for **F1-score**.
5. **Interpretability & Diagnostics:** Dissect model behavior using Gini impurity rankings, parent feature aggregation, Confusion Matrices, ROC curves, and Precision-Recall curves.
6. **Production Deployment:** Build an interactive, responsive **Streamlit AI Dashboard** (`app.py`) for live player evaluation and viva demonstration.

---

## 📊 Dataset Description
The system is built upon the canonical **Online Gaming Behavior Dataset**:
- **Instances:** `40,034` player records.
- **Attributes:** `13` features (1 unique identifier, 11 behavioral/demographic inputs, 1 engagement tier).
- **Data Integrity:** `0` missing values, `0` duplicate rows.
- **Original Source File:** `online_gaming_behavior_dataset.csv` (preserved 100% untouched).

---

## 🏷️ Discovered Features & Data Dictionary

| Column Name | Data Type | Category | Range / Categories | Operational Significance |
| :--- | :---: | :---: | :---: | :--- |
| `PlayerID` | Integer | Identifier | 9000 – 49033 | Unique sequential ID (**excluded** to prevent data leakage). |
| `Age` | Integer | Demographic | 15 – 49 years (Mean: 31.99) | Player life stage and age cohort. |
| `Gender` | Categorical | Demographic | `Male` (59.8%), `Female` (40.2%) | Demographic representation. |
| `Location` | Categorical | Demographic | `USA` (40.0%), `Europe` (30.0%), `Asia` (20.2%), `Other` (9.8%) | Geographic server region and latency environment. |
| `GameGenre` | Categorical | Behavioral | `Action`, `RPG`, `Simulation`, `Sports`, `Strategy` | Gameplay style preference (~20% evenly distributed). |
| `PlayTimeHours` | Float | Telemetry | 0.0 – 24.0 hrs (Mean: 12.02) | Weekly continuous hours invested in active play. |
| `InGamePurchases` | Binary | Monetization | `0` (79.9%), `1` (20.1%) | Indicates whether player made in-game microtransactions. |
| `GameDifficulty` | Categorical | UX / Mechanics | `Easy` (50.0%), `Medium` (30.0%), `Hard` (20.0%) | Skill challenge level selected by player. |
| `SessionsPerWeek` | Integer | Telemetry | 0 – 19 logins (Mean: 9.47) | Weekly frequency of distinct game sessions. |
| `AvgSessionDurationMinutes` | Integer | Telemetry | 10 – 179 mins (Mean: 94.79) | Average length of an individual gaming session. |
| `PlayerLevel` | Integer | Progression | Level 1 – 99 (Mean: 49.66) | In-game progression and mastery level. |
| `AchievementsUnlocked` | Integer | Gamification | 0 – 49 (Mean: 24.53) | Total in-game milestone achievements completed. |
| **`EngagementLevel`** | Categorical | Target Source | `Medium` (48.4%), `High` (25.8%), `Low` (25.8%) | Categorical engagement tier (used to derive target). |

---

## 📐 Methodology & Retention Proxy Formulation

### Academic Retention Proxy
The benchmark dataset contains cross-sectional player telemetry and **does not contain a longitudinal future churn timestamp** (e.g., return within D1, D7, or D30). To establish an operational supervised ML formulation, we construct a documented retention proxy:

$$\text{RetentionStatus} = \begin{cases} \text{Retained}, & \text{if } \text{EngagementLevel} \in \{\text{'Medium'}, \text{'High'}\} \\ \text{At Risk}, & \text{if } \text{EngagementLevel} = \text{'Low'} \end{cases}$$

$$\text{RetentionTarget} = \begin{cases} 1, & \text{if } \text{RetentionStatus} = \text{'Retained'} \quad (74.21\% \text{ of dataset}) \\ 0, & \text{if } \text{RetentionStatus} = \text{'At Risk'} \quad (25.79\% \text{ of dataset}) \end{cases}$$

### Target Leakage Safeguard
Because `RetentionTarget` is derived mathematically from `EngagementLevel`, the raw column `EngagementLevel` is **strictly excluded** from input features $X$, along with `PlayerID`, `RetentionStatus`, and `RetentionTarget`.

---

## ⚙️ Data Preprocessing & Leakage Prevention

All transformations are encapsulated inside an scikit-learn `ColumnTransformer` fitted **strictly on training splits** ($X_{train}$):
```
ColumnTransformer
 ├── Numerical Pipeline (7 features):
 │    └── SimpleImputer(strategy='median')
 └── Categorical Pipeline (4 features):
      ├── SimpleImputer(strategy='most_frequent')
      └── OneHotEncoder(handle_unknown='ignore', sparse_output=False)
```
- **Why no feature scaling?** Random Forest uses axis-aligned orthogonal decision boundaries; it is strictly invariant to monotonic feature scaling. Omitting `StandardScaler` preserves direct feature interpretability and speeds up inference.
- **One-Hot Encoding Expansion:** Expands 4 categorical features into 14 dummy levels, resulting in **21 total engineered features**.

---

## 🌲 Random Forest Algorithm Architecture
Random Forest is an ensemble meta-estimator that fits multiple decision tree classifiers on various sub-samples of the dataset and uses averaging to improve predictive accuracy and control over-fitting.

### Key Mathematical Mechanics:
1. **Bootstrap Aggregating (Bagging):** Each tree $b \in \{1, \dots, B\}$ is trained on a bootstrap sample $D_b$ drawn with replacement from $X_{train}$.
2. **Feature Subsampling:** At each node split, only a random subset of features $m \le p$ is considered, decorrelating individual trees.
3. **Class Weighting:** `class_weight='balanced'` assigns penalty weights inversely proportional to class frequencies:
   $$w_j = \frac{N}{2 \cdot N_j}$$
   This prevents the majority retained class ($74.2\%$) from overwhelming the at-risk minority class ($25.8\%$).
4. **Ensemble Voting:** Final prediction is obtained by soft probability averaging:
   $$\hat{P}(y=1|x) = \frac{1}{B} \sum_{b=1}^{B} P_b(y=1|x)$$

---

## 🚀 Hyperparameter Optimization

Optimization was conducted using **`RandomizedSearchCV`** across 5 stratified folds:
- **CV Strategy:** `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`
- **Optimization Target:** **F1-Score** (`scoring='f1'`)

| Hyperparameter | Search Space | Optimal Selected Value | Rationale |
| :--- | :---: | :---: | :--- |
| `n_estimators` | `[100, 150, 200, 250]` | **`150`** | Balances ensemble variance reduction and inference latency. |
| `max_depth` | `[10, 15, 20, 25, None]` | **`None`** | Permits deep trees constrained by leaf sample requirements. |
| `min_samples_split` | `[2, 5, 10]` | **`5`** | Requires at least 5 samples to create an internal node. |
| `min_samples_leaf` | `[1, 2, 4]` | **`2`** | Regularizes terminal nodes to prevent memorization. |
| `max_features` | `['sqrt', 'log2', None]` | **`None`** | Considers all features per split for maximal discriminability. |

- **Best 5-Fold Cross-Validation F1-Score:** **`0.9636`** (96.36%)

---

## 📈 Comprehensive Model Evaluation

Evaluated on the **untouched holdout test partition** ($N = 8,007$ players):

### 1. Final Metric Scorecard
| Evaluation Metric | Holdout Test Score | Cross-Validation Score (Mean) |
| :--- | :---: | :---: |
| **Accuracy** | **0.9462** (94.62%) | — |
| **Precision (Retained)** | **0.9655** (96.55%) | — |
| **Recall (Retained)** | **0.9618** (96.18%) | — |
| **F1-Score (Retained)** | **0.9637** (96.37%) | **0.9636** |
| **ROC-AUC Score** | **0.9430** (94.30%) | — |
| **At-Risk Recall (Class 0)** | **0.9012** (90.12%) | — |
| **Macro F1-Score** | **0.9299** | — |

### 2. Holdout Confusion Matrix ($N = 8,007$)
```
                     Predicted At Risk    Predicted Retained
Actual At Risk            1,861 (90.1%)          204 (9.9%)
Actual Retained             227 (3.8%)         5,715 (96.2%)
```
- **90.12% of at-risk players** (1,861 out of 2,065) are correctly intercepted.
- **Low false-positive rate** for at-risk flags ensures active players are rarely miscategorized.

### 3. Top Behavioral Feature Importance (Aggregated View)
Aggregating one-hot encoded levels back into conceptual domain features demonstrates that **session habits dominate demographics**:
1. **`SessionsPerWeek` (42.14%)**: Frequency of weekly logins is the primary retention driver.
2. **`AvgSessionDurationMinutes` (37.35%)**: Session length reflects gameplay immersion.
3. **`PlayerLevel` (5.67%)**: In-game mastery and time investment.
4. **`AchievementsUnlocked` (5.16%)**: Gamification and completionist motivation.
5. **`PlayTimeHours` (3.79%)**: Cumulative weekly playtime.
6. **Demographics & Monetization (< 5% combined)**: Gender, Location, Age, and InGamePurchases play minor secondary roles.

---

## 💻 Web Application Architecture & Features

The Streamlit web application (`app.py`) provides an interactive interface for live retention forecasting:

```
Gaming Retention AI (Streamlit)
 ├── @st.cache_resource ──> Loads models/gaming_retention_model.joblib
 ├── Sidebar: Persona Presets (Veteran, Disengaged, Casual, Custom)
 ├── Player Input Form (Demographics, Telemetry Sliders, Progression)
 ├── Dynamic Inference Engine:
 │    ├── Prediction Banner ("PLAYER LIKELY TO BE RETAINED" vs "PLAYER IS AT RISK")
 │    ├── 4 Metric Cards (Status, Retention %, Risk %, Model Name)
 │    ├── Dual Visual Probability Progress Bars
 │    ├── AI Behavioral Insights (Feature ranking & variance against dataset averages)
 │    └── Model Information & Audit Table
 └── Expandable Viva Defense & Academic Methodology Notes
```

---

## 🛠️ How to Run the Project

### 1. Prerequisites & Environment Setup
Clone this repository and create a virtual environment:
```bash
git clone https://github.com/MdKasif0/Gaming-Retention.git
cd Gaming-Retention

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Streamlit Web Application
Launch the interactive dashboard locally:
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

### 3. Run the Research Notebooks (Local or Google Colab)
The project includes self-contained notebooks organized by CRISP-DM phase:
- **Phase 1:** `notebooks/01_data_understanding_and_inspection.ipynb`
- **Phase 2:** `notebooks/02_preprocessing_and_feature_engineering.ipynb`
- **Phase 3:** `notebooks/03_model_training_and_tuning.ipynb`
- **Phase 4:** `notebooks/04_model_evaluation.ipynb`
- **Master Unified Notebook:** `gaming_retention.ipynb`

To open in Jupyter:
```bash
jupyter notebook gaming_retention.ipynb
```
*Colab Integration:* In Google Colab or Antigravity IDE, select **Kernel** $\rightarrow$ **Connect to Colab** $\rightarrow$ **Auto Connect** to execute with cloud compute.

---

## ⚠️ Limitations & Methodological Disclaimers

### Critical Viva Defense Disclaimers:
1. **Operational Proxy Distinction:**
   > *"This academic model uses `EngagementLevel` as a proxy for retention. Medium and High engagement are classified as Retained, while Low engagement is classified as At Risk. This does not represent a direct measurement of future player churn."*
2. **Synchronous Cross-Sectional Data:** All telemetry variables were recorded concurrently in a single snapshot rather than longitudinal time series with distinct observation and prediction windows.
3. **Genre Behavioral Variations:** Casual players in specific genres (e.g., Simulation) may play few sessions indefinitely without churning, yet are flagged as 'At Risk' due to lower frequency.

---

## 🔮 Future Improvements
1. **Longitudinal Time-Series Tracking:** Incorporate rolling window telemetry (e.g., login velocity over 7, 14, and 30 days) to model churn trajectory over time.
2. **Survival Analysis:** Implement Cox Proportional Hazards or Kaplan-Meier estimators to model *time-to-churn* probabilities.
3. **Automated Interventions:** Connect retention risk predictions to automated in-game reward dispatchers (push notifications, daily login streaks, targeted discounts).
4. **SHAP (SHapley Additive exPlanations):** Integrate TreeSHAP into the Streamlit dashboard to generate individualized waterfall plots for each specific player input.

---

## 👨‍💻 Author & Academic Attribution
- **Author:** Md Kasif Uddin
- **Repository:** [https://github.com/MdKasif0/Gaming-Retention](https://github.com/MdKasif0/Gaming-Retention)
- **Framework:** CRISP-DM (Cross-Industry Standard Process for Data Mining)
