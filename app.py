import streamlit as st
import joblib
import pandas as pd

# Загружаем модель
model = joblib.load("model.joblib")

st.title("🚢 Titanic Survival Predictor")
st.write("Введите данные пассажира:")

# Ввод данных пользователем
pclass = st.selectbox("Класс билета", [1, 2, 3])
sex = st.selectbox("Пол", ["Мужчина", "Женщина"])
age = st.slider("Возраст", 1, 80)
fare = st.number_input("Стоимость билета", 0.0, 500.0)

# Преобразуем пол в числовой формат
sex = 0 if sex == "Мужчина" else 1

# Создаём DataFrame для модели
input_data = pd.DataFrame([[pclass, sex, age, fare]], columns=["Pclass","Sex","Age","Fare"])

# Кнопка предсказания
if st.button("Предсказать"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ Пассажир выживет")
    else:
        st.error("❌ Пассажир не выживет")