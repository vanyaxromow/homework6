my_dict = {'Ivan': 1994, 'Alina': 1998, 'Denis': 1989, 'Katya': 1985}
print(my_dict)
print(my_dict.get('Ivan'))
print(my_dict.get('Olya'))
my_dict.update({'Vasia': 1957,
                'Nastya': 1960})
d = my_dict.pop('Denis')
print(d)
print(my_dict)
my_set = {1, 2, 3, 4, 1, 2, 3, 4, True, 'Snake_Case', ('one', 'two', 'three')}
print(my_set)
my_set.update([17, (1, 2)])
my_set.remove('Snake_Case')
print(my_set)