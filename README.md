# 🏦 Vanguard Elite: Automated Credit Underwriting & Risk Prediction System

An end-to-end Machine Learning production pipeline built to automate credit clearance workflows, mitigate financial risk, and predict loan suitability using historical consumer data.

## 🚀 Key Features
- **Rigid Preprocessing:** Clean statistical imputation (Mode/Median) with full multi-class categorical encoding.
- **Advanced Feature Engineering:** Synthesized macroeconomic metrics (`Total_Income` and `Income_Loan_Ratio`) to measure continuous asset leverage.
- **Tuned Ensemble Architecture:** Optimizing Random Forest parameters via `GridSearchCV` to secure an **81.88% cross-validation accuracy**.
- **Consensus Voting Core:** Built a `VotingClassifier` ensemble to minimize decision variance in live workloads.
- **Leak-Proof Production Pipeline:** Wrapped preprocessing and models inside `sklearn.pipeline.Pipeline`.
- **Sub-Second Inference Engine:** Serialized pipeline to a binary artifact (`.pkl`) with a custom real-time inference function.

## 🗺️ System Architecture Roadmap
1. **Workspace Setup & Ingestion:** Loading and structural profiling of the source matrix.
2. **Data Integrity Imputation:** Handling missing values and data regularizations.
3. **Exploratory Data Analysis:** Profiling multi-variate dependencies and Pearson correlation heatmaps.
4. **Model Tuning & Optimization:** Multi-algorithmic grid searches to find the elite estimator weights.
5. **Serialization & Inference Simulation:** Exporting binary stream and testing dynamic applicant profiles.

## 📦 Tech Stack
- **Languages & Frameworks:** Python, Scikit-Learn, Joblib, Pandas, NumPy
- **Visualizations:** Seaborn, Matplotlib, Plotly Express

# 🏦 Vanguard Elite: Automated Credit Underwriting & Risk Prediction System

An end-to-end Machine Learning production pipeline built to automate credit clearance workflows, mitigate financial risk, and predict loan suitability using historical consumer data.

## 📁 Repository Structure
- 📁 `dataset/`: Contains the baseline historical consumer profiles used for training and testing.
- 📁 `frontend-assets/`: Visual snapshots and UI/UX screenshots of the live inference dashboard application.
- 📄 `Vanguard_Elite_Loan_Prediction_Pipeline.ipynb`: Core data processing, exploration, analytics, and modeling workbook.
- 📄 `optimized_loan_predictor_pipeline.pkl`: Serialized model pipeline artifact ready for enterprise deployment.
- 📄 `Vanguard_Elite_Underwriting_Report.pdf`: Comprehensive executive underwriting summary and evaluation report.
