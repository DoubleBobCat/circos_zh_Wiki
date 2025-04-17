---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Highlight Parameters - Part II - Using z-depth
---

### lesson
z-depth, which controls the order in which highlights are drawn, is a critical
parameter in creating effective images. Judiciously layering your data can
make the difference between a good figure and a great figure.

By default, Circos will draw data, such as highlights, in a consistent, but
unspecified, order for a given z-depth. This means that the order isn't
random, but I reserve the right to change the way it's computed between
versions.

#### avoiding occlusion
If you have a large set of overlapping highlights of various sizes, you stand
the chance of having smaller highlights covered by larger highlights. To avoid
this, set the z-depth to be inversely proportional to the higlight size, so
that the highlights are drawn in order of decreasing size.

The random.highlights.txt file associated with this tutorial contains 100
random highlights on chromosome 1. The highlight size is distributed normally
with avg = sd = 5 Mb.

The highlights are colored based on size, with the size range mapped into
evenly sized bins that correspond to colors chr0 ... chr24. This is the
conventional chromosome-based color scheme, which I've subverted for the
current purpose.

```    
    hs1 1725862 8379128 fill_color=chr7
    hs1 4080887 11075336 fill_color=chr8
    hs1 5183662 14345280 fill_color=chr10
    hs1 10044837 11066617 fill_color=chr1
    hs1 10565297 13980978 fill_color=chr4
    hs1 11557401 23262460 fill_color=chr13
    hs1 12870075 25724192 fill_color=chr15
    hs1 13920706 18409477 fill_color=chr5
    hs1 25404101 33003848 fill_color=chr8
    
    ...
```
As you can see, highlight not only overlap but also subsume each other. Track
1 inside the circle in this tutorial's image shows the highlights drawn in the
default order, without using z-depth to control how they're drawn.

The largest highlight is max(size) = 20.4 Mb, so let's add a z-depth to each
highlight and define it by the integer component of z =
100-100*size/max(size).

```    
    hs1 1725862 8379128 fill_color=chr7,z=68
    hs1 4080887 11075336 fill_color=chr8,z=66
    hs1 5183662 14345280 fill_color=chr10,z=55
    hs1 10044837 11066617 fill_color=chr1,z=95
    hs1 10565297 13980978 fill_color=chr4,z=84
    hs1 11557401 23262460 fill_color=chr13,z=43
    hs1 12870075 25724192 fill_color=chr15,z=37
    hs1 13920706 18409477 fill_color=chr5,z=78
    hs1 25404101 33003848 fill_color=chr8,z=63
    ...
```
Track 2 in this tutorial image shows the highlights as ordered by these
z-depth values. Using z-depth to prevent small highlights from being draw over
by larger ones is highly recommended. Keep in mind that a large number of
small highlights draw in the foreground can completely cover a larger
highlight drawn in the background.

You can also avoid occlusion by adjusting the radial position of the highlight
elements. Using the same data file as above, I created another track in which
the r0,r1 values were defined based on the size of the highlight region. I set
r0 = 0.4r - 200*k and r1 = 0.4r + 200*k, where k = size/max(size).

```    
    hs1 1725862 8379128 fill_color=chr7,z=68,r0=0.4r-65.3669p,r1=0.4r+65.3669p
    hs1 4080887 11075336 fill_color=chr8,z=66,r0=0.4r-68.719p,r1=0.4r+68.719p
    hs1 5183662 14345280 fill_color=chr10,z=55,r0=0.4r-90.011p,r1=0.4r+90.011p
    hs1 10044837 11066617 fill_color=chr1,z=95,r0=0.4r-10.0388p,r1=0.4r+10.0388p
    hs1 10565297 13980978 fill_color=chr4,z=84,r0=0.4r-33.5584p,r1=0.4r+33.5584p
    hs1 11557401 23262460 fill_color=chr13,z=43,r0=0.4r-115p,r1=0.4r+115p
    hs1 12870075 25724192 fill_color=chr15,z=37,r0=0.4r-126.289p,r1=0.4r+126.289p
    hs1 13920706 18409477 fill_color=chr5,z=78,r0=0.4r-44.1012p,r1=0.4r+44.1012p
    hs1 25404101 33003848 fill_color=chr8,z=63,r0=0.4r-74.6659p,r1=0.4r+74.6659p
```
Track 3 in the image shows the highlights with this additional formatting. By
scaling the radial extent logarithmically, it's possible to reduce the radial
size difference and make the track more attractive, while still retaining
visibility of larger highlights drawn in the background.
### images
![Circos tutorial image - Highlight Parameters - Part II - Using
z-depth](/documentation/tutorials/highlights/z-depth/img/01.png)
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
    
    24bit = yes
    auto_alpha_colors = yes
    auto_alpha_steps  = 5
    
    </image>
    
    chromosomes_units           = 1000000
    
    chromosomes        = hs1
    chromosomes_breaks = -hs1:120-145;-hs1:180-200
    
    chromosomes_display_default = no
    
    <highlights>
    
    z = 0
    fill_color = green
    
    <highlight>
    file       = data/3/random.highlights.txt
    r0         = 0.8r
    r1         = 0.8r + 200p
    </highlight>
    
    <highlight>
    file       = data/3/random.highlights.z_by_size.txt
    r0         = 0.6r
    r1         = 0.6r + 200p
    </highlight>
    
    <highlight>
    file       = data/3/random.highlights.zr_by_size.txt
    stroke_thickness = 1
    stroke_color     = black
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
``````
  

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
    stroke_thickness = 2
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 3
    thickness        = 1.5r
    </break>
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 100p
    stroke_thickness = 2
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
    size           = 6p
    thickness      = 1p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %.2f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 1p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    </tick>
    <tick>
    spacing        = 10u
    size           = 16p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = vdgrey
    grid_thickness = 2p
    </tick>
    </ticks>
```
  

* * *
