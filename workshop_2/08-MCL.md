---
title: "Session 08 - MCL protein clustering"
author: "Leighton Pritchard"
output: 
  html_document:
    number_sections: yes
    theme: cosmo
    toc: yes
    toc_float: yes
---

<img src="data/JHI_STRAP_Web.png" style="width: 150px; float: right;"> 

## Learning Outcomes

* Use **MCL** (Markov Clustering) to cluster protein sequences into groups of putative orthologues
* Comparison of RBBH and MCL-based orthologue prediction for the same dataset

**NOTE:** `OrthoMCL` <http://orthomcl.org/orthomcl/> is typically preferred over `MCL` for orthologue finding, but the principles are similar.

## Introduction

As discussed in the lecture, `MCL` (Markov Clustering) is a mathematical approach to generating clusters of similar sequences, given an input matrix of sequence similarity.

To identify putative orthologues, the input matrix is typically the result of an all-against-all `BLASTP` comparison for the protein complements of two or more genomes. This is then passed to the `MCL` package, which generates clusters on the basis of that data. These clusters are then interpreted as families of proteins, or putative orthologues.

The production of these clusters with `MCL` is a multi-step process (not unlike generating a `nucmer` alignment), and you will go through these steps in this session.

## The input dataset

The two bacterial protein complements are located in the `rbbh_data` subdirectory:

* `rbbh_data/NC_004547.faa`
* `rbbh_data/NC_010694.faa`

The pre-prepared `blastp` output is in the `mcl_data` subdirectory:

* `mcl_data/all-vs-all.tab`


## Generating the all-vs-all `BLASTP` output

The first step of `MCL` clustering analysis is to generate output describing the sequence similarities. You would do this using `blastp`.

To perform an all-against-all comparison, you would need to concatenate all protein sequences from the comparator protein sets into a single FASTA file, and then build a database from that file. You would use `blastp` to query those protein sequences against themselves.

In order to restrict the number of false positive associations between sequences, at the risk of failing to identify divergent pairs of sequences that are truly homologous, you would set the `blastp` E-value cutoff appropriately. For the data you will use, the threshold values was 1e-30.

The search takes a while so, to save time, it has been run for you already, and the output file `all-vs-all.tab` should already be in the `mcl_data` directory. This process is described in the script file `run_mcl_blast.sh`, in this directory.

***Exercise 1 (5min): Inspect the contents and size of `mcl_data/all-vs-all.tab` using `head` and `wc`***

## Creating the input matrix/network

The `MCL` package cannot take default `blastp` output directly. We need to modify the contents of `all-v-all.tab` to generate a file with three columns: `sequenceID1`, `sequenceID2`, and `Evalue`.

**NOTE:** We could have generated a suitable file directly with custom `blastp` output, but did not.

You will use the Linux `cut` command to generate an `.abc` file containing this data.

```
cut -f 1,2,11 mcl_data/all-vs-all.tab > mcl_data/all-vs-all.abc
```

***Exercise 2 (5min): Use the command above to create the `all-vs-all.abc` file, and inspect its contents with `head` and `wc` to confirm the data is appropriate.***

You will now use `MCL`'s `mcxload` command to create two files

* `mcl_data/seq.mci` will contain the initial matrix/similarity network information
* `mcl_data/seq.tab` will contain identifiers for the sequences in the matrix. 

If you enter `mcxload -h` at the terminal, you will see that it takes many different arguments. The ones we are concerned with are:

* `--stream-mirror`: when there is a hit for protein A to B, this connects A to B, and B to A with the same value
* `--stream-neg-log10`: log-transforms the E value
* `-stream-tf 'ceil(200)'`: restricts the log-transformed E value to 200 or less

```
mcxload -abc mcl_data/all-vs-all.abc \
  --stream-mirror --stream-neg-log10 -stream-tf 'ceil(200)' \
  -o mcl_data/seq.mci -write-tab mcl_data/seq.tab
```

***Exercise 3 (5min): Use this command to create `seq.mci` and `seq.tab` in the `mcl_data` subdirectory. Inspect the files with `head` and `wc`***

* How does `seq.tab` relate to `seq.mci`?

Mathematically-speaking, your `blastp` output has now been converted into a *graph*. The first column of each line in `seq.mci` represents a *node* in the graph (identified by an integer), and the second column describes the *edges* and their corresponding weights, in `node:weight` pairs.

Some information is being lost in this process. A `blastp` match between two sequences A and B may not produce the same E-value when run in each direction. The `--stream-mirror` argument assigns the "best" (i.e. smallest) E-value as the edge weight between each pair of sequences. 

## Clustering the network

You will use the `mcl` program to perform the clustering operation. 

`mcl` takes a single argument to control the *inflation value* used in the algorithm. We will only apply one setting in this session but in real use you would want to ensure that clustering is robust for your chosen inflation value by varying this setting, and seeing whether the output clusters change to a large, or small, degree.

Here, you will use an inflation value of 6, and generate the output file `mcl_data/out.seq.mci.I60`, using the command:

```
mcl mcl_data/seq.mci -I 6 -use-tab mcl_data/seq.tab -o mcl_data/out.seq.mci.I60
```

***Exercise 4 (5min): Use the `mcl` command to create `out.seq.mci.I60` in the `mcl_data` subdirectory. Inspect it with `head` and `wc`***

* What does each line represent?
* How do the contents relate to `seq.tab`?
* How many clusters are there?

In this output, each line represents a cluster of sequences, where the sequence IDs of members of the cluster are all given in tab-separated plain text format.

## Generating `.crunch` output for `ACT`

As you will have seen in the exercise, `MCL` output is a plain text file with a format of one line per cluster. Each member of the cluster is identified with its FASTA sequence ID, and members are separated with the tab character. This is not convenient output for visualisation, as there is no location or source information for each protein, and while we would like to see pairwise arrangements of "equivalent"/"orthologous" proteins, this information is implicit in group membership - not written directly.

A Python script, `mcl_to_crunch.py` is provided to convert your `MCL` output to a more useful `.crunch` file. This script is quite brittle, and intended to work only for this exercise. You can run it with the command below.

```
mcl_to_crunch.py
```

***Exercise 5 (5min): Use the Python script `mcl_to_crunch.py` to generate `.crunch` format output. Use `head` and `wc` to inspect it.***

* How many "orthologous" pairs does MCL find?

## Visualising `MCL` protein pairs with `ACT`

***Exercise 6 (15min): Use `ACT` to visualise both the RBBH and `MCL` analyses. Comment on the results.***

**HINT:** Use the Session 04 materials, if you need a reminder.

**HINT:** Using the `.gbk` files for the two sequences will show you genome features, as well as the genome sequence.

**HINT:** Your file input dialogue should look like that below:

![ACT dialogue](./images/act_mcl_dialogue.png?raw=true =400x)

**HINT:** Look at the region around 1267200nt in `NC_010694` (*ccmF*) - what do you see?

* Do the RBBH and `MCL` outputs correspond exactly? Is there good overall correspondence between the methods? If not, why not?
* Are multiple-member clusters consistent with the concept of orthology? How does this affect interpretation of the MCL output? 
* If you wanted to identify orthologous proteins in two genomes, would you rather use RBBH or `MCL`, and why?
* If you wanted to find all members of a protein family in two genomes, would you rather use RBBH or `MCL`, and why?
