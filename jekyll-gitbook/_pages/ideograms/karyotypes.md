---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Karyotypes
---

## Karyotypes
### lesson
The karyotype file defines the axes. In biological context, these are
typically chromosomes, sequence contigs or clones.

Each axis (e.g. chromosome) is defined by unique identifier (referenced in
data files), label (text tag for the ideogram seen in the image), size and
color.

In addition to chromosomes, the karyotype file is used to define position,
identity and color of cytogenetic bands. For some genomes these band data are
available.

#### designing the Circos image
The most difficult part of creating a Circos image—any visualization for that
matter—is deciding what data to show. Chances are your data is too complex to
show (e.g. its native format doesn't have a trivial visual encoding, such as a
scatter plot).

Mapping data onto a Circos figure requires that you identify what patterns in
your data are (a) likely to be important and (b) likely to be present, and
create a figure that exposes such patterns. Remember, if the pattern exists,
you can't afford to miss it. If it doesn't exist, you can't afford to be
fooled into thinking that it's there, or left wondering whether it's occluded
by other data.

If you don't know where to start when creating Circos images from genomic and
non-genomic data, look through [published examples from the
literature](/images/scientific_literature/). Find images whose patterns map
onto your data types.

Don't think necessarily from the point of view of how to construct input
files. First, identify what you want to show and how. Make a sketch of the
kind of figure you want to make. This is the hard part.

#### defining chromosomes
Chromosome definitions are formatted as follows

```    
    chr - ID LABEL START END COLOR
```
The first two fields are always "chr", indicating that the line defines a
chromosome, and "-". The second field defines the parent structure and is used
only for band definitions.

The `id` is the identifier used in data files whereas the LABEL is the text
that will appear next to the ideogram on the image. If you are working with
multiple species, I suggest prefixing the chromosome number with a species
identifier (e.g., hs = _Homo sapiens_ , mm = _Mus musculus_ , etc). Even when
working with only one species, prefixing the chromosome with a species code is
highly recommended — this will greatly help in creating more transparent
configuration and data files.

The `start` and `end` values define the size of the chromosome. The karyotype
file should store the entire chromsome size, not just the region you wish to
draw. Other configuration file parameters control the drawable regions.

The `color` of the ideogram will be used, if you decide not to show the
cytogenetic bands and select the fill option. The color can be useful to
distinguish between species and chromosomes. Consider using the conventional
chromosome color scheme as defined in the `etc/color.conf` configuration file.
Colors are defined for each human chromosome and are named similiarly: `chr1`,
`chr2`, ... `chrx`, `chry`, `chrun`. Colors must be in lowercase.

The karyotype file is specified in the configuration file using

```    
    karyotype = data/karyotype/karyotype.human.txt
```
For example, the human karyotype for assembly
[GRCh37](https://www.ncbi.nlm.nih.gov/assembly/2758/) (hg19, Feb 2009) is
composed of 24 chromosomes

```    
    chr - hs1 1 0 249250621 chr1
    chr - hs2 2 0 243199373 chr2
    chr - hs3 3 0 198022430 chr3
    ...
    chr - hs22 22 0 51304566 chr22
    chr - hsX x 0 155270560 chrx
    chr - hsY y 0 59373566 chry
```
together with 862 bands

```    
    band hs1 p36.33 p36.33 0 2300000 gneg
    band hs1 p36.32 p36.32 2300000 5400000 gpos25
    band hs1 p36.31 p36.31 5400000 7200000 gneg
    ...
    band hsY q11.223 q11.223 22100000 26200000 gpos50
    band hsY q11.23 q11.23 26200000 28800000 gneg
    band hsY q12 q12 28800000 59373566 gvar
```
#### cytogenetic bands
Bands are defined in the same manner as chromosomes, but the first two fields
are now `band` and the `id` of the parent chromosome.

```    
    band hs1 p36.33 p36.33 0 2300000 gneg
    band hs1 p36.32 p36.32 2300000 5300000 gpos25
    band hs1 p36.31 p36.31 5300000 7100000 gneg
    ...
    band hs2 p25.3 p25.3 0 4300000 gneg
    band hs2 p25.2 p25.2 4300000 7000000 gpos50
    band hs2 p25.1 p25.1 7000000 12800000 gneg
    ...
```
You can obtain the karyotype structure from [UCSC Genome Viewer Table
Browser](https://genome.ucsc.edu/cgi-bin/hgTables?command=start) (Mapping and
Sequencing Tracks > Chromosome Band) . Not all genomes have these data,
however. For example, mouse (mm9) and rat (rn4) have band information, but not
dog (canfam2) or cow (bostau3)

##### band transparency
Cytogenetic band structure is drawn on top of the ideograms. The ideogram
itself can have an associated color—this is defined in the karotype file—and
when band transparency is turned on, this color shows through.

```    
    <ideogram>
    show_bands = yes
    fill_bands = yes
    band_transparency = 4
    ...
    </ideogram>
```
The value for band_transparency can be `1..auto_alpha_steps`, where
`auto_alpha_steps` is the number of automatically generated transparency steps
for each color (see `etc/image.conf`).

When `band_transparency=1`, the bands are _least_ transparent. Conversely,
when `band_transparency=auto_alpha_steps`, the bands are most transparent. For
a given `band_transparency` value, the opacity is given by
`band_transparency/(auto_alpha_steps+1)` (e.g. 2/6 when `band_transparency=2`
and `auto_alpha_steps=5`).

##### when to use bands
The cytogenetic bands feature is meant ... for cytogenetic bands. These
ideogram annotations have two specific properties: they cover the entire
ideogram and they don't overlap.

If you want to use the band feature to show other ideogram annotations, the
data must meet these two conditions. It's likely that unless your data _are_
cytogenetic banding patterns, they won't (e.g. gene regions, repeat regions,
etc). In these case, use the [highlight plot
block](/documentation/tutorials/highlights/on_data/) and draw the highlights
within the ideograms by setting

```    
    r0 = dims(ideogram,radius_inner)
    r1 = dims(ideogram,radius_outer)
```
#### defining multiple species
If you would like to draw ideograms from multiple species, list their
karyotype files in the `karyotype` parameter

```    
    karyotype = data/karyotype/karyotype.human.txt,data/karyotype/karyotype.rat.txt
``````    
    # data/karyotype/karyotype.human.txt
    chr - hs1 1 0 249250621 chr1
    chr - hs2 2 0 243199373 chr2
    chr - hs3 3 0 198022430 chr3
    ...
    
    # data/karyotype/karyotype.rat.txt
    chr - rn1 1 0 267910886 chr1
    chr - rn2 2 0 258207540 chr2
    chr - rn3 3 0 171063335 chr3
    ...
```
#### non-genomic karyotype files
Circos was designed to draw genomic data, but this isn't a limitation. If you
have any positional data that would benefit from a circular composition, you
can define abstract "chromosomes" to act as data domains.

For example, consider this "Naming Names" [NYT graphic of a presidential
debate](https://www.nytimes.com/interactive/2007/12/15/us/politics/DEBATE.html).
This image could be generated with Circos. In this case, the karyotype would
define each candidate as a "chromosome", and a segment of speech as a "band".
The NYT illustration is a wonderful analogy to comparative genomics - each
candidate (a genome) makes verbal reference to (shows synteny) to another
candidate (another genome).

If you have two integer ranges 0-1000 over which you wanted to display data,
you might define

```    
    chr - axis1 1 0 1000 green
    chr - axis2 2 0 1000 red
```
Furthermore, you could use the band functionality to display a checkered grid
within each domain to indicate length.

```    
    band axis1 band1 band1 0 99 grey
    band axis1 band2 band2 100 199 white
    band axis1 band1 band1 200 299 grey
    band axis1 band2 band2 300 399 white
    ...
```
The definitions in the karyotype file need not correspond to physical
structures. Among other things, you can use them to define contigs, such as
sequence or map contigs.
### images
![Circos tutorial image -
Karyotypes](/documentation/tutorials/ideograms/karyotypes/img/01.png) ![Circos
tutorial image -
Karyotypes](/documentation/tutorials/ideograms/karyotypes/img/02.png)
### configuration
#### circos.2.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    # specify the karyotype file here; try also
    #  data/2/karyotype.dog.txt
    #  data/2/karyotype.rat.txt
    #  data/2/karyotype.mouse.txt
    #  data/2/karyotype.all.txt (human+dog+rat+mouse)
    # but reduce frequency of ticks when increasing the 
    # number of ideograms
    karyotype = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    #angle_orientation = counterclockwise
    </image>
    
    chromosomes_units           = 1000000
    
    #chromosomes_display_default = yes
    
    chromosomes = hs1;hs2;hs3
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
``````
  

* * *

#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    ### single genomes
    
    # specify the karyotype file here - try other karyotypes in data/karyotype
    karyotype = data/karyotype/karyotype.human.txt
    #karyotype = data/karyotype/karyotype.drosophila.txt
    #karyotype = data/karyotype/karyotype.mouse.txt
    #karyotype = data/karyotype/karyotype.rat.txt
    
    ### multiple genomes
    
    # to draw chromosomes from multiple karyotypes, 
    # provide comma-separated list of files
    #karyotype          = data/karyotype/karyotype.human.txt,data/karyotype/karyotype.mouse.txt,data/karyotype/karyotype.rat.txt
    
    # adjust color using regular expressions matching chromosome names
    #chromosomes_color  = /hs/:red;/mm/:green;/rn/:blue
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 4
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.0025r
    break   = 0.5r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    <rules>
    use       = no
    <rule>
    # hide every other ideogram
    condition = var(display_idx) % 2
    show      = no
    </rule>
    <rule>
    condition = var(chr) eq "hs3"
    show_ticks = no
    </rule>
    <rule>
    condition = var(chr) eq "hs5"
    show_bands = no
    </rule>
    <rule>
    condition = var(chr) eq "hs7"
    color     = vdpurple
    </rule>
    <rule>
    condition = var(chr) eq "hs9"
    stroke_thickness = 0
    </rule>
    </rules>
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = 0.95r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    
    # you can format the label by using properties
    # of the ideogram, accessible with var(PROPERTY):
    #
    # chr, chr_with_tag, chrlength, display_idx, end, idx, 
    # label, length, reverse, scale, size, start, tag
    
    label_format     = eval(sprintf("chr%s",var(label)))
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 75p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    skip_first_label = no
    skip_last_label  = no
    radius           = dims(ideogram,radius_outer)
    tick_separation  = 2p
    label_separation = 5p
    multiplier       = 1e-6
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 1u
    show_label     = no
    thickness      = 2p
    color          = dgrey
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = no
    thickness      = 3p
    color          = vdgrey
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    grid_start     = 0.5r
    grid_end       = 0.999r
    </tick>
    
    </ticks>
```
  

* * *
