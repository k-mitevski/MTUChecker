# MTUchecker
Python script for checking the maximum transmission frame size, on an interface.

Useful for testing the MTU/MRRU on interfaces, may come handy when setting up VPN tunnels, L2TP, to check for overhead.

The script works only on windows since it uses OS ping commands. 
It starts from 1200 bytes up to 1550 in 8 byte steps. Of course you can tune it to your preference.
