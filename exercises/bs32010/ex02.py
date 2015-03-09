# ex02.py
#
# Functions and data useful in exercise 2 (k-mer spectra) of
# the BS32010 course at the University of Dundee

bact_files = {"Mycoplasma genitalium": ("NC_018495.fna",
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
bacteria = bact_files.keys()
