import streamlit as st
import numpy as np
import pickle
from PIL import Image
import base64

# Set page config
st.set_page_config(page_title="Diabetes Risk Predictor", layout="wide")

# Apply custom CSS for blurry background and better visibility
def set_bg():
    with open("bg.jpg", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <style>
            .stApp {{
                background: url("data:image/avif;base64,{encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                backdrop-filter: blur(6px);
                -webkit-backdrop-filter: blur(6px);
                color: #000000;
            }}

            .title-text {{
                font-size: 3.8rem;
                font-weight: bold;
                color: #0f2027;
                text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
            }}

            label, .stSlider label, .stNumberInput label {{
                color: #000000 !important;
                font-weight: 600 !important;
            }}

            .stMarkdown h3, .stMarkdown h2, .stMarkdown h1 {{
                color: #0f2027 !important;
            }}

            .stButton > button {{
                background-color: #0f2027;
                color: white;
                font-weight: bold;
                border-radius: 12px;
            }}

            .stButton > button:hover {{
                background-color: #2c5364;
                transition: 0.3s ease;
            }}
        </style>
    """, unsafe_allow_html=True)

# Apply background
set_bg()

# Load model and scaler
model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Sidebar Information
with st.sidebar:
    st.markdown("## 🏥 About")
    st.write("This app uses a **Logistic Regression** model trained on the **Pima Indians Diabetes Dataset** to predict diabetes risk.")
    st.warning("⚠️ Disclaimer: This app is based on a dataset and for educational purposes only. It is not a substitute for professional medical advice.")

# Main Heading
st.markdown('<h1 class="title-text">🧬 Diabetes Risk Predictor</h1>', unsafe_allow_html=True)
st.subheader("📊 Enter your health metrics below to predict your diabetes risk.")

# Input fields
st.markdown("### 🩺 Health Information:")
preg = st.number_input("👶 Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.slider("🍬 Glucose Level", 0, 200, 120)
bp = st.slider("🩸 Blood Pressure", 0, 140, 76)
skin = st.slider("💉 Skin Thickness", 0, 100, 20)
insulin = st.slider("🧪 Insulin Level", 0, 900, 80)
bmi = st.slider("⚖️ Body Mass Index (BMI)", 0.0, 70.0, 25.0)
dpf = st.slider("🧬 Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.slider("🎂 Age", 10, 100, 33)

# Predict Button
if st.button("🎯 Predict Risk"):
    features = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    scaled_features = scaler.transform(features)
    result = model.predict(scaled_features)[0]

    if result == 1:
        st.error("⚠️ You may be at risk of diabetes. Please consult a doctor.")
    else:
        st.success("✅ You are less likely to have diabetes.")

# Tips Section
st.markdown("---")
st.subheader("What to do next?")
st.markdown("""
- Maintain a healthy diet 🥗  
- Regular exercise 🏃‍♂️  
- Periodic health check-ups 🏥  
- Consult a professional if unsure
""")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<center>❤️ Made with love by <strong>Ajay</strong> using Streamlit</center>", unsafe_allow_html=True)
st.markdown("<center>⚠️ This tool is built for educational purposes and should not be used for real medical diagnosis.</center>", unsafe_allow_html=True)
