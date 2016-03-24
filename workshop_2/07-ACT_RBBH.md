---
title: "Session 07 - Visualising RBBH with ACT"
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

* Use ACT to visualise and interpret RBBH comparisons
* Understand how RBBH comparisons relate to whole-genome comparisons


## Introduction

In the accompanying notebook you have generated the `.crunch` file `NC_004547_vs_NC_010694.crunch` representing an RBBH comparison of two bacterial genomes. You will now use `ACT` to visualise this comparison, and `BLASTN+` to generate a pairwise genome comparison with which to compare the results.

## The input dataset

The two bacterial genome sequences are located in the `rbbh_data` subdirectory:

* `rbbh_data/NC_004547.fna`
* `rbbh_data/NC_010694.fna`

Your RBBH output should be located in the current directory:

* `NC_004547_vs_NC_010694.crunch`

You will need to generate a new comparison file from the two bacterial genomes using `BLAST`.

## Generating the pairwise genome comparison

***Exercise 1 (5min): Use `BLASTN+` (with the `megaBLAST` algorithm) to generate an output file suitable for visualisation using `ACT`, in the file `NC_004547_vs_NC_010694.tab`.***

**HINT:** Use the Session 04 materials, if you need a reminder.

## Visualising the two comparisons

***Exercise 2 (15min): Use `ACT` to visualise both the RBBH and pairwise genome comparisons. Comment on the results.***

**HINT:** Use the Session 04 materials, if you need a reminder.

**HINT:** Using the `.gbk` files for the two sequences will show you genome features, as well as the genome sequence.

**HINT:** Your file input dialogue should look like that below:

![ACT dialogue](./images/act_dialogue.png?raw=true =400x)

**HINT:** Look at the region around 1084000nt in `NC_010694` (*ssrA*) - what do you see? What about at 209000nt (`NC_010694`, *purH*)?

* If there is genome-scale restructuring, propose a series of events that could lead to what you see.
* Do the RBBH and genome comparisons correspond exactly? If not, why not?
* If you wanted to identify similar genes in two genomes, would you rather use `BLASTN+` or reciprocal `BLASTP`?
* What tools could you use for a similar comparison if you didn't have a feature annotation with which to do RBBH?