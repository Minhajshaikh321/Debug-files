from collections import Counter
def collections(size_price,n):
        p =0
        for i in size_price:
            print('i',i)
            if i[0] in n.keys() and n[i[0]] >0 :
                print(n)
                n[i[0]] = n[i[0]]-1
                print('n',n)
                p = p+i[1]
                print(p,'p')
        print(p)
num_shoes  = int(input())
print('num_shoes',num_shoes)
sizes = map(int,input().split())
print('sizes',sizes)
num_cust  = int(input())
print('num_cust',num_cust)
size_price = map(tuple,(map(int,input().split()) for _ in range(num_cust)))
print('size_price',size_price)
n = Counter(size_price)
collections(size_price,n)
print(collections)        