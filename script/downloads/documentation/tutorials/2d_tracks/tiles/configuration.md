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

## 4\. Tiles

[Lesson](/documentation/tutorials/2d_tracks/tiles/lesson)
[Images](/documentation/tutorials/2d_tracks/tiles/images)
[Configuration](/documentation/tutorials/2d_tracks/tiles/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes                 = hs9[a]:40-45;hs1[b]:40-45;hs9[c]:65-70;hs1[d]:50-55
    chromosomes_display_default = no
    
    <plots>
    
    type            = tile
    layers_overflow = hide
    
    <plot>
    file        = data/6/assembly.txt
    r1          = 0.98r
    r0          = 0.86r
    orientation = out
    
    layers      = 15
    margin      = 0.02u
    thickness   = 15
    padding     = 8
    
    stroke_thickness = 1
    stroke_color     = grey
    </plot>
    
    <plot>
    file        = data/6/genes.txt
    r1          = 0.84r
    r0          = 0.71r
    orientation = center
    
    layers      = 11
    margin      = 0.02u
    thickness   = 8
    padding     = 4
    
    layers_overflow       = collapse
    layers_overflow_color = red
    
    stroke_thickness = 1
    stroke_color     = dgreen
    color            = green
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    
    </plot>
    
    <plot>
    
    file        = data/6/variation.txt
    r1          = 0.69r
    r0          = 0.5r
    orientation = in
    
    layers      = 15
    margin      = 0.02u
    thickness   = 10
    padding     = 5
    
    stroke_thickness = 1
    stroke_color     = dblue
    color            = blue
    
    </plot>
    
    <plot>
    
    file            = data/6/segdup.txt
    r1              = 0.525r
    r0              = 0.2r
    orientation     = in
    
    layers          = 15
    margin          = 0.02u
    thickness       = 8
    padding         = 5
    
    layers_overflow = hide
    color           = orange
    
    <backgrounds>
    color = vlgrey_a5
    <background>
    y1    = 0.25r
    </background>
    <background>
    y1    = 0.5r
    </background>
    <background>
    y1    = 0.75r
    </background>
    <background>
    y1    = 1r
    </background>
    </backgrounds>
    
    <rules>
    <rule>
    condition = var(size) < 150kb
    color     = eval((qw(lgrey grey dgrey vdgrey black))[remap_round(var(size),10000,150000,0,4)])
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    file        = data/6/conservation.txt
    r0          = 0.2r
    r1          = 0.525r
    orientation = out
    
    layers      = 5
    margin      = 0.02u
    thickness   = 8
    padding     = 5
    
    layers_overflow       = grow
    layers_overflow_color = red
    
    color       = lpurple
    
    <rules>
    <rule>
    condition        = ! on(hs1)
    color            = blue
    stroke_thickness = 1
    stroke_color     = dblue
    </rule>
    </rules>
    
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
    spacing        = .1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = .5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 1u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

