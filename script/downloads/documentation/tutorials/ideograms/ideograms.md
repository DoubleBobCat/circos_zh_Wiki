Use the [latest version of Circos](/software/download/circos/) and read
[Circos best
practices](/documentation/tutorials/reference/best_practices/)—these list
recent important changes and identify sources of common problems.

If you are having trouble, post your issue to the [Circos Google
Group](https://groups.google.com/group/circos-data-visualization) and [include
all files and detailed error logs](/support/support/). Please do not email me
directly unless it is urgent—you are much more likely to receive a timely
reply from the group.

Don't know what question to ask? Read [Points of View: Visualizing Biological
Data](https://www.nature.com/nmeth/journal/v9/n12/full/nmeth.2258.html) by
Bang Wong, myself and invited authors from the [Points of View
series](https://mk.bcgsc.ca/pointsofview).

# 3 — Drawing Ideograms

## 1\. Ideograms

[Lesson](/documentation/tutorials/ideograms/ideograms/lesson)
[Images](/documentation/tutorials/ideograms/ideograms/images)
[Configuration](/documentation/tutorials/ideograms/ideograms/configuration)

### biological context

In a biological context, the axes in a Circos image usually correspond to
sequences, such as chromosomes, assembly contigs or clones.

#### chromosome vs ideogram

This distinction is important.

The chromosome is the entire sequence structure as defined in the karyotype
file. The ideogram is the depiction of the chromosome, or region thereof, in
the image.

A chromosome may have no ideograms (it is not drawn), a single ideogram (it is
drawn in its entirety, or only a portion of the chromosome is shown) or
multiple ideograms (there is an axis break, multiple regions are drawn).

A chromosome may be divided into any number of regions, each shown as an
individual ideogram in any order.

#### non-biological context

In general, the axes can correspond to an interval of any integer-valued
variable, such as the integer number line, a range of IP addresses, an indexed
list of names, etc.

The only requirement is that the you can express the axis as a range of a
defined length (e.g. [0,1000]) and that data points can be placed on the axis
by a position that corresponds to an interval (e.g. [50], [50,55], etc).

### Anatomy of a Circos Image

A Circos image is based on a circular axis layout. Data tracks appear inside
and/or outside the circular layout. Tracks include links, which connect two
chromosome positions, as well as standard data representations such as scatter
plots, histograms, and heatmaps.

Axis definition, placement, size and formatting form the core of a Circos
image. Each data point that Circos displays is associated with an interval on
one of the axes (e.g. `chr5:1000-1500`).

A significant portion of the configuration files (the <ideogram> block) is
dedicated to controlling the format of the ideograms. This tutorial will
address each of these in turn.

You can turn off the display of ideograms by setting `show=no` in the
<ideogram> block. The effect will be to hide the ticks, ideogram and
associated labels (i.e. the scale), but the data for the ideogram will still
be shown.

    
    
    <ideogram>
    show = no
    ...
    </ideogram>
    

### karyotype definition

A file is required that defines the size, identity and label of each
chromosome. If available, cytogenetic band position can be defined in this
file.

### ideogram filtering

The karyotype definition generally describes all of the chromosomes in a
genome. Using filters, you can selectively identify which chromosomes will be
drawn.

### ideogram order

The order of the ideograms around the image can be controlled. In specific
circumstances you may wish to rearrange the ideograms from their natural order
to accentuate data relationships between them.

### ideogram scale

The length scale (pixels per base) can be adjusted for individual ideograms.

### ideogram spacing

Spacing between individual ideograms in the circular composition can be
controlled globally and locally.

### axis breaks

A region of an ideogram may be removed from the image, or several regions of
an ideogram may be represented as individual ideograms. Axis breaks are used
to indicate that an ideogram is not drawn in its entirety.

### tick mark formatting

Tick mark formatting and placement can be controlled. Tick mark display can be
controlled to eliminate overlap between adjacent labels.

### grids

Selected tick marks can be extended into the image to form a radial grid
pattern.

### non-linear scale

The length scale (pixels per base) can be adjusted for individual ideogram
regions. Local scale adjustments are useful to draw focus to a region or to
diminish its contribution to the ideogram extent. The scale can be made to
vary smoothly across an ideogram. Scale variation is a continuous version of
splitting ideograms into multiple pieces, adjusting scale for each piece and
drawing them with axis breaks.

