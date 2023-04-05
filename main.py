

# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(lambda x: x))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")



# transformation = lambda x: x

values = [1, 23, 42, "asdfg"]
transformed_values = list(map(lambda x: x, values))
if values == transformed_values: print('ok')
else: print('fail')

# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)