
## Use of f-string
name = "GoatX"
a = f"Hello, this is {name}"
print(a)

# ## Use of format method ;format method paila paila use huntho ; but don't use this ;; f - string is quite handy
# syntax : template.format(p1, p2, ...)

name = "Harry"
sentence = "The name of the Youtuber is {}".format(name)
print(sentence)

print("###############")

name = "Harry"
channel = "CodeWithHarry"
type = "Coding"
sentence = "This is {} and his {} channel is {}".format(name, type, channel)
print(sentence)

print("***********")

name = "Harry"
channel = "CodeWithHarry"
type = "Coding"
sentence = "This is {0} and his {2} channel is {1}".format(name, channel, type)
print(sentence)
# place the argument with index; index starts from 0
