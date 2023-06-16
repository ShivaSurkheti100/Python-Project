
story = "once upon a time there was a youtuber named Harry who uploaded Python Course with notes with nice explanation "
print(story[0:4])
# String Functions
print(len(story))
a = "MC SHIVA"
print(len(a)) # len() returns the length of string

print(story.endswith("on"))
print(story.endswith("explanation")) # string.endswith() tells whether variable string ends with notes or not i.e. for 'story' string
print(story.endswith("nn"))

print(story.count("with")) # string.count() counts the total no. of occurence of any character
print(story.count("a")) # most of the time used to count the character ; sometimes string as well

print(story.capitalize())
# string.capitalize() capitalize the first character of a given string

rapper = "VTEN is the best of best in NEPHOP. "
print(rapper.find("VTEN"))
print(rapper.find("is"))
print(rapper.find("i"))
print(rapper.find("VTE"))  
print(rapper.find("best")) # agadi ko 'best' ko positon ko output dinxa paxadi ko 'best' ko hoina
print(rapper.find("VTN")) # yesko output -1 i.e 'rapper' string ma 'VTN' xaina
# string.find(word) finds a word and returns the index of first occurence of that word in the string

print(rapper.replace("best", "champ")) # 'best' word ja ja xa; sablai replace garxa yo function le
# string.replace(old word, new word) replaces the old word with new word 