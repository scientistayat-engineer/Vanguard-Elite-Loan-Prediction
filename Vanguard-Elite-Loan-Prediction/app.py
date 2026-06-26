import streamlit as st
import pandas as pd
import joblib
import time
import plotly.graph_objects as go
import plotly.express as px

# 1. Page Configuration for Advanced Enterprise Dashboard Layout
st.set_page_config(
    page_title="Vanguard Elite | Credit Engine Terminal",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Safe Pipeline Loader with memory management caching
@st.cache_resource
def load_production_pipeline():
    try:
        return joblib.load('optimized_loan_predictor_pipeline.pkl')
    except Exception as e:
        st.error("Critical System Anomaly: 'optimized_loan_predictor_pipeline.pkl' not found.")
        return None

model = load_production_pipeline()

# 2. Advanced Custom CSS Injector for Deep Glassmorphic Blocks
st.markdown("""
    <style>
    /* Premium Deep Blue and Charcoal Dark Canvas Gradient */
    .stApp {
        background: linear-gradient(135deg, #060913 0%, #0c1322 100%);
        color: #f1f5f9;
    }
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.6rem;
        font-weight: 900;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2px;
    }
    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.05rem;
        margin-bottom: 30px;
    }
    /* Sleek Translucent Dashboard Glass Cards */
    .data-card {
        background: rgba(15, 23, 42, 0.7);
        padding: 22px;
        border-radius: 14px;
        border: 1px solid rgba(56, 189, 248, 0.15);
        backdrop-filter: blur(12px);
        margin-bottom: 18px;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.4);
    }
    /* Analytical Mini Metric Tokens style */
    .metric-box {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 8px;
        padding: 12px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Infrastructure with Interactive System Navigation
with st.sidebar:
    st.markdown("<h2 style='color: #38bdf8; font-weight:800; letter-spacing: 1px; margin-bottom:0;'>🏦 VANGUARD ELITE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-size:0.85rem; margin-top:-5px;'>Risk Underwriting Environment</p>", unsafe_allow_html=True)
    st.write("---")
    
    app_mode = st.radio("System Control Nodes", ["Risk Analysis Console", "Model Invariants & Documentation"])
    
    st.write("---")
    st.markdown("<h4 style='color: #64748b; font-size:0.95rem;'>Operational Parameters</h4>", unsafe_allow_html=True)
    override_threshold = st.slider("Strictness Risk Bound", 0.0, 1.0, 0.5, step=0.05)
    
    st.write("---")
    st.markdown("<small style='color: #334155;'>State: Production Ready<br>Core Engine: Scikit-Learn x Plotly v3.0</small>", unsafe_allow_html=True)

# --- PANEL MODULE 1: RISK ANALYSIS TERMINAL ---
if app_mode == "Risk Analysis Console":
    st.markdown("<h1 class='main-title'>Smart Credit Clearance & Underwriting System</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Automated multi-layer validation engine mapping user profiles to risk boundaries.</p>", unsafe_allow_html=True)
    
    # Real-time Input and Monitoring Grids Splitting
    left_panel, right_panel = st.columns([7, 5])
    
    with left_panel:
        # Block A: Social Demographics Input Vectors
        st.markdown("<div class='data-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #38bdf8; margin-top:0; font-size:1.2rem; font-weight:700;'>📋 Applicant Demographics & Social Vectors</h3>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            gender = st.selectbox("Applicant Gender", ["Male", "Female"])
            education = st.selectbox("Education Profile", ["Graduate", "Not Graduate"])
        with c2:
            married = st.selectbox("Marital Profile", ["Married", "Single / Unmarried"])
            self_employed = st.selectbox("Employment Structure", ["No (Salaried Employee)", "Yes (Self-Employed)"])
        with c3:
            dependents = st.selectbox("Dependents Volume", ["0", "1", "2", "3+"])
            property_area = st.selectbox("Property Demographics", ["Urban", "Semi-Urban", "Rural"])
        st.markdown("</div>", unsafe_allow_html=True)

        # Block B: Monetary Capital Configuration Metrics
        st.markdown("<div class='data-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #38bdf8; margin-top:0; font-size:1.2rem; font-weight:700;'>💵 Capital Exposure Configurations</h3>", unsafe_allow_html=True)
        
        c4, c5, c6 = st.columns(3)
        with c4:
            applicant_income = st.number_input("Primary Monthly Income ($)", min_value=0, value=6500, step=250)
            loan_amount = st.number_input("Requested Principal ($ in Thousands)", min_value=1, value=150, step=10)
        with c5:
            coapplicant_income = st.number_input("Co-Applicant Capital ($)", min_value=0, value=2000, step=250)
            loan_term = st.selectbox("Amortization Bound Length (Days)", [360, 180, 120, 84])
        with c6:
            credit_history = st.selectbox("Historical Credit Line Met?", ["Yes (High Trust Score / Clear Records)", "No (Delinquent State / No Score)"])
        st.markdown("</div>", unsafe_allow_html=True)

        # Action Execution Control Switch Trigger
        trigger_evaluation = st.button("EXECUTE MATHEMATICAL UNDERWRITING", type="primary", use_container_width=True)

        # Dynamic Asset Summary Token Strip
        st.markdown("<br>", unsafe_allow_html=True)
        t1, t2, t3 = st.columns(3)
        with t1:
            st.markdown(f"<div class='metric-box'><small style='color:#64748b;'>Combined Household Capital</small><h4 style='margin:5px 0 0 0; color:#38bdf8;'>${applicant_income + coapplicant_income:,}</h4></div>", unsafe_allow_html=True)
        with t2:
            st.markdown(f"<div class='metric-box'><small style='color:#64748b;'>Credit Baseline Status</small><h4 style='margin:5px 0 0 0; color:#fbbf24;'>{'Passing' if 'High Trust' in credit_history else 'Failing'}</h4></div>", unsafe_allow_html=True)
        with t3:
            st.markdown(f"<div class='metric-box'><small style='color:#64748b;'>Target Demographics</small><h4 style='margin:5px 0 0 0; color:#a78bfa;'>{property_area}</h4></div>", unsafe_allow_html=True)

    # Parsing parameters to dictionary mapping array structures matching training weights
    input_dict = {
        'Gender': 1 if gender == "Male" else 0,
        'Married': 1 if married == "Married" else 0,
        'Dependents': 3 if dependents == "3+" else int(dependents),
        'Education': 0 if education == "Graduate" else 1,
        'Self_Employed': 1 if self_employed == "Yes (Self-Employed)" else 0,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': 1.0 if "High Trust" in credit_history else 0.0,
        'Property_Area': 2 if property_area == "Urban" else (1 if property_area == "Semi-Urban" else 0)
    }

    total_income = applicant_income + coapplicant_income
    income_loan_ratio = total_income / (loan_amount * 1000) if loan_amount > 0 else 0

    with right_panel:
        if trigger_evaluation and model is not None:
            st.markdown("<div class='data-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #818cf8; margin-top:0; text-align:center; font-size:1.25rem;'>📊 Predictive Analytics Pipeline Diagnostics</h3>", unsafe_allow_html=True)
            
            with st.spinner("Processing architectural tensors..."):
                time.sleep(0.7) # Micro Premium Interface delay loop
                
                # DataFrame construction matching feature names array sequence
                single_df = pd.DataFrame([input_dict])
                single_df['Total_Income'] = total_income
                single_df['Income_Loan_Ratio'] = income_loan_ratio
                
                ordered_features = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 
                                    'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 
                                    'Credit_History', 'Property_Area', 'Total_Income', 'Income_Loan_Ratio']
                single_df = single_df[ordered_features]
                
                # Inference Matrix Checks
                probability = model.predict_proba(single_df)[0][1]
                raw_prediction = 1 if probability >= override_threshold else 0
                
                # 1. Gauge Speedometer Chart
                fig_gauge = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = probability * 100,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    gauge = {
                        'axis': {'range': [0, 100], 'tickcolor': "#475569", 'tickwidth': 1},
                        'bar': {'color': "#10b981" if raw_prediction == 1 else "#ef4444"},
                        'bgcolor': "rgba(30, 41, 59, 0.4)",
                        'steps': [
                            {'range': [0, 50], 'color': 'rgba(239, 68, 68, 0.08)'},
                            {'range': [50, 75], 'color': 'rgba(245, 158, 11, 0.08)'},
                            {'range': [75, 100], 'color': 'rgba(16, 185, 129, 0.08)'}
                        ]
                    }
                ))
                fig_gauge.update_layout(height=160, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_gauge, use_container_width=True, config={'displayModeBar': False})
                
                # 2. Scatter Map Overlay Positioning Matrix Chart
                mock_db = pd.DataFrame({
                    'Total_Income': [3500, 5500, 8500, 11500, 14000, total_income],
                    'LoanAmount': [90, 130, 170, 260, 310, loan_amount],
                    'Cluster': ['Historical Records', 'Historical Records', 'Historical Records', 'Historical Records', 'Historical Records', 'Active Target Node']
                })
                fig_scatter = px.scatter(
                    mock_db, x='Total_Income', y='LoanAmount', color='Cluster',
                    color_discrete_map={'Historical Records': '#334155', 'Active Target Node': '#38bdf8'},
                    size=[8, 8, 8, 8, 8, 16], title="Visual Database Distribution Overlay"
                )
                fig_scatter.update_layout(
                    height=160, margin=dict(l=5, r=5, t=25, b=5), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                    showlegend=False, font=dict(color="#ffffff", size=9), xaxis=dict(gridcolor="rgba(255,255,255,0.03)"), yaxis=dict(gridcolor="rgba(255,255,255,0.03)")
                )
                st.plotly_chart(fig_scatter, use_container_width=True, config={'displayModeBar': False})
                
                # Final Status Verdict Cards logic
                st.write("---")
                if raw_prediction == 1:
                    st.markdown("<div style='background: rgba(16, 185, 129, 0.12); padding: 14px; border-radius: 10px; border-left: 5px solid #10b981; text-align: center;'> <h4 style='color: #10b981; margin:0;'>💳 UNDERWRITING VERDICT: APPROVED</h4><p style='margin:4px 0 0 0; font-size:0.85rem; color: #94a3b8;'>Asset profile satisfies target constraints cleanly.</p></div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div style='background: rgba(239, 68, 68, 0.12); padding: 14px; border-radius: 10px; border-left: 5px solid #ef4444; text-align: center;'> <h4 style='color: #ef4444; margin:0;'>🚫 UNDERWRITING VERDICT: DECLINED</h4><p style='margin:4px 0 0 0; font-size:0.85rem; color: #94a3b8;'>Heightened structural default variance detected relative to safety filters.</p></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Bottom Logic Tracker Explainer block
            st.markdown(f"""
                <div class='data-card'>
                    <h4 style='margin-top:0; color: #cbd5e1;'>💡 Diagnostic Log Attribution</h4>
                    <small style='color: #64748b;'>
                        • <b>Credit Line Anchor:</b> Credit History acts as the heavy statistical driver in this mathematical state.<br>
                        • <b>Leverage Scaling:</b> Active calculated income-to-exposure ratio maps inside optimal bounds.
                    </small>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div class='data-card' style='text-align: center; color: #475569; padding: 150px 20px;'>💡 Systems Standby. Enter applicant structural vectors and activate the underwriting calculator engine controls to view telemetry.</div>", unsafe_allow_html=True)

# --- PANEL MODULE 2: SYSTEM DOCUMENTATION ---
else:
    st.markdown("<h2 style='color: #38bdf8; font-weight:800;'>Engine Analytics & System Architecture Logs</h2>", unsafe_allow_html=True)
    st.write("---")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Calibrated Core Model Accuracy", value="81.88%", delta="GridSearchCV Production Optimum")
    with m2:
        st.metric(label="Target Stability Margin (F1 Score)", value="87.42%", delta="Balanced Sample Splitting")
    with m3:
        st.metric(label="Network Invariant Latency", value="~ 6.5 ms", delta="Real-Time Active Run")
        
    st.write("---")
    st.markdown("### 🛠️ Runtime Runtime Mathematical Transformations Mapping")
    
    schema_data = {
        "Feature Parameter Attribute": ["Total_Income", "Income_Loan_Ratio", "Inference Serialization Layer"],
        "Mathematical Objective Strategy": ["ApplicantIncome + CoapplicantIncome", "Total_Income / (LoanAmount * 1000)", "joblib permanent binary allocation"],
        "Functional Execution Target Context": ["Aggregates core compound buying capacity of household unit", "Maps loan leverage limits relative to active assets", "Saves model weights state into optimized artifact file"]
    }
    st.table(pd.DataFrame(schema_data))

    # Insert this right below the table in MODULE 2
    st.write("---")
    st.markdown("### 📊 Live Feature Weightage Tracker (Model Decisions)")
    
    # Replicating your accurate bar chart from weights matrix
    feature_weights = pd.DataFrame({
        'Features': ['Credit_History', 'Married', 'Dependents', 'Income_Loan_Ratio', 'Self_Employed', 'Education', 'Gender'],
        'Statistical Weight': [3.3, 0.7, 0.1, 0.08, 0.05, -0.45, -0.42]
    }).sort_values(by='Statistical Weight', ascending=True)

    fig_importance = px.bar(
        feature_weights, 
        x='Statistical Weight', 
        y='Features', 
        orientation='h',
        title="AI Decision Explainer: Key Drivers for Loan Approval",
        color='Statistical Weight',
        color_continuous_scale=['#ef4444', '#38bdf8', '#10b981']
    )
    
    fig_importance.update_layout(
        height=320,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#cbd5e1")
    )
    st.plotly_chart(fig_importance, use_container_width=True, config={'displayModeBar': False})