my_dict = {'Alena' : 2001, 'Artem' : 2002, 'Katya' : 1999, 'Sasha' : 2005}
print(my_dict)
print(my_dict.get('Artem'))
print(my_dict.get('Nina'))
my_dict.update({'Alena' : 1995, 'Artem' : 1998})
s = my_dict.pop('Katya')
print(s)
print(my_dict)

my_set = {3,5, 'Artem', False, 3, 'Artem'}
print(my_set)
my_set.update([22, 'Cloud'])
my_set.discard(3)
print(my_set)
