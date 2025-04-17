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

# 8 — Axis Scaling

## 3\. Adjusting Scale for Regions

[Lesson](/documentation/tutorials/scaling/scale_regions/lesson)
[Images](/documentation/tutorials/scaling/scale_regions/images)
[Configuration](/documentation/tutorials/scaling/scale_regions/configuration)

### circos.conf

    
    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/7/karyotype.human.colorbychr.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes = hs1[a]:0-20;hs2[b]:0-20;hs1[c]:20-40;hs2[d]:20-40;hs1[e]:40-60;hs2[f]:40-60
    chromosomes_display_default = no
    chromosomes_scale = a:0.5;b:0.5;e:5;f:5
    
    #chromosomes = hs1[a]:0-50;hs1[b]:50-60;hs1[c]:60-)
    #chromosomes_scale = b:10
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
    
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    
    default = 0.5u
    break   = 0.1u
    
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
    stroke_thickness = 2
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
    label_radius   = dims(ideogram,radius) + 75p
    label_size     = 40p
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = no
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = no
    
    </ideogram>
    
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    tick_separation      = 3p
    label_separation     = 10p
    min_label_distance_to_edge = 10p
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    <tick>
    spacing        = 0.1u
    size           = 3p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    <tick>
    spacing        = 1u
    size           = 4p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 5u
    size           = 6p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 20p
    label_offset   = 5p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 20u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 20p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

