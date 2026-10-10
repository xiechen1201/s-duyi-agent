def flatten(nested_list):

    for el in nested_list:
       if type(el) == list:
           yield from flatten(el)
       else:
           yield el


nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(list(flatten(nested)))
# [1, 2, 3, 4, 5, 6, 7, 8]
