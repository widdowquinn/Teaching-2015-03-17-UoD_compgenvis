# ex02.py
#
# Functions and data useful in exercise 2 (k-mer spectra) of
# the BS32010 course at the University of Dundee

import pandas as pd                
from collections import defaultdict
import os

bact_datadir = "genome_data/gc_content"
files = {"Mycoplasma genitalium": ("NC_018495.fna",
                                   "NC_018496.fna",
                                   "NC_018497.fna",
                                   "NC_018498.fna"),
         "Mycoplasma pneumoniae": ("NC_000912.fna",
                                   "NC_016807.fna", 
                                   "NC_017504.fna",
                                   "NC_020076.fna"),
         "Nostoc punctiforme": ("NC_010628.fna",),
         "Escherichia coli": ("NC_000913.fna",
                              "NC_002695.fna",
                              "NC_004431.fna",
                              "NC_010468.fna"),
         "Mycobacterium tuberculosis": ("NC_016934.fna",
                                        "NC_017523.fna",
                                        "NC_022350.fna",
                                        "NC_000962.fna")}
bacteria = files.keys()

bact_files = {}
for k, v in files.items():
    bact_files[k] = tuple([os.path.join(bact_datadir, fn) for fn in v])

def count_str_kmers(instr, k, kdict=None):
    """Counts sequences of size k in instr, populating kdict.
    
    Loops over instr with a window of size k, populating the
    dictionary kdict with a count of occurrences of each k-mer.
    Returns the dictionary kdict.
    """
    if kdict is None:
        kdict = defaultdict(int)
    for idx in range(len(instr)-k):
        kdict[instr[idx:idx+k]] += 1
    return kdict

def count_seq_kmers(inseq, k):
    """Counts kmers of size k in the sequence inseq.
    
    Counts kmers in forward and reverse directions, returning
    a Pandas dataframe of k-mer and count.
    """
    kdict = count_str_kmers(str(inseq.seq), k)
    kdict = count_str_kmers(str(inseq.reverse_complement().seq), k, kdict)
    df = pd.DataFrame.from_dict(kdict, orient="index")
    df.columns = ("frequency",)
    return df
