---
title: "Session 05 - Multiple genome comparisons"
author: "Leighton Pritchard"
output: 
  html_document:
    number_sections: yes
    theme: cosmo
    toc: yes
    toc_float: yes
---

<img src="data/JHI_STRAP_Web.png" style="width: 150px; float: right;"> 

## Learning outcomes

* Use `Mauve` to align multiple prokaryotic genomes, simultaneously
* Interpret `Mauve`'s visual output for multiple draft genome alignments
* Use `ACT` to visualise and interpret multiple genome alignments


## Introduction

As discussed in the lecture, multiple genome alignment is more "difficult" than pairwise genome alignment. It falls into a class of *NP-complete* problems that are only tractable by the use of *heuristics* - rules of thumb that give an approximate, rather than an optimal solution to the alignment problem.

You will use `Mauve` to align draft and reference genomes of *Elizabethkingia*, the outbreak example you met in session 03, and to visualise and interpret the alignment. Then you will conduct pairwise alignments for the same sequences, and visualise those comparisons in `ACT`. 

## The input dataset

Your examples are again the *Elizabethkingia* genomes from session 03, found in the directory `genome_data/Elizabethkingia`:

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

## Prepare a directory for output files

We will begin by preparing a new directory for our output files, called `session-05_output`. To do this we use the command `mkdir` (make directory), by issuing the following command at the terminal:

```
mkdir -p session-05_output
```

(the `-p` argument is used so that no error is reported if the directory already exists.)



## Run `Mauve`

`Mauve` is an alignment package produced by the Genome Evolution Laboratory at the University of Wisconsin-Madison, and can be obtained at [http://gel.ahabs.wisc.edu/mauve/](http://gel.ahabs.wisc.edu/mauve/). There are command-line and GUI versions of `Mauve`, but this activity will only use the GUI version.

The algorithm that `Mauve` uses is equally applicable to draft and complete genome sequences, and can be run in single, and *progressive* (i.e. iterated) modes. In this activity, you will use the *progressive* mode to align the two draft *Elizabethkingia* assemblies against the `GCF_000495995.1` (*E. anophelis* NUH1) reference.

***Exercise 1a (5min): Start `Mauve`***

* Start `Mauve` at the command-line with the command:

```
Mauve
```

You should be greeted by the splash screen, and then a window as below:

![Mauve start window](images/mauve1.png?raw=True =300x)

***Exercise 1b (15min): Specify sequences for alignment, and run `Mauve`***

From the `File` menu item, select `Align with progressiveMauve`. You should then see a file selection dialogue box:

![Mauve `File` options](images/mauve2.png?raw=True =200x)

![Mauve file selection dialogue](images/mauve3.png?raw=True =200x)

There are tabs available for you to change parameters related to the alignment - you should ignore these for now, but note the level of control you have over elements of the alignment algorithm:

![Mauve progressive alignment parameter options](images/mauve4.png?raw=True =200x)

![Mauve progressive alignment scoring options](images/mauve5.png?raw=True =200x)

* Select the files to be aligned. You should choose the reference sequence first (though this can be changed after the alignment), so use the following order:
1. `GCF_000495995.1.fasta` (*E. anophelis* NUH1 reference)
2. `GCF_000496055.1.fasta` (*E. anophelis* NUH11)
4. `SRR3240397_final.fasta` (outbreak isolate)
5. `SRR3240414_final.fasta` (outbreak isolate)

* Once the appropriate files have been selected, click on the button with the dots, next to `Output`, and specify the output file location `session-05_output/elizabethkingia.mauve`

* Next, click on the `Align…` button:

![Mauve progressive alignment file choices](images/mauve6.png?raw=True =200x)

A window will pop up, informing you of progress. This can be saved as a log of the alignment.

![Mauve progressive alignment progress window](images/mauve7.png?raw=True =400x)

When it is complete, which may take a short while, `Mauve` will present you with a visualisation of the draft genome alignment:

![Mauve alignment](images/mauve8.png?raw=True =400x)

The alignment view shows the *E. anophelis* NUH1 genome in the top row, followed by the other three genomes in the specified order. 

The major *local collinear blocks* (LCBs) are indicated in colour blocks. The lines indicate  within the blocks represent the sequence conservation of that region. The thin lines linking LCBs are guides to the eye, so that rearrangements can be seen quickly. Blocks above the line are aligned in the forward direction with respect to the input data, and those below the line are reversed with respect to the input.

***Exercise 1c (15min): Inspect the alignment, and interpret the result***

* How many LCBs are indicated in the alignment?
* Do LCBs lie within, or cross, contig boundaries?
* Do the genomes sppear to be well-aligned? Could reordering contigs potentially improve the alignment?

**HINT:** Draft genome contigs are indicated with contig boundaries marked as red lines (i.e. the regions between consecutive red lines indicate individual contigs). By dragging the mouse/cursor along this bottom row, you should see the currently active contig IDs change in the status bar at the bottom.

The alignment produces four output files: 

```
session-05_output/
├── elizabethkingia.mauve
├── elizabethkingia.mauve.backbone
├── elizabethkingia.mauve.bbcols
└── elizabethkingia.mauve.guide_tree
```

Other than the `.guide_tree` file, these outputs are all in `Mauve`-specific formats, and are not immediately helpful.

**NOTE:** while `Mauve` has identified LCBs and it is clear that there are some contigs that could be moved to improve the overall alignment, it has not actually performed these movements to rearrange the input data.

## Mauve Contig Mover (MCM)

At this point all the input contigs remain in their original order, and have not been moved. It would be useful to move contigs around so that the order of alignment is similar between all four draft genomes.

The `Mauve Contig Mover` (MCM) is provided to do this for us, but can only reorder contigs in a single genome, compared to a reference. You will use it to reorder the draft outbreak isolate genome `SRR3240397_final` against the *E. anophelis* NUH1 reference.

***Exercise 1d (15min): Reorder draft genome contigs***

* Select `Tools -> Move Contigs` from the menu:

![MCM menu](images/mcm1.png?raw=True =200x)

* Specify the directory in which to keep the resulting progressive Mauve output - use `session-05_output`:

![MCM directory selection](images/mcm2.png?raw=True =200x)

An informative message will appear

![MCM information](images/mcm3.png?raw=True =400x)

* Choose input files in the dialogue box.

**NOTE:** This process requires that your **reference** sequence is named first. Use the following order:

1. `GCF_000495995.1.fasta` (*E. anophelis* NUH1 reference)
2. `SRR3240397_final.fasta` (outbreak isolate)


![MCM file choice](images/mcm4.png?raw=True =200x)

* Click on `start`. This will bring up another log window that will inform you about progress. You will also see new alignment windows pop up from time to time, showing the progression of the alignment process

**NOTE:** This process may take a short while.

Unlike `Mauve` proper, `MCM` will place intermediate alignments and output in subdirectories `alignmentN` of the chosen output directory. This allows you to inspect individual alignments, and to recover the final reordering of your draft contigs, in a convenient way. 

* In this case the number of alignments required is 4, and you should take `alignment4` to be your final alignment. These files can be found in `session-05_output/alignment4/`

```
session-05_output/alignment4/
├── GCF_000495995.1.fasta
├── GCF_000495995.1.fasta.sslist
├── SRR3240397_final.fasta
├── SRR3240397_final.fasta.sslist
├── SRR3240397_final_contigs.tab
├── alignment4
├── alignment4.backbone
├── alignment4.bbcols
└── alignment4.guide_tree
```

* Inspect the order of contigs in the final alignment for the draft outbreak genome. Interpretation of the visualisation is the same as for progressive `Mauve`

The order of contigs on the bottom row will not necessarily be the same order as originally given to progressive `Mauve` (indeed, this is what we want!). 

![MCM final alignment](images/mcm5.png?raw=True =400x)

* How many LCBs are there in the final alignment?
* Do you think the final alignment could be improved?

In practical terms, `MCM` has the advantage of producing output with explicit ordering information, in the `session-05_output/alignment4/SRR3240397_final_contigs.tab` file, and the final `session-05_output/alignment4/` file has the input contigs reordered into the best alignment, as determined by `Mauve`.

***Exercise 1e (5min): Inspect the reordered contig files***

* Use `head` to inspect `session-05_output/alignment4/SRR3240397_final_contigs.tab`
* Use `grep '>' session-05_output/alignment4/SRR3240397_final.fasta` to see that contigs have been reordered with respect to the input sequence in `genome_data/Elizabethkingia/SRR3240397_final.fasta`

You will take this reordered set of contigs forward to a pairwise alignment for visualisation in `ACT`.


## Visualising reordered fragments and alignments in `ACT`

If you attempt to align a draft genome in multiple fragments, reordered or not, and visualise it in `ACT` without any further process, you will probably be disappointed with the results. For example, if you were to run the alignment below:

```
blastn \
  -query session-05_output/alignment4/SRR3240397_final.fasta \
  -subject session-05_output/alignment4/GCF_000495995.1.fasta \
  -outfmt 6 -out session-05_output/disappointing.crunch
```

and attempt to visualise the results in `ACT`, you will get a result that is impossible to interpret:

![ACT disappointment](images/disappointing.png?raw=True =400x)

The issue here is that `ACT` runs together alignments for the different fragments in each genome (indicated by the brown markers). Although the `.crunch` file contains enough information for an alignment viewer to render the alignment correctly by offsetting alignment co-ordinates appropriately, `ACT` does not currently do this. 

One solution is to stitch the contigs together into a single contiguous sequence before running the pairwise alignment, and you will do this using the `stitch_six_frame_stops.py` script in the `scripts` directory. This joins the contigs in the order presented in the input FASTA file, connecting them with the sequence

```
NNNNNCATCCATTCATTAATTAATTAATGAATGAATGNNNNN
```

which contains start and stop codons in all frames. You can do this by running:

```
stitch_six_frame_stops.py \
  -i session-05_output/alignment4/SRR3240397_final.fasta \
  -o session-05_output/alignment4/SRR3240397_stitched.fasta \
  --id=SRR3240397_stitched -v
```

***Exercise 2a (5min): Stitch contigs in the `GCF_000495995.1.fasta` reference, and reordered  `SRR3240397_final.fasta` file***

* Use the `stitch_six_frame_stops.py` script to create two new files: `session-05_output/alignment4/SRR3240397_stitched.fasta` and `session-05_output/alignment4/GCF_000495995.1.stitched.fasta`

**NOTE:** the script also generates a corresponding `.gff3` file for convenience, which details the locations of the original contigs on the output stitched sequence.

***Exercise 2b (5min): Run a pairwise `megaBLAST` alignment using the two stitched genomes***

**HINT:** modify the `blastn` code above and write output to `session-05_output/reordered_megablast.crunch`

* Visualise the resulting alignment in `ACT`
* How does the outbreak isolate compare to the reference? Is there a conserved sequence backbone? Are there rearrangements?

**HINT:** The final output should look like that below

![ACT success](images/success.png?raw=True =400x)