
with open("poems.txt") as f:
    t = f.read()
    if "twinkle" in t:
        print("twinkle is present")
    else:
        print("twinkle is not present")

# old method
f = open("poems.txt")
t = f.read()
if "twinkles" in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
    
# sabai content read garnalai    
with open("poems.txt") as f:
    t = f.read()
    print(t)

