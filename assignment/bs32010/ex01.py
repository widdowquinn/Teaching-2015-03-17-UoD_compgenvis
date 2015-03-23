# ex01.py
#
# Functions and data useful in the 2015 assignment for the BS32010 course
# at the University of Dundee

from Bio import SeqIO  # For working with sequence data
from Bio.Graphics.ColorSpiral import get_color_dict  # For defining colours

import matplotlib.pyplot as plt  # For creating graphics

import pandas as pd  # For working with dataframes

import os  # For working with local files

bact_files = {"Dickeya": ("NC_012880.fna", "NC_012912.fna",
                          "NC_013592.fna", "NC_014500.fna"),
              "Klebsiella": ("NC_011283.fna", "NC_013850.fna",
                             "NC_016612.fna", "NC_017540.fna"),
              "Draft Genome": ("draft_genome.fasta",),
              "Pseudomonas": ("NC_004578.fna", "NC_007492.fna",
                              "NC_010322.fna", "NC_022808.fna"),
              "Staphylococcus": ("NC_004461.fna", "NC_013893.fna",
                                 "NC_017337.fna", "NC_007795.fna")}

bacteria = bact_files.keys()

unknown = pd.DataFrame([dict(species="Unknown", length=4338079, 
                             GC=0.5334391098, color=(1, 0.2, 0.2)), ])


def calc_size_gc(*names):
    """ When passed names corresponding to the bacteria
    listed in bact_files, returns a Pandas dataframe
    representing sequence length and GC content for
    each chromosome.
    """
    # Use a Pandas DataFrame to hold data. Dataframes are 
    # useful objects/concepts, and support a number of 
    # operations that we will exploit later.
    df = pd.DataFrame(columns=['species', 'length', 'GC', 'color'])
    # Get one colour for each species, from Biopython's 
    # ColorSpiral module
    colors = get_color_dict(names, a=6, b=0.2)
    # Loop over the passed species names, and collect data
    for name in names:
        try:
            for filename in bact_files[name]:
                ch = SeqIO.read(os.path.join('data', filename), 'fasta')
                ch_size = len(ch.seq)
                ch_gc = float(ch.seq.count('C') + ch.seq.count('G')) / ch_size
                df = df.append(pd.DataFrame([dict(species=name, length=ch_size, 
                                                  GC=ch_gc,
                                                  color=colors[name]), ]), 
                               ignore_index=True)
        except KeyError:
            print "Did not recognise species: %s" % name
            continue
    return df


# Plot chromosome size and GC data
def plot_data(dataframe, filename=None, return_fig=False):
    """ When passed a dataframe corresponding to the output
    of calc_size_gc, renders a scatterplot of chromosome length
    against GC content.
    """
    # One advantage of using a Pandas dataframe is that we can
    # operate on the data by the content of the data. Here we're
    # treating the dataframe as a series of subsets on the basis
    # of named species. This allows us to label our scatterplot
    # by species, too.
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(111)
    ax.set_position([0.15, 0.15, 0.45, 0.75])
    for k, sub in dataframe.groupby("species"):
        ax.scatter(x=sub.GC, y=sub.length, c=list(sub.color), label=k, s=50)
    ax.set_xlabel("GC content/%")
    ax.set_ylabel("chromosome length/bp")
    ax.set_title("Chr length vs GC%, grouped by species")
    leg = ax.legend(bbox_to_anchor=(1.0, 0.5), loc='center left')
    if filename is not None:
        fig.savefig(filename)
    if return_fig:
        return fig

