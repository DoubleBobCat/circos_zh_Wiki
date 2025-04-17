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

# 9 — Recipes

## 12\. Inverted Links

[Lesson](/documentation/tutorials/recipes/inverted_links/lesson)
[Images](/documentation/tutorials/recipes/inverted_links/images)
[Configuration](/documentation/tutorials/recipes/inverted_links/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1:0-120;hs2:100-)
    
    <links>
    
    <link>
    
    file          = data/8/ribbon.txt
    ribbon        = yes
    flat          = yes
    radius        = 0.95r
    bezier_radius = 0r
    crest         = 0.2
    color         = lgrey
    
    <rules>
    <rule>
    # you can also test whether only one end is
    # reversed using var(inv)
    condition  = var(rev1) && ! var(rev2)
    color      = red
    </rule>
    <rule>
    condition  = var(rev2) && ! var(rev1)
    color      = orange
    </rule>
    <rule>
    condition  = var(rev1) && var(rev2) 
    color      = blue
    </rule>
    
    </rules>
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### circos.segdup.conf

    
    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/8/karyotype.human.colorbychr.txt
    
    <image>
    dir = .
    file  = circos.png
    24bit = yes
    png = yes
    svg = yes
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    #angle_orientation = counterclockwise
    
    auto_alpha_colors = yes
    auto_alpha_steps  = 5
    </image>
    
    chromosomes_units           = 1000000
    
    chromosomes_display_default = no
    chromosomes = hs1;hs2
    #chromosomes                 = hs1:0-120;hs2:100-)
    
    <highlights>
    <highlight>
    file        = data/8/chr.highlight.txt
    r0 = 0.99r
    r1 = 0.995r
    </highlight>
    </highlights>
    
    <links>
    <link linkexample>
    
    file          = data/8/segdup.01.txt
    radius        = 0.95r
    flat          = yes
    ribbon        = yes
    bezier_radius = 0r
    crest         = 0.2
    color         = blue
    
    <rules>
    <rule>
    importance = 100
    condition  = _REV2_ == 1
    color      = lorange
    </rule>
    
    </rules>
    </link>
    </links>
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    units_ok = bupr
    units_nounit = n
    
    #debug_group = ticks
    

  

* * *

### bands.conf

    
    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 3
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.005r
    break   = 0.5r
    
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
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius) - 50p
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
    
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.85r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    tick_separation      = 3p
    label_separation     = 5p
    radius               = dims(ideogram,radius_outer)+50p
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
    

  

* * *

