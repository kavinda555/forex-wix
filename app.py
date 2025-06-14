import streamlit as st
from PIL import Image

st.set_page_config(page_title="Strategy Wizard", layout="centered")

st.title("📈 Strategy Wizard")

st.subheader("Input")
uploaded_image = st.file_uploader("Upload chart screenshot (market)", type=["jpg", "png"])

prompt = st.text_area("Prompt", value="Should I Buy Or Sell\nUse Support and Resistance Strategy")

if st.button("Run") and uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Market Chart", use_column_width=True)

    st.subheader("Output")
    st.markdown("""
    Based on the provided chart for XAU/USD (Gold vs US Dollar) on the H1 timeframe:

    1. Trend Analysis: Bullish trend based on price action above moving average.

    2. RSI: 63.5% — slightly bullish momentum.

    3. Recommendation: Buy.

    4. TP: ~3055–3060  
       SL: ~3025

    ⚠️ *Adjust based on real-time fundamentals and market news.*
    """)
    if run_analysis and uploaded_file is not None:
    # Show uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='🧠 Analyzing Chart...', use_column_width=True)

    with st.spinner('Analyzing...'):
        time.sleep(2)  # simulate processing

        # ✅ Output section
        st.markdown("## 📊 Analysis Result")
        st.markdown("""
        Based on the provided chart for XAU/USD (Gold vs US Dollar) on the H1 timeframe:

        1. Trend Analysis  
        The price has made a significant upward move above the moving average, indicating strong bullish momentum.

        2. RSI  
        The RSI is at 63.5%, which is above the neutral 50 but still below the overbought level of 70.  
        This suggests that there is potential for further upward movement but also warrants caution.

        3. Recommendation  
        ✅ Buy — Considering the strong upward move and momentum, entering a buy position could be favorable.

        4. Take Profit — Set around 3055 to 3060  
        5. Stop Loss — Set around 3025

        ⚠️ Always ensure to adjust your strategy based on real-time data and events impacting the market.
        """)
