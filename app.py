import os
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==============================================================================
# 1. PAGE CONFIGURATION & STYLING
# ==============================================================================
st.set_page_config(
    page_title="Gaming Retention AI",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for clean, professional college dashboard styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .disclaimer-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 0.9rem 1.2rem;
        border-radius: 4px;
        margin-bottom: 1.5rem;
        font-size: 0.92rem;
        color: #92400E;
    }
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 1.2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #6B7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .metric-val-green {
        font-size: 1.8rem;
        font-weight: 700;
        color: #059669;
        margin-top: 0.3rem;
    }
    .metric-val-red {
        font-size: 1.8rem;
        font-weight: 700;
        color: #DC2626;
        margin-top: 0.3rem;
    }
    .metric-val-blue {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2563EB;
        margin-top: 0.3rem;
    }
    .badge-retained {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-weight: 700;
        font-size: 1.2rem;
        display: inline-block;
        border: 1px solid #10B981;
    }
    .badge-at-risk {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        font-weight: 700;
        font-size: 1.2rem;
        display: inline-block;
        border: 1px solid #EF4444;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1F2937;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
        margin-bottom: 1.0rem;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. MODEL AND METADATA LOADING (CACHED)
# ==============================================================================
@st.cache_resource
def load_assets():
    """
    Loads the serialized Random Forest pipeline and metadata from /models.
    Cached across user interactions to ensure optimal latency.
    """
    model_path = Path("models/gaming_retention_model.joblib")
    metadata_path = Path("models/model_metadata.joblib")
    
    if not model_path.exists() or not metadata_path.exists():
        st.error(f"Required model files missing in {model_path.parent}. Ensure training phase has completed.")
        st.stop()
        
    pipeline = joblib.load(model_path)
    metadata = joblib.load(metadata_path)
    return pipeline, metadata

pipeline, metadata = load_assets()

# Extract model schema from metadata
expected_features = metadata.get("input_features", [])
cat_cols = metadata.get("categorical_features", [])
num_cols = metadata.get("numerical_features", [])

# Categorical options discovered from the Online Gaming Behavior Dataset
CATEGORICAL_OPTIONS = {
    "Gender": ["Male", "Female"],
    "Location": ["USA", "Europe", "Asia", "Other"],
    "GameGenre": ["Action", "RPG", "Simulation", "Sports", "Strategy"],
    "GameDifficulty": ["Easy", "Medium", "Hard"]
}

# Baseline dataset averages for interactive telemetry comparison
DATASET_BENCHMARKS = {
    "PlayTimeHours": 12.02,
    "SessionsPerWeek": 9.47,
    "AvgSessionDurationMinutes": 94.79,
    "PlayerLevel": 49.66,
    "AchievementsUnlocked": 24.53,
    "Age": 31.99
}

# ==============================================================================
# 3. HEADER & METHODOLOGY DISCLAIMER
# ==============================================================================
st.markdown('<div class="main-header">🎮 Gaming Retention AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Based Online Gaming Player Retention Prediction Using Random Forest</div>', unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer-box">
    <strong>⚠️ Important Methodology Disclaimer:</strong><br>
    This academic model uses <code>EngagementLevel</code> as a proxy for retention. 
    <strong>Medium</strong> and <strong>High</strong> engagement are classified as <strong>Retained</strong> (1), while 
    <strong>Low</strong> engagement is classified as <strong>At Risk</strong> (0). 
    This operational definition does not represent a direct longitudinal measurement of future player churn.
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. SIDEBAR CONTROLS & DEMO PRESETS
# ==============================================================================
with st.sidebar:
    st.header("⚙️ Configuration & Presets")
    st.markdown("Select a preset player persona or customize values manually in the main panel.")
    
    preset = st.selectbox(
        "Load Preset Persona (Viva Demo):",
        [
            "Custom Player (Manual Inputs)",
            "Active Veteran Player (High Retention)",
            "Disengaged Casual Player (High Churn Risk)",
            "Weekend Moderate Gamer (Threshold Cohort)"
        ]
    )
    
    st.markdown("---")
    st.markdown("**Project Quick Facts:**")
    st.markdown(f"- **Algorithm:** `{metadata.get('algorithm', 'RandomForestClassifier')}`")
    st.markdown(f"- **Ensemble Size:** `{metadata.get('number_of_trees', 150)} Trees`")
    st.markdown(f"- **Features:** `{len(expected_features)} Input Features`")
    st.markdown(f"- **CV F1-Score:** `{metadata.get('best_cv_f1_score', 0.9636)*100:.2f}%`")
    st.markdown(f"- **Test Accuracy:** `{metadata.get('test_metrics', {}).get('accuracy', 0.9462)*100:.2f}%`")

# Set default values based on selected preset
if preset == "Active Veteran Player (High Retention)":
    default_age = 26
    default_gender = "Female"
    default_location = "USA"
    default_genre = "Action"
    default_playtime = 21.5
    default_purchases = 1
    default_difficulty = "Medium"
    default_sessions = 16
    default_duration = 145
    default_level = 88
    default_achievements = 44
elif preset == "Disengaged Casual Player (High Churn Risk)":
    default_age = 38
    default_gender = "Male"
    default_location = "Europe"
    default_genre = "RPG"
    default_playtime = 3.2
    default_purchases = 0
    default_difficulty = "Hard"
    default_sessions = 2
    default_duration = 35
    default_level = 9
    default_achievements = 4
elif preset == "Weekend Moderate Gamer (Threshold Cohort)":
    default_age = 31
    default_gender = "Male"
    default_location = "Asia"
    default_genre = "Strategy"
    default_playtime = 10.5
    default_purchases = 0
    default_difficulty = "Easy"
    default_sessions = 7
    default_duration = 85
    default_level = 42
    default_achievements = 20
else:
    default_age = 30
    default_gender = "Male"
    default_location = "USA"
    default_genre = "Sports"
    default_playtime = 12.0
    default_purchases = 0
    default_difficulty = "Medium"
    default_sessions = 9
    default_duration = 95
    default_level = 50
    default_achievements = 25

# ==============================================================================
# 5. INPUT SECTION: PLAYER INFORMATION
# ==============================================================================
st.markdown('<div class="section-header">👤 Player Information & Telemetry Inputs</div>', unsafe_allow_html=True)
st.caption("Enter the player's demographic and behavioral metrics to estimate their retention probability.")

with st.form(key="player_prediction_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("1. Demographics & Context")
        age = st.number_input("Player Age", min_value=15, max_value=60, value=default_age, step=1, help="Valid age range between 15 and 60 years.")
        gender = st.selectbox("Gender", options=CATEGORICAL_OPTIONS["Gender"], index=CATEGORICAL_OPTIONS["Gender"].index(default_gender))
        location = st.selectbox("Geographic Location", options=CATEGORICAL_OPTIONS["Location"], index=CATEGORICAL_OPTIONS["Location"].index(default_location))
        game_genre = st.selectbox("Primary Game Genre", options=CATEGORICAL_OPTIONS["GameGenre"], index=CATEGORICAL_OPTIONS["GameGenre"].index(default_genre))

    with col2:
        st.subheader("2. Session Telemetry")
        playtime_hours = st.slider(
            "Weekly Play Time (Hours)", 
            min_value=0.0, max_value=24.0, value=float(default_playtime), step=0.5,
            help="Total cumulative weekly hours spent in active gameplay."
        )
        sessions_per_week = st.slider(
            "Sessions Per Week (Frequency)", 
            min_value=0, max_value=20, value=int(default_sessions), step=1,
            help="Number of distinct game logins per week."
        )
        avg_session_duration = st.slider(
            "Average Session Duration (Minutes)", 
            min_value=10, max_value=180, value=int(default_duration), step=5,
            help="Mean duration of an individual gaming session."
        )

    with col3:
        st.subheader("3. Gameplay & Monetization")
        game_difficulty = st.selectbox("Selected Game Difficulty", options=CATEGORICAL_OPTIONS["GameDifficulty"], index=CATEGORICAL_OPTIONS["GameDifficulty"].index(default_difficulty))
        in_game_purchases = st.radio(
            "In-Game Purchases (Monetization)", 
            options=[0, 1], 
            format_func=lambda x: "Made In-Game Microtransactions (1)" if x == 1 else "No In-Game Purchases (0)",
            index=default_purchases
        )
        player_level = st.number_input("Player Progression Level", min_value=1, max_value=99, value=default_level, step=1, help="In-game account or character level (1 to 99).")
        achievements_unlocked = st.number_input("Achievements Unlocked", min_value=0, max_value=49, value=default_achievements, step=1, help="Total milestone achievements completed (0 to 49).")

    submit_button = st.form_submit_button(
        label="🎯 Predict Player Retention",
        use_container_width=True,
        type="primary"
    )

# ==============================================================================
# 6. INFERENCE & RESULTS DASHBOARD
# ==============================================================================
if submit_button:
    # 1. Assemble input DataFrame matching exact feature order of the training pipeline
    input_dict = {
        "Age": int(age),
        "Gender": str(gender),
        "Location": str(location),
        "GameGenre": str(game_genre),
        "PlayTimeHours": float(playtime_hours),
        "InGamePurchases": int(in_game_purchases),
        "GameDifficulty": str(game_difficulty),
        "SessionsPerWeek": int(sessions_per_week),
        "AvgSessionDurationMinutes": int(avg_session_duration),
        "PlayerLevel": int(player_level),
        "AchievementsUnlocked": int(achievements_unlocked)
    }
    
    # Guarantee identical column sequence
    input_df = pd.DataFrame([input_dict])[expected_features]
    
    # 2. Run inference through saved pipeline
    try:
        prediction = pipeline.predict(input_df)[0]
        prediction_probabilities = pipeline.predict_proba(input_df)[0]
        
        prob_at_risk = float(prediction_probabilities[0]) * 100
        prob_retained = float(prediction_probabilities[1]) * 100
        confidence = max(prob_at_risk, prob_retained)
        
        st.markdown('<div class="section-header">📊 Retention Prediction Dashboard</div>', unsafe_allow_html=True)
        
        # Display primary banner
        if prediction == 1:
            st.markdown(
                '<div style="text-align: center; margin: 1rem 0;">'
                '<span class="badge-retained">✅ PLAYER LIKELY TO BE RETAINED</span>'
                '</div>', 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div style="text-align: center; margin: 1rem 0;">'
                '<span class="badge-at-risk">⚠️ PLAYER IS AT RISK</span>'
                '</div>', 
                unsafe_allow_html=True
            )
        
        # Metric Cards
        card1, card2, card3, card4 = st.columns(4)
        
        with card1:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-title">Model Classification</div>
                <div class="{}">{}</div>
            </div>
            """.format(
                "metric-val-green" if prediction == 1 else "metric-val-red",
                "RETAINED" if prediction == 1 else "AT RISK"
            ), unsafe_allow_html=True)
            
        with card2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Retention Probability</div>
                <div class="metric-val-green">{prob_retained:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)
            
        with card3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Risk Probability</div>
                <div class="metric-val-red">{prob_at_risk:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)
            
        with card4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Prediction Confidence</div>
                <div class="metric-val-blue">{confidence:.1f}%</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Probability Visual Indicator
        st.markdown("**Retention vs. At-Risk Probability Breakdown:**")
        col_bar1, col_bar2 = st.columns([prob_retained, prob_at_risk if prob_at_risk > 0 else 0.01])
        with col_bar1:
            st.progress(prob_retained / 100.0, text=f"Retained Probability: {prob_retained:.1f}%")
        with col_bar2:
            st.progress(prob_at_risk / 100.0, text=f"At-Risk Probability: {prob_at_risk:.1f}%")
            
        # ==============================================================================
        # 7. AI INSIGHTS & TELEMETRY BENCHMARK COMPARISON
        # ==============================================================================
        st.markdown('<div class="section-header">💡 AI Behavioral Insights</div>', unsafe_allow_html=True)
        
        insight_col1, insight_col2 = st.columns([1.2, 1])
        
        with insight_col1:
            st.markdown("### Feature Importance Drivers")
            st.markdown("""
            In our trained **Random Forest** model, behavioral habits vastly outweigh demographic factors:
            1. **Sessions Per Week (`42.1%` Gini Importance):** Login cadence is the strongest behavioral determinant of whether a player remains retained.
            2. **Avg Session Duration (`37.4%` Gini Importance):** Longer, immersive play sessions strongly protect against disengagement.
            3. **Player Progression (`Level` 5.7% + `Achievements` 5.2%):** Unlocking milestones creates psychological sunk-cost commitment.
            4. **Demographics & Monetization (< 5%):** Age, gender, region, and microtransactions have minimal direct influence compared to weekly gameplay rituals.
            """)
            
        with insight_col2:
            st.markdown("### Player Telemetry vs. Dataset Average")
            comparison_df = pd.DataFrame({
                "Metric": ["Sessions / Week", "Session Duration (min)", "Weekly Playtime (hrs)", "Player Level"],
                "Player Value": [sessions_per_week, avg_session_duration, playtime_hours, player_level],
                "Dataset Mean": [
                    DATASET_BENCHMARKS["SessionsPerWeek"],
                    DATASET_BENCHMARKS["AvgSessionDurationMinutes"],
                    DATASET_BENCHMARKS["PlayTimeHours"],
                    DATASET_BENCHMARKS["PlayerLevel"]
                ]
            })
            comparison_df["Variance"] = comparison_df["Player Value"] - comparison_df["Dataset Mean"]
            st.dataframe(
                comparison_df.style.format({
                    "Player Value": "{:.1f}",
                    "Dataset Mean": "{:.1f}",
                    "Variance": "{:+.1f}"
                }),
                use_container_width=True,
                hide_index=True
            )
            
    except Exception as e:
        st.error(f"Inference Error: {str(e)}")

# ==============================================================================
# 8. MODEL INFORMATION & SCIENTIFIC AUDIT
# ==============================================================================
st.markdown('<div class="section-header">🔬 Model Information & Performance Architecture</div>', unsafe_allow_html=True)

m_col1, m_col2 = st.columns(2)

with m_col1:
    st.markdown("### Model Specifications")
    st.markdown(f"""
    - **Supervised Task:** Binary Retention Classification (`0 = At Risk`, `1 = Retained`)
    - **Core Algorithm:** `RandomForestClassifier` (Ensemble Bagging)
    - **Ensemble Size:** `150` Decision Trees
    - **Class Weighting:** `balanced` (mitigates 74.2% vs 25.8% class imbalance)
    - **Input Features:** `11` raw attributes (`7` numerical, `4` categorical)
    - **Engineered Dimensions:** `21` features after One-Hot Encoding
    - **Pipeline Preprocessing:** Integrated `ColumnTransformer` (Median Imputation + OneHotEncoder)
    """)

with m_col2:
    st.markdown("### Holdout Test Set Evaluation ($N = 8,007$)")
    test_metrics = metadata.get("test_metrics", {
        "accuracy": 0.9462,
        "precision": 0.9655,
        "recall": 0.9618,
        "f1_score": 0.9637,
        "roc_auc": 0.9430
    })
    
    perf_table = pd.DataFrame({
        "Evaluation Metric": ["Accuracy", "Precision (Retained)", "Recall (Retained)", "F1-Score", "ROC-AUC Score"],
        "Holdout Test Score": [
            f"{test_metrics.get('accuracy', 0.9462)*100:.2f}%",
            f"{test_metrics.get('precision', 0.9655)*100:.2f}%",
            f"{test_metrics.get('recall', 0.9618)*100:.2f}%",
            f"{test_metrics.get('f1_score', 0.9637)*100:.2f}%",
            f"{test_metrics.get('roc_auc', 0.9430)*100:.2f}%"
        ]
    })
    st.dataframe(perf_table, use_container_width=True, hide_index=True)

# ==============================================================================
# 9. ABOUT THIS PROJECT & VIVA DEFENSE GUIDE
# ==============================================================================
st.markdown('<div class="section-header">📖 About This Project</div>', unsafe_allow_html=True)

with st.expander("Click to view Academic Context, Methodology & Viva Defense Notes", expanded=False):
    st.markdown("""
    ### 1. Project Objective
    To build an interpretable, end-to-end Machine Learning pipeline that detects disengaged online video game players early, allowing game studios to trigger personalized retention campaigns before permanent churn occurs.

    ### 2. Dataset Overview
    - **Dataset:** *Online Gaming Behavior Dataset*
    - **Instances:** 40,034 player records with complete telemetry, demographics, and progression data.
    - **Integrity:** 0 missing values, 0 duplicate rows.

    ### 3. Retention Proxy Methodology
    Because the dataset does not contain future longitudinal churn dates (e.g., return within D1, D7, or D30), we define an operational retention proxy from aggregated engagement:
    - **Medium & High Engagement $\\rightarrow$ Retained (`1`):** Represents regular, active players.
    - **Low Engagement $\\rightarrow$ At Risk (`0`):** Represents disengaged players with severe session attrition.

    ### 4. Why Not a True Future Churn Predictor?
    In empirical machine learning, a true churn predictor requires a separate observation window $[t_0, t_1]$ and prediction window $[t_1, t_2]$. Because our data is cross-sectional (measured concurrently), this model is formally defined as an **Engagement-Tier Retention Proxy Classifier**.

    ### 5. Key Limitations
    - Telemetry metrics are static weekly averages rather than time-series decline trajectories.
    - Some players in casual genres (e.g., Simulation) may play few sessions per week without ever intending to abandon the game.
    """)

# Footer
st.markdown("---")
st.caption("AI-Based Online Gaming Player Retention Prediction | Academic Machine Learning Project | Google Colab & Antigravity IDE")
