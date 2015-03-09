# README.md - shiny

## Overview

This directory contains subdirectories holding the R/Shiny code for example/activity Apps in a comparative genomics workshop. In order to run these Shiny Apps locally, you should start **RStudio**, import the Shiny library, and use `runApp` with the absolute path to one of this directory's subdirectories. For example:

```
setwd("<path_to_current_directory>")
library(shiny)
runApp("nucleotide_frequencies")
```

Alternatively, you can use the version hosted at [shinyapps.io](http://shinyapps.io):

* [https://widdowquinn.shinyapps.io/nucleotide_frequencies/](https://widdowquinn.shinyapps.io/nucleotide_frequencies/)

## Prerequisites to run locally

These Shiny Apps were written and tested with the following software configurations, but other versions of the software may work:

* **RStudio** 0.98.501 <http://www.rstudio.com/ide/download/desktop>
* **R** 3.0.2 <http://www.r-project.org]>

These `R` Libraries are also required:

* **shiny**
* **ggplot2**
* **gridExtra**
* **Bioconductor** (for **Biostrings**)
* **reshape2**
* **hash**

# Shiny Apps

* `nucleotide_frequencies`