import streamlit as st
import pickle
import numpy as np

# Load the trained model and encoders
with open("ML_final (1).pkl", "rb") as file:
    model_data = pickle.load(file)

if model_data["model"] is None:
    st.error("⚠️ Model not loaded! Train and save the model again.")
    st.stop()

model = model_data["model"]

scaler = model_data["scaler"]
weather_encoder = model_data["weather_encoder"]
pitch_encoder = model_data["pitch_encoder"]

# Streamlit App Title
st.title("🏏 T20 Cricket Score Predictor")

# User Inputs
st.sidebar.header("Match Details")
overs_played = st.sidebar.slider("Overs Played", min_value=1, max_value=20, value=10)
wickets_lost = st.sidebar.slider("Wickets Lost", min_value=0, max_value=10, value=3)
run_rate = st.sidebar.number_input("Current Run Rate", min_value=0.0, max_value=15.0, value=7.5)
opponent_strength = st.sidebar.slider("Opponent Strength (1-10)", min_value=1, max_value=10, value=5)

pitch_condition = st.sidebar.selectbox("Pitch Condition", ['Bowling', 'Balanced', 'Batting'])
weather = st.sidebar.selectbox("Weather", ["Sunny", "Cloudy", "Overcast"])

# Encode categorical inputs
pitch_encoded = pitch_encoder.transform([pitch_condition])[0]
weather_encoded = weather_encoder.transform([weather])[0]

# Prepare input data
input_data = np.array([[overs_played, wickets_lost, run_rate, opponent_strength, pitch_encoded, weather_encoded]])

# Scale input features
input_scaled = scaler.transform(input_data)

# Predict the score
if st.sidebar.button("Predict Score"):
    predicted_score = model.predict(input_scaled)[0]
    st.success(f"🏏 Predicted Final Score: **{int(predicted_score)} Runs**")

