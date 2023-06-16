# to print Python kun line no. ma xa

content = True
i = 1 # i is line counter
with open("log.txt") as f:
    while content:
        content = f.readline()
        
        if "python" in content.lower(): # avoids case sensitive; Python vaye pani python vayepani ; baal hunna 
            print(content)
            print(f"Yes python is present in line number {i}")

        i += 1

            
    
      
