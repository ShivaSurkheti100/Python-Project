
#  dictionary is the collection of key-value pairs --key means word and value means meaning analogically

myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"

}
print("Options are", myDict.keys())
a = input("Enter the Hindi word\n")
print("The meaning of your word is:", myDict[a]) 

# 13th line will not throw an error if the key is not present in the dictionary
# print("The meaning of your word is", myDict.get(a)) --> dict.get() avoids error and prints none
# program crash huna bata jogauna we have to avoid error sakesamma



