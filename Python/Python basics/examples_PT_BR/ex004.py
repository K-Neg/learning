x = input('Digite algo: ')
print('E letra --> {}', x.isalpha())
print('E numero --> {}', x.isnumeric())
print('E tudo --> {}', x.isalnum())
print('Só tem espaço -->', x.isspace())

print('O tipo primitivo desse valor é ', type(x))
