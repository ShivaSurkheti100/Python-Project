# string format() method allows you to format selected parts of a string

name = "GoatX"
passion = "maths"
marks = 98

sentence = "Its me your boy {}. I like {} so I obtained {} marks in it"
print(sentence.format(name, passion, marks))

sentence = "Its me your boy {}. I like {} so I obtained {:.0f} marks in it"
print(sentence.format(name, passion, marks))

sentence = "Its me your boy {}. I like {} so I obtained {:.1f} marks in it"
print(sentence.format(name, passion, marks))

sentence = "Its me your boy {}. I like {} so I obtained {:.2f} marks in it"
print(sentence.format(name, passion, marks))

sentence = "Its me your boy {}. I like {} so I obtained {:.3f} marks in it"
print(sentence.format(name, passion, marks))

sentence = "Its me your boy {}. I like {} so I obtained {:.4f} marks in it"
print(sentence.format(name, passion, marks))

## Using Index numbers:
sentence = "I am {0} . I brought {1:.2f} marks at maths due to my good interest at {2}"
print(sentence.format(name, marks, passion))

