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

## 8\. Text—Rules

[Lesson](/documentation/tutorials/2d_tracks/text_3/lesson)
[Images](/documentation/tutorials/2d_tracks/text_3/images)
[Configuration](/documentation/tutorials/2d_tracks/text_3/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units = 1000
    chromosomes       = hs1:0-1
    chromosomes_display_default = no
    
    <plots>
    
    type       = text
    color      = black
    label_font = mono
    label_size = 32
    show_links = no
    rpadding   = 0.2r
    
    <plot>
    file       = data/6/sequence.txt
    r1         = 0.9r
    r0         = 0.3r
    label_size = 16
    padding    = -0.25r
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    <plot>
    file       = data/6/sequence.txt
    r1         = 0.9r
    r0         = 0.4r
    rpadding   = 0.25r
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    <plot>
    file       = data/6/sequence.long.txt
    r1         = 0.9r
    r0         = 0.7r
    
    label_rotate = no
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    <plot>
    file  = data/6/sequence.txt
    r0    = 1r+80p
    r1    = 1r+250p
    
    label_parallel = yes
    
    <rules>
    
    <rule>
    condition  = var(value) ne "A"
    show       = no
    </rule>
    
    <rule>
    condition  = 1
    label_size = eval(12+32*rand())
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### bands.conf

    
    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 0
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.01r
    break   = 0.5r
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    radius*       = 0.825r
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
    
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.775r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### rule.textcolor.conf

    
    
    <rule>
    condition = var(value) eq "A"
    color     = red
    </rule>
    <rule>
    condition = var(value) eq "T"
    color     = blue
    </rule>
    <rule>
    condition = var(value) eq "C"
    color     = green
    </rule>
    

  

* * *

### ticks.conf

    
    
    show_ticks       = yes
    show_tick_labels = yes
    show_grid        = no
    grid_start       = dims(ideogram,radius_inner)-0.5r
    grid_end         = dims(ideogram,radius_inner)
    
    <ticks>
    radius           = dims(ideogram,radius_outer)
    label_offset     = 5p
    label_size       = 20p
    multiplier       = 1
    color            = black
    format           = %d
    size             = 10p
    thickness        = 2p
    
    <tick>
    spacing        = 0.002u
    show_label     = no
    </tick>
    <tick>
    spacing        = .02u
    show_label     = yes
    </tick>
    <tick>
    spacing        = .1u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
    

  

* * *

