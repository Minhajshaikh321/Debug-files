
def sortfunc(s_list):
    for i in range(1,len(s_list)):
        while s_list[i-1]>s_list[i] and i>0:
            print('i-1',s_list[i-1],'i',s_list[i])
            s_list[i-1],s_list[i]=s_list[i],s_list[i-1]
            i-=1
    return s_list    
s_list=[3,5,1,7,9,17]
sortfunc(s_list)
