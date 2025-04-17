---
author: DoubleCat
date: 2025-04-11
layout: post
category: image_maps
title: Image Maps - Clickable Cytogenetic Bands
---

## Image Maps - Clickable Cytogenetic Bands
### lesson
Chromosomes can have cytogenetic bands associated with them in the karyotype
file. These bands serve to define distinct regions on the chromosome.
Typically, the bands are used to orient large-scale structures (>5Mb) on the
chromosome and act as visual markers. You can use these bands for any purpose,
however.

To associate a url with each band, use the `band_url` parameter in the
<ideogram> block.

```    
    <ideogram>
    band_url = script?start=[end]&end=[end]&label=[label]
    ...
```
#### parameters for bands
Bands have the following parameters available automatically in their URL

  * chr - chromosome of band 
  * parent - internal field 
  * name - name of the band 
  * start - base position of band start 
  * end - base position of band end 
  * size - size of band 
  * color - color of band 
  * label - the label of the band (this can be different than the name) 

Like for ideograms, you can include an `id` parameter in the band definition
and use it subsequently in the URL. So, in the karyotype file you might have

```    
    ...
    band hs1 p31.2 p31.2 68700000 69500000 gneg
    band hs1 p31.1 p31.1 69500000 84700000 gpos100 id=treasure_here
    band hs1 p22.3 p22.3 84700000 88100000 gneg
    ...
```
and then use a URL like

```    
    band_url = script?id=[id]
```
If you have image_map_missing_parameter=removeparam, then all bands without a
defined id parameter will have a URL like

```    
    script?id=
```
with the exception of chr1p31.1 which will have

```    
    script?id=treasure_here
```
But, if you define `image_map_missing_parameter=removeurl`, then only bands
with the id parameter defined will have a URL - other bands will not have an
entry in the image map.

#### managing overlapping links - ideograms and bands
Bands are drawn on top of ideograms and therefore band image map elements
locally override ideogram map elements. This is accomplished by placing the
band image map element before the ideogram element in the map file. Both
elements are there, but [W3 specification for client-side image
maps](https://www.w3.org/TR/REC-html40/struct/objects.html#h-13.6.1) specifies
that "If two or more defined regions overlap, the region-defining element that
appears earliest in the document takes precedence (i.e., responds to user
input)".

The second image in this tutorial demonstrates the result of defining both an
ideogram and a band url

```    
    ideogram_url = script?chr=[chr]
    band_url     = script?start=[start]&end=[end]&label=[label]
```
You'll notice that in the region of the ideogram band links are active in the
image map. However, since the ideogram image map also includes the label of
the ideogram, you can still access the link of the ideogram through the label.

In the case of bands without a URL, the ideogram link would be accesible
within the area of the band.
### images
![Circos tutorial image - Image Maps - Clickable Cytogenetic
Bands](/documentation/tutorials/image_maps/bands/img/01.png) ![Circos tutorial
image - Image Maps - Clickable Cytogenetic
Bands](/documentation/tutorials/image_maps/bands/img/02.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.hg18.txt
    
    <image>
    <<include etc/image.conf>>
    
    ################################################################
    # Here are the new image map parameters
    
    image_map_use      = yes
    
    image_map_missing_parameter = removeurl
    
    image_map_name     = circosmap
    
    #image_map_file     = circos-tutorial.html
    #image_map_protocol = http
    #image_map_xshift = 0
    #image_map_yshift = 0
    #image_map_xfactor = 0.266667
    #image_map_yfactor = 0.266667
    image_map_overlay              = yes
    #image_map_overlay_fill_color  = lred_a1
    image_map_overlay_stroke_color = red
    image_map_overlay_stroke_thickness = 4
    
    </image>
    
    chromosomes_units           = 1000000
    #chromosomes                 = hs1:0-50
    chromosomes_display_default = yes
    
    <<include etc/housekeeping.conf>>
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
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    #ideogram_url = https://www.google.com
    #ideogram_url = https://www.google.com/search?q=[chr]
    #ideogram_url = script?type=ideogram&start=[start]&end=[end]&length=[chrlength]&chr=[chr]&tag=[tag]&label=[label]&idx=[idx]&display_idx=[display_idx]&scale=[scale]
    #ideogram_url = script?chr=[chr]
    band_url = script?start=[start]&end=[end]&label=[label]
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius) - 70p
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.85r
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
    tick_separation      = 3p
    label_separation     = 5p
    radius               = dims(ideogram,radius_outer)
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
