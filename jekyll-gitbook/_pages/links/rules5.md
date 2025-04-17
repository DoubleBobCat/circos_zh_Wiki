---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Link Rules - Part V
---

### lesson
In the previous examples of rules, I triggered rules to adjust format
parameters of links or data points based on their position (start, end,
chromosome) or y-value (for plots). In this example, I'll show how to trigger
rules based on values of format parameters. This may seem a little strange at
first, but trust me, it's useful!

The input data set for this example is a subset of segmental duplications.
I've formatted the links by randomly assigning one of the following formats to
the data lines

  * `color = red`
  * `color = blue`
  * `thickness = 5`

Here's an excerpt of the data file

```    
    segdup00002 hs1 486 76975
    segdup00002 hs15 100263879 100338121
    segdup00011 hs1 71096 76975 thickness=5
    segdup00011 hs1 388076 393885 thickness=5
    ...
    segdup00062 hs1 120975 125718 color=blue
    segdup00062 hs1 220708073 220712741 color=blue
    segdup00071 hs1 129327 166636 color=red
    segdup00071 hs1 665046 702417 color=red
    ...
```
There are four kinds of links, therefore, those with: no additional format,
red color, blue color and thickness 5.

I'll show you how to write rules that adjust parameters of the links based on
these format parameters. Consider these two rules

```    
    <rule>
    condition  = var(thickness) == 4
    condition  = rand() < 0.25
    thickness  = 10
    color      = green
    z          = 15
    </rule>
    
    <rule>
    condition  = var(color) eq "red"
    thickness  = 4
    z          = 10
    flow       = restart
    </rule>
    
    <rule>
    condition  = var(color) ne "grey" && var(thickness) == 2
    z          = 5
    </rule>
```
The first rule applies to any links with a thickness of 4 red and assigns them
a thickness of 10, colors them green and sets their z-depth to 15. The second
condition applies the rule to only 25% of these links, since the value of
`rand()` is smaller than 0.25 this fraction of the time.

The next rule sets the thickness and z-depth of red links and then restarts
the rule chain. Thus, red links which are made thicker can be further modified
by the first rule, on the second loop through the rule chain. A rule can
restart the rule chain only once in order to avoid an endless loop.

The final rule sets the z-depth of any non-grey links whose thickness is 2.
### images
![Circos tutorial image - Link Rules - Part
V](/documentation/tutorials/links/rules5/img/01.png) ![Circos tutorial image -
Link Rules - Part V](/documentation/tutorials/links/rules5/img/02.png)
![Circos tutorial image - Link Rules - Part
V](/documentation/tutorials/links/rules5/img/03.png) ![Circos tutorial image -
Link Rules - Part V](/documentation/tutorials/links/rules5/img/04.png)
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
    chromosomes_display_default = no
    chromosomes       = hs1;hs2;hs3;hs4
    
    <links>
    
    radius = 0.975r
    crest  = 1
    color  = grey
    bezier_radius        = 0r
    bezier_radius_purity = 0.5
    thickness    = 2
    
    <link>
    
    file         = data/5/segdup.bundle3.colored.txt
    
    <rules>
    
    <rule>
    condition  = var(thickness) == 4
    condition  = rand() < 0.25
    thickness  = 10
    color      = green
    z          = 15
    </rule>
    
    <rule>
    condition  = var(color) eq "red"
    thickness  = 4
    z          = 10
    flow       = restart
    </rule>
    
    <rule>
    condition  = var(color) ne "grey" && var(thickness) == 2
    z          = 5
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
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
