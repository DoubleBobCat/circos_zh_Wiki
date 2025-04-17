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

# 11 — Image Maps

## 2\. Image Maps - Clickable Cytogenetic Bands

[Lesson](/documentation/tutorials/image_maps/bands/lesson)
[Images](/documentation/tutorials/image_maps/bands/images)
[Configuration](/documentation/tutorials/image_maps/bands/configuration)

### circos.conf

    
    
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
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius) - 70p
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.85r
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
    

  

* * *

