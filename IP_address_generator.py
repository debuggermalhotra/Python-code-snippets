#Generating random IP address
from random import randint
import sys


octet2=randint(0,255)
octet3=randint(0,255)
octet4=randint(0,255)


IPclass=input("What do you want to be the class of IP address? (A/B/C/D/E): ")

if IPclass == 'a' or IPclass=='A':
        octet1=randint(0,127)
elif IPclass == 'b' or IPclass=='B':
        octet1=randint(128,191)
elif IPclass == 'c' or IPclass=='C':
        octet1=randint(192,223)
elif IPclass == 'd' or IPclass=='D':
        octet1=randint(224,239)
elif IPclass == 'e' or IPclass=='E':
        octet1=randint(239,255)
else:
    print("Please enter a valid class!!")
    sys.exit(1)

print("\n\nHere is an IP address for you: ")
print(str(octet1)+"."+str(octet2)+"."+str(octet3)+"."+str(octet4))

        
        

    
        
        

        
        
        

