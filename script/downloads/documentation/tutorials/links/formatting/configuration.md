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

# 6 — Links and Relationships

## 3\. Link Formatting

[Lesson](/documentation/tutorials/links/formatting/lesson)
[Images](/documentation/tutorials/links/formatting/images)
[Configuration](/documentation/tutorials/links/formatting/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units = 1000000
    chromosomes_display_default = no
    chromosomes       = hs1;hs2;hs3
    
    <links>
    
    z      = 0
    radius = 0.975r
    crest  = 0.5
    bezier_radius        = 0.5r
    bezier_radius_purity = 0.75
    
    <link>
    z            = 50
    color        = green_a2
    thickness    = 4
    file         = data/5/segdup.bundle3.txt
    bezier_radius_purity = 0.2
    crest = 1
    </link>
    
    <link>
    z            = 40
    color        = orange_a2
    thickness    = 4
    file         = data/5/segdup.bundle2.txt
    bezier_radius_purity = 0.2
    crest = 1
    </link>
    
    <link>
    z            = 30
    color        = blue_a2
    thickness    = 4
    file         = data/5/segdup.bundle1.txt
    bezier_radius_purity = 0.2
    crest        = 1
    </link>
    
    <link>
    z            = 20
    color        = dgrey_a2
    thickness    = 3
    file         = data/5/segdup.txt
    record_limit = 500
    </link>
    
    <link>
    z            = 15
    color        = grey_a2
    thickness    = 3
    file         = data/5/segdup.txt
    record_limit = 1000
    </link>
    
    <link>
    z            = 10
    color        = lgrey_a2
    thickness    = 2
    file         = data/5/segdup.txt
    record_limit = 2500
    </link>
    
    <link>
    z            = 5
    color        = vlgrey_a2
    thickness    = 1
    file         = data/5/segdup.txt
    record_limit = 10000
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
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(ideogram,radius) + 0.075r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 100p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    
    <tick>
    spacing        = 1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

