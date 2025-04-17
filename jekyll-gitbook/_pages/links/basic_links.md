---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Drawing Basic Links
---

## Drawing Basic Links
### lesson
One of the core uses of Circos is to show the relationships between positions
on axes. Axes might be chromosomes and might indicate translocations. Or the
axes could be categories or entities (e.g. countries) and indicate some
relationship between them, such as migration of people.

A lot of the syntax for defining parameters that control how links are defined
carry over directly from the syntax for highlights.

#### <links> block
All link data sets are defined within the <links> block. Typically this block
contains global parameter settings in its root - these values become the
default values for all link data.

Individual link data sets are defined within <link> blocks.

```    
    <links>
    
     # global parameters here
    
     <link>
     ...
     </link>
    
     <link>
     ...
     </link>
    
    </links>
```
#### data format
Link data files are composed of position pairs defined on one line.

```    
    ...
    hs1 100 200 hs2 250 300
    hs1 400 550 hs3 500 750
    hs1 600 800 hs4 150 350
    ...
```
##### two-line format
Links may also be defined across two lines. The lines are associated together
using a link `id`, which is unique for each pair. You must also have exactly
two lines for each link `id`.

```    
    ...
    segdup00010 hs1 100 200 
    segdup00010 hs2 250 300
    segdup00011 hs1 400 550
    segdup00011 hs3 500 750
    segdup00012 hs1 600 800
    segdup00012 hs4 150 350
    ...
```
The two-line format is deprecated and may not be supported in future versions.

##### link options
As with highlights, you can add an optional field to specify link-specific
options.

```    
    ...
    hs1 100 200 hs2 250 300 color=blue
    hs1 400 550 hs3 500 750 color=red,thickness=5p
    hs1 600 800 hs4 150 350 color=black
    ...
```
#### example
In this example, I draw data from a file of coordinates defined by segmental
duplications. Each coordinate pair defines two regions of the genome that are
defined as segmental duplications (>1kb in length, >90% similarity).

```    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    color         = black_a5
    radius        = 0.95r
    bezier_radius = 0.1r
    thickness     = 1
    </link>
    
    </links>
``````
##### links with custom karyotype files
If you need to draw links on segments for which the karyotype is not available
— when the segments are not chromosomes from a common species — you'll need to
[create your own karyotype
file](/documentation/tutorials/ideograms/karyotype).

For example, if you had 3 contigs of size 1000, 1500 and 2500 bp, you might
create this file

```    
    # karyotype.txt
    chr - contig1 1 0 1000 black
    chr - contig2 2 0 1500 blue
    chr - contig3 3 0 2500 red
```
and in `circos.conf` use

```    
    karyotype = karyotype.txt
```
Your link file might look like this

```    
    contig1 10 20 contig2 500 520 
    contig3 50 80 contig3 750 760
    ...
```
Here the first link defines connections between `contig1:10-20` and
`contig2:500-520` and the second between `contig3:50-80` and
`contig3:750-760`.

##### link parameters
The basic parameters for links are

  * `radius` — this is the radial position of the termination of the link; for relative values, if `radius` < 1 then it is defined in terms of the inner ideogram radius, otherwise it is defined in terms of the outer ideogram radius 
  * `bezier_radius` — the radial position of the third control point (in addition to the two positions defined by the link coordinates) used to draw the Bezier curve; if this parameter is not defined then straight lines will be used 
  * `color` — color of the link line 
  * `thickness` — thickness of the link line (note that this is not stroke_thickness, since the line isn't technically stroked) 
  * `record_limit` — if this is defined, the number of records read from the file is capped; coordinate records are sampled from the start of the file; useful for debugging 

#### link defaults
All track types have default values. For links, these are

```    
    ribbon           = no
    color            = black
    thickness        = 1
    radius           = 0.40r
    bezier_radius    = 0r
    crest                = 0.5
    bezier_radius_purity = 0.75
```
and loaded from `etc/tracks/link.conf` in the Circos distribution. This file
is set by the `track_defaults` parameter, which is set normally in
`etc/housekeeping.conf`. You can override defaults by setting the parameter to
`undef`

```    
    <link>
     ...
     crest = undef
     ...
    </link>
```
or undefining `track_defaults`

```    
    <<include etc/housekeeping.conf>>
    track_defaults* = undef
```
Note that the `*` syntax is required because you are overriding a parameter
which is already defined at the same level in the configuration file.

#### bezier curves
Links can be drawn as straight lines or as [quadratic Bezier
curves](https://en.wikipedia.org/wiki/B%C3%A9zier_curve).

For the latter, the start `p1` and end `p3` control points are defined by the
coordinate positions (angularly) and the radius parameter (radially). The
middle control point `p2` is defined by the mid point between the coordinates
(angularly) and `bezier_radius` parameter (radially).

The Bezier curve is drawn to have its tangent at `p1` defined by the line
`p1-p2` and at `p3` defined by the line `p2-p3` (see the image associated with
this tutorial).
### images
![Circos tutorial image - Drawing Basic
Links](/documentation/tutorials/links/basic_links/img/01.png) ![Circos
tutorial image - Drawing Basic
Links](/documentation/tutorials/links/basic_links/img/02.png) ![Circos
tutorial image - Drawing Basic
Links](/documentation/tutorials/links/basic_links/img/03.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3
    chromosomes_display_default = no
    
    # If you adjust the radius of the ideograms, links incident
    # on these ideograms will inherit the new radius.
    #chromosomes_radius = hs2:0.9r;hs3:0.8r
    
    # Links (bezier curves or straight lines) are defined in <links> blocks.
    # Each link data set is defined within a <link> block. 
    #
    # As with highlights, parameters defined
    # in the root of <links> affect all data sets and are considered
    # global settings. Individual parameters value can be refined by
    # values defined within <link> blocks, or additionally on each
    # data line within the input file.
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.95r
    color         = black_a4
    
    # Curves look best when this value is small (e.g. 0.1r or 0r)
    bezier_radius = 0.1r
    thickness     = 1
    
    # These parameters have default values. To unset them
    # use 'undef'
    #crest                = undef
    #bezier_radius_purity = undef
    
    # Limit how many links to read from file and draw
    record_limit  = 2000
    
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
    
    # If you want to turn off all track default values, 
    # uncomment the line below. This overrides the
    # value of the parameter imported from etc/housekeeping.conf
    
    #track_defaults* = undef
    # The defaults for links are
    #
    # ribbon           = no
    # color            = black
    # thickness        = 1
    # radius           = 0.40r
    # bezier_radius    = 0r
    # crest                = 0.5
    # bezier_radius_purity = 0.75
    #
    # See etc/tracks/link.conf in Circos distribution
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 0
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.01r
    break   = 0.5r
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(ideogram,radius) + 0.075r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 100p
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
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    
    <tick>
    spacing        = 1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
