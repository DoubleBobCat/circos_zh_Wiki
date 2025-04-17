---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Automation & Macros
---

### lesson
This is an advanced topic.

#### referencing configuration parameters
Within a configuration file, you can refer to a configuration parameter value
using `conf()`.

If the parameter you wish to refer to is in the same block, then use
`conf(param)`.

```    
    x = 1
    y = conf(x)
```
If the parameter is in a specific block hierarchy elsewhere, list the blocks
first.

```    
    <b1>
     <b2>
      x = 1
     </b2>
    </b1>
    
    y = conf(b1,b2,x)
```
Note that you cannot currently access a block hierarchy that includes multiple
blocks with the same n ame.

If the parameter is somewhere up the hierarchy from where it is called, use
`conf(.,param)`

```    
    <b1>
     x = 1
     <b2>
      <b3>
       y = conf(.,x)
      </b3>
     </b2>
    </b1>
```
#### automating tracks
Together with track counters, the `conf()` function can be used to create
different tracks from the same configuration file. This is extremely useful
when you need to show several tracks using data whose source and/or format can
be parametrized.

For example, you can create the four heatmaps in this example from the same
block. The heatmap blocks are

```    
    type  = heatmap
    file  = data/5/segdup.hs1234.heatmap.txt
    r1    = 0.89r
    r0    = 0.88r
    color = hs1_a5,hs1_a4,hs1_a3,hs1_a2,hs1_a1,hs1
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
```
They have the same `type`, `file`, `scale_log_base` parameters and <rules>
block. The `r0` and `r1` parameters change by 0.01 for successive blocks and
the `color` parameter can be parametrized by the index of the chromosome (e.g.
`hsi` for `i = 1..4`).

Instead of including the block above four times, once for each heatmap, with
hard-coded `r0`, `r1` and `color` values, we can generate these parameter
values automatically using block counters, which are internal variables that
provide a 0-indexed identifier for each block in the configuration file.

This block below will be parsed the same as the one above. When it is included
several times, the value of `counter(heatmap)` will be incremented each time,
allowing for dynamically changing `r0`, `r1` and `color` parameters.

```    
    # heatmap.conf
    
    type           = heatmap
    file           = data/5/segdup.hs1234.heatmap.txt
    
    # The 'c' parameter (arbitrarily named) is referenced
    # within heatmap.conf as conf(.,c). conf(x) retrieves
    # the value of parameter 'x' in the current block and
    # conf(.,x) looks up the configuration tree until
    # it finds x.
    
    c = eval(sprintf("hs%d",counter(heatmap)+1))
    
    # track_r0(counter,start,width,padding) 
    # track_r1(counter,start,width,padding) 
    # are helper functions that return the start/end radius of a track
    # formatted as float+"r", e.g. 0.925r
    # 
    # r0 = start + counter * (width + padding) 
    # r1 = start + counter * (width + padding) + width
    #
    # The calls to conf(.,x) reference the  block's h0, hw and hp
    # parameters. The counter(heatmap) is an 0-start automatically incremented
    # index, which is incremented by 1 for each type=heatmap plot.
    #
    r1    = eval(track_r1(counter(heatmap),conf(.,h0),conf(.,hw),conf(.,hp)))
    r0    = eval(track_r0(counter(heatmap),conf(.,h0),conf(.,hw),conf(.,hp)))
    
    # conf(.,c) references the  block's 'c' parameter
    color          = conf(.,c)_a5,conf(.,c)_a4,conf(.,c)_a3,conf(.,c)_a2,conf(.,c)_a1,conf(.,c)
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    <rule>
    # hides any data point whose 'id' parameter is not
    # the same as the  block 'c' parameter
    condition = var(id) ne "conf(.,c)"
    show      = no
    </rule>
    </rules>
```
Here's how to include the block multiple times.

```    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
```
You can include the block directives in the `heatmap.conf` file so that the
main configuration file is even simpler.

```    
    # circos.conf
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    <<include heatmap.conf>>
    # heatmap.conf
    <plot>
    ...
    </plot>
```
#### `conf` vs `var`
The `conf(x)` function retrieves the value of a configuration parameter at the
time that the configuration file is compiled. This happens in the initial part
of the code **before** any data is processed.

You can see the effect of the `conf(x)` function by running

```    
    > circos -cdump plots
    ...
    {
     c => 'hs2',
     color => 'hs2_a5,hs2_a4,hs2_a3,hs2_a2,hs2_a1,hs2',
     file => 'data/5/segdup.hs1234.heatmap.txt',
     r0 => '0.890000r',
     r1 => '0.900000r',
     rules => {
                rule => [
                          {
                            condition => 'on(hs1)',
                            show => 0
                          },
                          {
                            condition => 'var(id) ne "hs2"',
                            show => 0
                          }
                        ]
              },
     scale_log_base => '0.25',
     type => 'heatmap'
    }
    ...
```
After parsing the configuration file, the value of the `c`, `r0`, `r1` and
`color` parameters has already been determined. These are now constant for the
rest of the time Circos is running.

On the other hand, the `var(x)` function retrieves the value of the `x`
parameter for a data point and is evaluated **dynamically** for each data
point.

The condition of the second rule has already been parsed and the call to
`conf(.,c)` has returned, for the case of this block, `hs2`. As each data
point is tested, the value of `var(id)` will be replaced by the point's `id`
parameter and the condition will be tested with this value.
### images
![Circos tutorial image - Automation &
Macros](/documentation/tutorials/quick_start/automation_and_macros/img/01.png)
### configuration
#### circos.conf
```    
    # 1.9 MODULAR CONFIGURATION, MACROS
    
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
    type  = text
    file  = data/6/genes.labels.txt
    r1    = 0.8r
    r0    = 0.6r
    label_font = light
    label_size = 12p
    rpadding   = 5p
    show_links     = no
    link_dims      = 0p,2p,5p,2p,2p
    link_thickness = 2p
    link_color     = black
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    <rule>
    condition  = var(value) =~ /a/i
    label_font = bold
    flow       = continue
    </rule>
    <rule>
    condition  = var(value) =~ /b/i
    color      = blue
    </rule>
    </rules>
    
    </plot>
    
    # By using counters and automatic track placement, we can
    # create 4 heatmaps with identical configurations (heatmap.conf).
    # The conf() function is used within heatmap.conf to reference
    # configuration parameters.
    
    h0 = 0.88 # start of heatmap tracks 
    hw = 0.01 # width of heatmap track (-'ve if tracks progress inward)
    hp = 0    # padding between heatmap tracks
    
    # Look in heatmap.conf for explanation.
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
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
    <<include axes.conf>>
    </plot>
    
    </plots>
    
    <links>
    <link>
    file          = data/5/segdup.txt
    radius        = 0.6r
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

#### heatmap.conf
```    
    type           = heatmap
    file           = data/5/segdup.hs1234.heatmap.txt
    
    # The 'c' parameter (arbitrarily named) is referenced
    # within heatmap.conf as conf(.,c). conf(x) retrieves
    # the value of parameter 'x' in the current block and
    # conf(.,x) looks up the configuration tree until
    # it finds x.
    
    c = eval(sprintf("hs%d",counter(heatmap)+1))
    
    # track_r0(counter,start,width,padding) 
    # track_r1(counter,start,width,padding) 
    # are helper functions that return the start/end radius of a track
    # formatted as float+"r", e.g. 0.925r
    # 
    # r0 = start + counter * (width + padding) 
    # r1 = start + counter * (width + padding) + width
    #
    # The calls to conf(.,x) reference the <plot> block's h0, hw and hp
    # parameters. The counter(heatmap) is an 0-start automatically incremented
    # index, which is incremented by 1 for each type=heatmap plot.
    #
    r1    = eval(track_r1(counter(heatmap),conf(.,h0),conf(.,hw),conf(.,hp)))
    r0    = eval(track_r0(counter(heatmap),conf(.,h0),conf(.,hw),conf(.,hp)))
    
    # conf(.,c) references the <plot> block's 'c' parameter
    color          = conf(.,c)_a5,conf(.,c)_a4,conf(.,c)_a3,conf(.,c)_a2,conf(.,c)_a1,conf(.,c)
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    <rule>
    condition = var(id) ne "conf(.,c)"
    show      = no
    </rule>
    </rules>
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
