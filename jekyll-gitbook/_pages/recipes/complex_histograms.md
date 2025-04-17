---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Complex Histograms
---

### lesson
#### mapping value to histogram fill
The fill of histogram bins can be changed based on the histogram bin value
using a rule like the following.

```    
    # remap the histogram value from the range [-0.6,0.6] onto the index [0,5], then
    # use the index to select the color from the list
    # dorange orange lorange lblue blue dblue
    # 
    # Perl syntax for referencing an element of a list is qw(a b c d)[index]
    # where index starts at 0.
    <rule>
    condition  = 1
    fill_color = eval(qw(dorange orange lorange lblue blue dblue)[remap_int(var(value),-0.6,0.6,0,5)])
    </rule>
```
#### layered background color and macros
Recall that you can use `conf()` to reference a configuration parameter. This
is described in detail in the [Automation and Macros
tutorial](//documentation/tutorials/quick_start/automation_and_macros).

In this example, I create a background for the histogram track that has six
colored layers: tones of blue for positive values and tones of orange for
negative values. Both cutoffs for the layers and colors will be defined as
parameters within the <plot> block.

Each separate colored layer in the background is defined by its own
<background> block.

```    
    <plot>
    ...
    # define background color cutoffs
    bgy1 = 0.2    # first cutoff
    bgy2 = 0.5    # second cutoff
    bgc1 = orange # bg color for negative values
    bgc2 = blue   # bg color for positive values
    ...
    
    <backgrounds>
    # use the parameters above using conf(.,param)
    <background>
    color = lconf(.,bgc2)
    y0    = conf(.,bgy2)
    </background>
    <background>
    color = vlconf(.,bgc2)
    y1    = conf(.,bgy2)
    y0    = conf(.,bgy1)
    </background>
    <background>
    color = vvlconf(.,bgc2)
    y1    = conf(.,bgy1)
    y0    = 0
    </background>
    <background>
    color = vvlconf(.,bgc1)
    y1    = 0
    y0    = -conf(.,bgy1)
    </background>
    <background>
    color = vlconf(.,bgc1)
    y1    = -conf(.,bgy1)
    y0    = -conf(.,bgy2)
    </background>
    <background>
    color = lconf(.,bgc1)
    y1    = -conf(.,bgy2)
    </background>
    </backgrounds>
    
    </plot>
```
#### y-axis grid and macros
The axis grid can also reference the histogram cutoff values.

```    
    <axes>
    
    # every 25% with low transparency
    <axis>
    color     = grey_a1
    thickness = 2
    spacing   = 0.25r
    
    # every 5% with higher transparency
    <axis>
    color     = grey_a3
    thickness = 1
    spacing   = 0.05r
    </axis>
    
    # thick line at y=0
    <axis>
    color     = grey_a1
    thickness = 5
    position  = 0
    </axis>
    
    # at each background cutoff, a thick white line
    <axis>
    color     = white
    thickness = 5
    position  = -conf(.,bgy2),-conf(.,bgy1),conf(.,bgy1),conf(.,bgy2)
    </axis>
    
    </axes>
```### images
![Circos tutorial image - Complex
Histograms](/documentation/tutorials/recipes/complex_histograms/img/01.png)
![Circos tutorial image - Complex
Histograms](/documentation/tutorials/recipes/complex_histograms/img/02.png)
### configuration
#### circos.conf
```    
    # Define a parameter that will be used in <rules> block to
    # globally toggle rules on/off. This can be convenient if you
    # have many <rules> blocks and want to turn them all off using
    # one parameter.
    use_rules = yes
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype                   = data/karyotype/karyotype.human.txt
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    
    #chromosomes = hs1;hs2;hs3;hs4;hs5;hs6
    
    <plots>
    
    type       = histogram
    file       = data/8/histogram.txt
    color      = black
    thickness  = 2
    extend_bin = no
    
    <plot>
    r0   = 0.3r
    r1   = 0.975r
    min  = -0.6
    max  = 0.6
    
    # define background colors and cutoffs
    bgy1 = 0.2
    bgy2 = 0.5
    bgc1 = orange
    bgc2 = blue
    
    <backgrounds>
    <background>
    color = lconf(.,bgc2)
    # reference the background cutoffs using conf(.,PARAM)
    y0    = conf(.,bgy2)
    </background>
    <background>
    color = vlconf(.,bgc2)
    y1    = conf(.,bgy2)
    y0    = conf(.,bgy1)
    </background>
    <background>
    color = vvlconf(.,bgc2)
    y1    = conf(.,bgy1)
    y0    = 0
    </background>
    <background>
    color = vvlconf(.,bgc1)
    y1    = 0
    y0    = -conf(.,bgy1)
    </background>
    <background>
    color = vlconf(.,bgc1)
    y1    = -conf(.,bgy1)
    y0    = -conf(.,bgy2)
    </background>
    <background>
    color = lconf(.,bgc1)
    y1    = -conf(.,bgy2)
    </background>
    
    </backgrounds>
    
    <axes>
    <axis>
    color     = grey_a1
    thickness = 2
    spacing   = 0.25r
    </axis>
    <axis>
    color     = grey_a3
    thickness = 1
    spacing   = 0.05r
    </axis>
    <axis>
    color     = grey_a1
    thickness = 5
    position  = 0
    </axis>
    # at each background cutoff, draw a white line
    <axis>
    color     = white
    thickness = 5
    position  = -conf(.,bgy2),-conf(.,bgy1),conf(.,bgy1),conf(.,bgy2)
    </axis>
    </axes>
    
    <rules>
    use        = conf(use_rules)
    # remap the histogram value from the range [-0.6,0.6] onto the index [0,5], then
    # use the index to select the color from the list
    # dorange orange lorange lblue blue dblue
    # 
    # Perl syntax for referencing an element of a list is qw(a b c d)[index]
    # where index starts at 0.
    <rule>
    condition  = 1
    fill_color = eval(qw(dorange orange lorange lblue blue dblue)[remap_round(var(value),-0.6,0.6,0,5)])
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
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
    radius           = 0.90r
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
    radius               = dims(ideogram,radius_outer)
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
