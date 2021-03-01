import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from MySort import MySort

def Cookie_Plot(InputFile):
    Nmeas = 1
    times = []
    times_avg = []
    
#   InputFile = "Cookie.txt"

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.InsertionSort(times)
    times_avg = Sorter.InsertionSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    
    time_mean = np.mean(times)
    time_std = np.std(times)
    
    #Ploting 
    
    Title = "Who Is Eating All My Darn Cookie!?"+ "\n" "Rate($\lambda$) = " + str(rate)+ "  Measurements/Experiment:"+ str(Nmeas)
    
    delta = 1
    xmin = min(times) - delta
    xmax = max(times) + delta
    q    = .2 #quantile
    qq   = .9  #Quantile
    n    = len(times)
    
    
    plt.figure()     
    plt.hist(times, Nmeas+1, density=True, facecolor='r', alpha=0.5,histtype='stepfilled', label = "Time",edgecolor='none')
    plt.axvline(x=time_mean, linewidth=1, color='g', label ="mean time")
    plt.axvline(x=time_mean+time_std, linewidth=1, color='b', label = "One-$\sigma$ ")
    plt.axvline(x=times[int(q*(n+1))] ,linewidth=1, color='g', label = "20th Quantile ",linestyle='--')
    plt.axvline(x=times[int(qq*(n+1))] ,linewidth=1, color='r', label = "90th Quantile ",linestyle='--')
    plt.axvline(x=time_mean+2*time_std, linewidth=1, color='b',linestyle='--', label = "Two-$\sigma$ ")
    plt.axvline(x=time_mean-time_std, linewidth=1, color='b')

    plt.xlabel('Time between missing cookie [days]')
    plt.ylabel('Probability')
    plt.xlim(xmin, xmax)
    plt.title(Title)
    plt.grid(True)
    plt.legend()

    plt.show()

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Cookie_Plot(str(InputFile))
    
