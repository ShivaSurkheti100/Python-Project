

def greet(name):
    print(f"Good Morning, {name}")

# print(__name__)   # have to use here to print <m06_file1> in <m07_file2.py>
if __name__ == "__main__" :   #  __name__ evaluates to the name of module in Python
    n = input("Enter a name: ")
    greet(n)

# main is entry point
# 6th line ko further comment;look below 
# if the module is being run direclty from command line , __name__ is set to string  "__main__"
# for module being directly run ; __main__ print hunxa




