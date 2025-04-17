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

## 7\. Combining Scales

[Lesson](/documentation/tutorials/scaling/combining_scales/lesson)
[Images](/documentation/tutorials/scaling/combining_scales/images)
[Configuration](/documentation/tutorials/scaling/combining_scales/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    <zooms>
    
    <zoom>
    chr    = hs1
    start  = 120u
    end    = 125u
    scale  = 10
    smooth_distance = 2r
    smooth_steps    = 10
    </zoom>
    
    <zoom>
    chr    = hs1
    start  = 150u
    end    = 160u
    scale  = 0.2
    smooth_distance = 5r
    smooth_steps    = 10
    </zoom>
    
    <zoom>
    chr    = hs2
    start  = 5u
    end    = 10u
    scale  = 5
    smooth_distance = 10u
    smooth_steps    = 10
    </zoom>
    
    <zoom>
    chr    = hs2
    start  = 78u
    end    = 82u
    scale  = .25
    smooth_distance = 20u
    smooth_steps    = 20
    </zoom>
    
    <zoom>
    chr    = hs3
    start  = 25u
    end    = 150u
    scale  = 0.5
    smooth_distance = 15u
    smooth_steps = 5
    </zoom>
    
    <zoom>
    chr    = hs3
    start  = 72u
    end    = 73u
    scale  = 10
    smooth_distance = 5u
    smooth_steps = 10
    </zoom>
    
    </zooms>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    chromosomes        = hs1;hs2[a]:0-100;hs2[b]:150-);hs3
    chromosomes_breaks = -hs2:40-60
    chromosomes_scale  = a:2;b:0.5
    
    <plots>
    
    <plot>
    type  = heatmap
    file  = data/7/heatmap.zoom-05.txt
    r1    = 0.95r
    r0    = 0.90r
    color = spectral-9-div
    stroke_color     = black
    stroke_thickness = 1
    scale_log_base   = 1.5
    </plot>
    
    <plot>
    type = histogram
    file = data/7/heatmap.zoom-05.txt
    r1   = 0.89r
    r0   = 0.60r
    color     = black
    thickness = 2
    
    min = 0
    max = 10
    
    <axes>
    <axis>
    color     = lgrey
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
    

  

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
    default = 0.005r
    break   = 0.5r
    
    <<include breaks.conf>>
    
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
    label_separation = 10p
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1e-6
    color            = black
    thickness        = 2p
    label_offset     = 5p
    format           = %d
    
    <tick>
    #chromosomes_display_default = no
    chromosomes    = -hs9
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
    spacing        = 100u
    show_label     = yes
    label_size     = 24p
    size           = 22p
    </tick>
    
    </ticks>
    

  

* * *

