
🚀 IntelliAllergen

AI-powered allergen detection system for safer food choices.

IntelliAllergen helps users instantly identify potential food allergens using a trained Machine Learning model. With a clean Streamlit interface and real-time predictions, the app empowers people with food sensitivities to make informed decisions.

🌟 Vision

To create a world where individuals with food allergies can confidently make safe food choices through accessible, reliable, AI-driven allergen detection.

🎯 Mission

To deliver an intuitive and accurate platform that identifies allergens from ingredient-level food data, enabling users to avoid harmful reactions.

✨ Features

🔍 Real-time allergen detection

🚨 Instant allergen alerts

🧾 Multi-ingredient support

🎛 Simple and clean Streamlit UI

⚙️ Customizable user inputs

⚡ Fast model inference

🧠 Tech Stack

Python

Streamlit (Frontend)

scikit-learn (Random Forest model)

Pandas, NumPy

Joblib (Model loading)

Category Encoders

📁 Project Structure
IntelliAllergen/
├── app.py                     # Main Streamlit application
├── requirements.txt           # Dependencies for deployment
├── Model/
│   ├── Allergen_detection.pkl
│   ├── leave_one_out_encoder.pkl
├── Datasets/
│   ├── Allergen_Status_of_Food_Products.csv
│   ├── preprocessed_data.csv
├── Scripts/
│   ├── notebooks...
│   ├── preprocessing scripts...

🚀 Run Locally
1. Clone the Repository
git clone https://github.com/roysarvesh/IntelliAllergen.git
cd IntelliAllergen

2. Install Dependencies
pip install -r requirements.txt

3. Run the Streamlit App
streamlit run app.py

🌐 Live Demo

👉 https://intelliallergen-dersed6g6a64x9vy8x82et.streamlit.app/

🤝 Contributing

Contributions are always welcome!
Open an issue or submit a pull request. 
