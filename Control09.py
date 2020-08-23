import pandas as pd
import numpy as np

CONTROL_NUMBER = 9
DEBUG = False

def execute(outdir):
    print("[Control 09] Executing...")
    #################################

    print("[Control 09] Reading groups.csv")
    try:
        df = pd.read_csv(outdir+"\\groups.csv", encoding = "ISO-8859-1")
    except Exception as e:
        print("[Control 09] FATAL ERROR: "+str(e))

    print("[Control 09] Reading users.csv")
    usersMatrix = pd.read_csv(outdir+"\\UsersMatrix.txt", sep="|",encoding = "ISO-8859-1")
    

    #################################
    print("[Control 09] Setting GROUP index")
    try:
        df.index=df['Group']
    except KeyError:
        print("Couldn't set new index")


    #################################
    #df loc[ boolean series ]
    #df.loc[df.iloc[:,0]=="Usuarios"]

    
    #################################
    print("[Control 09] Setting USERS index")
    try:
        #df = df.loc[['Users']]
        #booleandf =df.iloc[:,0].str.contains(r'^Usuarios$|^Users$')
        booleandf =df['Group'].str.contains(r'^Usuarios$|^Users$')
        
        df = texts = df.loc[booleandf]
    except KeyError:
        print("Couldn't index users")

    if(len(df)==0):
        print("[Control 09] ERROR: Seems like Users Local Group does not exist.")
    else:
        print("[Control 09] Found ",len(df)," users within the Users local group.")
    


    #################################
    # Validate Everyone Use
    print("[Control 09] Validating")
    userIssues = []
    notfound=[]
    for i in range(len(df)):
        Member = df.iloc[i].Member
        for u in range(len(usersMatrix)):
            # If the current i is in u (is defined in UsersMatrix.txt) 
            if usersMatrix.iloc[u].User == Member:
                # If the current user represents an exception
                if( usersMatrix.iloc[u].Exception=="true"):
                    userIssues.append(i)
                    #print("("+str(i+1)+") Exception found: " +directories.iloc[i].Directory_Name+ " -> " +AD_Object+ " -> " +permission)
                # continue with the next i
                break;
            ## If no known user where found with permissions
            if u == len(usersMatrix)-1:
                # append index to the array
                userIssues.append(i)
                notfound.append(Member)
                print("[Control 09] ("+str(i+1)+") User not identified: " +Member)
    print("[Control 09] Exceptions found: "+str(len(userIssues)))        


    #################################
    workprogramText=""
    if(len(userIssues)>0):
        workprogramText+="We observed the local users group have the following exceptions:\n\n"
        for ex in range(len(userIssues)):
            workprogramText+=df.iloc[userIssues[ex]].Member+"\n"
        workprogramText+="\nFor more details, check evidence #"+str(CONTROL_NUMBER)
    else:
        workprogramText="We observed that the members of the local user group are appropiate\n\nFor more details, check evidence #"+str(CONTROL_NUMBER)



    #################################
    exceptionFound = ''
    if(len(userIssues)>0):
        exceptionFound = 'Yes'
    else:
        exceptionFound = 'No'


    #################################
    # Prepare df for Alteryx Output
    print("[Control 09] Writing Files")
    res = np.array([CONTROL_NUMBER,workprogramText,exceptionFound],dtype='<U1000').reshape(1,3)
    wp_res = pd.DataFrame(res,columns=["Control_No","Results","Exception_Found"])


    #################################
    #Alteryx.write(df,1)
    df.to_csv(outdir+"\\09.csv")


    #################################
    wp_res.to_csv(outdir+"\\wp_09.csv",index=False)
    

    #################################
    pd.DataFrame(notfound,columns=['User']).to_csv(outdir+"\\not_found09.csv",index=False)#Alteryx.write(pd.DataFrame(notfound,columns=['User']),3)
    
    print("[Control 09] Executed")
    #################################



    #################################



    #################################
