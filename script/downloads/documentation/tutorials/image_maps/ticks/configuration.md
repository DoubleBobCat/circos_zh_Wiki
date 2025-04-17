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

## 3\. Clickable Tick Marks

[Lesson](/documentation/tutorials/image_maps/ticks/lesson)
[Images](/documentation/tutorials/image_maps/ticks/images)
[Configuration](/documentation/tutorials/image_maps/ticks/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    
    <ideogram>
    band_url* = undef
    </ideogram>
    
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    
    ################################################################
    # Here are the new image map parameters
    
    image_map_use      = yes
    
    image_map_missing_parameter = removeurl
    
    #image_map_name     = circos
    #image_map_file     = circos-tutorial.html
    #image_map_protocol = http
    #image_map_xshift = 0
    #image_map_yshift = 0
    
    # original image is 3000 x 3000, resized for web at 800 x 800
    
    image_map_xfactor = 0.266667
    image_map_yfactor = 0.266667
    image_map_overlay                  = yes
    #image_map_overlay_fill_color      = lred_a5
    image_map_overlay_stroke_color     = red
    image_map_overlay_stroke_thickness = 2
    
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

    
    
    show_ticks       = yes
    show_tick_labels = yes
    
    show_grid  = no
    
    <ticks>
    
    radius         = dims(ideogram,radius_outer)
    label_offset   = 10p
    multiplier     = 1e-6
    color          = black
    
    <tick>
    
    spacing        = 25u
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
    
    url              = script?type=tick&chr=chr[label]&start=[start]&end=[end]
    map_size         = 100p
    
    #map_radius_inner = 0.5r
    #map_radius_outer = 1.2r
    
    </tick>
    
    <tick>
    
    show = no
    
    spacing        = 5u
    spacing_type   = relative
    rspacing       = 0.25
    size           = 10p
    radius         = 0.9r
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_relative = yes
    label_offset   = 0p
    format         = %.0f
    rmultiplier    = 100
    suffix         = %
    grid           = yes
    grid_color     = grey
    grid_thickness = 2p
    
    url              = script?type=tick&chr=chr[label]&start=[start]&end=[end]
    map_size         = -100p
    
    #map_radius_inner = 0.5r
    #map_radius_outer = 1.2r
    
    </tick>
    
    </ticks>
    

  

* * *

