def merge_the_tools(string, k):
    # your code goes here
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        print('len',len_temp)
        if item not in temp:
            temp.append(item)
            print('temp',temp)
        if len_temp == k:
            print('len_temp',len_temp)
            print (''.join(temp))
            print('temp',temp)
            temp = []
            len_temp = 0
string, k = "ABAAAC", 2
merge_the_tools(string, k)