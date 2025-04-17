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

## 16\. Automating Tracks

[Lesson](/documentation/tutorials/recipes/automating_tracks/lesson)
[Images](/documentation/tutorials/recipes/automating_tracks/images)
[Configuration](/documentation/tutorials/recipes/automating_tracks/configuration)

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
    
    chromosomes = hs1;hs2;hs3;hs4;hs5;hs6
    
    track_width   = 0.055
    track_start   = 0.925
    track_step    = 0.06
    
    <plots>
    
    type       = histogram
    color      = black
    extend_bin = no
    min        = 0
    max        = 1
    
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
    <<include plot.conf>>
    <<include plot.conf>>
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### file.conf

    
    
    file = data/8/16/histogram.counter(plot).txt
    

  

* * *

### fillcolor.conf

    
    
    fill_color = eval(sprintf("spectral-11-div-%d",counter(plot)%11+1))
    

  

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
    radius         = 0.85r
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
    
    post_increment_counter = 1 # applies to default block counter (i.e. plot)
    init_counter           = thickness:0
    thickness              = eval(max(1,8-int(counter(thickness))))
    post_increment_counter = thickness:0.5
    
    <<include file.conf>>
    <<include r0r1.conf>>
    <<include fillcolor.conf>>
    <<include rules.conf>>
    
    <backgrounds>
    <background>
    color       = eval((qw(vvvlgrey vvlgrey vlgrey lgrey grey dgrey vdgrey vvdgrey))[counter(plot) % 8])
    </background>
    </backgrounds>
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
    # values for each histogram automatically
    # using this rule. Don't forget to set
    # flow=continue so that rule testing
    # doesn't short-circuit.
    #<rule>
    #condition  = 1
    #value      = eval(rand())
    #flow       = continue
    #</rule>
    
    <rule>
    condition  = var(value) > 0.25 && var(value) < 0.75
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

