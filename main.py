# Визуализация данных на карте России

# Необходимые библиотеки
import json
# from urllib.request import urlopen
import pandas as pd
import plotly.express as px
# import plotly.graph_objects as go
from plotly import offline

# Возможность изменять данные исходной карты субъектов
'''
with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/russia.geojson') \
        as response:
    counties = json.load(response)
regions_republic_1 = ['Бурятия', 'Тыва', 'Адыгея', 'Татарстан', 'Марий Эл',
                      'Северная Осетия – Алания', 'Алтай',
                      'Дагестан', 'Ингушетия', 'Башкортостан']
regions_republic_2 = ['Удмуртская республика', 'Кабардино-Балкарская республика',
                      'Карачаево-Черкесская республика', 'Чеченская республика']
for k in range(len(counties['features'])):
    counties['features'][k]['properties']['cartodb_id'] = k
    if counties['features'][k]['properties']['name'] in regions_republic_1:
        counties['features'][k]['properties']['name'] = 'Республика ' + counties['features'][k]['properties']['name']
    elif counties['features'][k]['properties']['name'] == 'Ханты-Мансийский автономный округ - Югра':
        counties['features'][k]['properties']['name'] = 'Ханты-Мансийский АО'
    elif counties['features'][k]['properties']['name'] == 'Чувашия':
        counties['features'][k]['properties']['name'] = 'Чувашская Республика'
    elif counties['features'][k]['properties']['name'] in regions_republic_2:
        counties['features'][k]['properties']['name'] = counties['features'][k]['properties']['name'].title()
        
with open('counties.json', 'w') as f:
    map_file = json.dump(counties, f, indent=4)
'''
# Обозначение файлов и получение анализируемых данных
map_file_counties = 'counties.json'
map_file_districts = 'districts.json'
data_file = input('Выберете файл:')
with open(data_file, encoding="utf-8") as f:
    data = json.load(f)
# Обозначение списков
region_names_list = []
researching_data = list(data[0])
data_value_list = []
districts_name_list = []

# Разделение субъектов по округам
CentrFD = ['Белгородская область',
           'Брянская область',
           'Владимирская область',
           'Воронежская область',
           'Ивановская область',
           'Калужская область',
           'Костромская область',
           'Курская область',
           'Липецкая область',
           'Московская область',
           'Орловская область',
           'Рязанская область',
           'Смоленская область',
           'Тамбовская область',
           'Тверская область',
           'Тульская область',
           'Ярославская область',
           'Москва']
NorthWestFD = ['Республика Карелия',
               'Республика Коми',
               'Архангельская область',
               'Ненецкий автономный округ',
               'Вологодская область',
               'Калининградская область',
               'Ленинградская область',
               'Мурманская область',
               'Новгородская область',
               'Псковская область',
               'Санкт-Петербург']
SouthFD = ['Республика Адыгея',
           'Республика Калмыкия',
           'Республика Крым',
           'Краснодарский край',
           'Астраханская область',
           'Волгоградская область',
           'Ростовская область',
           'Севастополь']
NorthCavFD = ['Республика Дагестан',
              'Республика Ингушетия',
              'Кабардино-Балкарская Республика',
              'Карачаево-Черкесская Республика',
              'Республика Северная Осетия - Алания',
              'Чеченская Республика',
              'Ставропольский край']
VolgFD = ['Республика Башкортостан',
          'Республика Марий Эл',
          'Республика Мордовия',
          'Республика Татарстан',
          'Удмуртская Республика',
          'Чувашская Республика',
          'Пермский край',
          'Кировская область',
          'Нижегородская область',
          'Оренбургская область',
          'Пензенская область',
          'Самарская область',
          'Саратовская область',
          'Ульяновская область']
UralFD = ['Курганская область',
          'Свердловская область',
          'Тюменская область',
          'Ханты-Мансийский АО',
          'Ямало-Ненецкий автономный округ',
          'Ненецкий автономный округ',
          'Челябинская область']
SibFD = ['Республика Алтай',
         'Республика Тыва',
         'Республика Хакасия',
         'Алтайский край',
         'Красноярский край',
         'Иркутская область',
         'Кемеровская область',
         'Новосибирская область',
         'Омская область',
         'Томская область']
FarEastFD = ['Республика Бурятия',
             'Республика Саха (Якутия)',
             'Забайкальский край',
             'Камчатский край',
             'Приморский край',
             'Хабаровский край',
             'Амурская область',
             'Магаданская область',
             'Сахалинская область',
             'Еврейская автономная область',
             'Чукотский автономный округ']
FDs = ['Российская Федерация', ]

# Запрос данных
print('Данные, которые можно получить: ')
for data_name in researching_data[1:]:
    print(f'\t{data_name}')
get_data = input('Скопировать и вставить ')

# Определение принадлежности к округу

for region in data:

    if region['Название'] in CentrFD or region['Название'] == 'Центральный федеральный округ':
        districts_name_list.append('Центральный федеральный округ')
    if region['Название'] in NorthWestFD or region['Название'] == 'Северо-Западный федеральный округ':
        districts_name_list.append('Северо-Западный федеральный округ')
    if region['Название'] in SouthFD or region['Название'] == 'Южный федеральный округ':
        districts_name_list.append('Южный федеральный округ')
    if region['Название'] in NorthCavFD or region['Название'] == 'Северо-Кавказский федеральный округ':
        districts_name_list.append('Северо-Кавказский федеральный округ')
    if region['Название'] in VolgFD or region['Название'] == 'Приволжский федеральный округ':
        districts_name_list.append('Приволжский федеральный округ')
    if region['Название'] in UralFD or region['Название'] == 'Уральский федеральный округ':
        districts_name_list.append('Уральский федеральный округ')
    if region['Название'] in SibFD or region['Название'] == 'Сибирский федеральный округ':
        districts_name_list.append('Сибирский федеральный округ')
    if region['Название'] in FarEastFD or region['Название'] == 'Дальневосточный федеральный округ':
        districts_name_list.append('Дальневосточный федеральный округ')


# Функции
# Наполнение списков для округов
def data_for_districts_counties_map():
    for region in data:
        if region["Название"] == "Центральный федеральный округ":
            CentrFD_data = round(region[get_data], 2)
        if region["Название"] == "Северо-Западный федеральный округ":
            NorthWestFD_data = round(region[get_data], 2)
        if region["Название"] == "Южный федеральный округ":
            SouthFD_data = round(region[get_data], 2)
        if region["Название"] == "Северо-Кавказский федеральный округ":
            NorthCavFD_data = round(region[get_data], 2)
        if region["Название"] == "Приволжский федеральный округ":
            VolgFD_data = round(region[get_data], 2)
        if region["Название"] == "Уральский федеральный округ":
            UralFD_data = round(region[get_data], 2)
        if region["Название"] == "Сибирский федеральный округ":
            SibFD_data = round(region[get_data], 2)
        if region["Название"] == "Дальневосточный федеральный округ":
            FarEastFD_data = round(region[get_data], 2)
    ao = input('Есть ли округа? (да/любой символ) ')
    if ao != 'да':
        region_names_list.append('Ханты-Мансийский АО')
        region_names_list.append('Ямало-Ненецкий автономный округ')
        region_names_list.append('Ненецкий автономный округ')
        data_value_list.append(UralFD_data)
        data_value_list.append(UralFD_data)
        data_value_list.append(NorthWestFD_data)
        districts_name_list.append('Уральский федеральный округ')
        districts_name_list.append('Уральский федеральный округ')
        districts_name_list.append('Северо-Западный федеральный округ')
    for region in data:
        region_name = region["Название"]
        if region_name in CentrFD or region_name == "Центральный федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = CentrFD_data
            data_value_list.append(region[get_data])
        if region_name in NorthWestFD or region_name == "Северо-Западный федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = NorthWestFD_data
            data_value_list.append(region[get_data])
        if region_name in SouthFD or region_name == "Южный федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = SouthFD_data
            data_value_list.append(region[get_data])
        if region_name in NorthCavFD or region_name == "Северо-Кавказский федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = NorthCavFD_data
            data_value_list.append(region[get_data])
        if region_name in VolgFD or region_name == "Приволжский федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = VolgFD_data
            data_value_list.append(region[get_data])
        if region_name in UralFD or region_name == "Уральский федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = UralFD_data
            data_value_list.append(region[get_data])
        if region_name in SibFD or region_name == "Сибирский федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = SibFD_data
            data_value_list.append(region[get_data])
        if region_name in FarEastFD or region_name == "Дальневосточный федеральный округ":
            region_names_list.append(region["Название"])
            region[get_data] = FarEastFD_data
            data_value_list.append(region[get_data])


def data_for_districts_districts_map():
    for region in data:
        region_names_list.append(region["Название"])
        data_value_list.append(round(region[get_data], 2))


# Наполнение списков для карты по субъектам
def data_for_counties():
    for region in data:
        region_names_list.append(region["Название"])
        data_value_list.append(round(float(region[get_data]), 2))
    ao = input('Есть ли округа? (да/любой символ) ')
    if ao != 'да':
        region_names_list.append('Ханты-Мансийский АО')
        region_names_list.append('Ямало-Ненецкий автономный округ')
        region_names_list.append('Ненецкий автономный округ')
        data_value_list.append(0)
        data_value_list.append(0)
        data_value_list.append(0)
        districts_name_list.append('Уральский федеральный округ')
        districts_name_list.append('Уральский федеральный округ')
        districts_name_list.append('Северо-Западный федеральный округ')


# Создание df по данным и объединение с df по карте
def map(map_file):
    unit = input('Введите единицы измерения: ')
    with open(map_file, encoding="utf-8") as f:
        map = json.load(f)
    df_regions = pd.DataFrame()
    df_regions['Название региона'] = [map['features'][i]['properties']["name"]
                                      for i in range(len(map['features']))]
    df_regions['id'] = [map['features'][i]['properties']["cartodb_id"]
                        for i in range(len(map['features']))]
    df = pd.DataFrame()
    df['Название региона'] = region_names_list
    df['Показатель'] = data_value_list
    df['Федеральный округ'] = districts_name_list
    df = df.merge(df_regions, on='Название региона')
    print(df_regions)
    type_of_map = input('Выберети тип карты по цвету:'
                        '\n\tдискретная ч/б'
                        '\n\tдискретная цвет'
                        '\n\tнепрерывная ч/б'
                        '\n\tнепрерывная цвет'
                        '\n\tСкопируйте и вставьте ')
    if type_of_map == 'дискретная ч/б':
        df = df.sort_values(by='Показатель')
        df['Показатель'] = df['Показатель'].astype(str)
        marker_line_color = '#000000'
        color_sequence = px.colors.sequential.gray_r
    if type_of_map == 'дискретная цвет':
        df = df.sort_values(by='Показатель')
        df['Показатель'] = df['Показатель'].astype(str)
        color_sequence = px.colors.sequential.YlOrRd
        marker_line_color = '#000000'
    if type_of_map == 'непрерывная ч/б':
        color_sequence = 'gray_r'
        marker_line_color = '#000000'
    if type_of_map == 'непрерывная цвет':
        color_sequence = 'YlOrRd'
        marker_line_color = '#000000'
    fig = px.choropleth_mapbox(df, geojson=map,
                               locations='id',
                               color='Показатель',
                               hover_name='Название региона',
                               hover_data={'Федеральный округ': True, 'id': False},
                               color_discrete_sequence=color_sequence,
                               color_continuous_scale=color_sequence,
                               featureidkey='properties.cartodb_id',
                               mapbox_style='carto-position')
    fig.update_layout(mapbox_style="carto-positron",
                      mapbox_zoom=2, mapbox_center={"lat": 66, "lon": 94})
    fig.update_traces(marker_line_width=0.2, marker_line_color=marker_line_color)
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0},
                      title=f'{data_file.title()[:-5]} \n{get_data} в РФ, {unit}')
    offline.plot(fig, filename=data_file[:-5] + '.html')

chosen_map = input('Выберите карту:'
                   '\n\tСубъекты'
                   '\n\tОкруга')
if chosen_map == 'Субъекты':
    chosen_map = 'counties.json'
    chosen_regions = input('Выберите способ отображения:'
                           '\n\tПо субъектам'
                           '\n\tПо округам')
    if chosen_regions == 'По субъектам':
        data_for_counties()
    if chosen_regions == 'По округам':
        data_for_districts_counties_map()
if chosen_map == 'Округа':
    data_for_districts_districts_map()
    chosen_map = 'districts.json'

map(chosen_map)
