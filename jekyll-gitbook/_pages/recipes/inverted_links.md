---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Inverted Links
---

## Inverted Links
### lesson
In this tutorial, I will show how to write rules that format inverted links.

A link is considered inverted if the orientation of its two ends is inverted
with respect to one another. For example, given a link defined by the two ends
`chrA:start1-end1` and `chrB:start2-end2`, the link is inverted if

```    
    start1 < end1 && start2 > end2
    
    or
    
    start1 > end1 && start2 < end2
```
The interpretation of the case

```    
    start1 > end1 && start2 > end2
```
depends on your application.

#### link geometry
Recall that links are defined by specifing the position and orientation of
their ends. When links are drawn as ribbons, the relative orientation of the
link's ends affects whether the ribbon has a twist (see [Link—Twists
tutorial](//documentation/tutorials/links/twists)).

In that tutorial, you saw that you can make a link ribbon flat (i.e. without a
twist), regardless of the orientation of the link, by setting

```    
    flat = yes
```
in the link block. By adding the `twist` parameter to the link, the ribbon
could be made to twist even if `flat=yes` was set.

```    
    hs1 100 200 hs2 100 200
    # this link's ribbon will be twisted, even if flat=yes is set
    hs3 100 200 hs4 100 200 twist=1
```
Adding the `inverted` parameter to one of the link's ends in the data file
swaps its start and end coordinates. This parameter is useful if you want to
keep start < end for all your links, but still store information about the
orientation.

```    
    hs1 100 200 hs2 100 200
    # when a link end has inverted*=1, its start/end coordinates
    # are reversed. For the start of the link use inverted1 and
    # for the end inverted2.
    hs3 100 200 hs4 100 200 inverted1=1
```
The difference between the `twist` and `inverted` parameters is that `twist`
is meant to affect how a link's ribbon is drawn and `inverted` is meant to
actually alter how a link is defined.

Keep in mind that the orientation of the link's ideograms has an effect on the
link's twist. Link ribbons, by default, have their corners drawn in the order
start1 -> end1 -> end2 -> start2, which results in a twist for a link with
start < end for both ends when the ideograms are oriented in the same
direction.

#### testing for inversion
To test whether a link is inverted, use the `var(rev1)` and `var(rev2)`
keywords in a rule. Each of these strings evaluate to 1 if the start and end
of the link are inverted, respectively.

For example, this rule will color orange all links which have their ends
inverted.

```    
    <rule>
    condition  = var(rev2)
    color      = orange
    </rule>
```
You can test one or both ends for inversion, though if both ends of a link are
inverted the link itself could be consider as not inverted. It is up to you
how to interpret this case.

```    
    <rule>
    condition  = var(rev1) && var(rev2)
    color      = red
    </rule>
    
    <rule>
    condition  = var(rev1)
    color      = green
    </rule>
    
    <rule>
    condition  = var(rev2)
    color      = orange
    </rule>
```
#### defining inverted links
To indicate that a link is inverted, you can either reverse the coordinates of
one of its ends, or assign it the `inverted` parameter.

```    
    # this is a normal link
    chr1 100 200 chr2 100 200
    
    # this is an inverted link - its first end is inverted
    chr1 200 100 chr2 100 200
    
    # this is an inverted link - its first end is inverted using the 'inverted' flag
    chr1 100 200 chr2 100 200 inverted1=1
    
    # this is an inverted link - its second end is inverted
    chr1 100 200 chr2 200 100
    
    # this is an inverted link - its second end is inverted using the 'inverted' flag
    chr1 100 200 chr2 100 200 inverted2=1
```
How you choose to store information about inversion is up to you. Unless you
are using the link input file in other analysis that requires strictly that
`start<=end`, I suggest you use explicit coordinate inversion.
### images
![Circos tutorial image - Inverted
Links](/documentation/tutorials/recipes/inverted_links/img/01.png) ![Circos
tutorial image - Inverted
Links](/documentation/tutorials/recipes/inverted_links/img/07.png)
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
    chromosomes_display_default = no
    chromosomes                 = hs1:0-120;hs2:100-)
    
    <links>
    
    <link>
    
    file          = data/8/ribbon.txt
    ribbon        = yes
    flat          = yes
    radius        = 0.95r
    bezier_radius = 0r
    crest         = 0.2
    color         = lgrey
    
    <rules>
    <rule>
    # you can also test whether only one end is
    # reversed using var(inv)
    condition  = var(rev1) && ! var(rev2)
    color      = red
    </rule>
    <rule>
    condition  = var(rev2) && ! var(rev1)
    color      = orange
    </rule>
    <rule>
    condition  = var(rev1) && var(rev2) 
    color      = blue
    </rule>
    
    </rules>
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### circos.segdup.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/8/karyotype.human.colorbychr.txt
    
    <image>
    dir = .
    file  = circos.png
    24bit = yes
    png = yes
    svg = yes
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    #angle_orientation = counterclockwise
    
    auto_alpha_colors = yes
    auto_alpha_steps  = 5
    </image>
    
    chromosomes_units           = 1000000
    
    chromosomes_display_default = no
    chromosomes = hs1;hs2
    #chromosomes                 = hs1:0-120;hs2:100-)
    
    <highlights>
    <highlight>
    file        = data/8/chr.highlight.txt
    r0 = 0.99r
    r1 = 0.995r
    </highlight>
    </highlights>
    
    <links>
    <link linkexample>
    
    file          = data/8/segdup.01.txt
    radius        = 0.95r
    flat          = yes
    ribbon        = yes
    bezier_radius = 0r
    crest         = 0.2
    color         = blue
    
    <rules>
    <rule>
    importance = 100
    condition  = _REV2_ == 1
    color      = lorange
    </rule>
    
    </rules>
    </link>
    </links>
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    
    #debug_group = ticks
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
