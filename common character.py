def common_str():
    str1=input('enter first string:')
    str2=input('enter second string:')
    s1=set(str1)
    s2=set(str2)
#     print(s1)
#     print(s2)
    lst=s1 & s2
    print('common charaters are',list(lst))
common_str()    