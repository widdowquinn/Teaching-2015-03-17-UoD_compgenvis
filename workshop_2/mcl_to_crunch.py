#!/usr/bin/env python
#
# mcl_to_crunch.py
#
# Helper script for the BS32010 workshop session covering use of MCL
# to generate clusters of protein sequences that are putative orthologues.
#
# (c)The James Hutton Institute 2016
# Author: Leighton Pritchard

import os
import itertools

from Bio import SeqIO
from collections import defaultdict

# Function to split a full sequence reference ID into only the last value
def split_seqid(seqid):
    return seqid.split('|')[-2]

# Function to read MCL cluster output into a list of tuples. Each tuple
# contains all members of a single MCL cluster
def read_mcl(filename):
    """Returns a list of tuples, where each tuple contains all the 
    sequence identifiers for a single cluster, described in an
    MCL cluster output file
        
    - filename, the MCL cluster output file
    """
    clusters = []  # The list of clusters
    with open(filename, 'rU') as fh:
        for line in [l.strip().split() for l in fh if len(l.strip())]:
            clusters.append(tuple([split_seqid(l) for l in line]))
    return clusters

# Function to process GenBank files into a dictionary of CDS features,
# keyed by protein ID, where the values are a tuple of (source, start, end, 
# strand) information.
def read_genbank(*filenames):
    """Returns a dictionary of CDS annotations, where the dictionary keys
    are the CDS protein ID accession numbers, and the values are
    (source, start, end, strand, id) information about the CDS location
    on the chromosome.
        
    - *filenames, the organism's GenBank annotation files
    """
    ft_dict = {}
    for filename in filenames:
        with open(filename, 'rU') as fh:
            record = SeqIO.read(fh, 'genbank')
            # Reconstruct the name in the corresponding .fna file
            record_name = '|'.join(["gi", record.annotations['gi'],
                                    "ref", record.id])
            for ft in [f for f in record.features if f.type == "CDS"]:
                ft_dict[ft.qualifiers['protein_id'][0]] = \
                    (record_name, int(ft.location.start), 
                     int(ft.location.end), ft.location.strand)
    print("Loaded %d features" % len(ft_dict))
    return ft_dict
                
# Function to split a full sequence reference ID into only the last value
def split_seqid_last(seqid):
    return seqid.split('|')[-1].split('.')[0]

# Function to create a .crunch file from our cluster and annotation data
def write_crunch(clusters, features, outdir="."):
    """Writes a .crunch format file describing our MCL output clusters.
    Match scores and percentage identities are set arbitrarily to 100%.
        
    - clusters, list of tuples produced by read_mcl
    - features, dictonary produced by read_genbank
    - outdir, directory in which to place output .crunch format files
    """
    # Loop over clusters, and store each pairwise combination in a 
    # suitable set
    pairs_dict = defaultdict(set)
    for cluster in clusters:
        pairs = itertools.combinations(cluster, 2)
        for pair in pairs:
            # Using sorted in this way ensures that each organism pair 
            # will be counted only once
            ft1, ft2 = sorted([features[pair[0]], features[pair[1]]])
            source1, source2 = (split_seqid_last(ft1[0]),
                                split_seqid_last(ft2[0]))
            if source1 != source2:
                key = "%s_vs_%s" % (source1, source2)
                pairs_dict[key].add((ft1, ft2))
    # Report the number of entries in each grouping/comparison,
    # and write files
    for k, v in pairs_dict.items():
        print("Comparison: %s, Matches: %d" % (k, len(v)))
        with open(os.path.join(outdir, "%s_mcl.crunch" % k), 'w') as fh:
            for ft1, ft2 in v:
                fh.write(" ".join(["100", "100",
                                   str(ft1[2]) if ft1[3] < 0 else str(ft1[1]),
                                   str(ft1[1]) if ft1[3] < 0 else str(ft1[2]),
                                   str(ft1[0]),
                                   str(ft2[2]) if ft2[3] < 0 else str(ft2[1]),
                                   str(ft2[1]) if ft2[3] < 0 else str(ft2[2]),
                                   str(ft2[0])]                                
                              ) + "\n")

if __name__ == '__main__':
    all_clusters = read_mcl("mcl_data/out.seq.mci.I60")
    clusters = [c for c in all_clusters if len(c) > 1]
    features = read_genbank("rbbh_data/NC_004547.gbk",
                            "rbbh_data/NC_010694.gbk")
    write_crunch(clusters, features)
