import random

from models import Data
Data.create_table()
names = ['Kostya', 'Segrey', 'Ivan Ivanovich', 'Petr', 'Evgeniya', 'Ekaterina', 'Zhenya', 'Kirill', 'Anton', 'Vasya',
         'Igor', 'Viktor']

for name in names:
    Data.create(name=name, age=random.randint(18, 40))
