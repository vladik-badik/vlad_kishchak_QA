my_list= [2,3.5,4,6.33,7,8,9,10]
new_list=[]
for i in range(len(my_list)-1):
    new_list.append(my_list[i])
    avg= (my_list[i] + my_list[i+1]) / 2
    new_list.append(avg)

new_list.append(my_list[-1])
print(new_list)