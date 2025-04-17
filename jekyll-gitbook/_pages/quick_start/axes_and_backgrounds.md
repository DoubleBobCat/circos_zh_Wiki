---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Axes & Backgrounds
---

## Axes & Backgrounds
### lesson
A track's background can be colored using <backgrounds> block and graduated
using <axes> block.

```    
    <plot>
    ...
    # axes
    <axes>
     <axis>
     ...
     </axis>
     <axis>
     ...
     </axis>
     ...
    </axes>
    
    # backgrounds
    <backgrounds>
     <background>
     ...
     </background>
     <background>
     ...
     </background>
     ...
    </backgrounds>
    
    </plot>
```
#### axes
Much like ticks, axes are defined in groups. Each group can be spaced either
with absolute or relative spacing. You can provide an axis line at specific
positions and, for groups which have spacing, skip some positions.

  * `spacing` \- absolute or relative spacing of the axis 
  * `position` \- fixed position (or positions) for axes 
  * `position_skip` \- fixed position (or positions) to skip when drawing axis lines 
  * `y0` \- absolute or relative start of axis lines 
  * `y1` \- absolute or relative start of axis lines 
  * `color` \- color of axis lines 
  * `thickness` \- thickness of axis lines 

```    
    <axes>
    
    # Show axes only on ideograms that have data for this track
    show = data
    
    thickness = 1
    color     = lgrey
    
    <axis>
    spacing   = 0.1r
    </axis>
    
    <axis>
    spacing   = 0.2r
    color     = grey
    </axis>
    
    <axis>
    position  = 0.5r
    color     = red
    </axis>
    
    <axis>
    position  = 0.85r
    color     = green
    thickness = 2
    </axis>
    
    </axes>
```
#### backgrounds
Background elements are color rings within the track boundary between `y0` and
`y1` limits. Multiple background elements can e used to give the track a
striped or gradated look. Each element is defined as a separate <background>
block, which are processed in order of appearance.

If `y0` and `y1` limits are not specified, the boundaries of the track are
used.

```    
    <backgrounds>
    
    # Show the backgrounds only for ideograms that have data
    show  = data
    
    <background>
    color = vvlgrey
    </background>
    <background>
    color = vlgrey
    # the "r" suffix indicates position relative to track data range
    y0    = 0.2r
    y1    = 0.5r
    </background>
    <background>
    color = lgrey
    y0    = 0.5r
    y1    = 0.8r
    </background>
    <background>
    color = grey
    # if y1 is not specified, the plot maximum is used (e.g. y1=1r)
    y0    = 0.8r
    </background>
    
    </backgrounds>
```
#### stand-alone axes and blackground <plot> blocks
In most cases, the purpose of a <plot> block is to show data. Axes and
backgrounds associated with a <plot> block that contains data will always be
drawn _under_ the data.

To precisely control whether axes and backgrounds are placed below or over the
data, use a bare <plot> block (one without `file` or `type` parameter). Doing
so will use the <plot> block to draw the axes and background only, without any
data.

```    
    <plot>
    
    # no file or type parameter
    
    r0 = 0.5r
    r1 = 0.75r
    
    # use z to determine whether this block (axes,background) will be
    # drawn on top of other plot blocks. 
    
    z  = 10
    
    <axes>
     ...
    </axes>
    
    <backgrounds>
     ...
    </backgrounds>
    
    </plot>
```
Here is an example of how to use this kind of axes <plot> block. Depending on
the `z` parameter of the axis <plot> block, the axes are drawn above or below
the data in the second block. By setting the axis color to have transparency
(`grey_a3`), the axes will blend with the histogram bins when drawn on top of
then.

```    
    <plots>
    
    # positions are inherited by both <plot> blocks
    
    r0 = 0.5r
    r1 = 0.8r
    
    <plot>
     z = 10 # drawn on top of data
     # z = -10 # drawn below data
     <axes>
      <axis>
       spacing   = 0.1r
       color     = grey_a3
       thickness = 1
      </axis>
     </axes>
    </plot>
    
    <plot>
     # default z value is 0
     type = histogram
     file = data.txt
    </plot>
    
    </plots>
``````### images
![Circos tutorial image - Axes &
Backgrounds](/documentation/tutorials/quick_start/axes_and_backgrounds/img/01.png)
### configuration
#### circos.conf
```    
    # 1.6 AXES AND BACKGROUNDS
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1234]$/
    chromosomes_radius          = hs4:0.9r
    
    <colors>
    chr1* = red
    chr2* = orange
    chr3* = green
    chr4* = blue
    </colors>
    
    chromosomes_reverse = /hs[234]/
    chromosomes_scale   = hs1=0.5r,/hs[234]/=0.5rn
    
    <plots>
    
    <plot>
    
    type = histogram
    file = data/5/segdup.hs1234.hist.txt
    r1   = 0.88r
    r0   = 0.81r
    
    fill_color = vdgrey
    extend_bin = no
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    # A track's background can be colored. Using y0/y1 ranges you can
    # generate a striped track with focus on specific data ranges.
    
    <<include backgrounds.conf>>
    
    </plot>
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.stacked.txt
    r1   = 0.99r
    r0   = 0.92r
    
    fill_color  = hs1,hs2,hs3,hs4
    orientation = in
    extend_bin  = no
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    # Like backgrounds, axes are defined in groups. 
    #
    # spacing   - absolute or relative spacing of the axis
    # position  - fixed position (or positions) for axes
    # position_skip - fixed position (or positions) to skip when drawing axis lines
    # y0        - absolute or relative start of axis lines
    # y1        - absolute or relative start of axis lines
    # color     - color of axis lines
    # thickness - thickness of axis lines
    
    <<include axes.conf>>
    
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.8r
    bezier_radius = 0r
    color         = black_a4
    thickness     = 2
    
    <rules>
    <<include rules.link.conf>>
    </rules>
    
    </link>
    
    </links>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>                
    </image>
    
    <<include etc/colors_fonts_patterns.conf>> 
    <<include etc/housekeeping.conf>> 
    data_out_of_range* = trim
```
  

* * *

#### axes.conf
```    
    <axes>
    # Show axes only on ideograms that have data for this track
    show = data
    
    thickness = 1
    color     = lgrey
    <axis>
    spacing   = 0.1r
    </axis>
    <axis>
    spacing   = 0.2r
    color     = grey
    </axis>
    <axis>
    position  = 0.5r
    color     = red
    </axis>
    <axis>
    position  = 0.85r
    color     = green
    thickness = 2
    </axis>
    
    </axes>
```
  

* * *

#### backgrounds.conf
```    
    <backgrounds>
    # Show the backgrounds only for ideograms that have data
    show  = data
    <background>
    color = vvlgrey
    </background>
    <background>
    color = vlgrey
    y0    = 0.2r
    y1    = 0.5r
    </background>
    <background>
    color = lgrey
    y0    = 0.5r
    y1    = 0.8r
    </background>
    <background>
    color = grey
    y0    = 0.8r
    </background>
    
    </backgrounds>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    # Ideogram position, fill and outline
    radius           = 0.90r
    thickness        = 20p
    fill             = yes
    stroke_color     = dgrey
    stroke_thickness = 2p
    
    # Minimum definition for ideogram labels.
    
    show_label       = yes
    # see etc/fonts.conf for list of font names
    label_font       = default 
    label_radius     = 1.075r  # if ideogram radius is constant, and you'd like labels close to image edge, 
                               # use the dims() function to access the size of the image
                               # label_radius  = dims(image,radius) - 60p
    label_size       = 30
    label_parallel   = yes
    
    </ideogram>
``````
  

* * *

#### rule.exclude.hs1.conf
```    
    <rule>
    condition = on(hs1)
    show      = no
    </rule>
```
  

* * *

#### rules.link.conf
```    
    <rule>
    condition     = var(intrachr)
    show          = no
    </rule>
    <rule>
    condition     = 1
    color         = eval(var(chr2))
    flow          = continue
    </rule>
    <rule>
    condition     = from(hs1)
    radius1       = 0.99r
    </rule>
    <rule>
    condition     = to(hs1)
    radius2       = 0.99r
    </rule>
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = 1r
    color            = black
    thickness        = 2p
    
    # the tick label is derived by multiplying the tick position
    # by 'multiplier' and casting it in 'format':
    #
    # sprintf(format,position*multiplier)
    #
    
    multiplier       = 1e-6
    
    # %d   - integer
    # %f   - float
    # %.1f - float with one decimal
    # %.2f - float with two decimals
    #
    # for other formats, see https://perldoc.perl.org/functions/sprintf.html
    
    format           = %d
    
    <tick>
    spacing        = 5u
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 25u
    size           = 15p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
