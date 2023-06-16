
for i in range (2, 21): # tables from 2 to 20
    with open(f"tables/Mutliplication_table_of_{i}", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")
            '''if j!=10:
                f.write("\n") ; yetti use garda; 11 th line ma space aaudaina'''
    # break lagayo vane # table i = 2 samma matra chalxa
