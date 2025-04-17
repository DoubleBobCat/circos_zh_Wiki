---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Ideograms
---

### lesson
#### biological context
In a biological context, the axes in a Circos image usually correspond to
sequences, such as chromosomes, assembly contigs or clones.

##### chromosome vs ideogram
This distinction is important.

The chromosome is the entire sequence structure as defined in the karyotype
file. The ideogram is the depiction of the chromosome, or region thereof, in
the image.

A chromosome may have no ideograms (it is not drawn), a single ideogram (it is
drawn in its entirety, or only a portion of the chromosome is shown) or
multiple ideograms (there is an axis break, multiple regions are drawn).

A chromosome may be divided into any number of regions, each shown as an
individual ideogram in any order.

##### non-biological context
In general, the axes can correspond to an interval of any integer-valued
variable, such as the integer number line, a range of IP addresses, an indexed
list of names, etc.

The only requirement is that the you can express the axis as a range of a
defined length (e.g. [0,1000]) and that data points can be placed on the axis
by a position that corresponds to an interval (e.g. [50], [50,55], etc).

#### Anatomy of a Circos Image
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

```    
    <ideogram>
    show = no
    ...
    </ideogram>
```
#### karyotype definition
A file is required that defines the size, identity and label of each
chromosome. If available, cytogenetic band position can be defined in this
file.

#### ideogram filtering
The karyotype definition generally describes all of the chromosomes in a
genome. Using filters, you can selectively identify which chromosomes will be
drawn.

#### ideogram order
The order of the ideograms around the image can be controlled. In specific
circumstances you may wish to rearrange the ideograms from their natural order
to accentuate data relationships between them.

#### ideogram scale
The length scale (pixels per base) can be adjusted for individual ideograms.

#### ideogram spacing
Spacing between individual ideograms in the circular composition can be
controlled globally and locally.

#### axis breaks
A region of an ideogram may be removed from the image, or several regions of
an ideogram may be represented as individual ideograms. Axis breaks are used
to indicate that an ideogram is not drawn in its entirety.

#### tick mark formatting
Tick mark formatting and placement can be controlled. Tick mark display can be
controlled to eliminate overlap between adjacent labels.

#### grids
Selected tick marks can be extended into the image to form a radial grid
pattern.

#### non-linear scale
The length scale (pixels per base) can be adjusted for individual ideogram
regions. Local scale adjustments are useful to draw focus to a region or to
diminish its contribution to the ideogram extent. The scale can be made to
vary smoothly across an ideogram. Scale variation is a continuous version of
splitting ideograms into multiple pieces, adjusting scale for each piece and
drawing them with axis breaks.
### images
![Circos tutorial image -
Ideograms](/documentation/tutorials/ideograms/ideograms/img/01.png) ![Circos
tutorial image -
Ideograms](/documentation/tutorials/ideograms/ideograms/img/02.png)
### configuration
#### circos.conf
```    
    # MINIMUM CIRCOS CONFIGURATION 
    #
    # The 'hello world' Circos tutorial. Only required
    # configuration elements are included.
    #
    # Common optional elements are commented out.
    
    # Defines unit length for ideogram and tick spacing, referenced
    # using "u" prefix, e.g. 10u
    #chromosomes_units           = 1000000
    
    # Show all chromosomes in karyotype file. By default, this is
    # true. If you want to explicitly specify which chromosomes
    # to draw, set this to 'no' and use the 'chromosomes' parameter.
    # chromosomes_display_default = yes
    
    # Chromosome name, size and color definition
    karyotype = data/karyotype/karyotype.human.txt
    
    <ideogram>
    
    <spacing>
    # spacing between ideograms
    default = 0.005r
    </spacing>
    
    # ideogram position, thickness and fill
    radius           = 0.90r
    thickness        = 10p
    fill             = yes
    
    #stroke_thickness = 1
    #stroke_color     = black
    
    # ideogram labels
    # <<include ideogram.label.conf>>
    
    # ideogram cytogenetic bands, if defined in the karyotype file
    # <<include bands.conf>>
    
    </ideogram>
    
    # image size, background color, angular position
    # of first ideogram, transparency levels, output
    # file and directory
    #
    # it is best to include these parameters from etc/image.conf
    # and override any using param* syntax
    #
    # e.g.
    # <image>
    # <<include etc/image.conf>>
    # radius* = 500
    # </image>
    <image>
    <<include etc/image.conf>> # included from Circos distribution 
    </image>
    
    # RGB/HSV color definitions, color lists, location of fonts,
    # fill patterns
    <<include etc/colors_fonts_patterns.conf>> # included from Circos distribution
    
    # debugging, I/O an dother system parameters
    <<include etc/housekeeping.conf>> # included from Circos distribution
    
    # <ticks> blocks to define ticks, tick labels and grids
    #
    # requires that chromosomes_units be defined
    #
    # <<include ticks.conf>>
```
  

* * *

#### bands.conf
```    
    # optional
    
    show_bands            = yes
    fill_bands            = yes
    band_transparency     = 4
```
  

* * *

#### ideogram.label.conf
```    
    # optional
    
    show_label       = yes
    label_radius     = dims(ideogram,radius) + 0.075r
    label_size       = 24
    label_parallel   = yes
``````
  

* * *

#### ticks.conf
```    
    # ticks are optional
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    size             = 15p
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    color          = grey
    size           = 10p
    </tick>
    
    </ticks>
```
  

* * *
