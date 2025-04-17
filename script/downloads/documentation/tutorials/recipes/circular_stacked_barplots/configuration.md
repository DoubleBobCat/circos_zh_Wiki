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

## 18\. Circular Stacked Bar Plots

[Lesson](/documentation/tutorials/recipes/circular_stacked_barplots/lesson)
[Images](/documentation/tutorials/recipes/circular_stacked_barplots/images)
[Configuration](/documentation/tutorials/recipes/circular_stacked_barplots/configuration)

### circos.conf

    
    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/8/scale.txt
    
    chromosomes_units           = 1
    chromosomes_display_default = yes
    
    # if using 7 species
    
    # well spaced
    
    #track_width = 0.08
    #track_step  = 0.1
    #track_start = 0.9
    
    # abutting
    
    track_width = 0.1
    track_step  = 0.105
    track_start = 0.9
    
    # if using 3x7 species
    #track_width = 0.03
    #track_step  = 0.04
    #track_start = 0.95
    
    <plots>
    
    <<include speciesplot.conf>>
    <<include speciesplot.conf>>
    <<include speciesplot.conf>>
    <<include speciesplot.conf>>
    <<include speciesplot.conf>>
    <<include speciesplot.conf>>
    <<include speciesplot.conf>>
    
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    #<<include speciesplot.conf>>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### ghcolorrule.conf

    
    
    <rules>
    <rule>
    condition  = 1
    # ghN -> spectral-10-div-N
    fill_color = eval(sprintf("spectral-10-div-%d",substr(var(id),2)))
    </rule>
    </rules>
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    # no ideogram (no ticks, no tick labels, no axis)
    show = no
    
    <spacing>
    
    # start/end of ideogram abut to create a closed plot
    default = 0u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 2p
    stroke_thickness = 0
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.9r
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

### speciesplot.conf

    
    
    <plot>
    type  = highlight
    file  = data/8/species.counter(plot).txt
    r1    = eval(sprintf("%fr",conf(track_start) - conf(track_step) * counter(plot) + conf(track_width) ))
    r0    = eval(sprintf("%fr",conf(track_start) - conf(track_step) * conf(counter,plot) ))
    fill_color       = black
    stroke_thickness = 1
    stroke_color     = grey
    <<include ghcolorrule.conf>>
    </plot>
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-1
    
    <tick>
    spacing        = 2u
    size           = 7p
    thickness      = 3p
    color          = black
    show_label     = no
    label_size     = 24p
    label_offset   = 5p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    size           = 10p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 24p
    label_offset   = 5p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 50u
    size           = 16p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 5p
    format         = %d
    suffix = %
    </tick>
    
    </ticks>
    

  

* * *

