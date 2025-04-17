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

## 5\. Heat maps

[Lesson](/documentation/tutorials/2d_tracks/heat_maps/lesson)
[Images](/documentation/tutorials/2d_tracks/heat_maps/images)
[Configuration](/documentation/tutorials/2d_tracks/heat_maps/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units  = 1000000
    chromosomes        = hs1;hs2
    chromosomes_breaks = -hs1:120-140
    chromosomes_display_default = no
    
    track_width = 0.05
    track_pad   = 0.02
    track_start = 0.95
    
    <plots>
    
    type    = heatmap
    
    # default file for all tracks
    file             = data/6/snp.number.1mb.txt
    
    # a 9 color diverging spectral palette specified using a color list name
    color  = spectral-9-div
    
    # referenced via conf(plots,color_alt)
    color_alt = black,spectral-8-div,grey
    
    # or the reverse list
    #color = spectral-9-div-rev
    
    # or you can even combine lists
    # color = ylorrd-9-seq-rev,ylgnbu-9-seq
    
    stroke_thickness = 1
    stroke_color     = black
    min              = 1000
    max              = 5000
    
    <plot>
    <<include r0r1.conf>>
    file             = data/6/variation.heatmap.txt
    stroke_thickness = 0
    min              = 2000
    max              = 250000
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    scale_log_base   = 0.5
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    scale_log_base   = 1   # this is the default value
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    scale_log_base   = 2
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    scale_log_base   = 3
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    scale_log_base   = 5
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    color            = conf(plots,color_alt)
    file             = data/6/heatmap.step.txt
    pattern          = hline,vline
    color_mapping    = 0  # default
    min              = 0
    max              = 10
    stroke_thickness = 0
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    color            = conf(plots,color_alt)
    file             = data/6/heatmap.step.txt
    pattern          = hline,solid,vline
    color_mapping    = 1
    min              = 0
    max              = 10
    stroke_thickness = 0
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    color            = conf(plots,color_alt)
    file             = data/6/heatmap.step.txt
    pattern          = hline,solid,vline
    color_mapping    = 2
    min              = 0
    max              = 10
    stroke_thickness = 0
    </plot>
    
    <plot>
    <<include r0r1.conf>>
    color            = conf(plots,color_alt)
    file             = data/6/heatmap.step.txt
    pattern          = hline,checker,vline
    color_mapping    = 2
    min              = 2
    max              = 8
    stroke_thickness = 0
    </plot>
    
    </plots>
    
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

### r0r1.conf

    
    
    # set track radius values based on track counter
    r1  = eval(sprintf("%fr",conf(track_start)-counter(plot)*(conf(track_width)+conf(track_pad))))
    r0  = eval(sprintf("%fr",conf(track_start)-counter(plot)*(conf(track_width)+conf(track_pad))-conf(track_width)))
    

  

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
    format           = %d
    
    <tick>
    spacing        = 1u
    show_label     = no
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    size           = 15p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
    

  

* * *

