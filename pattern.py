# def pyfunc(r):
#     for x in range(r):
#         print(' '*(r-x-1)+'*'*(2*x+1))    
# pyfunc(9)

# pattern1:increasing triangle
# def pattern(n):
#     # pattern 2 for dicreasing traingle
#     for i in range(n):
#         for j in range(i,n):
#             print('*',end=" ")
#         print()
# pattern(5)    

# pattern9 prism pattern
def pattern2(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for k in range(i):
            print("*",end=" ")
        for m in range(i+1):
            print("*",end=" ")
        print()
pattern2(5)        