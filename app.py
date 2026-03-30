import streamlit as st
import joblib
import numpy as np

# Загружаем модель
model = joblib.load("model.joblib")

st.title("🚢 Titanic Survival Predictor")
st.write("Введите данные пассажира:")

# Ввод данных пользователем
pclass = st.selectbox("Класс билета", [1, 2, 3])
sex = st.selectbox("Пол", ["Мужчина", "Женщина"])
age = st.slider("Возраст", 1, 80)
fare = st.number_input("Стоимость билета", 0.0, 500.0)

sex = 0 if sex == "Мужчина" else 1

# Кнопка предсказания
if st.button("Предсказать"):
    data = np.array([[pclass, sex, age, fare]])
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.success("✅ Пассажир выживет")
    else:
        st.error("❌ Пассажир не выживет")