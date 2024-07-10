
"""## Подключим необходимые библиотеки"""

import faostat # Получение данных с fao.org
import pandas as pd # Работа с dataFrame
from matplotlib import pyplot as plt # Создание графиков
import seaborn as sns # Изменение видов графиков

"""# Получим данные о производстве с/х продукции (арбузы) и преобразуем их в dataFrame"""

# Параметры для получения данных
mypars = { 'area': '2',
              'element': '2312',
              'item': '567',
              'year': [list(range(1961, 2022))],}
# Получение данных из раздела "Продукты животноводства и сельскохозяственных культур"
harvest_data = faostat.get_data_df('QCL', pars=mypars, strval=False)
harvest_data

"""## Произведем обработку данных, избавимся от лишних столбцов и переименуем остальные для наглядности"""

# Удаление столбцов
del harvest_data['Domain Code']
del harvest_data['Domain']
del harvest_data['Element']
del harvest_data['Area Code']
del harvest_data['Element Code']
del harvest_data['Item Code']
del harvest_data['Year Code']
del harvest_data['Unit']
# Изменение имен столбцов
harvest_data.columns = ['Country', 'Product', 'Year', 'Quantity of production']
harvest_data

"""## Получим данные о численности населения и преобразуем их в dataFrame"""

# Параметры для получения данных
mypars = { 'area': '2',
              'element': '511',
              'item': '3010',
              'year': [list(range(1961, 2022))],}
# Получение данных из раздела "Численность населения"
population_data = faostat.get_data_df('OA', pars=mypars, strval=False)
population_data

"""## Произведем обработку данных, избавимся от лишних столбцов и переименуем остальные для наглядности"""

# Удаление столбцов
del population_data['Domain Code']
del population_data['Domain']
del population_data['Area Code']
del population_data['Element Code']
del population_data['Item Code']
del population_data['Item']
del population_data['Year Code']
del population_data['Element']
del population_data['Unit']
# Изменение имен столбцов
population_data.columns = ['Country', 'Year', 'Population (thousand)']
population_data

"""## Получим данные о экспорте с/х продукции (арбузы)"""

# Параметры для получения данных
mypars = { 'area': '2',
              'element': '152',
              'item': '567',
              'year': [list(range(1961, 2022))],}
# Получение данных из раздела "Стоимость сельскохозяйственной продукции""
export_data = faostat.get_data_df('QV', pars=mypars, strval=False)
export_data

"""## Произведем обработку данных, избавимся от лишних столбцов и переименуем остальные для наглядности"""

# Удаление столбцов
del export_data['Domain Code']
del export_data['Domain']
del export_data['Area Code']
del export_data['Element Code']
del export_data['Item Code']
del export_data['Item']
del export_data['Year Code']
del export_data['Element']
del export_data['Unit']
# Изменение имен столбцов
export_data.columns = ['Country', 'Year', 'Export (thousand $)']
export_data

"""## Объединим данные в один датасет"""

# Объединим по полям Country, Year сначала датасеты по производству и экспорты, потом с датасетом по населению
merged_data = pd.merge(pd.merge(harvest_data, export_data, on=['Country', 'Year'], how='outer'),
                      population_data, on=['Country', 'Year'], how='outer')
merged_data

"""## Импортируем датасет в csv файл"""

merged_data.to_csv('afghanistan_data.csv', index=False)

"""## Посчитаем и выведем максимум, минимум, среднее, размах, асимметрию, эксцесс, медиану для значений производства, экспорта и населения."""

# Перебираем все столбцы и с помощью функций pandas, найдем необходимые значения
for column in ['Quantity of production', 'Population (thousand)', 'Export (thousand $)']:
    print(f"Статистика для поля '{column}':")
    print(f"Максимум: {merged_data[column].max()}")
    print(f"Минимум: {merged_data[column].min()}")
    print(f"Среднее: {merged_data[column].mean()}")
    print(f"Размах: {merged_data[column].max() - merged_data[column].min()}")
    print(f"Асимметрия: {merged_data[column].skew()}")
    print(f"Эксцесс: {merged_data[column].kurtosis()}")
    print(f"Медиана: {merged_data[column].median()}")
    print()

"""## Построим график изменения населения со временем"""

# Функция построения графика
def _plot_series(series, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    xs = series['Year'] # ось x
    ys = series['Population (thousand)'] # ось y
    plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)]) # строим график
    # Добавим значения на каждом 10 годе
    increasing_points = []
    for i in range(1, len(ys), 10):
          increasing_points.append((xs[i], ys[i]))

    # Добавим метки на график
    for x, y in increasing_points:
        plt.annotate(f"{y:.0f}", (x, y), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=8)

    # Добавим метку для пиковой точки
    peak_index = ys.argmax()
    peak_x, peak_y = xs[peak_index], ys[peak_index]
    plt.annotate(f"{peak_y:.0f}", (peak_x, peak_y), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=8)

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = merged_data.sort_values('Year', ascending=True)
_plot_series(df_sorted, '')
# Установка интервала отображения годов
ax.set_xticks(df_sorted['Year'].values[::2])
ax.set_xticklabels(df_sorted['Year'].values[::2], rotation=90)
plt.title('Population gradation with each passing year')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
plt.ylabel('Population (thousand)')

def _plot_series(series, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    xs = series['Year']
    ys = series['Export (thousand $)']

    plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

    # Добавим значения на каждом 10 годе
    increasing_points = []
    for i in range(1, len(ys), 10):
        increasing_points.append((xs[i], ys[i]))

    # Добавим метки на график
    for x, y in increasing_points:
        plt.annotate(f"{y:.0f}", (x, y), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=8)

    # Добавим метку для пиковой точки
    peak_index = ys.argmax()
    peak_x, peak_y = xs[peak_index], ys[peak_index]
    plt.annotate(f"{peak_y:.0f}", (peak_x, peak_y), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=8)

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = merged_data.sort_values('Year', ascending=True)
_plot_series(df_sorted, '')

# Установка интервала отображения годов
ax.set_xticks(df_sorted['Year'].values[::2])
ax.set_xticklabels(df_sorted['Year'].values[::2], rotation=90)

plt.title('Export gradation with each passing year')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
plt.ylabel('Export (thousand $)')

def _plot_series(series, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    xs = series['Year']
    ys = series['Quantity of production']

    plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

    # Добавим значения на каждом 10 годе
    increasing_points = []
    for i in range(1, len(ys), 10):
        increasing_points.append((xs[i], ys[i]))

    # Добавим метки на график
    for x, y in increasing_points:
        plt.annotate(f"{y:.0f}", (x, y), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=8)

    # Добавим метку для пиковой точки
    peak_index = ys.argmax()
    peak_x, peak_y = xs[peak_index], ys[peak_index]
    plt.annotate(f"{peak_y:.0f}", (peak_x, peak_y), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=8)


fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = merged_data.sort_values('Year', ascending=True)
_plot_series(df_sorted, '')

# Установка интервала отображения годов
ax.set_xticks(df_sorted['Year'].values[::2])
ax.set_xticklabels(df_sorted['Year'].values[::2], rotation=90)

plt.title('Quantity of production gradation with each passing year')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
plt.ylabel('Quantity of production')
