---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Combining Scales
---

### lesson
In this final example, I combine all the scale adjustments discussed in this
tutorial section into one image. I've added a histogram plot, in addition to
the heat map, that shows the scale across the ideograms. The histogram y-axis
is graduated every 0.5 from 0x to 10x. The y-axis labels were added in post-
processing (Circos does not know how to do this - yet).

Chromosomes 1, 2 and 3 are displayed, with chromosome 2 split into three
ideograms. Two ranges on chromosome 2 are defined 0-100 and 150-), as well as
an axis break 40-60Mb. Chromosomes 1 and 3 have a baseline scale of 1x and
chromosome 2 has a baseline scale of 2x (first two ideograms) and 0.5x (third
ideogram).

Notice how the three ideograms on chromosome two are defined. First, Circos is
told to draw two regions 0-100 (ideogram id "a") and 150-) (ideogram id "b").
Scale factors of 2x and 0.5x are then assigned to these ideograms. Finally, an
axis break is introduced at 40-60Mb, which breaks the "a" ideogram into two.
However, the global scale is still 2x across the two new pieces, which are
still internally labeled as "a", and therefore the ideogram label is 2a for
both pieces.

At the moment, you cannot define a different global scale for ideograms that
contain an axis break. If you needed the same regions drawn, each with a
different global scale, you would define them as follows, for example

```    
    chromosomes: hs2[a]:0-40;hs2[b]:60-100;hs2[c]:150-)
    chromosomes_scale: a:2;b:3;c:0.5
```
There are several local scale adjustments in this example. On chromosome 1,
there are two zoom regions that are smoothed and their smoothing regions
overlap. Recall the rule that for a given region the scale factor is taken to
be the largest absolute zoom level for any zoom region that overlaps with it.
As the smoothing of the 10x and 0.2x regions run into each other, the is a
sudden scale shift (marked by red arrot in the vicinity of chr1:140Mb).
Currently, scale smoothing is not iterative - there is no additional smoothing
applied between adjacent smoothing regions.

On chromosome 2 there is a 5x zoom region at the start of the first ideogram.
Its smoothing region runs off the edge of the ideogram.

On chromosome 3 there are two nested zoom regions. The outer region is 0.5x
25-150Mb and the inner region is 10x 72-73Mb. Both are smoothed, but their
smoothing does not overlap.

Currently, a region is smoothed by gradually adjusting its scale from that
defined in the configuration file to the ideogram's base scale. In the last
case, where one region (10x) was nested inside another (0.5x), the inner
region is still smoothed between 10x and 1x, the latter being the ideograms'
base scale. Keep this in mind when nesting regions.

Finally, a word about tick marks and scale adjustment. Experiment with the
tick mark parameters `label_separation`, `tick_separation` and
`min_label_distance_to_edge`. If you are going to be significantly expand the
scale in some regions, define tick marks with sufficiently small spacing to
cover the expanded region in ticks. Set the tick_separation to avoid tick mark
crowding in regions with a lower scale.

If you are going to change scale, make sure that this fact is made clear in
your figure. You can mark this fact by using highlights or a heatmap. Circos
will produce a report of zoom regions as it's drawing the image, and you can
use this output to create data files to annotate the figure (you need to run
Circos twice — once to generate the file and again to plot it).

```    
    ...
    zoomregion ideogram 1 chr hs2  17000001  18000001 scale  2.82 absolutescale  2.82
    zoomregion ideogram 1 chr hs2  18000001  19000001 scale  2.55 absolutescale  2.55
    zoomregion ideogram 1 chr hs2  19000001  20000001 scale  2.27 absolutescale  2.27
    zoomregion ideogram 1 chr hs2  20000001  40000000 scale  2.00 absolutescale  2.00
    zoomregion ideogram 2 chr hs2  59999999  60000001 scale  1.83 absolutescale  1.83
    zoomregion ideogram 2 chr hs2  60000001  61000001 scale  1.75 absolutescale  1.75
    zoomregion ideogram 2 chr hs2  61000001  62000001 scale  1.67 absolutescale  1.67
    zoomregion ideogram 2 chr hs2  62000001  63000001 scale  1.58 absolutescale  1.58
    zoomregion ideogram 2 chr hs2  63000001  64000001 scale  1.50 absolutescale  1.50
    zoomregion ideogram 2 chr hs2  64000001  65000001 scale  1.42 absolutescale  1.42
    zoomregion ideogram 2 chr hs2  65000001  66000001 scale  1.33 absolutescale  1.33
    zoomregion ideogram 2 chr hs2  66000001  67000001 scale  1.25 absolutescale  1.25
    ...
```
The absolute scale is `max(scale,1/scale)`.
### images
![Circos tutorial image - Combining
Scales](/documentation/tutorials/scaling/combining_scales/img/01.png) ![Circos
tutorial image - Combining
Scales](/documentation/tutorials/scaling/combining_scales/img/02.png) ![Circos
tutorial image - Combining
Scales](/documentation/tutorials/scaling/combining_scales/img/03.png) ![Circos
tutorial image - Combining
Scales](/documentation/tutorials/scaling/combining_scales/img/04.png)
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
    
    <zooms>
    
    <zoom>
    chr    = hs1
    start  = 120u
    end    = 125u
    scale  = 10
    smooth_distance = 2r
    smooth_steps    = 10
    </zoom>
    
    <zoom>
    chr    = hs1
    start  = 150u
    end    = 160u
    scale  = 0.2
    smooth_distance = 5r
    smooth_steps    = 10
    </zoom>
    
    <zoom>
    chr    = hs2
    start  = 5u
    end    = 10u
    scale  = 5
    smooth_distance = 10u
    smooth_steps    = 10
    </zoom>
    
    <zoom>
    chr    = hs2
    start  = 78u
    end    = 82u
    scale  = .25
    smooth_distance = 20u
    smooth_steps    = 20
    </zoom>
    
    <zoom>
    chr    = hs3
    start  = 25u
    end    = 150u
    scale  = 0.5
    smooth_distance = 15u
    smooth_steps = 5
    </zoom>
    
    <zoom>
    chr    = hs3
    start  = 72u
    end    = 73u
    scale  = 10
    smooth_distance = 5u
    smooth_steps = 10
    </zoom>
    
    </zooms>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    chromosomes        = hs1;hs2[a]:0-100;hs2[b]:150-);hs3
    chromosomes_breaks = -hs2:40-60
    chromosomes_scale  = a:2;b:0.5
    
    <plots>
    
    <plot>
    type  = heatmap
    file  = data/7/heatmap.zoom-05.txt
    r1    = 0.95r
    r0    = 0.90r
    color = spectral-9-div
    stroke_color     = black
    stroke_thickness = 1
    scale_log_base   = 1.5
    </plot>
    
    <plot>
    type = histogram
    file = data/7/heatmap.zoom-05.txt
    r1   = 0.89r
    r0   = 0.60r
    color     = black
    thickness = 2
    
    min = 0
    max = 10
    
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
    data_out_of_range* = trim
```
  

* * *

#### bands.conf
```    
    show_bands            = no
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 3
```
  

* * *

#### breaks.conf
```    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color     = black
    fill_color       = blue
    thickness        = 0.25r
    stroke_thickness = 2
    </break_style>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 2
    thickness        = 2r
    </break_style>
``````
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    break   = 0.5r
    
    <<include breaks.conf>>
    
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
    thickness        = 50p
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
    tick_separation  = 3p
    label_separation = 10p
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    label_offset     = 5p
    format           = %d
    
    <tick>
    #chromosomes_display_default = no
    chromosomes    = -hs9
    spacing        = 0.5u
    show_label     = no
    size           = 6p
    </tick>
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 16p
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 18p
    size           = 14p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    size           = 18p
    </tick>
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    <tick>
    spacing        = 100u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    </ticks>
```
  

* * *
