# AI-Based Online Gaming Player Retention Prediction Using Random Forest

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E.svg)
![Google Colab](https://img.shields.io/badge/Colab-Connected-F9AB00.svg)

A machine learning project designed to predict player retention and churn risk in online gaming environments using behavioral telemetry, player demographics, and Random Forest classification.

---

## 📌 Project Overview
Player retention is the lifeblood of modern video games and Free-to-Play (F2P) live-service ecosystems. This project models player engagement patterns and predicts **`EngagementLevel`** (`High`, `Medium`, `Low`) based on in-game behavioral metrics.

### Key Objectives
1. **Behavioral Profiling:** Analyze player telemetry including weekly playtime, login frequency, and session length.
2. **Predictive Modeling:** Train a multiclass **Random Forest Classifier** with hyperparameter tuning to forecast retention tiers.
3. **Feature Explainability:** Uncover the most influential drivers of player engagement (Gini importance & SHAP values) to guide player retention strategies.

---

## 📊 Dataset: Online Gaming Behavior Dataset
The dataset contains **40,034 player instances** and **13 attributes** with zero missing values or duplicate records:

| Feature | Type | Description |
| :--- | :---: | :--- |
| `PlayerID` | Identifier | Unique sequential player identifier (excluded from training) |
| `Age` | Demographic | Player age (range: 15–49, mean: 31.99) |
| `Gender` | Demographic | Binary (`Male`: 59.85%, `Female`: 40.15%) |
| `Location` | Demographic | Geographic region (`USA`, `Europe`, `Asia`, `Other`) |
| `GameGenre` | Behavioral | Genre (`Strategy`, `Sports`, `Action`, `RPG`, `Simulation`) |
| `PlayTimeHours` | Telemetry | Weekly continuous playtime in hours (mean: 12.02 hrs) |
| `InGamePurchases` | Monetization | Microtransaction history (`0` = non-buyer, `1` = buyer) |
| `GameDifficulty` | UX | Difficulty setting (`Easy`, `Medium`, `Hard`) |
| `SessionsPerWeek` | Telemetry | Weekly login frequency (range: 0–19 sessions) |
| `AvgSessionDurationMinutes` | Telemetry | Average duration per session in minutes (mean: 94.79 min) |
| `PlayerLevel` | Progression | In-game progression level (range: 1–99) |
| `AchievementsUnlocked` | Gamification | Total achievements earned (range: 0–49) |
| **`EngagementLevel`** | **Target** | Player engagement tier (`Medium`: 48.39%, `High`: 25.82%, `Low`: 25.79%) |

---

## 📁 Project Architecture
```
Gaming Retention/
├── data/
│   └── online_gaming_behavior_dataset.csv     # Local project data folder
├── notebooks/
│   └── 01_data_understanding_and_inspection.ipynb # Phase 1: Discovery & Audit
├── models/                                     # Serialized ML models (.pkl / .joblib)
├── outputs/                                    # Generated figures and evaluation metrics
├── gaming_retention.ipynb                      # Root execution notebook
├── online_gaming_behavior_dataset.csv          # Original benchmark dataset
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Local Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/MdKasif0/Gaming-Retention.git
   cd Gaming-Retention
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/01_data_understanding_and_inspection.ipynb
   ```

### Google Colab Execution
- Connect via the **Antigravity IDE Google Colab Extension** by selecting `Select Kernel` > `Colab` > `Auto Connect`.
- Run all cells sequentially.
