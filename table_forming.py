import pandas as pd
import numpy as np
import random
from pyproj import Proj, transform

lonlat = Proj(init="epsg:4326")
sphmerc = Proj(init="epsg:3857")


shape_kladr = pd.read_csv('annotation/shape_kladr.csv')
transformed_shape = []

for i, row in shape_kladr.iterrows():
    t_shp = []
    for sm in row['shape'][13:].replace('(','').replace(')','').split(','):
        sm_1, sm_2 = map(float, sm.split())
        # print(list(transform(sphmerc, lonlat, sm_1, sm_2)))
        t_shp.append(' '.join(map(str, list(transform(sphmerc, lonlat, sm_1, sm_2)))))
    
    transformed_shape.append(t_shp)

shape_kladr['transformed_shape'] = transformed_shape
n = shape_kladr.shape[0]

# Заданные соотношения
is_building_ratio = 0.8
amount_houses_ratio = 0.7
amount_pools_ratio = 0.1
amount_angar_ratio = 0.5
amount_teplica_ratio = 0.4

# Функции для генерации случайных значений
def generate_is_building():
    return 1 if random.random() < is_building_ratio else 0

def generate_amount_houses():
    if random.random() < amount_houses_ratio:
        return random.randint(1, 2)
    else:
        return 0

def generate_amount_pools():
    return 1 if random.random() < amount_pools_ratio else 0

def generate_amount_angar():
    if random.random() < amount_angar_ratio:
        return random.randint(1, 2)
    else:
        return 0

def generate_amount_teplica():
    if random.random() < amount_teplica_ratio:
        return random.randint(1, 2)
    else:
        return 0

new_columns = []
for i in range(n):
    is_building = generate_is_building()
    if is_building:
        amount_houses = generate_amount_houses()
        amount_pools = generate_amount_pools()
        amount_angar = generate_amount_angar()
        amount_teplica = generate_amount_teplica()

        new_columns.append([is_building, amount_houses, amount_pools, amount_angar, amount_teplica])
    else:
        new_columns.append([0, 0, 0, 0, 0])

shape_kladr[['is_building', 'amount_houses', 'amount_pools', 'amount_angar', 'amount_teplica']] = new_columns
shape_kladr.to_csv('go_to_prod.csv', index=False)
