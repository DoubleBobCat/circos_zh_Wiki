---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Scatter Plots
---

### lesson
Syntax for 2D data types is similar to that for links. You define all 2D plots
within >plots< block, with one plot per <plot> block. Within a plot block, you
define formatting and data file for the plot, and can insert optional >rules>
block that contains multiple <rule> blocks.

There are several 2D data types and the scatter plot is one. The image for
this example contains three scatter plots, all derived from the same data
file. Each plot is formatted slightly differently. The data are SNP density
for windows of 100kb (number of SNPs from dbSNP per base).

#### default settings
Each plot type has default settings which you can find in `etc/tracks`. For
example,

```    
    # etc/tracks/scatter.conf
    glyph            = circle
    glyph_size       = 10
    color            = grey
    stroke_color     = black
    stroke_thickness = 0
    r1               = 0.79r
    r0               = 0.7r
    orientation      = out
```
These settings are applied to every <plot> block of `type=scatter`. YOu can
undefine a setting using `undef`,

```    
    stroke_color = undef
```
#### basic scatter plot syntax
2D data types share have the same format parameters, with a few exceptions.
For the scatter plot, a basic definition might look like this

```    
    <plots>
    
    <plot>
    
    show  = yes
    type  = scatter
    
    file  = data/6/snp.density.txt
    r1    = 0.75r
    r0    = 0.90r
    max   = 1.0
    min   = 0.0
    
    glyph            = rectangle
    glyph_size       = 8
    color            = red
    stroke_color     = dred
    stroke_thickness = 1
    
    </plot>
    
    </plots>
``````
The parameters are

  * `show` \- as with highlights or links, determines whether to draw the plot or not 
  * `type` \- determines the type of plot and can be one of scatter, line, histogram, heatmap, etc. 
  * `file` \- file that contains plot data 
  * `min/max` \- the range of the plot axis, data outside this range are clipped 
  * `r0/r1` \- the inner and outer radius of the plot track, which may be formatted in absolute or relative (or mix) form, just like for highlights 
  * `glyph` \- shape of glyph to use for the scatter plot and can be one of circle, rectangle, or triangle 
  * `glyph_size` \- size of the glyph, in pixels 
  * `color` \- if used, the the glyph will be solid and of this color 
  * `stroke_color` \- if used, the glyph will have an outline of this color 
  * `stroke_thickness` \- if used, the glyph's outline will have this thickness, in pixels 

The data file format for 2D plots is

```    
    chr start end value options
```
Note that a value is associated with an explicit span, and not a single base
pair position. For example,

```    
    # value 0.005 at span 1000-2000
    hs1 1000 2000 0.005
    # value 0.010 at span 2001-2001, e.g. a single base position
    hs1 2001 2001 0.010
```
The reason why Circos uses start _and_ end positions for the data file is to
maintain consistency between data and link files. Glyphs are drawn at the
middle of the span. Thus, in the above example, the glyphs would be drawn at
positions 1,500 and 2,001.

Points whose values fall outside of the min/max range defined in the plot
parameters are not drawn. You do not need to write rules to exclude these
points.

#### plot background
The `r0` and `r1` parameters define the radial start and end positions of the
plot track. You can optionally add background fill(s) to the track with a
`<backgrounds>` block. using the following parameters

```    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
```
By defining several `<background>` blocks, you can stripe and layer the
background fills. Use `y0/y1` to define the radial extent of the fill.

```    
    <backgrounds>
    <background>
    color     = vlgrey
    # absolute fill range
    y1        = 0.5
    y0        = 0
    </background>
    <background>
    color     = vlred
    # relative fill range
    y1        = 1r
    y0        = 0.75r
    </background>
    </backgrounds>
```
#### plot axis
You can draw a set of y-axis grid lines within your plot track using the
`<axes>` block.

```    
    <axes>
    <axis>
    color     = grey
    thickness = 1
    spacing   = 0.05r
    </axis>
    </axes>
```
The axes are a series of concentric arcs with a given `spacing`. The spacing
value can be absolute or relative.

#### plot format rules
Formatting rules work for plots in the same manner as for links. Within the
condition field, use `var(value)` to represent the data value for a particular
point.

For example,

```    
    <rule>
    condition    = var(value) > 0.5
    stroke_color = dgreen
    color        = green
    glyph        = rectangle
    glyph_size   = 6
    </rule>
```
would turn all points whose value is larger than 0.5 to be rectangles of size
6 with a dark green outline and green fill.

You can hide certain data points by setting `show=no` within the rule.
### images
![Circos tutorial image - Scatter
Plots](/documentation/tutorials/2d_tracks/scatter_plots/img/01.png) ![Circos
tutorial image - Scatter
Plots](/documentation/tutorials/2d_tracks/scatter_plots/img/02.png)
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
    chromosomes       = hs1;hs2;hs3
    #chromosomes_reverse = hs2
    chromosomes_display_default = no
    
    ################################################################
    # 
    # define 3 scatter plots, using the same data file
    #
    
    <plots>
    
    # all are scatter plots
    
    type             = scatter
    
    stroke_thickness = 1
    
    # first plot shows all points and selectively formats points at small/large
    # y-axis values to be red/green and triangles/rectangles
    
    <plot>
    
    file             = data/6/snp.density.txt
    fill_color       = grey
    stroke_color     = black
    glyph            = circle
    glyph_size       = 10
    
    max   = 0.013
    min   = 0
    r1    = 0.95r
    r0    = 0.65r
    
    # optional y0/y1 values (absolute or relative) in <background> blocks
    # define the start/end limits of background color
    #
    # y0 = 0.006
    # y0 = 0.75r
    
    <backgrounds>
    <background>
    color     = vvlgreen
    y0        = 0.006
    </background>
    <background>
    color     = vlgrey
    y1        = 0.006
    y0        = 0.002
    </background>
    <background>
    color     = vvlred
    y1        = 0.002
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = lgreen
    thickness = 1
    spacing   = 0.05r
    y0        = 0.006
    </axis>
    <axis>
    color     = dgreen
    thickness = 2
    spacing   = 0.1r
    y0        = 0.006
    </axis>
    
    <axis>
    color     = lgrey
    thickness = 1
    spacing   = 0.05r
    y1        = 0.006
    y0        = 0.002
    </axis>
    <axis>
    color     = dgrey
    thickness = 2
    spacing   = 0.1r
    y1        = 0.006
    y0        = 0.002
    </axis>
    
    <axis>
    color     = lred
    thickness = 1
    spacing   = 0.05r
    y1        = 0.002
    </axis>
    
    <axis>
    color     = dred
    thickness = 2
    spacing   = 0.1r
    y1        = 0.002
    </axis>
    
    </axes>
    
    <rules>
    
    <rule>
    condition    = var(value) > 0.006
    stroke_color = dgreen
    fill_color   = green
    glyph        = rectangle
    glyph_size   = 8
    </rule>
    
    <rule>
    condition    = var(value) < 0.002
    stroke_color = dred
    fill_color   = red
    glyph        = triangle
    </rule>
    
    </rules>
    
    </plot>
    
    # the second plot is a crop of the first plot, placed outside
    # the ideogram circle, showing only points with large y-values
    
    <plot>
    
    file             = data/6/snp.density.txt
    fill_color       = green
    stroke_color     = dgreen
    glyph            = rectangle
    glyph_size       = 8
    
    max   = 0.013
    min   = 0.007
    r1    = 1.175r
    r0    = 1.075r
    
    <backgrounds>
    # you can stack backgrounds by using transparent color
    <background>
    color     = vlgreen_a4
    y0        = 0.75r
    </background>
    <background>
    color     = vlgreen_a4
    y0        = 0.5r
    </background>
    <background>
    color     = vlgreen_a4
    y0        = 0.25r
    </background>
    <background>
    color     = vlgreen_a4
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = green_a3
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    <rules>
    
    <rule>
    condition    = var(value) < 0.007
    show         = no
    </rule>
    
    </rules>
    
    </plot>
    
    # the third plot is a crop of the first plot, placed closer to the
    # center of the circle, showing only points with small y-values
    
    <plot>
    
    file             = data/6/snp.density.txt
    fill_color       = red
    stroke_color     = dred
    glyph            = rectangle
    glyph_size       = 8
    
    max   = 0.0015
    min   = 0.000
    r1    = 0.60r
    r0    = 0.35r
    
    <backgrounds>
    <background>
    color     = vlred_a4
    y1        = 0.25r
    </background>
    <background>
    color     = vlred_a4
    y1        = 0.5r
    </background>
    <background>
    color     = vlred_a4
    y1        = 0.75r
    </background>
    <background>
    color     = vlred_a4
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = red_a5
    thickness = 1
    spacing   = 0.025r
    </axis>
    <axis>
    color     = red_a3
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    <rules>
    <rule>
    condition    = var(value) > 0.002
    show         = no
    </rule>
    </rules>
    
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
