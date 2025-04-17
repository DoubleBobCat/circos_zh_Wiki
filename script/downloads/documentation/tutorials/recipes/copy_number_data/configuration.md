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

# 9 — Recipes

## 13\. Copy Number Data

[Lesson](/documentation/tutorials/recipes/copy_number_data/lesson)
[Images](/documentation/tutorials/recipes/copy_number_data/images)
[Configuration](/documentation/tutorials/recipes/copy_number_data/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes                 = -hsX;-hsY
    chromosomes_display_default = yes
    
    <plots>
    
    # Data out of bounds should be hidden. Otherwise the
    # default is to clip the data to range min/max.
    range = hide
    
    # scatter plot for values [-3,0]
    <plot>
    type = scatter
    file = data/8/13/data.cnv.txt
    r0   = 0.6r
    r1   = 0.75r
    min  = -3
    max  = 0
    glyph = circle
    glyph_size = 8
    color = red
    
    <axes>
    <axis>
    color     = lred
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    <backgrounds>
    <background>
    color = vlred_a5
    </background>
    </backgrounds>
    
    <rules>
    <rule>
    condition  = 1
    glyph_size = eval( 6 + 4*abs(var(value)))
    flow       = continue
    </rule>
    <rule>
    condition  = var(value) < -2
    stroke_color = black
    stroke_thickness = 2
    </rule>
    </rules>
    </plot>
    
    # scatter plot for values [0,3]
    <plot>
    type = scatter
    file = data/8/13/data.cnv.txt
    r0   = 0.75r
    r1   = 0.9r
    min  = 0
    max  = 3
    glyph = circle
    glyph_size = 8
    color = green
    
    <axes>
    <axis>
    color     = lgreen
    thickness = 2
    spacing   = 0.1r
    </axis>
    </axes>
    
    <backgrounds>
    <background>
    color = vlgreen_a5
    </background>
    </backgrounds>
    
    <rules>
    <rule>
    condition  = 1
    glyph_size = eval( 6 + 4*abs(var(value)))
    flow       = continue
    </rule>
    <rule>
    condition    = var(value) > 2
    stroke_color = black
    stroke_thickness = 2
    </rule>
    </rules>
    
    </plot>
    
    # scatter plot for values [-3,3] turned into a heat map
    # by using r0=r1
    <plot>
    type = scatter
    file = data/8/13/data.cnv.txt
    r0   = 0.935r
    r1   = 0.935r
    min  = -3
    max  = 0
    glyph = square
    glyph_size = 8
    fill_color = red
    
    <rules>
    <rule>
    condition  = 1
    fill_color = eval( "red_a" . remap_int(var(value),-3,3,1,5) )
    </rule>
    </rules>
    
    </plot>
    
    # scatter plot for values [0,3] turned into a heat map
    # by using r0=r1
    <plot>
    type = scatter
    file = data/8/13/data.cnv.txt
    r0   = 0.955r
    r1   = 0.955r
    min  = 0
    max  = 3
    glyph = square
    glyph_size = 8
    fill_color = green
    
    <rules>
    <rule>
    condition  = 1
    fill_color = eval( "green_a" . remap_int(var(value),0,3,1,5) )
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
    band_transparency     = 3
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.005r
    break   = 0.5r
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color = black
    fill_color   = blue
    thickness    = 0.25r
    stroke_thickness = 2
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 2
    thickness        = 1.5r
    </break>
    
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

