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

## 1\. Image Maps - Introduction and Clickable Ideograms

[Lesson](/documentation/tutorials/image_maps/ideograms/lesson)
[Images](/documentation/tutorials/image_maps/ideograms/images)
[Configuration](/documentation/tutorials/image_maps/ideograms/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    
    ################################################################
    # Image map
    
    image_map_use      = yes
    
    # If a url uses a variable field, such as [id], and
    # the corresponding parameter (e.g. id) is not defined,
    # then 
    # - if image_map_missing_parameter=exit, Circos will exit with an error
    # - if image_map_missing_parameter=removeparam (or not defined), the
    #      undefined parameter string will be removed
    # - if image_map_missing_parameter=removeurl, url will not be used 
    #      for that data point or data set
    
    #image_map_missing_parameter = exit
    
    # This is the name of the map, which will appear in the
    # <map name="NAME"> tag of the map. If not defined, the
    # name of the image will be used.
    
    #image_map_name     = circosmap
    
    # The image map will be written to this file. If this
    # value is not defined, then the filename will be used
    # with an html extension. If the file specified here
    # does not have a directory component, the output
    # directory defined by the dir parameter (see above)
    # will be prefixed (i.e. the map and image will be
    # created in the same directory).
    
    #image_map_file     = map.html
    
    # If urls are not preceeded by a protocol, then this
    # protocol will be automatically added to each url. This is
    # not strictly necessary, since your browser will assume 
    # that http is used. However, if you need https or some other
    # protocol, this is the field to adjust.
    
    #image_map_protocol = http
    
    # These values, when defined, will be added to each
    # x,y coordinate of the map element boundary. These offsets
    # are useful if the Circos image will be composited with
    # another image, or cropped, or manipulated in any manner
    # that shifts its original (0,0) (upper left) corner. You
    # can define one or both values, and they can be negative.
    
    #image_map_xshift = 0
    #image_map_yshift = 0
    
    # These factors will be used to multiply the x,y coordinates for each
    # map element boundary. These parameters are useful if you are going
    # to resize the image later. For example, if you create a 3000 x 3000
    # pixel image (radius=1500px), but publish a 800 x 800 pixel image,
    # set both factors to 800/3000 = 2.666667. Unless you are stretching
    # the image (don't do it!) both factors should have the same value
    
    #image_map_xfactor = 0.266667
    #image_map_yfactor = 0.266667
    
    # For debugging purposes, you can overlay the image map elements on
    # top of the PNG image (not SVG). Each element in the overlay can have
    # a fill color and stroke color. Note that if you add any x/y shift or
    # multiplicative factors (above) then the overlay will reflect those
    # factors.
    
    image_map_overlay                  = yes
    #image_map_overlay_fill_color      = lred_a5
    image_map_overlay_stroke_color     = red
    image_map_overlay_stroke_thickness = 2
    
    </image>
    
    chromosomes_units           = 1000000
    #chromosomes                = hs1:0-50
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

