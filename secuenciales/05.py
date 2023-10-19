import os
os.system("cls")

gigabyte = int(input("gigabyte: ")) 

megabytes = gigabyte  * 1024
kilobytes = megabytes * 1024
bytes    = kilobytes * 1024

print( f"megabytes={megabytes:.2f}" )
print( f"kilobytes={kilobytes:.2f}" )
print( f"bytes={bytes:.2f}" )