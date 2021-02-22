# imports of external packages to use in our code
import sys
import numpy as np
from Random import Random


def generator_Of_Random_Coin(Seedd, Probb, Ntosss, Nexpp, Outputt):
    #Assignments of defaults
    Seed = 53422

    # Single coin-toss probability for "1"
    Prob = 0.3

    # number of coin tosses (per experiment)
    Ntoss = 10

    # number of experiments
    Nexp = 10

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob = ptemp
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Ntoss = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    Seed = int(Seedd)
    Prob = float(Probb)
    Ntoss = int(Ntosss)
    Nexp = int(Nexpp)
    random = Random(Seed)
    doOutputFile = True
    
    if doOutputFile == True:
         outfile = Outputt 
    else:
        outfile = "Flips.txt"
    
    if doOutputFile: #flag to check if there is file
        outfile = open(outfile, 'w+')
        for e in range(0,Nexp):
            for t in range(0,Ntoss):
                outfile.write(str(random.Geometric(Prob))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Ntoss):
                print(random.Geometric(Prob), end=' ')
            print(" ")
    return (outfile)

        
if __name__ == "__main__":
   
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print ("Usage: %s [-probability]" % sys.argv[0])
        print ("Usage: %s [-number of toss]" % sys.argv[0])
        print ("Usage: %s [-number of experiments]" % sys.argv[0])
        print ("Usage: %s [-name of output file]" % sys.argv[0])
        sys.exit(1)
        
    #read the user-provided seed from the command line (if there)
    seedd, probb, ntoss, nexp, outfile = sys.argv[1:6]
    generator_Of_Random_Coin(seedd, probb, ntoss, nexp, outfile)
    