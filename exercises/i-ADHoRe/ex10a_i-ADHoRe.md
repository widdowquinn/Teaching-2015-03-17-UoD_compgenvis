# ex10_i-ADHoRe - Finding synteny with i-ADHoRe

## Prerequisites

This activity was written and tested using the following software versions, though others may work:

* **i-ADHoRe** 3.0.01 <http://bioinformatics.psb.ugent.be/software/details/i--ADHoRe>

# 1. Running i-ADHoRe

In this activity, you will employ `i-ADHoRe` to identify genomic collinearity and synteny in the two *Pectobacterium* and *Erwinia* genomes that were used in earlier exercises.

## Generating the input files

`i-ADHore` uses a configuration (`.ini`) file to describe program settings. This may be an unfamiliar approach to you, but it has advantages, such that settings are saved and recoverable and reusable, enabling *reproducibility* in science. This is not always true for GUIs, or when parameters are set at the command-line. This `.ini` configuration file needs to be generated.

`i-ADHoRe` also requires a set of `.lst` files containing lists of genes, one file per genome, with strands indicated in the format:

```
gene1-
gene2+
gene3+
...
```

and a file that lists the relationships between gene pairs. In this case, we are using RBBH, but that is not the only definition of relationships that can be useful. 

We construct this file this by concatenating `find_rbbh` activity output into the file `data/rbbh_data.tab` and cutting out the first two colums with the command:

```
$ cat ../data/rbbh_output/NC_004547_vs_NC_010694.tab ../data/rbbh_output/NC_004547_vs_NC_013421.tab | cut -f 1,2 > data/rbbh_data.tab
```

This then needs to be processed to use the correct feature locus tags. The Python script `generate_config.py` is provided to do this, and also to generate the i-ADHoRe config file. You should run this with:

```
$ python generate_config.py
```

which will generate `.lst` files in the directory `genome_lists`, as well as `rbbh_input.tab` and `i-ADHoRe_config.ini` in the current directory.

## Running i-ADHoRe

Now that the input and config files are written, `i-ADHoRe` can be run with the command:

```
$ i-adhore i-ADHoRe_config.ini
```

This will take a few seconds, produce many lines of output in your terminal, and will write a number of files to the directory `i-ADHoRe_activity`, including visualisations of the GHM for each alignment, e.g.

![GHM visualisation for *Pectobacterium* comparison](images/pecto_ghm.png?raw=True =300x)

and `.svg` files for each of the multiplicons (i.e. regions of collinearity) identified by `i-ADHoRe`:

![Multiplicon visualisation from `i-ADHoRe`](images/AlignmentMultiplicon7.png?raw=True =400x)

`i-ADHoRe` also produces a number of text files describing the relationships between the input genomes.

**ACTIVITY 1:** What proportions of each genome are collinear to each other? What proportion of each genome is repeated?

*HINT*: You will need to inspect `i-ADHoRe`'s output files to determine these results.

## What next?

As you will have seen above, `i-ADHoRe`'s output is thorough, but complex. Also, the default visualisations are not very user-friendly.

Move on to the next stage of this activity, by running the `i-ADHoRe.ipynb` iPython notebook. Issue:

```
ipython notebook
```

in the current directory.


