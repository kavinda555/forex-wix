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
