lst = ['abc','kbd','klpd','aab']
lst2 = sorted(lst)
print (lst2)
lst2 = sorted(lst,reverse=True)
print(lst2)

#dictionaries and sets
#basket is a set, uses same method to create as dictionary, except
#we dont use the associative values

basket = {'apple', 'mango', 'pear', 'peach', 'orange'}

# print the set
print("full basket: ",basket)

#test for members
print("'orange' in basket: ", 'orange' in basket)
print("'pineapple' in basket: ", 'pineapple' in basket)
print("'peach' not in basket: ", 'peach' not in basket)

#dictionaries have the associative values for easy lookup
#eg, a list of employees with specific skills associated

dic = {'HON':109, 'Rockwell':89, 'Thales':75}

print("The dictionary is: ", dic)

dic['Boeing'] = 100

print("The dictionary is: ", dic)

print("Honeywell value is: ", dic['HON'])

del dic['Rockwell']

print("The dictionary is: ", dic)

print("Intel is in the list: ", 'Intel' in dic)
