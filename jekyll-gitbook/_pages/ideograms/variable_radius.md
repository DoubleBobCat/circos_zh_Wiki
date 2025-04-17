---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Variable Radius
---

### lesson
By default, every ideogram is placed at the same radial position. This is
controlled by the radius parameter within the <ideogram> block (conventionally
found in `ideogram.conf`).

```    
    <ideogram>
    ...
    radius = 0.85r
    ...
    </ideogram>
```
The value is relative to the image radius.

You can place individual ideograms at different radial positions by using the
`chromosomes_radius` parameter in the root of the configuration tree.

```    
    chromosomes_radius = hs1:0.5r;hs2:0.55r;hs3:0.6r;hs4:0.65r;hs5:0.7r;hs6:0.75r;hs7:0.8r;hs8:0.85r;hs9:0.9r;hs10:0.95r
```
The radial position values in this parameter are relative to the default
ideogram radius, defined by radius in the <ideogram> block.

For example, if the image radius is `1500p` and the default ideogram radius is
`0.9r`, then all ideograms are at 1350 pixels (1500×0.9) from the center. Now,
if chromosomes_radius further specifies `hs1:0.5r`, then `hs1` will appear at
675 pixels from the center (1500×0.9×0.5).

Once the radial position of an ideogram has been redefined using
`chromosomes_radius`, all features associated with that ideogram (plots,
links, text, etc) will be automatically relocated to match the new ideogram
position. In other words, you do not need to remember that specific ideograms
may be at different positions.

#### setting radius for tagged ideograms
If you've tagged your ideograms when creating regions,

```    
    chromosomes = hs1[a]:0-50;hs1[b]:150-);hs2[c]:0-50;hs2[d]:150-);hs3[e]
```
then adjusting the radius of any region can be done by using the tag

```    
    chromosomes_radius = hs1:0.8r;a:0.9r;d:0.8r
```
The radius values will be processed in order, with subsequent radius values
overriding previous ones. For example, each region of `hs1` will be set to
0.8r, but the region tagged by `a` will be 0.9r.

#### suppressing ticks and tick labels
When decreasing the radius of an ideogram you may find that the ticks and
their labels crowd together. In these cases, it is useful to use the
`tick_separation` and `label_separation` parameters in the <ticks> block to
define the minimum distance between ticks and their labels.
### images
![Circos tutorial image - Variable
Radius](/documentation/tutorials/ideograms/variable_radius/img/01.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.hg19.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = yes
    chromosomes_radius          = hs1:0.40r;hs2:0.43r;hs3:0.45r;hs4:0.48r;hs5:0.50r;hs6:0.53r;hs7:0.56r;hs8:0.58r;hs9:0.61r;hs10:0.63r;hs11:0.66r;hs12:0.69r;hs13:0.71r;hs14:0.74r;hs15:0.77r;hs16:0.79r;hs17:0.82r;hs18:0.84r;hs19:0.87r;hs20:0.90r;hs21:0.92r;hs22:0.95r;hsX:0.97r;hsY:1.00r
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 4
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.0025r
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
    label_font       = bold
    # labels outside circle
    #label_radius     = dims(ideogram,radius) + 0.05r
    #labels inside circle
    label_radius     = dims(ideogram,radius) - 175p
    label_with_tag   = yes
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
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
    skip_first_label = no
    skip_last_label  = no
    radius           = dims(ideogram,radius_outer)
    tick_separation  = 3p
    label_separation = 1p
    multiplier       = 1e-6
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 1u
    show_label     = no
    thickness      = 2p
    color          = dgrey
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = no
    thickness      = 3p
    color          = vdgrey
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    grid_start     = 0.5r
    grid_end       = 0.999r
    </tick>
    
    </ticks>
```
  

* * *
