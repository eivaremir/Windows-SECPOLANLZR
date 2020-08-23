import Control09 
import sys
print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))
print(sys.argv[2])
input()

outdir = "C:\\Users\\EMORALES\\Documents\\Clientes\\Banistmo 2020\\ITGCs\\Dominio"

print("Windows Security Policies Anylyzer Core v0.9")
print("Author: Eivar Morales")
print("Working Directory: ",outdir)


# Executing Controls...
Control09.execute(outdir)
