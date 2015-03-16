# README.md - Teaching-2015-03-UoD_compgenvis

## Overview

This repository contains teaching materials used in delivering the 3rd year bioinformatics course lectures on "Comparative Genome Analysis and Visualisation" at the University of Dundee, 2015

## Getting Started

You can grab a local copy of all the files for this workshop/lecture using `git clone`:

```
$ git clone https://github.com/widdowquinn/Teaching-2015-03-17-UoD_compgenvis.git
```

The lecture is presented in a tutorial/workshop format, with interactive examples and exercises using [iPython notebooks](http://ipython.org/notebook.html). 

* Slides for the talk are provided in the `presentation` subdirectory, in LaTeX format for use with [Beamer](http://en.wikipedia.org/wiki/Beamer_%28LaTeX%29).
* Example exercises and data are found in the `exercises` subdirectory.

### Prerequisites

The exercises and examples have been written, and are known to run, with the following software, but they may also run happily on other versions:

* **Python 2.7**
* **iPython (with pylab and matplotlib) 1.1.0**
* **Biopython 1.63+**
* **Pandas 0.13**
* **i-ADHoRe-3.0.01**
* **ncbi-blast-2.2.29+**
* **blast-2.2.26**
* **MUMmer3.23**

## Executing iPython notebooks

To start iPython in a suitable form in your browser, execute

```
$ ipython notebook
```

at the command-line. It is possible to start iPython in other ways (e.g. in the terminal window, without inline plots, or using the Qt console), but this is the way the course examples/exercises were intended to be run.

It may be useful to revise some material from Peter Cock's Biopython workshop - the notes and exercises can be obtained from 

* [https://github.com/peterjc/biopython_workshop](https://github.com/peterjc/biopython_workshop)

### Notebook/Markdown exercises

The notebooks can be inspected online with the NBViewer and MarkDown links below

* **ex01:** [%GC content and genome size](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/ex01_gc_content.ipynb)
* **ex02:** [k-mer spectra](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/ex02_kmer_spectra.ipynb)
* **ex03:** [average nucleotide identity (ANI)](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/ex03_ani.ipynb)
* **ex04:** [pairwise genome alignment](https://github.com/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/whole_genome_alignment/whole_genome_alignments_A.md)
* **ex05:** [multiple genome alignment](https://github.com/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/whole_genome_alignment/whole_genome_alignments_B.md)
* **ex06:** [visualisation in Biopython](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/ex06_biopython_visualisation.ipynb)
* **ex07:** [bacterial gene prediction](https://github.com/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/predict_CDS/bacterial_CDS_prediction.md)
* **ex08:** [finding reciprocal best blast hits (RBBH)](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/ex08_find_rbbh.ipynb)
* **ex09a:** [finding MCL orthologues (MarkDown)](https://github.com/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/mcl_orthologues/ex09a_mcl_orthologues.md)
* **ex09b:** [finding MCL orthologues (iPython)](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/mcl_orthologues/ex09b_mcl_orthologues.ipynb)
* **ex10a:** [finding synteny with i-ADHoRe](https://github.com/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/i-ADHoRe/ex10a_i-ADHoRe.md)
* **ex10b:** [visualising synteny with i-ADHoRe](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/i-ADHoRe/ex10b_i-ADHoRe.ipynb)
* **ex11:** [visualising the two-speed genome](http://nbviewer.ipython.org/github/widdowquinn/Teaching-2015-03-17-UoD_compgenvis/blob/master/exercises/ex11_pi_two_speed.ipynb)

## Licensing

### Presentation

The presentation is licensed under the Creative Commons Attribution ShareAlike license: 

* [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)

summarised below

    You are free to:

    Share — copy and redistribute the material in any 
            medium or format
    Adapt — remix, transform, and build upon the 
            material for any purpose, even commercially.
    
    The licensor cannot revoke these freedoms as long 
    as you follow the license terms.
    
    Under the following terms:

    Attribution — You must give appropriate credit, 
                 provide a link to the license, and 
                 indicate if changes were made. You 
                 may do so in any reasonable manner, 
                 but not in any way that suggests the 
                 licensor endorses you or your use.                  
    ShareAlike — If you remix, transform, or build 
                 upon the material, you must distribute 
                 your contributions under the same 
                 license as the original.
    No additional restrictions — You may not apply 
                 legal terms or technological measures 
                 that legally restrict others from 
                 doing anything the license permits.

    Notices:

    You do not have to comply with the license for 
    elements of the material in the public domain or 
    where your use is permitted by an applicable 
    exception or limitation.
    
    No warranties are given. The license may not give 
    you all of the permissions necessary for your 
    intended use. For example, other rights such as 
    publicity, privacy, or moral rights may limit how 
    you use the material.

### Software and code

Unless otherwise indicated, all code is subject to the following agreement:

    (c) The James Hutton Institute 2014, 2015
    Author: Leighton Pritchard

    Contact: leighton.pritchard@hutton.ac.uk

    Address: 
    Leighton Pritchard,
    Information and Computational Sciences,
    James Hutton Institute,
    Errol Road,
    Invergowrie,
    Dundee,
    DD6 9LH,
    Scotland,
    UK

The MIT License

Copyright (c) 2014-2015 The James Hutton Institute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
