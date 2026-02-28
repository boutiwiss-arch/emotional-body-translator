# app.py
import streamlit as st

st.title("Emotional Body Translator")

st.write("Input your current body signals to see what your emotions might be:")

# Example input
heart_rate = st.number_input("Heart rate (bpm)", min_value=30, max_value=200, value=70)
breathing_rate = st.number_input("Breathing rate (breaths per minute)", min_value=5, max_value=40, value=12)

# Simple emotion logic
if heart_rate > 120:
    emotion = "Excited or Anxious"
elif heart_rate < 60:
    emotion = "Calm or Tired"
else:
    emotion = "Neutral or Content"

st.write(f"Predicted emotion based on body signals: **{emotion}**")