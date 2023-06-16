# f.write() takes string 

def game():
    return 8086    # you can change the value returned

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
if hiScoreStr == '':  # or use "" ; but don't use <" ">
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
elif int(hiScoreStr) < score : # typecasting to integer score tw integer hunxa so
    with open("hiscore.txt", "w") as f:
        f.write(str(score))   # string ma typecasting







