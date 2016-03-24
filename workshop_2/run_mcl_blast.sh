#!/usr/bin/env bash
#
# run_BLAST.sh
#
# Short schell script to run all-vs-all BLAST job for example MCL
# clustering to find putative orthologues in three bacteria. This
# is for an activity in a UoD training workshop/course on 
# comparative genomics.

# Grab the protein sequences from the find_rbbh activity
cat rbbh_data/NC_004547.faa rbbh_data/NC_010694.faa > mcl_data/proteins.faa

# Build the BLAST protein database
makeblastdb -in mcl_data/proteins.faa -dbtype prot

# Run the BLASTP search (default parameters)
blastp -query mcl_data/proteins.faa -db mcl_data/proteins.faa \
    -out mcl_data/all-vs-all.tab -outfmt 6 -evalue 1e-30
