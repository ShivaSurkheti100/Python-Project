
# list.sort() data lai increasing order ma rakxa

l1 = [1, 8, 7, 2, 21, 15]
#l1_sorted = l1.sort() # returns None type
#print(l1_sorted)
print(l1)
l1.sort() # sorts teh list / makes ordered sequence of data in increasing order
print(l1)

# list.reverse() reverses the elements of list
l2 = [ 2, 3,555, 7, 9459]
l2.reverse()
print(l2)

# list.append() used most of the times 
# it appends or adds element at the end of the list
l3 = [3, 4, 5, 44, 55, 56]
l3.append(45)
l3.append(575)
l3.append(100)
print(l3)

# list.insert()
l4 = [ 2.4, 5, 55, 78] 
l4.insert(2, 544) # inserts 544 at index 2
print(l4)

# list.pop()
l5 = [21, 32, 56, 5.7]
l5.pop(2) # removes element at index 2
print(l5)

# list.remove()

l6 = [True, False, "VTEN", 66, 7.9]
l6.remove("VTEN") # removes VTEN from list
l6.remove(True) # removes True from list
l6.remove(66)   # removes 66 from list
print(l6)
