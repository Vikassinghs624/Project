# #write a program that will give us armstrong numbers between 1 to 1000
num = list(range(1,1000))
arm_list =[]
for i in num:
    j= str(i)
    if len(j) == 1:
        if (int(j))**3 == int(j):
            arm_list.append(int(j))
    if len(j) == 2:
        s =[]
        for k in j:
            s.append(int(k) ** 3)
        if sum(s) == int(j):
            arm_list.append(int(j))
    if len(j) == 3:
        l=[]
        for m in j:
            l.append(int(m)**3)
        if sum(l) == int(j):
            arm_list.append(int(j))



print(arm_list)
