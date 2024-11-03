immutable_tuple = (1,True,[5,6],'immutatable')
print(immutable_tuple)

# immutable_tuple[1] = False Попытка включения данной строки приводит к ошибке, так как элементы кортежа  изменить нельзя.
# Возможно изменение Элемента списка, который является элементом кортежа.

immutable_tuple[2][1] = 0
print(immutable_tuple)

mutable_list = [1,True,[5,6],'immutatable']
mutable_list[1] = False
print(mutable_list)

