# Session 03 - ANI <img src="data/JHI_STRAP_Web.png" style="width: 150px; float: right;"> 

## Learning Outcomes

* Use Average Nucleotide Identity to compare and classify genomes
* Understand whole genome-based taxonomic classification
* Visualisation of all-against-all pairwise genome comparisons

## Introduction

In their 2007 paper, Goris *et al.* introduced ANI using BLAST (ANIb) as a substitute for experimental DNA-DNA hybridisation (DDH) for determining prokaryotic species boundaries. 

* Goris *et al.* (2009)["DNA-DNA hybridization values and their relationship to whole-genome sequence similarities."](http://dx.doi.org/10.1099/ijs.0.64483-0) *Int. J. Syst. Evol. Microbiol.*, **57**:81-91

The 2009 paper by Richter and Rosselló-Móra adapts the ANI method to use the MUMmer alignment package (ANIm). 

* Richter and Rosselló-Móra (2009) ["Shifting the genomic gold standard for the prokaryotic species definition"](http://dx.doi.org/10.1073/pnas.0906412106) *Proc. Natl. Acad. Sci. USA* **45**:19126–19131

By both methods, it is proposed that bacterial species boundaries lie in the 94-96% identity range of ANI score. That is: isolates with greater than ≈95% ANI identity should be considered the same species; those with lower should be considered different species.

The two methods are broadly equivalent, especially when sequence similarity is very high. The main difference is that `MUMmer` comparisons tend to be faster than `BLASTN+` comparisons, so ANIm is the quicker method. However, the ANIb method fragments the input sequences, leading to some bias/loss of information, whereas ANIm is by default more stringent in the selection of genome sequence regions for comparison, leading to some minor differences in classification.

ANIb and ANIm methods both  still require sequence alignment. This means that a decision, however reasonable, clear-cut, and automatable it might be, has to be made concerning what parts of the genomes are equivalent, and suitable for comparison. An alternative approach might be to use an alignment-free method that considers all the genome sequence information, without bias. Richter and Rosselló-Móra also proposed such a method in their 2009 paper, based on tetranucleotide frequencies (TETRA). 

Richter and Rosselló-Móra provided the [JSpecies](http://www.imedea.uib.es/jspecies/) software, which is written in Java, is GUI-based, and provides some summary graphics, in addition to ANIb, TETRA, and ANIm output. - as of March 2016 it has not been updated for over five years Here, we will use the more recent package `pyani` that performs the same calculations. The `pyani` package is written in Python, and is run at the command-line.

* JSpecies: [http://imedea.uib-csic.es/jspecies/](http://imedea.uib-csic.es/jspecies/)
* pyani: [http://widdowquinn.github.io/pyani/](http://widdowquinn.github.io/pyani/)

## The input dataset

Between November to March 2016, dozens of people in Wisconsin have been made ill, and there have been several deaths, due to a rare bacterial blood infection caused by the bacterium *Elizabethkingia*:

* [54 cases of Elizabethkingia in Wisconsin; one Michigan resident has died](http://fox6now.com/2016/03/20/54-cases-of-elizabethkingia-in-wisconsin-one-michigan-resident-has-died/) (Fox6Now, 20/3/2016)
* [Scientists scramble to trace source of blood infection in Wisconsin](http://www.startribune.com/scientists-search-to-unravel-mystery-behind-blood-infection-outbreak-in-wisconsin/372610031/) (StarTribune, 18/3/2016)
* [A Crash Course In Elizabethkingia, The Rare Bacterial Infection Spreading Across Wisconsin](http://www.wpr.org/crash-course-elizabethkingia-rare-bacterial-infection-spreading-across-wisconsin) [Wisconsin Public Radio 9/3/2016]

*Elizabethkingia* is an emerging pathogen in hospital environments, but is believed to be widespread harmlessly in water. It has also been [isolated from condensation on the Russian space station *Mir*](http://dx.doi.org/10.1078/072320203770865828) (*E.mircola*), and can be spread by insect vectors (*E.anophelis*).

As of 21/3/2016 there are 30 published genome sequences of this genus available at [NCBI](http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=308865). Genome assemblies for 18 of the outbreak isolates are available *via* Dr Kat Holt (University of Melbourne), at [https://github.com/katholt/elizabethkingia](https://github.com/katholt/elizabethkingia). We will analyse a subset of the available *Elizabethkingia* genome sequences with ANI, to attempt to classify them.

Genome sequences for analysis, including two outbreak isolates. are located in `genome_data/Elizabethkingia`.

```
genome_data/Elizabethkingia/
├── GCF_000401415.1.fasta
├── GCF_000447375.1.fasta
├── GCF_000495995.1.fasta
├── GCF_000496055.1.fasta
├── GCF_000769445.1.fasta
├── SRR3240397_final.fasta
├── SRR3240414_final.fasta
├── classes.txt
└── labels.txt
```

The outbreak strain IDs begin with the letters `SRR`.

## Running ANIm

To run ANIm with the `pyani` package, we use the `average_nucleotide_identity.py` script, at the command-line.

Open a new Terminal window, and make sure you can run the script by issuing the command:

```bash
average_nucleotide_identity.py -h
```

This will bring up the help/usage string for the script. As you will see, and as is common for command-line applications, there are many options that can be specified. Those that will be useful to us are:

* `-i`: to specify the input genomes
* `-o`: to specify where the output files will be written
* `-v`: to make the script tell us in detail what it is doing
* `-g`: to produce graphical output
* `-l`: to specify an output log file describing the analysis
* `--labels`: to specify labels for our genomes, on the graphical output
* `--classes`: to specify classes for our genomes, on the graphical output

By default, the script runs ANIm, though it can also perform ANIb and TETRA analysis.

### Running the analysis

Our genome files, as well as the files `labels.txt` and `classes.txt` are in the directory `genome_data/Elizabethkingia`. We want to write our output to a new directory, which we'll call `Elizabethkingia_ANIm`. 

It is good practice to retain a log file, for reproducibility, and to describe exactly what was done. We will put this in `Elizabethkingia_ANIm.log`

So, our command-line will be:

```
average_nucleotide_identity.py -v -g \ 
  -i genome_data/Elizabethkingia/ \
  -o Elizabethkingia_ANIm \ 
  --labels genome_data/Elizabethkingia/labels.txt \ 
  --classes genome_data/Elizabethkingia/classes.txt \  
  -l Elizabethkingia_ANIm.log
```

** EXERCISE 1 (10min): Enter this command at the terminal, and run it. **

**NOTE:** This will take a few minutes to complete (3min on my laptop, but it will be slower in the session)

### ANIm identity output

Open the file `Elizabethkingia_ANIm/ANIm_percentage_identity.pdf` that has been produced by your analysis, and inspect the figure.

The colour scheme has two regions: red and blue. Pairwise comparisons with >95% ANI identity are coloured red, those with <95% identity are coloured blue. Suggested species boundaries are given in the Goris and Richter papers as 95% identity.

The ATCC isolates of a species can be considered to be *reference* isolates, that define a species.

** EXERCISE 2 (10min): How many distinct species can you see in the dataset? **

* What are the species that you see?
* To which species do the outbreak isolates belong, according to this analysis?
* Do you see any potential problems with the data?

### Interpreting ANIm identity output

ANIm identity is calculated only for regions of a genome that are homologous. It is possible that two genomes might be compared that share very little overall homology (i.e. most regions of the genomes are not related), but where those regions that *are* homologous are very similar.

We can tell if this is the case in our analysis by inspecting the *alignment coverage* plot, which indicates how much of each genome was used in the pairwise alignment.

Open the file `Elizabethkingia_ANIm/ANIm_alignment_coverage.pdf` that has been produced by your analysis, and inspect the figure.

** EXERCISE 3 (5min): What is the extent of sequence homology in the dataset? **

* What is the typical percentage coverage of pairwise comparisons between species?
* Does this affect your interpretation in Exercise 2? If so, how?