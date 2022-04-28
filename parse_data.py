import os
import pickle

path = "/Users/sazouvi/PL_Work/CLB2/make-graph/data/"
os.chdir(path)

DKG = {}
Signing = {}

# we initialuze the dictionary with emptylist
# for now we won't go with more than 25 players anyway
for i in range(40):
    DKG[i] = []
    Signing[i] = []

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            currentline = line.split(",")
            #print(currentline[0], currentline[1],currentline[2])
            if currentline[0] == "DKG":
                stringTime = currentline[2][:-2]
                if stringTime[-2] == 'm':
                    time = float(stringTime[:-2])/1000.
                    DKG[int(currentline[1])].append(time)
                else:
                    time = float(stringTime[:-1])
                    if time<40: 
                        DKG[int(currentline[1])].append(time)
            if currentline[0] == "Signing":
                stringTime = currentline[2][:-2]
                if stringTime[-2] == 'm': # means the time is in millisecond                 
                    time = float(stringTime[:-2])/1000.                
                    # if time>5: 
                    #     print("more than 5s",currentline, time)
                    Signing[int(currentline[1])].append(time)
                else:
                    time = float(stringTime[:-1])
                    if time<14: 
                        Signing[int(currentline[1])].append(time)


# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}{file}"
        read_text_file(file_path)

pickle.dump( DKG, open( "/Users/sazouvi/PL_Work/CLB2/make-graph/pickles/DKG.p", "wb" ) )
pickle.dump( Signing, open( "/Users/sazouvi/PL_Work/CLB2/make-graph/pickles/Signing.p", "wb" ) )