#How many unique substring in this string
"""
If Input is abad then output will be a , b , d , ab =5
if Input is abac then output will be a, b, c,ab,abc then = 4
"""

k = "abcdee"
lst=list(k)
print(lst)

result=[]
for i in lst:
	if i not in result:
		result.append(i)

print(result)
list_sub=[]
temp_str=''
for i in range(len(lst)):
	temp_str=temp_str+lst[i]
	list_sub.append(temp_str)


print(list_sub)

ord_str_list=[]
for i in list_sub:
    tem_value=sorted(i)
    if len(tem_value)>= 2:
        count = 0
        for i in range (len(tem_value)-1):
            if tem_value[i]==tem_value[i+1]:
                count +=1
        if count == 0:
            ord_str_list.append(tem_value)

print(ord_str_list)

total=len(ord_str_list)+len(result)
print(total)

