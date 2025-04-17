---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Link Rules - Part II
---

## Link Rules - Part II
### lesson
Rules are worth learning—they allow you to customize the layering and
formating your links.

In the previous tutorial, we saw how links can be identified by changing their
color based on chromosome assignment.

In this tutorial, I extend the example and show you how you can layer and
format links based not only on which chromosomes they connect, but also based
on position and link end size.

### multiple conditions
A rule can have multiple condition parameters. They are evaluated using
**AND** , i.e. all conditions must be satisfied for the rule to pass. This
rule tests for links that are interchromosomal and whose start size is greater
than 40kb.

```    
    <rule>
    condition = var(interchr)
    condition = var(size1) > 40kb
    ...
    </rule>
```
While you can always combine the conditions in one parameter,

```    
    condition = var(interchr) && var(size1) > 40kb
```
it is more modular and transparent to take advantage of multiple conditions.
Just remember: the conditions are combined with AND, **not OR**.

### helper functions
There are several helper functions that simplify testing data point position.

  * `on(CHR)` returns 1 if data point on chromosome `CHR`, for links tests both ends 
  * `from(CHR)` returns 1 if start of link is on chromosome `CHR`, used for links only 
  * `to(CHR)` returns 1 if start of link is on chromosome `CHR`, used for links only 
  * `between(CHR1,CHR2)` returns 1 if link is between `CHR1` and `CHR2`, regardless of orientation, used for links only 
  * `fromto(CHR1,CHR2)` returns 1 if link is from `CHR1` to `CHR2`, used for links only 
  * `tofrom(CHR1,CHR2)` returns 1 if link is from `CHR2` to `CHR1`, used for links only 

The `on()` function has a variant that tests for both chromosome and
coordinate.

  * `on(CHR,START,END)` returns 1 if data point is on chromosome CHR and intersects coordinate START-END, for links tests both ends 

To test that the data point coordinate falls entirely within the interval, use
`within()`.

  * `within(CHR,START,END)` returns 1 if data point is on chromosome CHR and falls entirely within START-END, for links tests both ends 

### 5-rule example
The first rule, colors any interchromosomal links whose either end falls on
hs2:65-75Mb.

The next four rules change the color and thickness based on the maximum size
of the link ends. The links with the largest ends (> 40kb) are made green and
thick and successive rules retest with a lower maximum size cutoff.  #
multiple conditions are combined with AND  # i.e. all conditions must be
satisfied condition = var(interchr) condition = on(hs2,65Mb,75Mb) z = 60 color
= red thickness = 5  condition = max(var(size1),var(size2)) > 40kb z = 50
color = green thickness = 5  condition = max(var(size1),var(size2)) > 10kb z =
45 color = dgrey thickness = 4  condition = max(var(size1),var(size2)) > 5kb z
= 40 color = grey thickness = 3  condition = max(var(size1),var(size2)) > 1000
z = 35 color = lgrey thickness = 2

Notice that I did not set flow = continue for these rules, since they were
designed to short-circuit. The first rule that matches is the only rule that I
want to affect the format parameters.
### images
![Circos tutorial image - Link Rules - Part
II](/documentation/tutorials/links/rules2/img/01.png)
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
    
    z      = 0
    radius = 0.975r
    crest  = 1
    color  = vlgrey
    bezier_radius        = 0r
    bezier_radius_purity = 0.5
    thickness  = 2
    
    <link>
    
    file       = data/5/segdup.txt
    
    <rules>
    
    <rule>
    # multiple conditions are combined with AND 
    # i.e. all conditions must be satisfied
    condition  = var(interchr) 
    condition  = within(hs2,40Mb,80Mb)
    z          = 60
    color      = red
    thickness  = 5
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 40kb
    z          = 50
    color      = green
    thickness  = 5
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 10kb
    z          = 45
    color      = dgrey
    thickness  = 4
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 5kb
    z          = 40
    color      = grey
    thickness  = 3
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) > 1000
    z          = 35
    color      = lgrey
    thickness  = 2
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
