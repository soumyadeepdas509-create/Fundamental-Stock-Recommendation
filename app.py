import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Fundamental Stock Recommendation",
    layout="wide"
)

st.title("📈 Fundamental Stock Recommendation System")
st.write("Rule-Based Stock Analysis using Fundamental Parameters")

# -------------------------------
# User Inputs
# -------------------------------
company = st.text_input("Company Name")

market_cap = st.number_input("Market Cap (₹ Crore)", min_value=0.0)
pe_ratio = st.number_input("PE Ratio", min_value=0.0)
industry_pe = st.number_input("Industry PE", min_value=0.0)
pb_ratio = st.number_input("PB Ratio", min_value=0.0)
roe = st.number_input("ROE (%)", min_value=0.0)
eps = st.number_input("EPS")
dividend = st.number_input("Dividend Yield (%)", min_value=0.0)
book_value = st.number_input("Book Value", min_value=0.0)
debt_equity = st.number_input("Debt to Equity", min_value=0.0)

business_age = st.number_input("Business Age (Years)", min_value=0)

growth = st.selectbox("Growth Consistency", ["Yes", "No"])
leadership = st.selectbox("Leadership Stability", ["Yes", "No"])

promoter = st.number_input("Promoter Holding (%)", min_value=0.0)
profit_growth = st.number_input("Profit Growth (%)")
revenue_growth = st.number_input("Revenue Growth (%)")

cash_flow = st.selectbox("Operating Cash Flow", ["Positive", "Negative"])

roce = st.number_input("ROCE (%)")

# -------------------------------
# Analyze Button
# -------------------------------
if st.button("Analyze Stock"):

    score = 0
    passed = []
    failed = []

    # Rule 1
    if market_cap >= 5000:
        score += 1
        passed.append("Large Market Cap")
    else:
        failed.append("Small Market Cap")

    # Rule 2
    if pe_ratio < industry_pe:
        score += 1
        passed.append("PE lower than Industry PE")
    else:
        failed.append("PE higher than Industry PE")

    # Rule 3
    if pb_ratio <= 5:
        score += 1
        passed.append("Healthy PB Ratio")
    else:
        failed.append("High PB Ratio")

    # Rule 4
    if roe >= 20:
        score += 1
        passed.append("High ROE")
    else:
        failed.append("Low ROE")

    # Rule 5
    if eps > 0:
        score += 1
        passed.append("Positive EPS")
    else:
        failed.append("Negative EPS")

    # Rule 6
    if dividend >= 1:
        score += 1
        passed.append("Good Dividend Yield")
    else:
        failed.append("Low Dividend Yield")

    # Rule 7
    if debt_equity <= 0.5:
        score += 1
        passed.append("Low Debt")
    else:
        failed.append("High Debt")

    # Rule 8
    if business_age >= 10:
        score += 1
        passed.append("Established Business")
    else:
        failed.append("Young Business")

    # Rule 9
    if growth == "Yes":
        score += 1
        passed.append("Consistent Growth")
    else:
        failed.append("Inconsistent Growth")

    # Rule 10
    if leadership == "Yes":
        score += 1
        passed.append("Stable Leadership")
    else:
        failed.append("Leadership Issues")

    # Rule 11
    if promoter >= 50:
        score += 1
        passed.append("High Promoter Holding")
    else:
        failed.append("Low Promoter Holding")

    # Rule 12
    if profit_growth >= 15:
        score += 1
        passed.append("Good Profit Growth")
    else:
        failed.append("Low Profit Growth")

    # Rule 13
    if revenue_growth >= 10:
        score += 1
        passed.append("Good Revenue Growth")
    else:
        failed.append("Low Revenue Growth")

    # Rule 14
    if cash_flow == "Positive":
        score += 1
        passed.append("Positive Operating Cash Flow")
    else:
        failed.append("Negative Operating Cash Flow")

    # Rule 15
    if roce >= 20:
        score += 1
        passed.append("High ROCE")
    else:
        failed.append("Low ROCE")

    # -------------------------------
    # Recommendation
    # -------------------------------
    if score >= 13:
        recommendation = "🟢 STRONG BUY"
    elif score >= 10:
        recommendation = "🟢 BUY"
    elif score >= 7:
        recommendation = "🟡 HOLD"
    else:
        recommendation = "🔴 SELL"

    # -------------------------------
    # Percentage & Risk
    # -------------------------------
    percentage = (score / 15) * 100

    if percentage >= 85:
        risk = "Very Low"
    elif percentage >= 70:
        risk = "Low"
    elif percentage >= 50:
        risk = "Medium"
    else:
        risk = "High"

    # -------------------------------
    # Results
    # -------------------------------
    st.header("Analysis Result")

    st.write("### Company")
    st.write(company)

    st.write("### Recommendation")

    if "STRONG BUY" in recommendation:
        st.success(recommendation)
    elif "BUY" in recommendation:
        st.success(recommendation)
    elif "HOLD" in recommendation:
        st.warning(recommendation)
    else:
        st.error(recommendation)

    col1, col2, col3 = st.columns(3)
    col1.metric("Fundamental Score", f"{score}/15")
    col2.metric("Percentage", f"{percentage:.2f}%")
    col3.metric("Risk Level", risk)

    # -------------------------------
    # Overall Rating
    # -------------------------------
    rating = round((score / 15) * 5, 1)

    st.subheader("⭐ Overall Rating")
    st.metric("Rating", f"{rating}/5")

    stars = "⭐" * int(rating)
    if rating - int(rating) >= 0.5:
        stars += "✨"

    st.write(stars)

    # -------------------------------
    # Progress Bar
    # -------------------------------
    st.subheader("🎯 Fundamental Score Progress")
    st.progress(score / 15)
    st.write(f"{score}/15 ({percentage:.2f}%)")

    # -------------------------------
    # Gauge Meter
    # -------------------------------
    st.subheader("📊 Fundamental Health Meter")

    fig_gauge, ax = plt.subplots(figsize=(8, 1.8))
    ax.barh(["Health Score"], [score], color="green", height=0.4)
    ax.set_xlim(0, 15)
    ax.set_xlabel("Score out of 15")

    st.pyplot(fig_gauge)

    # -------------------------------
    # Passed Parameters
    # -------------------------------
    st.subheader("✅ Strengths")
    for item in passed:
        st.write(item)

    # -------------------------------
    # Failed Parameters
    # -------------------------------
    st.subheader("❌ Weaknesses")
    for item in failed:
        st.write(item)

    # -------------------------------
    # Bar Chart
    # -------------------------------
    parameters = [
        "ROE",
        "ROCE",
        "Profit Growth",
        "Revenue Growth",
        "Promoter Holding"
    ]

    values = [
        roe,
        roce,
        profit_growth,
        revenue_growth,
        promoter
    ]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(parameters, values)
    ax.set_title("Fundamental Analysis")
    ax.set_ylabel("Values")

    st.pyplot(fig)

    # -------------------------------
    # Pie Chart
    # -------------------------------
    st.subheader("📊 Fundamental Score Distribution")

    labels = ["Passed", "Failed"]
    sizes = [len(passed), len(failed)]
    colors = ["green", "red"]
    explode = (0.08, 0)

    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(
        sizes,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct="%1.1f%%",
        startangle=90,
        shadow=True
    )
    ax2.set_title("Passed vs Failed Parameters")

    st.pyplot(fig2)

    # -------------------------------
    # Save Report
    # -------------------------------
    result = pd.DataFrame({
        "Company": [company],
        "Recommendation": [recommendation],
        "Score": [score],
        "Percentage": [round(percentage, 2)],
        "Risk": [risk]
    })

    result.to_csv("analysis_report.csv", index=False)

    st.success("Analysis report saved successfully!")
