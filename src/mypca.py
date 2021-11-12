import sys
import numpy as np
from easy_fun import *
from sklearn.decomposition import PCA


def my_PCA(inputmat):
    X = inputmat
    model = PCA(n_components=10)
    projection = model.fit_transform(X)
    return projection, model.explained_variance_ratio_

def main():
    sys.stderr.write("mypca V 1.0.0\n")
    try:
        infilename = sys.argv[1]
        metadataname = sys.argv[2]
    except:
        sys.stderr.write("Error")
        sys.exit(-1)
        
    try:    
        outfilename = sys.argv[3]    
    except:
        outfilename = "default_out"
        pass
    
    indata = easy_loadtable(infilename)
    metadata = easy_loadmetadata(metadataname)
    outfile = open(outfilename, "w")

    print("Input data size:",indata.shape, "Metadata size:", len(metadata))

    projection, var_explained = my_PCA(indata)

    print("PCA dim:", projection.shape)
    print("Explained variance: PC1:", var_explained[0], "PC2:", var_explained[1])

    easy_scatter(projection[:,0], projection[:,1], metadata, 1, "mypca")

    for i in  range(projection.shape[0]):
        outfile.write(str(projection[:,0][i]) + "\t" + str(projection[:,1][i]) + "\n")
    outfile.close()

if __name__ == "__main__":
    main()
