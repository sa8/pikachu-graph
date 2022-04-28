import pickle

file = "DKG"
Data = pickle.load( open( "/Users/sazouvi/PL_Work/CLB2/make-graph/pickles/"+file+".p", "rb" ) )

for key, value in Data.items():
    for elt in value:
        if elt <34:
            print(key, elt)