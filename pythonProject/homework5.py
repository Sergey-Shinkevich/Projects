immutable_var = (5, True, 'Солнце')
print('immutable_var =', immutable_var)
# immutable_var[2] = 'Луна'
# Не разрешается менять значение кортежа, это его основное отличие от списка
mutable_list = [5, True, 'Солнце']
print('mutable_var =', mutable_list)
mutable_list[2] = 'Луна'
print('new mutable_var =', mutable_list)
