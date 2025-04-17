---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Line Plots
---

## Line Plots
### lesson
The line plot differs from the scatter plot in that there are no glyphs drawn
at each point position. Rather the points are joined by a line.

The line plot is formatted very similarly to the scatter plot, with the
following differences.

  * `type=line`
  * no glyphs - there are no glyph parameters - glyph and glyph_size do not apply. 
  * `stroke_thickness` and `stroke_color` are replaced by `thickness` and `color`, since the line isn't really outlined 
  * adjacent points whose distance is greater than `max_gap` are not joined by a line - this is useful to avoid drawing lines across large gaps (e.g. centromere) in data 

Points that fall outside of the `min/max` data range are placed at the
`min/max` extremes. Thus, if you have many adjacent points that fall outside
the data range the connecting line may run along the bottom or top of the plot
track.

If you want to explicitly remove these points from the data set, use a rule
that sets `show=no`. For example, if your `min/max` values are 0/0.5, then
this rule set will remove points falling outside the range from influencing
how the connecting line is drawn.

```    
    <rules>
    <rule>
    condition  = var(value) < 0 || var(value) > 0.5
    show       = no
    </rule>
    </rules>
```### images
![Circos tutorial image - Line
Plots](/documentation/tutorials/2d_tracks/line_plots/img/01.png) ![Circos
tutorial image - Line
Plots](/documentation/tutorials/2d_tracks/line_plots/img/02.png) ![Circos
tutorial image - Line
Plots](/documentation/tutorials/2d_tracks/line_plots/img/03.png)
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
    chromosomes       = hs1 # ;hs2;hs3
    chromosomes_display_default = no
    
    <plots>
    
    type      = line
    thickness = 2
    
    <plot>
    
    max_gap = 1u
    file    = data/6/snp.density.250kb.txt
    color   = vdgrey
    min     = 0
    max     = 0.015
    r0      = 0.5r
    r1      = 0.8r
    
    fill_color = vdgrey_a3
    
    <backgrounds>
    <background>
    color     = vvlgreen
    y0        = 0.006
    </background>
    <background>
    color     = vvlred
    y1        = 0.002
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = lgrey_a2
    thickness = 1
    spacing   = 0.025r
    </axis>
    </axes>
    
    <rules>
    
    <rule>
    condition    = var(value) > 0.006
    color        = dgreen
    fill_color   = dgreen_a1
    </rule>
    
    <rule>
    condition    = var(value) < 0.002
    color        = dred
    fill_color   = dred_a1
    </rule>
    
    </rules>
    
    </plot>
    
    # outside the circle, oriented out
    <plot>
    
    max_gap = 1u
    file    = data/6/snp.density.txt
    color   = black
    min     = 0
    max     = 0.015
    r0      = 1.075r
    r1      = 1.15r
    thickness = 1
    
    fill_color = black_a4
    
    <axes>
    <axis>
    color     = lgreen
    thickness = 2
    position  = 0.006
    </axis>
    <axis>
    color     = lred
    thickness = 2
    position  = 0.002
    </axis>
    </axes>
    
    </plot>
    
    <plot>
    z       = 5
    max_gap = 1u
    file    = data/6/snp.density.1mb.txt
    color   = red
    fill_color = red_a4
    min     = 0
    max     = 0.015
    r0      = 1.075r
    r1      = 1.15r
    </plot>
    
    # same plot, but inside the circle, oriented in
    <plot>
    max_gap = 1u
    file    = data/6/snp.density.txt
    color   = black
    fill_color = black_a4
    min     = 0
    max     = 0.015
    r0      = 0.85r
    r1      = 0.95r
    thickness   = 1
    orientation = in
    
    <axes>
    <axis>
    color     = lgreen
    thickness = 2
    position  = 0.01
    </axis>
    <axis>
    color     = vlgreen
    thickness = 2
    position  = 0.008
    </axis>
    <axis>
    color     = vlgreen
    thickness = 2
    position  = 0.006
    </axis>
    <axis>
    color     = red
    thickness = 2
    position  = 0.002
    </axis>
    </axes>
    
    </plot>
    
    <plot>
    z       = 5
    max_gap = 1u
    file    = data/6/snp.density.1mb.txt
    color   = red
    fill_color = red_a4
    min     = 0
    max     = 0.015
    r0      = 0.85r
    r1      = 0.95r
    orientation = in
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
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
    
    radius*       = 0.825r
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.775r
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
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    format           = %d
    
    <tick>
    spacing        = 1u
    show_label     = no
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    size           = 15p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
```
  

* * *
