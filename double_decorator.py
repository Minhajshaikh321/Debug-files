def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")


# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             print("enter another nonzero element")
#         else:    
#             #return
#             return func(a, b)
#     return inner
# @smart_divide
# def divide(a, b):
#     print('ans =',a%b)
# a=int(4)
# b=int(0)
# divide(a,b)