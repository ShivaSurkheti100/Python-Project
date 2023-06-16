
## Creating an empty dictionary
# a = { }

## Creating an empty set
b = set()

## Adding values to an empty set 
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5) # Adding a value repeatedly does not change a set
b.add(5)
b.add("laptop")
b.add(5.9)
b.add("4")
b.add((4, 6, 8)) # tuple can be added to set as tuple ko content cannot be changed

# b.add([3, 5, 6]) # List cannot be added in set; because list is hashable i.e list ko contents or elments can be changed
# b.add({4:5})     # dictionary also cannot be added to set ; kinaki ki dictionary ko contents can be changed
print(b)

## Length of the  set
print(len(b)) # prints the length of set

## Removal of an Item
b.remove((4, 6, 8)) # removes (4, 6, 8) from set b
# b.remove(48) # throws an error while trying to remove 48 (which is not present in the set)
print(b)

print(b.pop()) # removes an arbitrary element from the set and returns the element removed 
#  like 4 lai falyo vane 4 ani return garxa
print("")
print(b) # yo chai paxi baki vayeka  set b ko elements print gareko 
print(b.clear()) # returns NONE as b.clear empties set b
print(b) # prints  empty set i.e set()























