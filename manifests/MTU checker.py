import ipaddress
import os

while True:
   try:
      ip = str(ipaddress.IPv4Address(input("Enter your target IP address: "))) #IP address input
      break
   except ValueError: #error detection and restart if wrong address is typed
     print("Invalid Address")

while True:
    try:
        error = []
        for sweep in range(1200,1550,8): #sweep byte range 1200 to 1550 bytes in 8byte step
            result = os.system('ping -s 1 -n 1 -f -l {} {}'.format(sweep,ip)) #execute ping command on windows
            if result == 1: #Isolate fragmented packets
                error.append("DF on: " + str(sweep)+ 'bytes') #append errors separately
        print('\n')
        print('\n'.join(error)) #print errors only, vertically

        break
    except KeyboardInterrupt: #
        exit()