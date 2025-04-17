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

## 2\. Line Plots

[Lesson](/documentation/tutorials/2d_tracks/line_plots/lesson)
[Images](/documentation/tutorials/2d_tracks/line_plots/images)
[Configuration](/documentation/tutorials/2d_tracks/line_plots/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units = 1000000
    chromosomes       = hs1 # ;hs2;hs3
    chromosomes_display_default = no
    
    <plots>
    
    type      = line
    thickness = 2
    
    <plot>
    
    max_gap = 1u
    file    = data/6/snp.density.250kb.txt
    color   = vdgrey
    min     = 0
    max     = 0.015
    r0      = 0.5r
    r1      = 0.8r
    
    fill_color = vdgrey_a3
    
    <backgrounds>
    <background>
    color     = vvlgreen
    y0        = 0.006
    </background>
    <background>
    color     = vvlred
    y1        = 0.002
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = lgrey_a2
    thickness = 1
    spacing   = 0.025r
    </axis>
    </axes>
    
    <rules>
    
    <rule>
    condition    = var(value) > 0.006
    color        = dgreen
    fill_color   = dgreen_a1
    </rule>
    
    <rule>
    condition    = var(value) < 0.002
    color        = dred
    fill_color   = dred_a1
    </rule>
    
    </rules>
    
    </plot>
    
    # outside the circle, oriented out
    <plot>
    
    max_gap = 1u
    file    = data/6/snp.density.txt
    color   = black
    min     = 0
    max     = 0.015
    r0      = 1.075r
    r1      = 1.15r
    thickness = 1
    
    fill_color = black_a4
    
    <axes>
    <axis>
    color     = lgreen
    thickness = 2
    position  = 0.006
    </axis>
    <axis>
    color     = lred
    thickness = 2
    position  = 0.002
    </axis>
    </axes>
    
    </plot>
    
    <plot>
    z       = 5
    max_gap = 1u
    file    = data/6/snp.density.1mb.txt
    color   = red
    fill_color = red_a4
    min     = 0
    max     = 0.015
    r0      = 1.075r
    r1      = 1.15r
    </plot>
    
    # same plot, but inside the circle, oriented in
    <plot>
    max_gap = 1u
    file    = data/6/snp.density.txt
    color   = black
    fill_color = black_a4
    min     = 0
    max     = 0.015
    r0      = 0.85r
    r1      = 0.95r
    thickness   = 1
    orientation = in
    
    <axes>
    <axis>
    color     = lgreen
    thickness = 2
    position  = 0.01
    </axis>
    <axis>
    color     = vlgreen
    thickness = 2
    position  = 0.008
    </axis>
    <axis>
    color     = vlgreen
    thickness = 2
    position  = 0.006
    </axis>
    <axis>
    color     = red
    thickness = 2
    position  = 0.002
    </axis>
    </axes>
    
    </plot>
    
    <plot>
    z       = 5
    max_gap = 1u
    file    = data/6/snp.density.1mb.txt
    color   = red
    fill_color = red_a4
    min     = 0
    max     = 0.015
    r0      = 0.85r
    r1      = 0.95r
    orientation = in
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

