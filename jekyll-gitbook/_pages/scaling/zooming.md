---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Creating Zoomed Regions
---

## Creating Zoomed Regions
### lesson
Local scale adjustment is one of the coolest features of Circos. In the first
two examples in this tutorial section you saw how to adjust local scale by
splitting a chromosome into multiple ideograms and assigning each ideogram a
different scale value. This worked, but required that you create multiple
ideograms. Sometimes this is the right approach, especially if you need to
both crop and zoom your data domain.

Local adjustment of scale is for cases when you want to zoom parts of your
data domain without cropping. If you think of the ideogram as a rubber band,
applying a local scale adjustment is analogous to locally stretching or
compressing the rubber band. The effect is that you still see the entire
rubber band, but the length scale across it is variable.

You can adjust length scale locally by using the <zooms> block. For example,

```    
    <zooms>
     <zoom>
     chr = hs1
     start = 100u
     end   = 120u
     scale = 5
     </zoom>
     <zoom>
     chr = hs1
     start = 120u
     end   = 130u
     scale = 10
     </zoom>
    </zoom>
```
will locally stretch the region 100-120Mb of hs1 by 5x and the region
120-130Mb of hs1 by 10x. Remember that the "u" is a unit designation that
specifies the value to be in units of the value of chromosomes_units, which I
set to 1,000,000.

Notice that zoom definitions are independent of the "chromosomes" and
"chromosomes_breaks" parameters. In effect, you define length scales for
regions independently of the definition of which regions to draw. Obviouly,
zoom settings will only have an effect on your image if they apply to regions
of the genome that are drawn.

In this example, I have defined several zoom regions on hs1 and hs2. On hs1
the scale is increased, zooming into a part of the chromosome. On hs2 the
scale is decreased, collapsing certain regions. I've added a heatmap to the
image to help see the regions that are affected.

Both ideograms in the image in this example are internally demarcated into
regions with the following scale.

```    
                                      START       END
    zoomregion ideogram 0 chr hs1         0  99999999 scale  1.00 absolutescale  1.00
    zoomregion ideogram 0 chr hs1  99999999 119999999 scale  2.00 absolutescale  2.00
    zoomregion ideogram 0 chr hs1 119999999 129999999 scale  3.00 absolutescale  3.00
    zoomregion ideogram 0 chr hs1 129999999 139999999 scale  5.00 absolutescale  5.00
    zoomregion ideogram 0 chr hs1 139999999 142500001 scale 10.00 absolutescale 10.00
    zoomregion ideogram 0 chr hs1 142500001 247249719 scale  1.00 absolutescale  1.00
    zoomregion ideogram 1 chr hs2         0  99999999 scale  1.00 absolutescale  1.00
    zoomregion ideogram 1 chr hs2  99999999 119999999 scale  0.50 absolutescale  2.00
    zoomregion ideogram 1 chr hs2 119999999 139999999 scale  0.25 absolutescale  4.00
    zoomregion ideogram 1 chr hs2 139999999 160000001 scale  0.10 absolutescale 10.00
    zoomregion ideogram 1 chr hs2 160000001 180000001 scale  0.25 absolutescale  4.00
    zoomregion ideogram 1 chr hs2 180000001 200000001 scale  0.50 absolutescale  2.00
    zoomregion ideogram 1 chr hs2 200000001 242951149 scale  1.00 absolutescale  1.00
```
#### defining zoomed regions
In this example the regions to which zooming was applied did not overlap (e.g.
100-120Mb, 120-140Mb, 140-160Mb, and so on). In the next example you'll see
what happens when you define overlapping regions with different zoom levels.
Hint: the largest absolute zoom wins.
### images
![Circos tutorial image - Creating Zoomed
Regions](/documentation/tutorials/scaling/zooming/img/01.png) ![Circos
tutorial image - Creating Zoomed
Regions](/documentation/tutorials/scaling/zooming/img/02.png) ![Circos
tutorial image - Creating Zoomed
Regions](/documentation/tutorials/scaling/zooming/img/03.png) ![Circos
tutorial image - Creating Zoomed
Regions](/documentation/tutorials/scaling/zooming/img/04.png)
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
    start  = 100u
    end    = 120u
    scale  = 2
    </zoom>
    <zoom>
    chr    = hs1
    start  = 120u
    end    = 130u
    scale  = 3
    </zoom>
    <zoom>
    chr    = hs1
    start  = 130u
    end    = 140u
    scale  = 5
    </zoom>
    <zoom>
    chr    = hs1
    start  = 140u
    end    = 142.5u
    scale  = 10
    </zoom>
    <zoom>
    chr    = hs2
    start  = 100u
    end    = 120u
    scale  = 0.5
    </zoom>
    <zoom>
    chr    = hs2
    start  = 120u
    end    = 140u
    scale  = 0.25
    </zoom>
    <zoom>
    chr    = hs2
    start  = 140u
    end    = 160u
    scale  = 0.1
    </zoom>
    <zoom>
    chr    = hs2
    start  = 160u
    end    = 180u
    scale  = 0.25
    </zoom>
    <zoom>
    chr    = hs2
    start  = 180u
    end    = 200u
    scale  = 0.5
    </zoom>
    </zooms>
    
    chromosomes_units = 1000000
    chromosomes = hs1;hs2
    chromosomes_display_default = no
    
    <plots>
    <plot>
    type  = heatmap
    file  = data/7/heatmap.zoom-01.txt
    r1    = 0.95r
    r0    = 0.90r
    color = spectral-9-div
    stroke_color     = black
    stroke_thickness = 1
    scale_log_base   = 0.33
    </plot>
    </plots>
    
    <<include etc/housekeeping.conf>>
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
