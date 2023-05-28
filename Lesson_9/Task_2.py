import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# Находим минимальное значение population
min_population = data['population'].min()

# Фильтруем строки, где population равно минимальному значению
min_population_data = data[data['population'] == min_population]

# Находим максимальное значение households в отфильтрованных данных
max_households = min_population_data['households'].max()

# Выводим результат
print("Максимальное количество households в зоне с минимальным значением population:", max_households)
