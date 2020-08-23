import sys
import SettingsParser
import Control09 

############################################################
# Gather the working directory
outdir = sys.argv[1]


############################################################
print("Windows Security Policies Analyzer Core v0.9")
print("Author: Eivar Morales")
print("Working Directory: ",outdir)

############################################################
# Parse Settings
print("Parsing Settings",outdir)
s = readXML(outdir)
print("Reading Sensitive Permissions")
SensPerms = parseSensitivePermissions(s)
print("Reading Audit Labels")
AuditLables = parseNoAuditLabels(s)


print("Settings read")
############################################################
# Read Script Processed Results

print("Reading script processed results...")
print("Reading groups.csv")
try:
    groups = pd.read_csv(outdir+"\\groups.csv", encoding = "ISO-8859-1")
except Exception as e:
    print("[Control 09] FATAL ERROR: "+str(e))

print("Reading users.csv")
usersMatrix = pd.read_csv(outdir+"\\UsersMatrix.txt", sep="|",encoding = "ISO-8859-1")
    

print("Script processed results read")
############################################################
# Executing Controls...
Control09.execute(outdir,groups,usersMatrix)
