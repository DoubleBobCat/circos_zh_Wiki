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

## 7\. Variable Radius Link Ends

[Lesson](/documentation/tutorials/recipes/variable_link_ends/lesson)
[Images](/documentation/tutorials/recipes/variable_link_ends/images)
[Configuration](/documentation/tutorials/recipes/variable_link_ends/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units = 1000000
    #chromosomes       = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    chromosomes_display_default = yes
    
    <links>
    
    <link>
    
    file          = data/5/segdup.bundle4.txt
    radius        = 0.95r
    bezier_radius = 0r
    color         = vvdgrey
    thickness     = 2
    record_limit  = 2500
    
    <rules>
    
    # if a rule is triggered, continue testing with other rules
    flow       = continue
    
    # remap the color of the link to the first chromosome
    <rule>
    condition  = 1
    color      = eval(sprintf("%s_a4",var(chr1)))
    </rule>
    
    # Alter radial position of one or both ends of a link, depending
    # on its position. The function on(RX) tests whether a link
    # is on a chromosome matching the regular expression RX.
    
    <rule>
    # to/from hs1
    condition  = on(hs1$)
    radius     = 0.85r
    </rule>
    
    <rule>
    # to hs10, hs11 or hs12
    condition  = to(hs1[012])
    radius2    = 0.75r
    </rule>
    
    <rule>
    # from hs10, hs11, hs12
    condition  = from(hs1[012])
    radius1    = 0.75r
    </rule>
    
    <rule>
    # from hs14 and has start beyond 100mb
    condition  = from(hs14) && var(start1) > 100mb
    radius1    = 1r+50p
    z          = 5
    thickness  = 3
    color      = blue
    </rule>
    
    <rule>
    # to hs5 and has end within 50mb of position 100mb
    condition  = to(hs5) && abs(var(start2) - 100mb) < 50mb
    radius2    = 1r+50p
    z          = 5
    thickness  = 3
    color      = red
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
    
    

  

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

