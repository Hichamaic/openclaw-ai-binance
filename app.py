import streamlit as st

st.set_page_config(page_title="OpenClaw AI", layout="wide")

st.title("🟡 OpenClaw AI – Smart Trading Assistant")
st.write("Assistant for beginners inside Binance ecosystem")

menu = st.sidebar.selectbox(
    "Choose Service",
    ["Portfolio Risk Analyzer",
     "Futures Safety Calculator",
     "Trader Genome Profile",
     "Crypto Education Hub",
     "Protection Mode"]
)

# ===============================
# Portfolio Analyzer
# ===============================
if menu == "Portfolio Risk Analyzer":

    st.header("🧠 Portfolio Risk Analyzer")

    capital = st.number_input("Investment Capital ($)", 0, 100000, 1000)

    btc = st.number_input("BTC %", 0, 100, 0)
    eth = st.number_input("ETH %", 0, 100, 0)
    bnb = st.number_input("BNB %", 0, 100, 0)
    others = st.number_input("Others %", 0, 100, 0)

    if st.button("Analyze Portfolio"):

        total = btc + eth + bnb + others

        if total != 100:
            st.error("Portfolio allocation must equal 100%")
        else:
            concentration = max(btc, eth, bnb, others)

            if concentration < 40:
                risk = "🟢 Low Risk"
            elif concentration < 70:
                risk = "🟡 Medium Risk"
            else:
                risk = "🔴 High Risk"

            st.subheader("Risk Level")
            st.write(risk)

            st.write("Highest Allocation:", concentration, "%")

            if concentration > 50:
                st.warning("⚠ Your portfolio is highly concentrated.")

# ===============================
# Futures Calculator
# ===============================
elif menu == "Futures Safety Calculator":

    st.header("🔥 Futures Safety Calculator")

    capital = st.number_input("Capital ($)", 0, 100000, 1000)
    leverage = st.number_input("Leverage", 1, 100, 10)
    entry = st.number_input("Entry Price", 0.0)
    exit_price = st.number_input("Exit Price", 0.0)

    if st.button("Calculate"):

        if entry > 0:

            pnl = (exit_price - entry) * leverage

            roi = (pnl / capital) * 100 if capital > 0 else 0

            st.write("PNL Estimate:", round(pnl, 2))
            st.write("ROI %:", round(roi, 2))

            if leverage > 20:
                st.warning("⚠ High leverage is risky for beginners.")

# ===============================
# Trader Genome Profile
# ===============================
elif menu == "Trader Genome Profile":

    st.header("🧠 Trader Genome AI (Simulation)")

    history = st.slider("Trading Experience (Months)", 0, 60, 6)

    if st.button("Generate Profile"):

        if history < 6:
            profile = "🟡 Beginner Trader"
            advice = "Focus on learning before high risk trading."
        elif history < 24:
            profile = "🟢 Balanced Trader"
            advice = "Diversify and manage risk."
        else:
            profile = "🔵 Advanced Trader"
            advice = "You may explore advanced strategies."

        st.write("Profile:", profile)
        st.write("Advice:", advice)

# ===============================
# Education Hub
# ===============================
elif menu == "Crypto Education Hub":

    st.header("📚 Beginner Crypto Education")

    topic = st.selectbox(
        "Choose Topic",
        ["Spot Trading",
         "Futures Trading",
         "Leverage Risk",
         "Market Volatility"])

    if st.button("Learn"):

        st.info("Educational explanation for beginners.")

# ===============================
# Protection Mode
# ===============================
elif menu == "Protection Mode":

    st.header("🛡 Beginner Protection Mode")

    st.write("✅ High leverage warning")
    st.write("✅ Portfolio concentration alert")
    st.write("✅ Beginner safety tips")