### Binod(name) detector in python


import os  ## os module helps to access contents of directory
def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
        ## Detecting all forms of Binod like bInoD
        if "binod" in fileContent.lower():
            return True
        else:
            return False

if __name__ == "__main__":
    ## Listing all the contents of this folder
    dir_contents = os.listdir()# os.listdir() access contents of directory
    #print(dir_contents)

    nBinod = 0
    ## For each text file, run isBinod for them
    for item in dir_contents:
        # print(item)
        if item.endswith("txt"): # or use this syntax: if (".txt") in item: > print(item)
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)
            if(flag):
                print(f"******Binod is found in {item}******")
                nBinod += 1
            else:
                print(f"Binod not found in {item}")

print("******Binod Detector Summary*******")
print(f"{nBinod} files found with Binod hidden into them")

## detects both "Binod" and "binod" in fileContent.lower()

        




            
