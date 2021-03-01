import sys
from Random import Random

def Cookie_Derp(Seedd, Ratee, Nmeass, Nexpp, OutputFileNamee):
    # default seed
    Seed = 5555

    # default rate parameter for cookie disappearance (rate =1, means a cookies per day)
    Rate = 1

    # default number of time measurements (time to next missing cookie) - per experiment
    Nmeas = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # class instance of our Random class using seed
    Seed = int(Seedd)
    Rate = float(Ratee)
    Nmeas = int(Nmeass)
    Nexp = int(Nexpp)
    random = Random(Seed)
    doOutputFile = True
    
    if doOutputFile == True:
        OutputFileName = OutputFileNamee 
    else:
        OutputFileName = "Cookie.txt"

    if doOutputFile:
        outfile = open(OutputFileName, 'w+')
        outfile.write(str(Rate)+"\n")
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                outfile.write(str(random.Exponential(Rate))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        print(Rate)
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                print(random.Exponential(Rate), end=' ')
            print(" ")
    
if __name__ == "__main__":
   
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print ("Usage: %s [-rate]" % sys.argv[0])
        print ("Usage: %s [-number of measurments]" % sys.argv[0])
        print ("Usage: %s [-number of experiments]" % sys.argv[0])
        print ("Usage: %s [-name of output file]" % sys.argv[0])
        sys.exit(1)
        
    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-rate' in sys.argv:
        p = sys.argv.index('-rate')
        ptemp = float(sys.argv[p+1])
        if ptemp > 0:
            rate = ptemp
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nmeas = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    seedd, rate, Nmeas, nexp, outfile = sys.argv[1:6]
    Cookie_Derp(seedd, rate, Nmeas, nexp, outfile)            