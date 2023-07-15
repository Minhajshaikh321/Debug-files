# num=4
def num_pattern(num):

    for row in range(num):
    #     print('row',row)
        val=row+1
        dec=num-1
    #     print('val',val,'dec',dec)
        for col in range(row+1):
    #         print('col',col)
            print(val,end=" ")
            val=val+dec
            dec=dec-1
        print()    

n=num_pattern(4)