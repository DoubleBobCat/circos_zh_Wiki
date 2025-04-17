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

## 16\. Automating Heatmaps

[Lesson](/documentation/tutorials/recipes/automating_heatmaps/lesson)
[Images](/documentation/tutorials/recipes/automating_heatmaps/images)
[Configuration](/documentation/tutorials/recipes/automating_heatmaps/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    chromosomes = hs1;hs2;hs3
    
    track_width   = 0.007
    track_start   = 0.991
    track_step    = 0.01
    
    <plots>
    
    type = heatmap
    min  = 0
    max  = 1
    
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    <<include 10plot.conf>>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### 10plot.conf

    
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    

  

* * *

### color.conf

    
    
    # The track counter will run 0-99, and we want to map this into range 3..11 
    # to smoothly vary the spectral color map
    #color = spectral-11-div
    color = eval(sprintf("spectral-%d-div",remap_round(counter(plot),0,99,11,3)))
    
    # The track counter will run 0-99, and we want to map this into range 3..9
    # to smoothly vary the red color map
    # color = eval(sprintf("reds-%d-seq",remap_round(counter(plot),0,99,9,3)))
    
    # Combine two color maps
    #color = eval(sprintf("blues-%d-seq-rev,oranges-%d-seq-rev",remap_round(counter(plot),0,99,9,3),remap_round(counter(plot),0,99,9,3)))
    

  

* * *

### file.conf

    
    
    file    = data/8/17/genes.counter(plot).txt
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    show = no
    
    <spacing>
    
    default = 0u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 20p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 1r
    show_label     = no
    label_with_tag = yes
    label_font     = default
    label_radius   = dims(ideogram,radius) + 0.075r
    label_size     = 60p
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    </ideogram>
    
    

  

* * *

### plot.conf

    
    
    <plot>
    <<include file.conf>>
    <<include r0r1.conf>>
    <<include color.conf>>
    <<include rules.conf>>
    scale_log_base = eval(0.05*(100-counter(plot)))
    </plot>
    

  

* * *

### r0r1.conf

    
    
    r0      = eval(sprintf("%fr",conf(track_start)-counter(plot)*conf(track_step)))
    r1      = eval(sprintf("%fr",conf(track_start)+conf(track_width)-counter(plot)*conf(track_step)))
    orientation = eval( counter(plot) % 2 ? "in" : "out" )
    

  

* * *

### rules.conf

    
    
    <rules>
    
    # If you wish, you can generate the random
    # values using this rule. Don't forget to set
    # flow=continue so that rule testing
    # doesn't short-circuit.
    #<rule>
    #condition  = 1
    #value      = eval(rand())
    #flow       = continue
    #</rule>
    
    <rule>
    importance = 100
    condition  = var(value) < 0.005
    #fill_color = white
    show = no
    </rule>
    </rules>
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 24pp
    label_offset   = 5p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 20u
    size           = 16p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

