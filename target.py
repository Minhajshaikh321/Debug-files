def target(num,target):

    for i in range(len(num)):
        for j in range(len(num)):
            if num[j] + num[i]==target:
                a=[j,i]
    return a

num=[2,7,11]
pt=9
print(target(num,pt)) 