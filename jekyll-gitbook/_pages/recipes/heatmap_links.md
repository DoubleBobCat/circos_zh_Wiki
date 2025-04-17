---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Heat Map Links
---

### lesson
You can color links by an associated value to create a heatmap effect.

Heatmaps were discussed in [2d Tracks—Heatmap
tutorial](//documentation/tutorials/2d_tracks/heatmaps).

#### assigning value to links
At this time there is no way to associate a value with a link in the same way.
However, you can subvert one of the link parameters to do so. For example, use
a `value` parameter.

```    
    hs12 117427133 132349534 hs2 94056542 114056542 value=2
    hs22 33232924 49691432 hs4 88399610 108399610 value=5
```
#### coloring links by value
Now that each link has a value, it's time to use it to set its color. Rules
are used for this.

To reference the link's value, use `var(value)`.

The first rule maps the "url" value onto a list of colors. In this example,
the "url" value is in the range [0,4]. To map the value to a color, you will
need to use an eval() block and write a Perl one-liner to sample a list. If
the list contains entries that do not have a space (e.g. single word colors),
you can use the qw() operator which turns words into a list.

```    
    qw(red orange green blue purple)
```
Perl's syntax to sample an element of a list is

```    
    ( ...list here...)[i]
```
Combining these

```    
    (qw(red orange green blue purple))[i]
```
In this case the value of `i` is the `value` parameter, reference by
`var(value)`.

```    
    <rules>
    
    <rule>
    # always trigger this rule
    condition  = 1
    # use the link's value to sample from a list of colors
    color      = eval((qw(red orange green blue purple))[ var(value) ])
    # continue parsing other rules
    flow       = continue
    </rule>
    
    <rule>
    # always trigger this rule
    condition  = 1
    # add _a3 to the color of the ribbon, giving it 50% transparency (3/6)
    color      = eval(sprintf("%s_a3",var(color)))
    </rule>
    
    </rules>
```### images
![Circos tutorial image - Heat Map
Links](/documentation/tutorials/recipes/heatmap_links/img/01.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    <links>
    
    <link>
    
    file   = data/8/11/links.withvalue.txt
    ribbon = yes
    flat   = yes
    
    radius        = 0.95r
    bezier_radius = 0r
    crest         = 0.2
    
    <rules>
    <rule>
    # always trigger this rule
    condition  = 1
    # use the link's value to sample from a list of colors
    color      = eval((qw(red orange green blue purple))[ var(value) ])
    # continue parsing other rules
    flow       = continue
    </rule>
    
    <rule>
    # always trigger this rule
    condition  = 1
    # add _a3 to the color of the ribbon, giving it 50% transparency (3/6)
    color      = eval(sprintf("%s_a3",var(color)))
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 3
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    break   = 0.5r
    
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
    stroke_thickness = 2
    thickness        = 1.5r
    </break>
    
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
    label_radius     = dims(image,radius) - 50p
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.85r
    thickness        = 30p
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
    tick_separation      = 3p
    label_separation     = 5p
    radius               = dims(ideogram,radius_outer)+50p
    multiplier           = 1e-6
    color          = black
    size           = 20p
    thickness      = 4p
    label_offset   = 5p
    format         = %d
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 16p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 18p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    </tick>
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
```
  

* * *
