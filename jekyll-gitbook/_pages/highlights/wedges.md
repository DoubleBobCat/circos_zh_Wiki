---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Wedge Highlights
---

### lesson
Highlights are special track type used for highlighting regions of the image
created by Circos. Highlights are defined in a <highlights> block are
different than tracks defined in a <plots> block in the following ways

  * highlights are drawn underneath any grids and other data 
  * highlights can be automatically locked to lie within the radial extent of the ideograms 

In effect, highlights give you the ability to draw a colored slice, defined by
start/end radius and start/end genomic position, anywhere within the image.
Used creatively, highlights can be used to draw attention to a region of the
genome, specify area masks, and even draw ideograms from another species as
concentric circles.

If you want to draw highlights on top of data, use a `type=highlight` <plot>
block, which is described in detail
[here](//documentation/tutorials/highlights/on_data).

#### wedge vs ideogram highlights
Wedge highlights have flexible radial start and end positions. These radial
positions are defined by the `r0` and `r1` parameters (see below).

Ideogram highlights are drawn inside the ideograms, on top of the cytogenetic
bands, if those are drawn.

#### defining highlights
Highlights are defined in external data files. A highlight file is composed of
at least three fields, with potentially a fourth field that defines formatting
for each highlight. For example, a simple highlight file might contain lines
such as

```    
    ...
    hs1 1298972 1300443
    hs1 1311738 1324571
    hs1 1397026 1421444
    hs1 1437417 1459927
    ...
```
Formatting and data files for highlights are defined in <highlights> blocks.
In the example below, the same highlight data file, `genes.txt`, which uses
gene transcription regions to define highlights, is drawn three times in the
figure.

```    
    <highlights>
    
    z          = 0
    fill_color = green
    
    <highlight>
    file       = data/3/genes.txt
    r0         = 0.6r
    r1         = 0.8r
    </highlight>
    
    <highlight>
    file       = data/3/genes.txt
    r0         = 0.7r
    r1         = 0.75r
    z          = 5
    </highlight>
    
    <highlight>
    file       = data/3/genes.txt
    r0         = 1.1r
    r1         = 1.15r
    fill_color = blue
    stroke_color = dblue
    stroke_thickness = 2
    </highlight>
    
    </highlights>
```
First, all highlights are confined within a <highlights> block. A given
highlight can have its parameters specified in three places. In increasing
order of precedence these are

  * the `highlights` block 
  * individual `highlight` block 
  * data file 

Thus, if a highlight is formatted to have a red fill color in the data file,
this value overrides any other color setting for that highlight in <highlight>
or <highlights> blocks.

#### highlight radial position
The primary highlight feature that you want to control is the radial start and
end position, defined by `r0` (inner) and `r1` (outer) radii. Both values are
defined relative (`r`) to the ideogram radius or in terms of absolute pixels
(`p`) from the center of the image.

Defining relative radial position is helpful because if you adjust the image
size, the position of the highlights will not be altered, relative to other
features in the image. For example

```    
    r0 = 0.5r
    r1 = 0.75r
```
will set the highlight radial position to be `0.5-0.75` of the fraction of the
inner ideogram radius. Highlights with `r0`,`r1` > 1 will be defined relative
to the outer ideogram radius.

It is possible to mix relative and absolute values. For example,

```    
    r0 = 0.5r
    r1 = 1r-25p
```
will draw the highlight from 50% of the inner ideogram radius all the way to
the inner ideogram radius, less 25 pixels. Specifying absolute values provides
pixel-level control over position of highlight features. This becomes
important when you wish to present your image at different scales, when a
constant 5px margin may be more meaningful than a 1% margin.

#### z-depth
Each highlight is specified by a single data file line and is defined by a
genomic start and end position on the same chromosome. Highlights are drawn
independently and you can control which highlights are drawn first by
specifying a highlight's z-depth value.

Nearly ll Circos data structures can be assigned a z-depth value to control
which elements are drawn in front.

In the block definition of this tutorial section, you'll see that the
`highlights` block has a default z-depth value assigned

```    
    z = 0
```
This is the default z-depth value, and as such does not have to be explicitly
stated. It's helpful to do so, however, especially when planning to adjust the
z-depth later.

The second highlight block defines a set of highlights drawn at `z=5`. Since
this block's z-depth is higher, it will be drawn on top of the first highlight
block. In effect, what will happen is that the highlights defined by the first
block will be drawn first, followed by highlights of the second block.

The net effect is a set of red, shorter highlights (100px tall) drawn on top
of the green highlights defined by the first block.

#### highlight formatting
The following parameters can be controlled for each highlight

  * `r0` \- inner radius of highlight 
  * `r1` \- outer radius of highlight 
  * `offset` \- an offset applied to both r0 and r1 (useful for overriding default r0,r1 values defined at lower precedence) 
  * `fill_color` \- color of the highlight slice 
  * `stroke_color` \- color of the highlight border, drawn if stroke_thickness is set 
  * `stroke_thickness` \- border thickness, if any, of the highlight slice 
  * `z` \- z-depth of the highlight, controlling the order in which highlights are drawn 
  * `ideogram` \- toggles the position of the highlight to be within the ideogram extent 

All of these are explored in other parts of this tutorial section.
### images
![Circos tutorial image - Wedge
Highlights](/documentation/tutorials/highlights/wedges/img/01.png)
### configuration
#### circos.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units           = 1000000
    
    chromosomes        = hs1;hs2;hs3
    chromosomes_breaks = -hs1:50-150;-hs2:0-100;-hs3:0-25;-hs3:80-120;-hs3:150-)
    
    chromosomes_display_default = no
    
    ################################################################
    #
    # define highlights within <highlights> block
    #
    # note that the radial axis grid is drawn on top of the highlights
    
    <highlights>
    
    # the default value for z-depth and fill_color for all highlights
    
    z = 0
    fill_color = green
    
    # we'll draw three highlight sets, all using the same data file
    
    # the first set will be drawin from 0.6x 1x-25pixels of the ideogram
    # radius and will be green (color by default)
    
    <highlight>
    file       = data/3/genes.txt
    r0         = 0.6r
    r1         = 1.0r - 100p
    </highlight>
    
    # the second set will be drawn on top of the first (higher z-depth)
    # and will be 100px in the radial direction, starting at 0.7x the
    # ideogram radius
    
    <highlight>
    file       = data/3/genes.txt
    r0         = 0.7r
    r1         = 0.7r + 100p
    z          = 5
    fill_color = red
    </highlight>
    
    # the third set will be outside the circle (r0,r1>1) and will be
    # blue with dark blue border around each highlight
    
    <highlight>
    file       = data/3/genes.txt
    r0         = 1.1r
    r1         = 1.15r
    fill_color = blue
    stroke_color = dblue
    stroke_thickness = 2
    </highlight>
    
    </highlights>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 3u
    break   = 1u
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color = black
    fill_color   = blue
    thickness    = 0.25r
    stroke_thickness = 2p
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 3p
    thickness        = 1.5r
    </break>
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 100p
    stroke_thickness = 2p
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = yes
    label_with_tag = yes
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 48p
    
    # cytogenetic bands
    band_stroke_thickness = 2p
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    show_grid          = yes
    grid_start         = 0.5r
    grid_end           = 1.0r
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 10p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 1u
    size           = 3p
    thickness      = 1p
    color          = black
    show_label     = no
    label_size     = 12p
    label_offset   = 0p
    format         = %.2f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 1p
    color          = black
    show_label     = yes
    label_size     = 8p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    </tick>
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 8p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = vdgrey
    grid_thickness = 2p
    </tick>
    </ticks>
```
  

* * *
