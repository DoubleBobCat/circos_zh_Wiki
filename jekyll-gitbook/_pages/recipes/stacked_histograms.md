---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Stacked Histograms
---

## Stacked Histograms
### lesson
#### stacking data sets
Stacked histograms are an extenstion of the histogram track. To plot stacked
histograms, the only adjustment you require is to provide a series of values
for each histogram bin in your data file.

For example, here is a part of a data file for a stacked histogram in which 5
data sets are stacked.

```    
    ...
    hs7 65000000 69999999 0.388090,0.070074,0.547485,0.842239,0.525658
    hs7 70000000 74999999 0.886542,0.321023,0.145677,0.897684,0.264217
    hs7 75000000 79999999 0.854199,0.567889,0.574767,0.656331,0.418385
    hs7 80000000 84999999 0.286509,0.201049,0.552485,0.876529,0.999801
    hs7 85000000 89999999 0.154836,0.515471,0.389453,0.440168,0.475127
    ...
```
The first value will appear at the bottom of the bin's stack, then the second,
then third, and so on.

#### formatting stacked data sets
Individual format parameters (`color`, `thickness` `fill_color`, `pattern`)
for each data sets can be specified by providing a list of comma-separated
values.

For example, to make each data set filled with a different color, provide five
different values for `fill_color`.

```    
    fill_color = red,orange,yellow,green,blue
```
If you provide parameter values than data sets, they will be cycled.

Assigning individual values for color and thickness can produce useful
displays, particularly when `color=white` and `thickness` is varied.

```    
    color      = white
    fill_color = red,orange,yellow,green,blue
    fill_under = yes
    thickness  = 1,2,3,4,5
```
#### colors and patterns
You can independently cycle bins' color and pattern.

```    
    fill_color = red,grey,black
    pattern    = checker,solid
```
will create the following bins

```    
      color  pattern
      red    checker
      grey   solid
      black  checker
      red    solid
      grey   checker
      black  solid
      ...    ...
```
#### adjusting stack order
By default, the bins are stacked in order of appearance of their values in the
data file. Thus, given the colors

```    
    fill_color = red,orange,yellow,green,blue
```
the data line

```    
    hs1 0 4999999 0.237788,0.291066,0.845814,0.152208,0.585537
```
the bins will stack in the following order

  * 0.237788 (red) 
  * 0.291066 (orange) 
  * 0.845814 (yellow) 
  * 0.152208 (green) 
  * 0.585537 (blue) 

However, when

```    
    sort_bin_values = yes
```
is used, the bins will be stacked by decreasing value

  * 0.845814 (yellow) 
  * 0.585537 (blue) 
  * 0.291066 (orange) 
  * 0.237788 (red) 
  * 0.152208 (green) 
### images
![Circos tutorial image - Stacked
Histograms](/documentation/tutorials/recipes/stacked_histograms/img/01.png)
![Circos tutorial image - Stacked
Histograms](/documentation/tutorials/recipes/stacked_histograms/img/02.png)
![Circos tutorial image - Stacked
Histograms](/documentation/tutorials/recipes/stacked_histograms/img/03.png)
![Circos tutorial image - Stacked
Histograms](/documentation/tutorials/recipes/stacked_histograms/img/04.png)
![Circos tutorial image - Stacked
Histograms](/documentation/tutorials/recipes/stacked_histograms/img/05.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes                 = /hs[1-3]$/
    chromosomes_display_default = no
    
    <plots>
    
    <plot>
    
    file = data/8/histogram.stacked.txt
    type = histogram
    r0   = 0.6r
    r1   = 0.95r
    min  = 0
    max  = 5
    
    color      = white
    fill_color = red,orange,yellow,green,blue
    #fill_color = grey,grey,grey,black,black
    #pattern    = vline,hline,solid,checker,solid
    thickness  = 2
    #thickness  = 1,5,10,15,20
    
    sort_bin_values = no
    extend_bin      = no
    
    <axes>
    <axis>
    color     = lgrey
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
``````
  

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
