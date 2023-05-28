import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# Фильтруем строки, где population находится в диапазоне от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисляем среднюю стоимость дома в отфильтрованных данных
average_house_price = filtered_data['median_house_value'].mean()

# Выводим результат
print("Средняя стоимость дома, где кол-во людей от 0 до 500:", average_house_price)
