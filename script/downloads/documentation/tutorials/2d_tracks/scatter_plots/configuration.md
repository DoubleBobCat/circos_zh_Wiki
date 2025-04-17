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

## 1\. Scatter Plots

[Lesson](/documentation/tutorials/2d_tracks/scatter_plots/lesson)
[Images](/documentation/tutorials/2d_tracks/scatter_plots/images)
[Configuration](/documentation/tutorials/2d_tracks/scatter_plots/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3
    #chromosomes_reverse = hs2
    chromosomes_display_default = no
    
    ################################################################
    # 
    # define 3 scatter plots, using the same data file
    #
    
    <plots>
    
    # all are scatter plots
    
    type             = scatter
    
    stroke_thickness = 1
    
    # first plot shows all points and selectively formats points at small/large
    # y-axis values to be red/green and triangles/rectangles
    
    <plot>
    
    file             = data/6/snp.density.txt
    fill_color       = grey
    stroke_color     = black
    glyph            = circle
    glyph_size       = 10
    
    max   = 0.013
    min   = 0
    r1    = 0.95r
    r0    = 0.65r
    
    # optional y0/y1 values (absolute or relative) in <background> blocks
    # define the start/end limits of background color
    #
    # y0 = 0.006
    # y0 = 0.75r
    
    <backgrounds>
    <background>
    color     = vvlgreen
    y0        = 0.006
    </background>
    <background>
    color     = vlgrey
    y1        = 0.006
    y0        = 0.002
    </background>
    <background>
    color     = vvlred
    y1        = 0.002
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = lgreen
    thickness = 1
    spacing   = 0.05r
    y0        = 0.006
    </axis>
    <axis>
    color     = dgreen
    thickness = 2
    spacing   = 0.1r
    y0        = 0.006
    </axis>
    
    <axis>
    color     = lgrey
    thickness = 1
    spacing   = 0.05r
    y1        = 0.006
    y0        = 0.002
    </axis>
    <axis>
    color     = dgrey
    thickness = 2
    spacing   = 0.1r
    y1        = 0.006
    y0        = 0.002
    </axis>
    
    <axis>
    color     = lred
    thickness = 1
    spacing   = 0.05r
    y1        = 0.002
    </axis>
    
    <axis>
    color     = dred
    thickness = 2
    spacing   = 0.1r
    y1        = 0.002
    </axis>
    
    </axes>
    
    <rules>
    
    <rule>
    condition    = var(value) > 0.006
    stroke_color = dgreen
    fill_color   = green
    glyph        = rectangle
    glyph_size   = 8
    </rule>
    
    <rule>
    condition    = var(value) < 0.002
    stroke_color = dred
    fill_color   = red
    glyph        = triangle
    </rule>
    
    </rules>
    
    </plot>
    
    # the second plot is a crop of the first plot, placed outside
    # the ideogram circle, showing only points with large y-values
    
    <plot>
    
    file             = data/6/snp.density.txt
    fill_color       = green
    stroke_color     = dgreen
    glyph            = rectangle
    glyph_size       = 8
    
    max   = 0.013
    min   = 0.007
    r1    = 1.175r
    r0    = 1.075r
    
    <backgrounds>
    # you can stack backgrounds by using transparent color
    <background>
    color     = vlgreen_a4
    y0        = 0.75r
    </background>
    <background>
    color     = vlgreen_a4
    y0        = 0.5r
    </background>
    <background>
    color     = vlgreen_a4
    y0        = 0.25r
    </background>
    <background>
    color     = vlgreen_a4
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = green_a3
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    <rules>
    
    <rule>
    condition    = var(value) < 0.007
    show         = no
    </rule>
    
    </rules>
    
    </plot>
    
    # the third plot is a crop of the first plot, placed closer to the
    # center of the circle, showing only points with small y-values
    
    <plot>
    
    file             = data/6/snp.density.txt
    fill_color       = red
    stroke_color     = dred
    glyph            = rectangle
    glyph_size       = 8
    
    max   = 0.0015
    min   = 0.000
    r1    = 0.60r
    r0    = 0.35r
    
    <backgrounds>
    <background>
    color     = vlred_a4
    y1        = 0.25r
    </background>
    <background>
    color     = vlred_a4
    y1        = 0.5r
    </background>
    <background>
    color     = vlred_a4
    y1        = 0.75r
    </background>
    <background>
    color     = vlred_a4
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    color     = red_a5
    thickness = 1
    spacing   = 0.025r
    </axis>
    <axis>
    color     = red_a3
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    <rules>
    <rule>
    condition    = var(value) > 0.002
    show         = no
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

