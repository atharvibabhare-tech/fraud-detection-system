import streamlit as st
import pickle
import numpy as np

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🚨",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================

model = pickle.load(open("fraud_model.pkl", "rb"))

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: black;
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111111;
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Labels */
label {
    color: white !important;
    font-weight: bold;
}

/* Headings */
h1, h2, h3 {
    color: red;
    text-align: center;
}

/* Buttons */
.stButton>button {
    background-color: red;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: darkred;
    color: white;
}

/* Metric */
[data-testid="stMetricValue"] {
    color: white;
}

/* Input box text */
.stNumberInput input {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.title("🚨 Fraud Detection System")

st.markdown(
    "<h3>AI-Powered Financial Fraud Detection Dashboard</h3>",
    unsafe_allow_html=True
)

st.write("")

# =========================
# SIDEBAR INPUTS
# =========================

st.sidebar.header("💳 Transaction Details")

amount = st.sidebar.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=100.0
)

time = st.sidebar.number_input(
    "Transaction Time",
    min_value=0.0,
    value=1000.0
)

# Dummy Features
v1 = st.sidebar.number_input("V1", value=0.0)
v2 = st.sidebar.number_input("V2", value=0.0)
v3 = st.sidebar.number_input("V3", value=0.0)
v4 = st.sidebar.number_input("V4", value=0.0)

# =========================
# INPUT ARRAY
# =========================

input_data = np.array([[
    amount,
    time,
    v1,
    v2,
    v3,
    v4
]])

# =========================
# PREDICTION
# =========================

if st.button("🚨 Detect Fraud"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:

        st.error("🚨 Fraudulent Transaction Detected")

        st.metric(
            label="Risk Level",
            value="HIGH RISK"
        )

    else:

        st.success("✅ Genuine Transaction")

        st.metric(
            label="Risk Level",
            value="LOW RISK"
        )

# =========================
# FOOTER
# =========================

st.write("")
st.markdown("---")

st.markdown(
    "<center style='color:white;'>Created by Atharvi 💙</center>",
    unsafe_allow_html=True
)
