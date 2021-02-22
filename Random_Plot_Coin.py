import matplotlib.pyplot as plt
import numpy as np
import sys
import math

def Rando_Plot(fname,p_0):
    Ntoss = 1
    p0= float(p_0)
    p1 = 1-p0
    haveH0 = False
    haveH1 = False
    
    Npass0 = []
    LogLikeRatio0 = []
    Npass1 = []
    LogLikeRatio1 = []

    Npass_min = 1e8
    Npass_max = -1e8
    LLR_min = 1e8
    LLR_max = -1e8
    
    InputFile0 = fname
        
    with open(InputFile0) as ifile: #Opens files
        for line in ifile: #
            lineVals = line.split() #splits lines ups
            Ntoss = len(lineVals) #obtains the number of toss
            Npass = 0 #defines the number of experiments
            LLR = 0
            for v in lineVals:
                Npass += float(v)
                # adding LLR for this toss
                if float(v) >= 1:
                    LLR += math.log( p1/p0 ) #transformation 
                else:
                    LLR += math.log( (1.-p1)/(1.-p0) )
                    
            if Npass < Npass_min:
                Npass_min = Npass
            if Npass > Npass_max:
                Npass_max = Npass 
            if LLR < LLR_min:
                LLR_min = LLR
            if LLR > LLR_max:
                LLR_max = LLR #Updates the number of current iterations 
            Npass0.append(Npass)
            LogLikeRatio0.append(LLR)

    if haveH1:
        with open(InputFile1) as ifile:
            for line in ifile:
                lineVals = line.split()
                Ntoss = len(lineVals)
                Npass = 0
                LLR = 0
                for v in lineVals:
                    Npass += float(v);
                    # adding LLR for this toss
                    if float(v) >= 1:
                        LLR += math.log( p1/p0 )
                    else:
                        LLR += math.log( (1.-p1)/(1.-p0) )

                if Npass < Npass_min:
                    Npass_min = Npass
                if Npass > Npass_max:
                    Npass_max = Npass
                if LLR < LLR_min:
                    LLR_min = LLR
                if LLR > LLR_max:
                    LLR_max = LLR
                Npass1.append(Npass)
                LogLikeRatio1.append(LLR)

    title = str(Ntoss) +  " tosses / experiment"
    
    # make Npass figure
    plt.figure()
    plt.hist(Npass0, Ntoss+1, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(Npass1, Ntoss+1, density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()

    plt.xlabel('$\\lambda = N_{pass}$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()

    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0, Ntoss+1, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(LogLikeRatio1, Ntoss+1, density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()

    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-file name]" % sys.argv[0])
        print ("Usage: %s [-P0 probability]" % sys.argv[0])
    file_name,probp0 = sys.argv[1:3]
    Rando_Plot(str(file_name),probp0)