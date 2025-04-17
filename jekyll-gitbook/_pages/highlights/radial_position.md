---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Highlight Parameters - Part III - Radial Position
---

## Highlight Parameters - Part III - Radial Position
### lesson
In the previous section I demonstrated how you can adjust the radial extent,
by setting r0,r1 in the data file, to encode information about the highlight.
In that example, I used the highlight region size to control the radial
extent.

There are three data files for this section. All highlights regions are
randomly generated. Highlight color is encoded by the chromosome color scheme.

  * random.highlights.r.txt - random radial start 
  * random.highlights.rr.txt - radial start inversely proportional to size (largest highlights at the edge) 
  * random.highlights.rrr.txt - radial start inversely proportional to size (largest highlights at the center) 

From the images you can see that a little planning when it comes to radial
position can produce a much cleaner figure. The first figure is a mess, of
course. The last image, in which the small highlights are near the ideograms
presents the data clearly. Smaller features are best shown at larger radial
positions because they will subtend a larger angular distance along the circle
than if drawn closer to the center, and therefore are more clearly visible.
Larger structures can be drawn at smaller radial values.

#### formatting radial position
Here is an excerpt of one of the data files used in this section
(random.highlights.rrr.txt).

```    
    ...
    hs1 135818329 137808916 fill_color=chr7,z=67,r0=0.709600r,r1=0.759600r
    hs1 107513875 108981462 fill_color=chr5,z=76,r0=0.772761r,r1=0.822761r
    hs1 227449772 228946659 fill_color=chr5,z=75,r0=0.769223r,r1=0.819223r
    hs1 24598766 26578839 fill_color=chr7,z=68,r0=0.710869r,r1=0.760869r
    hs1 145258423 147866442 fill_color=chr10,z=58,r0=0.635033r,r1=0.685033r
    hs1 110729772 111813392 fill_color=chr4,z=82,r0=0.819133r,r1=0.869133r
    hs1 136155686 138376393 fill_color=chr8,z=64,r0=0.681808r,r1=0.731808r
    ...
```
All the radial positions are specified as relative values, indicated by the
"r" suffix. The relative value is expressed in terms of the inner ideogram
radius, if the value is <1, and in terms of the outer radius, if the value is
>1\. This way, highlights don't ever cross ideograms. By the way, if you would
like highlights inside the ideograms, use ideogram highlights, covered in the
next section.

In addition to relative radial positions, you can specify absolute positions
(suffix is "p", for pixel), or a combination of the two. Here are some
examples

```    
    # absolute positioning
    r0 = 500p      # start at 500 pixels from center
    r1 = 600p      # end at 600 pixels from center
    
    # relative positioning - helpful when resizing figure
    r0 = 0.5r      # start at 0.5*inner_ideogram_radius
    r0 = 0.6r      # end at 0.6*inner_ideogram_radius
    
    # relative radial position start, but absolute size
    r0 = 0.5r      # start at 0.5*inner_ideogram_radius
    r1 = 0.5r+100p # start at 0.5*inner_ideogram_radius + 100 pixels
    
    # like above, but centered at a radial position
    r0 = 0.5r-50p  # start at 0.5*inner_ideogram_radius
    r1 = 0.5r+50p  # start at 0.5*inner_ideogram_radius + 100 pixels
```### images
![Circos tutorial image - Highlight Parameters - Part III - Radial
Position](/documentation/tutorials/highlights/radial_position/img/01.png)
### configuration
#### circos.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units           = 1000000
    
    chromosomes        = hs1
    chromosomes_breaks = -hs1:120-145;-hs1:180-200
    
    chromosomes_display_default = no
    
    <highlights>
    
    z = 0
    fill_color = green
    
    #<highlight>
    #file       = data/3/random.highlights.r.txt
    #</highlight>
    
    #<highlight>
    #file       = data/3/random.highlights.rr.txt
    #</highlight>
    
    <highlight>
    file        = data/3/random.highlights.rrr.txt
    </highlight>
    
    </highlights>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
``````
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 3u
    break   = 1u
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color = black
    fill_color   = blue
    thickness    = 0.25r
    stroke_thickness = 2
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 3
    thickness        = 1.5r
    </break>
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 100p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = yes
    label_with_tag = yes
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.05r
    label_size     = 48
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    show_grid          = yes
    grid_start         = 0.5r
    grid_end           = 1.0r
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    tick_separation      = 2p
    min_label_distance_to_edge = 10p
    label_separation = 5p
    label_offset     = 2p
    label_size = 8p
    multiplier = 1/1u
    color = black
    
    <tick>
    spacing        = 1u
    size           = 6p
    thickness      = 1p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %.2f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 1p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    </tick>
    <tick>
    spacing        = 10u
    size           = 16p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    grid           = yes
    grid_color     = vdgrey
    grid_thickness = 2p
    </tick>
    </ticks>
```
  

* * *
