import matplotlib.pyplot as plt
from numpy.random import normal
import gzip

with gzip.open('merged.ug2g1977.uganda_gwas4435.LDprunedMAF05.genome.gz', 'rt') as f:
    for line in f:
        break
    d_max = {}
    for line in f:
        l = line.split()
        ID1 = l[0]
        ID2 = l[2]
        IBD = float(l[9])
        try:
            IBD_max1 = d_max[ID1]
        except KeyError:
            IBD_max1 = -1
        try:
            IBD_max2 = d_max[ID2]
        except KeyError:
            IBD_max2 = -1
        if IBD > IBD_max1:
            d_max[ID1] = IBD
        if IBD > IBD_max2:
            d_max[ID2] = IBD
    x = list(d_max.values())
    print(x)
    plt.hist(x, bins=100)
#    plt.title("IBD")
    plt.xlabel("Maximum IBD per sample")
    plt.ylabel("Count")
    plt.savefig('merged.ug2g1977.uganda_gwas4435.LDprunedMAF05.genome.max.png')
