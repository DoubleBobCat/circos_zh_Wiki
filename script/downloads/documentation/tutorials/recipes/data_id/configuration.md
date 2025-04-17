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

## 10\. ID Fields

[Lesson](/documentation/tutorials/recipes/data_id/lesson)
[Images](/documentation/tutorials/recipes/data_id/images)
[Configuration](/documentation/tutorials/recipes/data_id/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ticks.conf>>
    <<include ideogram.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    chromosomes = hs21:29.99-31.01
    
    <plots>
    
    <plot>
    file = data/8/repeats.withid.txt
    r0   = 0.8r
    r1   = 0.98r
    orientation = in
    type        = tile
    layers      = 50
    thickness   = 25p
    padding     = 5p
    margin      = 0.001u
    color       = black
    stroke_thickness = 2p
    stroke_color = black
    
    <rules>
    
    <rule>
    condition    = var(id) =~ /line/i
    color        = green
    flow         = continue
    </rule>
    
    <rule>
    condition    = var(id) =~ /line[12]/i
    stroke_color = red
    </rule>
    
    <rule>
    condition    = var(id) =~ /sine/i
    color        = blue
    stroke_color = blue
    </rule>
    
    <rule>
    condition    = var(id) =~ /simple/i
    color        = dgrey
    </rule>
    
    <rule>
    condition    = var(id) =~ /other/i
    color        = lgrey
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    
    type = text
    file = data/8/textid.txt
    
    color      = black
    
    label_font = bold
    label_size = 36p
    r0         = 0.51r
    r1         = 0.7r
    
    padding    = 15p
    rpadding   = 15p
    
    <rules>
    
    <rule>
    condition  = 1
    color      = eval(sprintf("set2-4-qual-%d",remap_int(var(id),1,100,1,4)))
    label_size = eval(sprintf("%dp",remap_int(var(id),1,100,12,48)))
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    
    file = data/8/linkid.txt
    
    bezier_radius = 0r
    radius        = 0.50r
    crest         = 0.25
    
    color     = dgrey
    thickness = 2
    
    <rules>
    <rule>
    # make sure that the id field matches the required number-number format
    condition  = var(id) =~ /(\d+)-(\d+)/
    thickness  = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; remap($match[0],1,100,1,10) )
    z          = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; $match[0] )
    color      = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; sprintf("spectral-9-div-%d_a%d", remap($match[1],1,100,1,9), remap($match[1],1,100,5,1 ) ) )
    </rule>
    </rules>
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

    
    
    radius           = 0.85r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_outer)+100
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    label_offset     = 2p
    multiplier = 1e-6
    color = black
    size  = 20p
    thickness = 4p
    
    <tick>
    spacing        = .005u
    color          = black
    show_label     = no
    label_size     = 8p
    label_offset   = 0p
    format         = %2.f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    
    <tick>
    spacing        = .05u
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 10p
    format         = %.2f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    
    <tick>
    spacing        = .25u
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 10p
    format         = %.2f
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
    

  

* * *

