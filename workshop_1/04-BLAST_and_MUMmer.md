# Session 04 - Pairwise genome comparisons <img src="data/JHI_STRAP_Web.png" style="width: 150px; float: right;"> 

## Learning Outcomes

* Use BLASTN and MUMmer at the command-line to compare prokaryotic genomes
* Interpret MUMMer dotplot output
* Use ACT to visualise and interpret pairwise genome alignments
* Use ACT to compare and interpret pairwise genome alignments

## Introduction

You will be comparing two relatively small, closely-related complete genomes using *pairwise sequence alignment*. The chosen genomes are relatively small so that all alignments should be fast. Also, being closely-related, we should see relatively little divergence between genomes. 

The two packages you will use to perform alignment are `BLAST+` and `MUMmer`. These are very widely-used alignment tools that employ quite different alignment algorithms, and have contrasting command-line syntax. They have been chosen to illustrate differences between bioinformatics tools that do the "same job".

You will run `BLASTN+` comparisons with two different algorithms, as discussed in the lecture: `BLASTN` and `megaBLAST`, and compare the outputs using the visualisation tool `ACT`.

You will also run a `mummer` comparison on the same genomes, and compare this output to that of the `megaBLAST` algorithm, again using `ACT`.

## The input dataset

The examples chosen are completely sequenced bacterial genomes, so there should not be any awkward issues with fragmentation, rearrangements or scaffolding. This is simpler than many current real-world applications.

You will compare the *E. coli* O157:H7 Sakai chromosome (`NC_002695.fna` - causes acute haemorrhagic diarrhoea) with that of *E. coli* CFT 073 (`NC_004431.fna` - causes urinary tract infections), using **megaBLAST** and **MUMmer**. These two bacteria are different isolates of the same bacterial species. Although they have distinguishable phenotypes, it is reasonable to expect them to be closely related at the sequence level.

The genomes are located in `genome_data/Ecoli`:

```
genome_data/Ecoli/
├── NC_002695.fna
└── NC_004431.fna
```

## Prepare a directory for output files

We will begin by preparing a new directory for our output files, called `session-04_output`. To do this we use the command `mkdir` (make directory), by issuing the following command at the terminal:

```
mkdir -p session-04_output
```

(the `-p` argument is used so that no error is reported if the directory already exists.)


## Run default `BLASTN+` (`megaBLAST`) comparison

As discussed in the lecture, the `BLAST+` package uses the `megaBLAST` algorithm - this behaviour is different from that of older versions of `BLAST` (known as "legacy BLAST").

To compare two nucleotide sequences, such as the *E. coli* genomes, we use the program `blastn`. To be sure that you can use `blastn`, issue the following command at the terminal:

```
blastn -h
```

You should see a short account of the options available for running `BLAST`. The options of interest to us are:

* `-query`: the location of the query sequence
* `-subject`: the location of the subject sequence
* `-outfmt`: the format you want your output in; here you want *tabular* format (option `6`)
* `-out`: the location you want to write your output to

We also want to time how long it takes to run this command, as a measure of the efficiency of the algorithm/alignment software (though better methods are available, we only need a rough estimate). To do this, we use the program `time`, which reports how long a command takes to run.

So, your command line will be:

```
time blastn \
  -query genome_data/Ecoli/NC_002695.fna \
  -subject genome_data/Ecoli/NC_004431.fna \
  -outfmt 6 \
  -out session-04_output/E_coli_megablast.tab
```

This will produce a plain text table of aligned regions between each genome, with one region per line.

** EXERCISE 1 (5min): Enter this command at the terminal, and run it **

**NOTE:** The command should execute and finish very quickly.

* How long did this comparison take to run?
* Check that the output was written correctly by issuing the command `head session-04_output/E_coli_megablast.tab`
* Use the command `wc -l session-04_output/E_coli_megablast.tab` to count the number of lines in the file.


## Run the legacy-style `BLASTN` comparison

You can make `BLASTN+` run the old (legacy-style) `BLASTN` algorithm search on the two *E. coli* genomes, by specifying the argument `-task blastn`.

** EXERCISE 2 (5min): Modify the `BLAST` command from exercise 1 to use the `BLASTN` algorithm, using the `-task blastn` argument. Write the output to the file `session-04_output/E_coli_blastn.tab` **

* How long did the alignment take to run? Which algorithm do you think is more efficient?
* Use the `head` and `wc` commands to inspect the output file. Do the results differ from the `megaBLAST` output? If so, how?


## Run `MUMmer` (`nucmer`) comparison.

As discussed in the lecture, `MUMmer` works quite differently to `BLAST` as an algorithm. It is also very different to use at the command-line, requiring multiple commands to produce an alignment and analysis, so you may find it useful to inspect the documentation ([link](http://mummer.sourceforge.net/manual/)) from time to time.

**NOTE:** `MUMmer` is both the name of a suite of alignment programs, as well as an alignment program (`mummer`) within that suite. This can be confusing at times.

You will use the `nucmer` package from `MUMmer` to perform the comparison. This is actually a script that implements a full pipeline of analysis, using `mummer` as its aligner. This pipeline allows multiple reference and multiple query sequences to be aligned in a many-to-many alignment. That makes `nucmer` particularly useful for scaffolding assembly contigs, or other fragmented sequences together against a reference genome. 

Applying `nucmer` to genome alignment is more involved than running a `blast` alignment. There are several stages to the analysis, and more are required when you want to produce visualisations or readily-interpretable output. These are:

1. Use `nucmer` to identify matching regions, producing a `.delta` file.
2. Use `delta-filter` to remove weaker matches from the `.delta` file output, and produce a `.filter` file.
3. Use `show-coords` and/or `show-aligns` to generate human-readable output from the `.delta` and/or `.filter` files.
4. Use `mummerplot` to visualise the filtered matches in the `.delta` or `.filter` files.

To perform the alignment you would use the `nucmer` command. You should issue `nucmer -h` at the terminal to ensure that it is installed.

The `nucmer` program can take many options to control how alignment is performed, and for this exercise we will be interested in the following:

* `--maxgap`: the largest allowed gap between adjacent matches in a cluster (≈how close homologous stretches must be to be considered a *cluster*)
* `--mincluster`: the minimum length of a cluster of matches (≈smallest homologous region)
* `--prefix`: a prefix for files that will contain your output alignment and other information

The program then takes the locations of the two files to be aligned as the final two arguments. As the algorithm produces a *symmetrical* alignment, the order of these sequences doesn't matter. So, your first command would be:

```
time nucmer --maxgap=500 --mincluster=100 \
  --prefix=session-04_output/E_coli_nucmer \
  genome_data/Ecoli/NC_002695.fna \
  genome_data/Ecoli/NC_004431.fna
```

** EXERCISE 3a (5min): Run the above command at the terminal **

* How long did the command take to run?
* What is the name of the output file that is written? What does it look like (**HINT:** use `head` and `wc -l`)?
* Is this easy to read, compared to `BLAST` output?

To generate more human-readable output, you can use the `show-coords` command, giving it the  `.delta` file you just generated as output. To place the modified data into the file `session-04_output/E_coli_nucmer.coords`, you can use the *redirection* symbol, as in the commmand:

```
show-coords -r session-04_output/E_coli_nucmer.delta > \
  session-04_output/E_coli_nucmer.coords
```

** EXERCISE 3b (5min): Run the above command at the terminal **

* Inspect the output file using `head`. Do you find this output easier to understand?

You can use the `show-aligns` command to see the aligned regions directly, indicating single-base changes, and larger insertions and deletions. 

```
show-aligns session-04_output/E_coli_nucmer.delta \
  "gi|15829254|ref|NC_002695.1|" \
  "gi|26245917|ref|NC_004431.1|" > \
  session-04_output/E_coli_nucmer.aligns
```

**NOTE:** the `show-aligns` command requires you to know and use the FASTA sequence IDs of your query and reference sequences - you can get these from the FASTA file.


** EXERCISE 3c (5min): Run the above command at the terminal **

* Inspect the output file using `head`. Do you find this output useful?

So far, you have been looking at the 'raw' alignment data. The `delta-filter` command can be used to restrict this output only to a subset of more informative matching regions. There are many options that can be used, and the ones we employ here are:

* `-q`: map each position in the query only to its best match in the reference
* `-r`: map each position in the reference only to its best match in the query

```
delta-filter -q -r \
  session-04_output/E_coli_nucmer.delta > \
  session-04_output/E_coli_nucmer.filter
```

** EXERCISE 3d (5min): Run the above command at the terminal **

* Inspect the output file using `head`.
* Make this output more human-readable with `show-coords`, writing the output to `session-04_output/E_coli_nucmer_filtered.coords`, and inspect the output.
* Has the filtering affected the number of reported matches? (**HINT:** use `wc -l` to count rows before and after filtering)

`MUMmer` provides tools for graphical visualisation of its output as dotplots. The `mummerplot` program is used for this, and can take many arguments for presentation. Those that concern us here are:

* `--pdf`: Render PDF output
* `-R`: plot ordered *reference* sequences from the named file
* `-Q`: plot ordered *query* sequences from the named file
* `--prefix`: prefix for output files

```
mummerplot --png \
  session-04_output/E_coli_nucmer.filter \
  -R genome_data/Ecoli/NC_002695.fna \
  -Q genome_data/Ecoli/NC_004431.fna \
  --prefix=session-04_output/E_coli_nucmer
```

** EXERCISE 3e (5min): Run the above command at the terminal **

**NOTE:** you may see some command-line warnings about deprecation - these can be ignored

* Generate a visualisation of the `E_coli_nucmer.delta` output file, and compare this with the plot generated from `E_coli_nucmer.filter` output.

## Visualising comparisons using ACT

`ACT` is an extension of the `Artemis` genome browser ([homepage](http://www.sanger.ac.uk/resources/software/artemis/#download)) designed to visualise genome comparisons. The software is free, and was developed at The Wellcome Trust Sanger Institute, and is widely used for genome annotation.

* `Artemis` manual: ([link](ftp://ftp.sanger.ac.uk/pub/resources/software/artemis/artemis.pdf))
* `ACT` manual: ([link](ftp://ftp.sanger.ac.uk/pub/resources/software/act/act.pdf))

`ACT` and `Artemis` will take sequence data in `FASTA` format, and annotations in `GFF` format. They will also read combined sequence and annotation data in `GenBank` format. Genome comparison data can be read in two essentially equivalent formats: `.crunch` files, and `BLAST` tabular output.

In this part of the session you will use ACT to visualise and compare the outputs of the `BLAST` and `MUMmer` comparisons you generated, above.

`ACT` can be started from the terminal with the command

```
act
```

** Exercise 4a (5min): Start `ACT` from the command-line **

You should see the splash screen indicated below:

![ACT splash screen](./images/act_fig1.png?raw=true =200x)


### Compare `BLAST` and `megaBLAST` output

You will have found above that the outputs of `BLASTN` and `megaBLAST` produced different output. To become more familiar with using `ACT` you will load in the two alignments, by following the instructions below.

* Use the `File -> Open` menu option to obtain the file selection dialogue box

![ACT file selection dialogue](./images/act_fig2.png?raw=true =200x)

* click on the `more files ...` button to obtain an option to enter a third sequence file (`Sequence file 3`):

![ACT file selection dialogue (expanded)](./images/act_fig3.png?raw=true =200x)

* Use the `Choose ...` buttons to select the `genome_data/Ecoli/NC_004431.fna` FASTA file for sequence files 1 and 3, and the `genome_data/Ecoli/NC_002695.fna` FASTA file as sequence file 2:

![ACT file selection dialogue (sequences selected)](./images/act_fig4.png?raw=true =200x)

* Use the `Choose ...` buttons to select the `session-04_output/E_coli_blastn.tab` and `session-04_output/E_coli_megablast.tab` files as comparison files 1 and 2, respectively:

![ACT file selection dialogue (all files selected)](./images/act_fig5.png?raw=true =200x)

* Then click the `Apply` button. 

You will see a notification window to say that some hits were flipped to match sequence orientation, and the main window will showing a portion of the genome alignment:

![ACT initial alignment view](./images/act_fig6.png?raw=true =400x)

In this view, the top pair of grey bars, and the bottom pair of grey bars each indicate the forward and reverse strands of the `NC_004431` (*E. coli* CFT 073) sequence. The centre pair of grey bars indicate the forward and reverse strands of the `NC_002695` (*E. coli* O157:H7) sequence. If there were functional annotations loaded for these sequences, they would be placed on these bars. However, we are currently looking only at the nucleotide sequences.

The red bars connecting each of the genomes indicate the locations of the sequence alignments you calculated. The top set are those from the `BLAST` comparison, and the bottom set are those from the `megaBLAST` comparison. As you can see in the figure above, they are very similar but not identical.

Use the scrollbars on the right-hand side (next to the genome tracks) to zoom out, and show the complete alignment:

**NOTE:** this can be quite fiddly on a small monitor - it may be helpful to maximise the `ACT` window to full-screen.

**Hint:** double-clicking on any of the red or blue alignment links will turn them yellow, and align the two connected genomes at that location, as you can see below. Selecting a link in this way also reports useful information about the alignment, on the left-hand side of the window.

![ACT initial alignment, zoomed out](./images/act_fig7.png?raw=true =400x)

Both `BLAST` and `megaBLAST` report many matches and there is a confusing mass of lines criss-crossing between many regions of the genomes.

To simplify the view, low-scoring alignments can be filtered, using the scroll-bars to the right of the screen. Applying the maximum filtering level makes the genome similarities clearer:

![ACT alignment, filtered](./images/act_fig8.png?raw=true =400x)

**HINT:** Filtering the large number of weak hits also speeds up the graphical rendering.

Now we can see that there are many large regions of similarity along the genome backbones, indicated by the red connections between genomes.

Red connections represent matches that run in the same direction on the two genomes being compared, and blue connections indicate alignments that run in opposite directions on each genome. (though note that `ACT` allows you to flip the orientation of any genome, interactively).

We can see from the 'wall' of red connections quite quickly that these two genomes are very similar across most of their lengths, and that the larger alignments are all in the same order.

However, there are many smaller alignments - mostly in blue - that appear to radiate from a single point on the `NC_004431` genome, to many points on the `NC_002695` genome, and *vice versa*. These are indicative of repeated regions of sequence similarity, which may suggest (for bacteria) phage integration, or other repetitive elements.

This kind of view also draws attention to the regions between alignments - where the two genomes differ. There are 'wedge-like' gaps - small in one genome, large in the other - that suggest an insertion or deletion in one or other genome. There are also gaps that are of approximately equal size in each genome, which may indicate sequence divergence at that location, or a common insertion site.

#### Genomic insertion

One way to identify a possible genomic insertion, such as a pathogenicity island, is to look at the nucleotide (GC) content in that region. It is often the case for bacteria that an inserted sequence may come from some other organism (*via* lateral/horizontal gene transfer: HGT/LGT) with a different balance of nucleotide usage. The inserted regions thus stand out when nucleotide use is plotted.

`ACT` allows us to show these graphs in conjunction with the genome comparison data.

Zoom in to the region around 3,276,000bp in the `NC_004431` sequence, and 3,685,500bp in the `NC_002695` sequence

![ACT focused insertion](./images/act_fig9.png?raw=true =400x)

Use the `Graph -> NC_002695.fna -> GC Content (%)` option from the menu bar to render a %GC content graph for the central genome: `NC_002695` *E. coli* O157:H7 Sakai:

![ACT graph choices](./images/act_fig10.png?raw=true =200x)

The resulting graph shows us that, where there is a section of genome sequence present in `NC_002695`, but not `NC_004431` (3709877-3737122 in `NC_002695` co-ordinates), there is a corresponding change in %GC content. This is potentially indicative of an insertion event that has resulted in a genomic island/insertion.

In fact, this region is genomic island GI28, as described in [Roos & van Passel (2011)](http://www.biomedcentral.com/1471-2164/12/427).

**NOTE:** You can use the slider to the right of the graph to vary the window size over which the %GC content statistic is calculated, to 'smooth' the plot.

![ACT showing graph](./images/act_fig11.png?raw=true =400x)

### Compare `megaBLAST` and `MUMmer` output

As noted above `nucmer` output can be complex, but it is possible to generate human-readable output. Unfortunately, the files produced by programs such as `show-coords` are not directly readable by `ACT`. This is a common issue with genome comparisons, as applications produce many different types of data, and there are few widely-accepted standards in the field.

However, the `.crunch` tabular file accepted by `ACT` is simple, and can be readily generated from the output of `MUMmer`'s `show-coords` package. The script `nucmer_to_crunch.py` the current directory can do this for you. It can be used on your `nucmer` output as follows:

```
./nucmer_to_crunch.py -i session-04_output/E_coli_nucmer.coords -o session-04_output/E_coli_nucmer.crunch -v
```

** Exercise 4b (10min): Run the code above, then use `ACT` to compare the `megaBLAST` and `MUMMer` alignments **

**HINT:** Your file selection dialogue should resemble that below:

![ACT file dialogue](./images/act_fig12.png?raw=true =200x)

* What are the differences between the two outputs?
* Do the differences appear to be significant?
* Is there any reason to choose one alignment tool over the other?

** Exercise 5 - stretch goal (20min): Run a pairwise genome alignment between any pair of *Elizabethkingia* genomes from session 03, and visualise the comparison using `ACT`. **