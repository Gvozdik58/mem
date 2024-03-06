import streamlit as st
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_occurrences(word, text):
    occurrences = re.findall(rf'\b{word}\b', text)
    return len(occurrences)

# Заголовок приложения
st.title('Анализ текста')

# Просим пользователя ввести текст
user_input = st.text_area('Пожалуйста, введите текст (до 10000 слов):', max_chars=10000)

if user_input:
    # Подсчет общего количества слов
    total_words = count_words(user_input)
    st.write(f'Общее количество слов: {total_words}')

    # Подсчет и анализ слова "в"
    count_v = count_occurrences('в', user_input)
    st.write(f'Количество слов "в": {count_v}')
    st.write(f'Доля слов "в" от общего числа слов: {count_v / total_words:.2%}')

    # Подсчет и анализ слова "на"
    count_na = count_occurrences('на', user_input)
    st.write(f'Количество слов "на": {count_na}')
    st.write(f'Доля слов "на" от общего числа слов: {count_na / total_words:.2%}')

    # Подсчет и анализ слова "с"
    count_s = count_occurrences('с', user_input)
    st.write(f'Количество слов "с": {count_s}')
    st.write(f'Доля слов "с" от общего числа слов: {count_s / total_words:.2%}')
