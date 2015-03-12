# ex06.py
#
# Functions and data useful in exercise 6 (biopython visualisation) of
# the BS32010 course at the University of Dundee

from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
from Bio.Graphics.GenomeDiagram import CrossLink
from Bio.SeqFeature import SeqFeature, FeatureLocation

from reportlab.lib import colors
from reportlab.lib.colors import linearlyInterpolatedColor, Color
from reportlab.lib.units import cm

# FUNCTIONS
# Draw a pairwise genome comparison
def render_pairwise_genome_comparison(genome1, genome2, megablast=None,
                                      crunchfile=None,
                                      png="image.png", pdf="image.pdf",
                                      low_ft_cut=50, low_link_cut=0,
                                      min_aln_len=0):
    """Renders a pairwise alignment figure using Biopython
    
    - genome1, the location of an input genome sequence
               in FASTA format (used as the reference)
    - genome2, the location of an input genome sequence
               in FASTA format (used as the comparator)
    - megablast, the location of the corresponding 
               alignment file, in megablast output format
    - crunchfile, the location of the corresponding .crunch 
               alignment file.
    - png, the filename for an output PNG
    - pdf, the filename for an output PDF
    - low_ft_cut, percentage identity at which features are 
               rendered grey
    - low_link_cut, lowest percentage identity at which 
               cross-links are rendered
    - min_aln_len, smallest alignment that will be rendered
               as a cross-link
          
    The figure shows each genome sequence, with a plot of GC content
    and GC skew, and the alignment as cross-links.
    """
    # Load sequence data, if possible
    s1 = SeqIO.read(genome1, "fasta")
    s2 = SeqIO.read(genome2, "fasta")

    # Set up diagram, tracks, and feature sets for each genome
    gd_diagram = GenomeDiagram.Diagram("Example Comparison")
    gd_genome1 = gd_diagram.new_track(1, name=s1.id, greytrack=False,
                                      greytrack_label=True,
                                      height=0.5, start=0, end=len(s1))
    gd_genome1_ftset = gd_genome1.new_set()
    gd_genome2 = gd_diagram.new_track(10, name=s2.id, greytrack=False,
                                      greytrack_label=True,
                                      height=0.5, start=0, end=len(s2))
    gd_genome2_ftset = gd_genome2.new_set()
    ftsets = {s1.id: gd_genome1_ftset, 
              s2.id: gd_genome2_ftset}  # convenience dictionary
    
    # Add whole genome sequence as a feature, on each track
    gd_genome1_ftset.add_feature(SeqFeature(FeatureLocation(0, len(s1))),
                                 sigil="BOX", color=colors.oldlace, 
                                 label="False")
    gd_genome2_ftset.add_feature(SeqFeature(FeatureLocation(0, len(s2))),
                                 sigil="BOX", color=colors.oldlace, 
                                 label="False")
    
    # Add alignment location features
    # Input file is megaBLAST
    if megablast is not None:
        # Megablast features coloured on yellow and cyan scales
        for sf1, sf2 in megablast_to_seqfeatures(megablast):
            add_crosslinked_features(gd_diagram, sf1, sf2, ftsets, 
                                     min_aln_len, low_link_cut,
                                     low_ft_cut,
                                     refcolor=colors.yellow,
                                     compcolor=colors.cyan)
    # Input file is .crunch
    if crunchfile is not None:
        # .crunch features coloured on green and blue scales,
        for sf1, sf2 in crunch_to_seqfeatures(crunchfile):
            add_crosslinked_features(gd_diagram, sf1, sf2, ftsets, 
                                     min_aln_len, low_link_cut,
                                     low_ft_cut,
                                     refcolor=colors.green,
                                     compcolor=colors.blue)

    # Write image to files. We have to resize PNG on CentOS for rendering.
    draw(gd_diagram, (100 * cm, 40 * cm),
         0, max(len(s1), len(s2)),
         pdf, "PDF")
    draw(gd_diagram, (20 * cm, 8 * cm),
         0, max(len(s1), len(s2)),
         png, "PNG")


# Draw a three-way genome comparison
def render_threeway_genome_comparison(genome1, genome2, genome3,
                                      megablastlist=[], crunchfilelist=[],
                                      png="image.png", pdf="image.pdf",
                                      low_ft_cut=0, low_link_cut=0,
                                      min_aln_len=0):
    """ This function takes the following arguments:
    
        - genome1, the location of an input genome sequence
                   in FASTA format
        - genome2, the location of an input genome sequence
                   in FASTA format
        - genome3, the location of an input genome sequence
                   in FASTA format
        - megablastlist, the location(s) of the corresponding 
                     alignment file(s), in megablast output format
        - crunchfilelist, the location(s) of the corresponding .crunch 
                      alignment file(s).
        - png, the filename for an output PNG
        - pdf, the filename for an output PDF
        - low_ft_cut, percentage identity at which features are 
                      rendered grey
        - low_link_cut, lowest percentage identity at which 
                        cross-links are rendered
        - min_aln_len, smallest alignment that will be rendered
                       as a cross-link
          
        and renders a pairwise alignment figure using 
        Biopython. The figure shows each genome sequence,
        with a plot of GC content and GC skew, and the 
        alignment as cross-links.
    """
    # Load sequence data, if possible
    s1 = SeqIO.read(genome1, "fasta")
    s2 = SeqIO.read(genome2, "fasta")
    s3 = SeqIO.read(genome3, "fasta")

    # Set up diagram, tracks, and feature sets for each genome
    gd_diagram = GenomeDiagram.Diagram("Example Comparison")
    gd_genome1 = gd_diagram.new_track(1, name=s1.id, greytrack=False,
                                      greytrack_label=True,
                                      height=0.5, start=0, end=len(s1))
    gd_genome1_ftset = gd_genome1.new_set()
    gd_genome2 = gd_diagram.new_track(10, name=s2.id, greytrack=False,
                                      greytrack_label=True,
                                      height=0.5, start=0, end=len(s2))
    gd_genome2_ftset = gd_genome2.new_set()
    gd_genome3 = gd_diagram.new_track(20, name=s3.id, greytrack=False,
                                      greytrack_label=True,
                                      height=0.5, start=0, end=len(s3))
    gd_genome3_ftset = gd_genome3.new_set()
    ftsets = {s1.id: gd_genome1_ftset, 
              s2.id: gd_genome2_ftset,
              s3.id: gd_genome3_ftset}  # convenience dictionary
    
    # Add whole genome sequence as a feature, on each track
    gd_genome1_ftset.add_feature(SeqFeature(FeatureLocation(0, len(s1))),
                                 sigil="BOX", color=colors.oldlace, 
                                 label="False")
    gd_genome2_ftset.add_feature(SeqFeature(FeatureLocation(0, len(s2))),
                                 sigil="BOX", color=colors.oldlace, 
                                 label="False")
    gd_genome3_ftset.add_feature(SeqFeature(FeatureLocation(0, len(s3))),
                                 sigil="BOX", color=colors.oldlace, 
                                 label="False")
    
    # Add alignment location features
    # Input file is megaBLAST
    for megablast in megablastlist:
        for sf1, sf2 in megablast_to_seqfeatures(megablast):
            add_crosslinked_features(gd_diagram, sf1, sf2, ftsets, 
                                     min_aln_len, low_link_cut,
                                     low_ft_cut,
                                     refcolor=colors.darkviolet,
                                     compcolor=colors.darkviolet)
    # Input file is .crunch
    for crunchfile in crunchfilelist:
        for sf1, sf2 in crunch_to_seqfeatures(crunchfile):
            add_crosslinked_features(gd_diagram, sf1, sf2, ftsets, 
                                     min_aln_len, low_link_cut,
                                     low_ft_cut,
                                     refcolor=colors.darkviolet,
                                     compcolor=colors.darkviolet)

    # Write image to files. We have to resize PNG on CentOS for rendering.
    draw(gd_diagram, (100 * cm, 40 * cm),
         0, max(len(s1), len(s2)),
         pdf, "PDF")
    draw(gd_diagram, (20 * cm, 8 * cm),
         0, max(len(s1), len(s2)),
         png, "PNG")

# Draw a linear GenomeDiagram of specified size, and named
# start and end points, and format
def draw(diagram, pagesize, start, end, filename, outfmt):
    diagram.draw(format="linear", pagesize=pagesize,
                 start=start, end=end, fragments=1)
    diagram.write(filename, outfmt)

        
# Add crosslinked features to the passed diagram
def add_crosslinked_features(diagram, sf1, sf2, ftsets, min_aln_len, low_link_cut,
                             low_ft_cut, refcolor=colors.red, compcolor=colors.blue):
    """ Add a crosslink between features sf1 and sf2 on the passed
        diagram (so long as the minimum identity and length 
        criteria are passed)
    """
    ft1 = ftsets[sf1.id].add_feature(sf1,
                                     color=linearlyInterpolatedColor(colors.grey, 
                                                                     refcolor,
                                                                     low_ft_cut, 100,
                                                                     sf1.qualifiers['ident']))
    ft2 = ftsets[sf2.id].add_feature(sf2,
                                     color=linearlyInterpolatedColor(colors.grey,
                                                                     compcolor,
                                                                     low_ft_cut, 100,
                                                                     sf1.qualifiers['ident']))    
    aln_len = min(abs(sf1.location.end - sf1.location.start),
                  abs(sf2.location.end - sf2.location.start))
    if (sf1.qualifiers['ident'] > low_link_cut) and (aln_len > min_aln_len):
        flip = False if sf1.strand == sf2.strand else True
        # Can't use transparencies in Color on CentOS 6, 
        # as only Python 2.6 present.
        if flip:
            c1, c2 = Color(0, 0, 1), colors.blue
        else:
            c1, c2 = Color(1, 0, 0), colors.red
        clcolor = linearlyInterpolatedColor(c1, c2, 
                                            low_link_cut, 100,
                                            sf1.qualifiers['ident'])                    
        diagram.cross_track_links.append(CrossLink(ft1, ft2, 
                                                    color=clcolor, 
                                                    flip=flip))
    

# Load in megaBLAST file data and return a set of linked SeqFeatures,
# two per tuple
def megablast_to_seqfeatures(filename):
    """ Parses the passed megablast comparison file, returning a generator of 
        (ft1, ft2) SeqFeature tuples.
        
        - filename, the location of the megaBLAST file
    """
    with open(filename, 'rU') as fh:
        for line in [l.strip().split('\t') for l in fh]:
            # Get start and end of alignment regions
            start1, end1, start2, end2 = \
                int(line[6]), int(line[7]), int(line[8]), int(line[9])
            # Identify strands
            strand1 = 1 if line[7] > line[6] else -1
            strand2 = 1 if line[9] > line[8] else -1
            # Generate SeqFeatures
            sf1 = SeqFeature(FeatureLocation(start1, end1, strand=strand1),
                             id=line[0], qualifiers={'ident': float(line[2]),
                                                     'score': float(line[-1]),
                                                     'eval': float(line[-2])})
            sf2 = SeqFeature(FeatureLocation(start2, end2, strand=strand2),
                             id=line[1], qualifiers={'ident': float(line[2]),
                                                     'score': float(line[-1]),
                                                     'eval': float(line[-2])})
            yield (sf1, sf2)

            
# Load in .crunch file data and return a set of linked SeqFeatures,
# two per tuple
def crunch_to_seqfeatures(filename):
    """ Parses the passed crunch comparison file, returning a generator of 
        (ft1, ft2) SeqFeature tuples.
        
        - filename, the location of the .crunch file
    """
    with open(filename, 'rU') as fh:
        for line in [l.strip().split() for l in fh if len(l.strip())]:
            # Get start and end of alignment regions
            start1, end1, start2, end2 = \
                int(line[2]), int(line[3]), int(line[5]), int(line[6])
            # Identify strands
            strand1 = 1 if line[3] > line[2] else -1
            strand2 = 1 if line[6] > line[5] else -1
            # Generate SeqFeatures
            sf1 = SeqFeature(FeatureLocation(start1, end1, strand=strand1),
                             id=line[4], qualifiers={'ident': float(line[1]),
                                                     'score': float(line[0])})
            sf2 = SeqFeature(FeatureLocation(start2, end2, strand=strand2),
                             id=line[7], qualifiers={'ident': float(line[1]),
                                                     'score': float(line[0])})
            yield (sf1, sf2)
