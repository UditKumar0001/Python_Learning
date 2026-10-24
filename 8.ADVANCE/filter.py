# def even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False

a = [1,2,3,4,5,6,7,8,9,21,354,56,76,32,54,657]

# result = filter(even, a)

result = filter(lambda x : True if x%2 == 0 else False, a)

print(list(result))
        
