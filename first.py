a=[['--' ,'EM L AW', '--' ,'--', 'EM L AW'],
   ['BDLT L VB' ,'--', '--','--' ,'BDLT L VB'],
   ['CCS L ZM', 'BDA L AS', 'BDA L AS' ,'BC g VB / CC g ZM' ,'CCS L ZM'],
   ['--' ,'--' ,'--' ,'EM L AW' ,'BC g VB / CC g ZM'],
   ['--', '--' ,'CCS L ZM' ,'BDA L AS' ,'--'],
   ['EM L AW' ,'CCS L ZM' ,'BC g VB / CC g ZM' ,'BDLT L VB' ,'--']]
# o/p=[{"monday":"__","tudesday":"Em L AW","thursday":""......}]
week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
d=[]
list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in range(len(a)):
    d.append({})
    for j in range (len(a[i])):
        # print('d',d[i])
        d[i][list1[j]] = a[i][j]
        #print('d i ',d[i][list1[j]])
print(d)        