immutable_var = (5, "house", False)
print(immutable_var)
immutable_var = ([5, "house"], False) #"элеметы кортежа неизменяемые но, можно изменить если поместить список в кортеж"
print(immutable_var)
mutable_list = [1, "car", True]
print(mutable_list)
mutable_list[2] = "2"
print(mutable_list)
