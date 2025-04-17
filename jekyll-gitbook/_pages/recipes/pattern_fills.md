---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Pattern Fills
---

### lesson
Ribbons, heatmaps and histograms can be drawn with a pattern fill by setting
the `pattern` parameter.

```    
    <link>
    ...
    ribbon = yes
    pattern = checker
    ...
    </link>
```
#### Patterns
The following patterns are available

  * solid 
  * hline 
  * hline-sparse 
  * vline 
  * vline-sparse 
  * checker 
  * checker-sparse 
  * dot 
  * dot-sparse 

Like fonts, patterns are named in their own block and imported from another
configuration file. The file that defines patterns is `etc/patterns.conf`. The
bitmaps for the patterns are found in `etc/tiles`.

```    
    # etc/pattern.conf
    vline        = tiles/vlines.png
    vline-sparse = tiles/vlines-sparse.png
    ...
```
The configuration file `etc/colors_fonts_patterns.conf` takes care of
importing all the pattern definitions.

```    
    <<include etc/colors_fonts_patterns.conf>>
```
You can add your own patterns by creating a PNG file and adding it to the
pattern block. Use an 8-bit PNG. Transparency is not supported for tiles.

If you do not specify a color for a pattern (see below), the pattern will be
used as it appears in the PNG file, without any change in colors.

#### Colored Patterns
A pattern's colors can be remapped using the color parameter. The predefined
patterns are black-on-white, but you can remap a pattern's color by defining a
list of `old:new` colors.

```    
    color = white:red,black:orange
```
To invert a black and white pattern,

```    
    color = white:black,black:white
```
To replace all the colors in a pattern that are not the same as the image's
background color, set the `color` value to a single word. For example, on an
image whose background is black

```    
    color = red
```
will color all non-black pixels in the pattern red.

In this tutorial, the links originally are defined with a color.

```    
    hs11 27363982 47363982 hs8 1 12346012 color=chr11
    hs11 113293528 133293528 hs21 24848956 44848956 color=chr11
    hs10 27542441 47542441 hs20 33053889 53053889 color=chr10
```
A rule is set up so that for 50% of the ribbons, a colored pattern is
selected.

For about 25% of the links, only a pattern is selected. Because each link
already has a color, the pattern is colored by the existing color (in this
case, chromosome color).

#### Patterns with Transparency
This is not supported by GD. Regardless of whether your PNG file has
transparency or not, the tiled pattern will not have transparent components.
### images
![Circos tutorial image - Pattern
Fills](/documentation/tutorials/recipes/pattern_fills/img/image-01.png)
![Circos tutorial image - Pattern
Fills](/documentation/tutorials/recipes/pattern_fills/img/image-02.png)
### configuration
#### circos.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <patterns>
    <<include etc/pattern.conf>>
    </patterns>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.hg18.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    <highlights>
    <highlight>
    file        = data/3/chr.highlights.txt
    r0 = 0.99r
    r1 = 0.995r
    </highlight>
    </highlights>
    
    <links>
    <link linkexample>
    
    file   = data/8/15/tmp.1
    ribbon = yes
    flat   = yes
    radius        = 0.95r
    bezier_radius = 0r
    crest         = 0.2
    
    color      = black
    
    <rules>
    <rule>
    importance = 100
    condition  = rand() < 0.5
    pattern    = eval((qw(hline vline checker dot))[rand(4)])
    color      = eval((qw(red orange yellow green blue purple))[rand(6)])
    z          = 10
    </rule>
    </rules>
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
``````
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 10u
    
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
    show_label     = yes
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 36
    label_parallel = no
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    band_transparency     = 0
    
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
    tick_separation      = 2p
    min_label_distance_to_edge = 0p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1e-6
    color = black
    
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 8p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 12p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
```
  

* * *
