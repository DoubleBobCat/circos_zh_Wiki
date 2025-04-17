---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: 2D Data Tracks
---

Use the [latest version of Circos](/software/download/circos/) and read
[Circos best
practices](/documentation/tutorials/reference/best_practices/)—these list
recent important changes and identify sources of common problems.

If you are having trouble, post your issue to the [Circos Google
Group](https://groups.google.com/group/circos-data-visualization) and [include
all files and detailed error logs](/support/support/). Please do not email me
directly unless it is urgent—you are much more likely to receive a timely
reply from the group.

Don't know what question to ask? Read [Points of View: Visualizing Biological
Data](https://www.nature.com/nmeth/journal/v9/n12/full/nmeth.2258.html) by
Bang Wong, myself and invited authors from the [Points of View
series](https://mk.bcgsc.ca/pointsofview).

# 7 — 2D Data Tracks

## 1\. Scatter Plots

[Lesson](/documentation/tutorials/2d_tracks/scatter_plots/lesson)
[Images](/documentation/tutorials/2d_tracks/scatter_plots/images)
[Configuration](/documentation/tutorials/2d_tracks/scatter_plots/configuration)

Syntax for 2D data types is similar to that for links. You define all 2D plots
within >plots< block, with one plot per <plot> block. Within a plot block, you
define formatting and data file for the plot, and can insert optional >rules>
block that contains multiple <rule> blocks.

There are several 2D data types and the scatter plot is one. The image for
this example contains three scatter plots, all derived from the same data
file. Each plot is formatted slightly differently. The data are SNP density
for windows of 100kb (number of SNPs from dbSNP per base).

### default settings

Each plot type has default settings which you can find in `etc/tracks`. For
example,

    
    
    # etc/tracks/scatter.conf
    glyph            = circle
    glyph_size       = 10
    color            = grey
    stroke_color     = black
    stroke_thickness = 0
    r1               = 0.79r
    r0               = 0.7r
    orientation      = out
    

These settings are applied to every <plot> block of `type=scatter`. YOu can
undefine a setting using `undef`,

    
    
    stroke_color = undef
    

### basic scatter plot syntax

2D data types share have the same format parameters, with a few exceptions.
For the scatter plot, a basic definition might look like this

    
    
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

    
    
    chr start end value options
    

Note that a value is associated with an explicit span, and not a single base
pair position. For example,

    
    
    # value 0.005 at span 1000-2000
    hs1 1000 2000 0.005
    # value 0.010 at span 2001-2001, e.g. a single base position
    hs1 2001 2001 0.010
    

The reason why Circos uses start _and_ end positions for the data file is to
maintain consistency between data and link files. Glyphs are drawn at the
middle of the span. Thus, in the above example, the glyphs would be drawn at
positions 1,500 and 2,001.

Points whose values fall outside of the min/max range defined in the plot
parameters are not drawn. You do not need to write rules to exclude these
points.

### plot background

The `r0` and `r1` parameters define the radial start and end positions of the
plot track. You can optionally add background fill(s) to the track with a
`<backgrounds>` block. using the following parameters

    
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    

By defining several `<background>` blocks, you can stripe and layer the
background fills. Use `y0/y1` to define the radial extent of the fill.

    
    
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
    

### plot axis

You can draw a set of y-axis grid lines within your plot track using the
`<axes>` block.

    
    
    <axes>
    <axis>
    color     = grey
    thickness = 1
    spacing   = 0.05r
    </axis>
    </axes>
    

The axes are a series of concentric arcs with a given `spacing`. The spacing
value can be absolute or relative.

### plot format rules

Formatting rules work for plots in the same manner as for links. Within the
condition field, use `var(value)` to represent the data value for a particular
point.

For example,

    
    
    <rule>
    condition    = var(value) > 0.5
    stroke_color = dgreen
    color        = green
    glyph        = rectangle
    glyph_size   = 6
    </rule>
    

would turn all points whose value is larger than 0.5 to be rectangles of size
6 with a dark green outline and green fill.

You can hide certain data points by setting `show=no` within the rule.

