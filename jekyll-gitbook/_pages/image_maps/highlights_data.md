---
author: DoubleCat
date: 2025-04-11
layout: post
category: image_maps
title: Clickable Highlights and Data
---

## Clickable Highlights and Data
### lesson
In addition to ideograms, bands and ticks, data elements such as highlights,
scatter plots, histograms, text and ribbons can be associated with a link. The
mechanism very similar to that of ideograms and bands.

#### defining url elements for highlights, plots and links
To associate an element with a URL, define a url parameter in its block. Here
are some examples

```    
    <highlights>
    
    <highlight>
    ...
    url              = script?type=highlight&start=[start]&end=[end]&chr=[chr]
    </highlight>
    
    </highlights>
    
    <plots>
    
    <plot>
    ...
    url              = script?type=plot&start=[start]&end=[end]
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    ...
    url              = script?type=ribbon&start=[start]&end=[end]
    </link>
    
    </links>
```
As soon as the url parameter is defined in a block, all data points (or
ribbons or highlights) for that block have links. You can use the following
parameters

  * chr 
  * start 
  * start1 (ribbons) 
  * start2 (ribbons) 
  * end 
  * end1 (ribbons) 
  * end2 (ribbons) 
  * size1 (ribbons) 
  * size2 (ribbons) 
  * color 
  * fill_color 
  * stroke_color 
  * stroke_thickness 
  * glyph (scatter) 
  * glyph_size (scatter) 
  * value (scatter, histogram, heatmap, text) 
  * id (for data points that have this element defined in the input file) 

The example image in this tutorial shows a an image with many types of
elements, each with its own url definition. Notice that for places where link
areas overlap, the element that was drawn last is the one that responds to
clicking.

#### using rules to adjust URLs
Rules can be used to adjust the `url` parameter. This works in the same manner
as for any other adjustable parameter.

```    
    <plot>
    type = text
    ...
    <rules>
    <rule>
    # any label that contains M will have a different URL
    condition  = var(value) =~ /M/
    url        = special?label=[label]
    </rule>
    </rules>
    </plot>
```### images
![Circos tutorial image - Clickable Highlights and
Data](/documentation/tutorials/image_maps/highlights_data/img/01.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    
    ################################################################
    # Here are the new image map parameters
    
    image_map_use      = yes
    image_map_strict   = removeparam
    
    #image_map_name     = circos
    #image_map_file     = circos.html
    #image_map_protocol = http
    #image_map_xshift   = 0
    #image_map_yshift   = 0
    #image_map_xfactor  = 0.266667
    #image_map_yfactor  = 0.266667
    image_map_overlay                  = yes
    #image_map_overlay_fill_color      = lred_a5
    image_map_overlay_stroke_color     = red
    image_map_overlay_stroke_thickness = 2
    </image>
    
    chromosomes_units           = 1000000
    chromosomes                 = hs1:0-50
    chromosomes_display_default = no
    
    <highlights>
    
    z          = 0
    fill_color = green
    url        = script?type=highlight&start=[start]&end=[end]&chr=[chr]
    
    # url is specified by the global url setting
    # in the <highlights> block, above
    
    <highlight>
    file             = data/10/highlights.1.txt
    r0               = 1.15r
    r1               = 1.075r
    fill_color       = blue
    stroke_color     = dblue
    stroke_thickness = 2
    </highlight>
    
    # url is specified within the <highlight> block, and
    # it overrides the global url setting in the outer
    # <highlights> block
    
    <highlight>
    file       = data/10/highlights.2.txt
    r0         = 0.925r
    r1         = 0.975r
    url        = script?type=highlight&id=[id]&color=[fill_color]&r0=[r0]&r1=[r1]
    </highlight>
    
    # url is included with each data point, e.g.
    # hs1 46486003 46541625 url=script?value=0.0401409
    
    <highlight>
    file       = data/10/highlights.3.txt
    z          = 5
    fill_color = red
    ideogram   = yes
    </highlight>
    
    </highlights>
    
    <plots>
    
    <plot>
    type = tile
    file = data/10/tiles.2.txt
    r0   = 0.81r
    r1   = 0.92r
    layers = 8
    margin = 0.05u
    layers_overflow = hide
    orientation = out
    thickness = 12
    padding = 3
    color = black
    url = script?type=tile&id=[id]
    </plot>
    
    <plot>
    type  = text
    color = black
    file  = data/10/text.2.txt
    r0    = 0.6r
    r1    = 0.8r
    
    label_size = 18p
    label_font = default
    
    show_links     = yes
    link_dims      = 0p,3p,5p,3p,3p
    link_thickness = 2p
    link_color     = red
    
    padding        = 0p
    rpadding       = 0p
    
    label_snuggle         = yes
    max_snuggle_distance  = 1r
    snuggle_tolerance     = 0.25r
    snuggle_sampling      = 5
    
    url = script?type=label&id=[id]&text=[value]
    
    <rules>
    <rule>
    importance = 10
    condition  = var(value) =~ /M/
    url        = M
    </rule>
    </rules>
    </plot>
    
    <plot>
    type  = scatter
    fill_color = black
    glyph = square
    glyph_size = 8p
    file  = data/10/plotdata.1.txt
    r0    = 0.55r
    r1    = 0.6r
    min   = -.1
    max   = 1.1
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    
    url = script?type=scatter-square&value=[value]&start=[start]&end=[end]
    </plot>
    
    <plot>
    type  = scatter
    fill_color = green
    glyph = circle
    glyph_size = 8p
    file  = data/10/plotdata.3.txt
    r0    = 0.55r
    r1    = 0.6r
    min   = -.1
    max   = 1.1
    url = script?type=scatter-circle&value=[value]&start=[start]&end=[end]
    </plot>
    
    <plot>
    type  = histogram
    fill_under = yes
    fill_color = black
    color = red
    thickness = 2
    file  = data/10/plotdata.1.txt
    r0    = 0.5r
    r1    = 0.55r
    min   = 0
    max   = 1
    
    <backgrounds>
    <background>
    color = vlgrey
    </background>
    </backgrounds>
    
    url = script?type=label&value=[value]
    
    </plot>
    
    <plot>
    type  = heatmap
    color = spectral-5-div
    file  = data/10/plotdata.2.txt
    r0    = 0.475r
    r1    = 0.5r
    min   = 0
    max   = 1
    url   = script?type=label&value=[value]&color=[color]
    </plot>
    
    <plot>
    type  = highlight
    fill_color = green
    file  = data/10/plotdata.4.txt
    r0    = 0.425r
    r1    = 0.45r
    url = script?type=highlight&start=[start]&end=[end]
    </plot>
    </plots>
    
    <links>
    <link>
    file   = data/10/ribbon.1.txt
    ribbon = yes
    flat   = yes
    color  = grey_a2
    radius = 0.4r
    bezier_radius = 0r
    url    = script?type=ribbon&start1=[start1]&end1=[end1]&start2=[start2]&end2=[end2]&size1=[size1]&size2=[size2]
    </link>
    </links>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 1u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 100p
    stroke_thickness = 2p
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.8r
    show_label     = yes
    label_with_tag = yes
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.2r
    label_size     = 48p
    label_parallel = yes
    label_case     = upper
    
    ideogram_url = script?type=ideogram&chr=[chr]
    
    # cytogenetic bands
    band_stroke_thickness = 2p
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    band_url = script?type=band&start=[start]&end=[end]&label=[label]
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks       = yes
    show_tick_labels = yes
    
    show_grid  = no
    
    <ticks>
    
    radius       = dims(ideogram,radius_outer)
    label_offset = 10p
    multiplier   = 1e-6
    color        = black
    
    <tick>
    spacing        = 1u
    size           = 10p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    
    url              = script?type=tick&start=[start]&end=[end]
    map_size         = 100p
    
    #map_radius_inner = 0.5r
    #map_radius_outer = 1.2r
    
    </tick>
    
    </ticks>
```
  

* * *
