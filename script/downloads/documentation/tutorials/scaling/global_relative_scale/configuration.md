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

## 2\. Global Relative Scale Adjustment

[Lesson](/documentation/tutorials/scaling/global_relative_scale/lesson)
[Images](/documentation/tutorials/scaling/global_relative_scale/images)
[Configuration](/documentation/tutorials/scaling/global_relative_scale/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt,data/karyotype/karyotype.mouse.txt,data/karyotype/karyotype.rat.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = hs1;hs2;hs3;/mm1[4-9]/
    #chromosomes_scale          = /hs/:0.25r
    #chromosomes_scale          = /mm/:0.0833r # if 6 mouse ideograms are drawn, these two
    chromosomes_scale           = /mm/:0.5rn   # are equivalent
    
    #chromosomes_display_default = yes
    #chromosomes_scale           = /hs/:0.25r
    #chromosomes_scale           = /mm/:0.0833r # if 6 mouse ideograms are drawn, these two
    #chromosomes_scale           = /mm/:0.5rn   # are equivalent
    #chromosomes_color           = /hs/:green;/mm/:red;/rn/:blue
    #chromosomes_scale           = /mm/:0.175rn;/rn/:0.2rn
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### bands.conf

    
    
    show_bands            = no
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 3
    

  

* * *

### breaks.conf

    
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color     = black
    fill_color       = blue
    thickness        = 0.25r
    stroke_thickness = 2
    </break_style>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 2
    thickness        = 2r
    </break_style>
    
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.0025r
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
    label_size       = 18
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(var(chr))
    
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 50p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    tick_separation  = 3p
    label_separation = 5p
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    label_offset     = 5p
    format           = %d
    
    <tick>
    spacing        = 0.5u
    show_label     = no
    size           = 6p
    </tick>
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 16p
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 18p
    size           = 14p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    size           = 18p
    </tick>
    
    <tick>
    spacing        = 20u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    <tick>
    spacing        = 50u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    </ticks>
    

  

* * *

