T20 Cricket Score Prediction (ML + Streamlit)

This project predicts the final T20 cricket score using a Machine Learning model.
It is built with Python, Scikit-Learn, and Streamlit.


Features

Predicts final T20 score using:

Overs played

Wickets lost

Current run rate

Opponent strength

Pitch condition

Weather condition



Streamlit-based user interface

Trained ML model stored in a .pkl file

Simple and fast prediction system



Project Files

ML.py – Streamlit prediction app

ML_final (1).pkl – Trained model file

requirements.txt – Required Python libraries



Installation

Clone the repository
git clone https://github.com/Ashvin7510/Streamlit.git

cd Streamlit

Install dependencies
pip install -r requirements.txt



How to Run

Run the Streamlit application:
streamlit run ML.py



Input Features

Overs Played (1–20)

Wickets Lost (0–10)

Current Run Rate

Opponent Strength (1–10)

Pitch Condition: Batting / Balanced / Bowling

Weather: Sunny / Cloudy / Overcast




Output

The model predicts the final score of the batting team.


Example:
Predicted Score: 168 Runs
