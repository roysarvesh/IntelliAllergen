import streamlit as st
import pandas as pd
import joblib
import os

# Load model and encoder
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "Allergen_detection.pkl")
encoder_path = os.path.join(current_dir, "leave_one_out_encoder.pkl")

loaded_model = joblib.load(model_path)
loaded_encoder = joblib.load(encoder_path)

# App title and description:
st.markdown("""
    <h1 style="text-align: center; font-size: 35px;">🍽️ IntelliAllergen - Allergen Detection App</h1>
    <p style="text-align: center; font-size: 18px;">Welcome to <b>IntelliAllergen</b>! 🌱 <br> 
    📋 Enter the Product Details & ensure you're Safe </p> 
""", unsafe_allow_html=True)

# Sidebar info
st.sidebar.title("ℹ️ About IntelliAllergen")
st.sidebar.markdown("""
- **Purpose**: Predict allergen probability  
- **Built with**: Streamlit + ML  
- **Created by**: Sarvesh Kumar Roy  
""")

# Custom CSS
st.markdown("""
<style>
    .stButton>button {
        font-size: 40px !important;
        font-weight: bold !important;
        height: 40px !important;
        width: 250px !important;
    }
</style>
""", unsafe_allow_html=True)

# Form for user input
with st.form(key="product_form"):
    error_flag = False
    col1, col2 = st.columns(2)

    with col1:
        food_product = st.text_input("🥘 Food Product")
        if food_product.isnumeric():
            st.error("Food Product should not contain numbers.")
            error_flag = True

        main_ingredient = st.text_input("🌾 Main Ingredient")
        if main_ingredient.isnumeric():
            st.error("Main Ingredient should not contain numbers.")
            error_flag = True

        sweetener = st.text_input("🍯 Sweetener")
        if sweetener.isnumeric():
            st.error("Sweetener should not contain numbers.")
            error_flag = True

        fat_oil = st.text_input("🧈 Fat/Oil")
        if fat_oil.isnumeric():
            st.error("Fat/Oil should not contain numbers.")
            error_flag = True

    with col2:
        seasoning = st.text_input("🧂 Seasoning")
        if seasoning.isnumeric():
            st.error("Seasoning should not contain numbers.")
            error_flag = True

        allergens = st.text_input("⚠️ Allergens")
        if allergens.isnumeric():
            st.error("Allergens should not contain numbers.")
            error_flag = True

        price = st.number_input("💲 Price ($)", min_value=0.0, step=0.1)
        customer_rating = st.number_input("⭐ Customer Rating (Out of 5)", min_value=0.0, max_value=5.0, step=0.1)

    col1, col2, col3 = st.columns([1, 1.3, 1])

    with col2:
        submit_button = st.form_submit_button("🔍 Predict Allergens 🚀")

# On submit
if submit_button:
    if error_flag:
        st.warning("⚠️ Please fix validation errors!")
    elif not all([food_product, main_ingredient, sweetener, fat_oil, seasoning, allergens]):
        st.warning("⚠️ Fill all fields! If something doesn't apply, write 'None'.")
    else:
        input_df = pd.DataFrame({
            "Food Product": [food_product],
            "Main Ingredient": [main_ingredient],
            "Sweetener": [sweetener],
            "Fat/Oil": [fat_oil],
            "Seasoning": [seasoning],
            "Allergens": [allergens],
            "Price ($)": [price],
            "Customer rating": [customer_rating]
        })

        # Encode categorical data
        categorical_cols = input_df.select_dtypes(include="object").columns
        encoded = loaded_encoder.transform(input_df[categorical_cols])
        final_input = pd.concat([input_df.drop(categorical_cols, axis=1), encoded], axis=1)

        # Prediction
        prediction = loaded_model.predict(final_input)[0]

        result = (
            "❌ This product contains allergens. 🚨"
            if prediction == 0
            else "✅ This product does NOT contain allergens. 🎉"
        )

        st.success(result)

# Footer
st.markdown("""
<hr>
<p style="text-align:center;">
    Built with ❤️ using Streamlit.<br>
    IntelliAllergen® 2026 • Made by <b>Sarvesh Kumar Roy</b>
</p>
""", unsafe_allow_html=True)
