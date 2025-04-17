---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Directed Links
---

### lesson
Circos draws links without orientation. To indicate the direction of the link,
you need to compose the link track with another track, which will provide an
indication of which end of the link is its end (or start, if you wish).

To do so, the best way is to use a scatter plot with a triangular glyph. The
glyph will act as a natural arrowhead at the end of the link.

To prepare your data, create a scatter plot data file that contains the
coordinates of the ends of the links. For example, if your links are

```    
    hs1 102024400 102025440 hs3 111883743 111884767
    hs1 152617218 152618252 hs3 111883745 111884756
    hs1 158502674 158503718 hs3 111883744 111884768
    ...
```
the list of ends might be

```    
    hs1 102024400 102025440 0
    hs1 152617218 152618252 0
    hs1 158502674 158503718 0
    ...
```
I've selected the second coordinate of the link as its end (arbitrarily, for
this example), and set the y-value of the associated data point to 0.

The scatter track that adds the arrow head would be defined like this

```    
    <plots>
    
    <plot>
    
    type  = scatter
    file  = linkends.txt
    
    glyph      = triangle
    glyph_size = 24p
    
    min = 0
    max = 1
    r0  = 0.99r
    r1  = 0.99r
    
    fill_color = black
    
    <rules>
    
    <rule>
    condition  = 1
    fill_color = eval(lc "chr".substr(var(chr),2))
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
```
I've added a rule that colors the glyph by the color of the chromosome on
which it lies.

The scatter plot is placed at `radius=0.99r`, which is just before where the
links end, to seamlessly join the triangular glyphs to the link line.

You can use other tracks to indicate the end of the link, such as a highlight
track, to give the link a thicker base, or a text track (to give the end of
the link a name).
### images
![Circos tutorial image - Directed
Links](/documentation/tutorials/recipes/directed_links/img/image-01.png)
![Circos tutorial image - Directed
Links](/documentation/tutorials/recipes/directed_links/img/image-02.png)
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
    
    karyotype = karyotype.human.hg18.txt
    
    <image>
    dir   = .
    file  = links-directed.png
    24bit = yes
    radius         = 1500p
    background     = white
    angle_offset   = -90
    auto_alpha_colors = yes
    auto_alpha_steps  = 5
    </image>
    
    chromosomes_units           = 1e6
    chromosomes_display_default = yes
    chromosomes = hs3:101-121
    chromosomes_scale = hs3:50
    
    <plots>
    <plot>
    type = scatter
    glyph = triangle
    glyph_size = 24p
    file = linkends.txt
    min = 0
    max = 1
    r0 = 0.99r
    r1 = 0.99r
    fill_color=black
    <rules>
    <rule>
    importance = 100
    condition  = 1
    fill_color = eval("chr".substr(_CHR_,2))
    </rule>
    </rules>
    </plot>
    </plots>
    
    <links>
    <link testlinks>
    file          = links.txt
    thickness     = 2
    bezier_radius = 0r
    radius        = 0.995r
    crest         = 0.25
    color         = black_a2
    </link>
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 120
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    
    #debug_group = ticks
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 5u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 20p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = no
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.10r
    label_size     = 36
    label_parallel = no
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = no
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = no
    
    band_transparency     = 1
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_outer)+100
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 5p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 5p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 5u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    #chromosomes_display_default=no
    #chromosomes    = hs3
    spacing        = 1u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 25u
    size           = 12p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
```
  

* * *
