# # function signature -> (name of func, parameter and their types, the return type)
# from typing import List

# a = 20

# def say_hello():
#     print("hello everyone!")
#     # return None

# # say_hello()

# def add(a: int, b: int, c: int = 10) -> int:
#     r = a + b 
#     return r

# a = 20
# """ This function shows scoping"""
# def g() -> int:
#     # global a
#     val = 21
#     global a
#     a += 1

#     def inner():
#         inner_val = 20
#         print(val + inner_val)
#         nonlocal val 
#         val += 1
#         return val**2
#     print(val)
    
#     return inner()

a = 23
def ad(b,c):
    d = b+c
    a = 25
    e = a + d
    print(a)
    return e
print(a)
print(ad(2,3))
# arr1 = []

# arr1.__iter__()

# # arr1.__ne

# print(g())
# print(a)

# r = add(2, b =3, c =4)
# print(r)

# arr = [1,2,3]

# def arr_sum() -> int:
#     return sum(arr)

# print(arr_sum())

# arr.append(10)

# print(arr_sum())

# print(r)

# def count_gen(n, chunk = 5):
#     i = 1

#     while i <= n:
#         yield i
#         i += chunk

# gen = count_gen(100)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# # print(gen)
