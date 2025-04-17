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

# 2 — Quick Start

## 2\. Ticks & Labels

[Lesson](/documentation/tutorials/quick_start/ticks_and_labels/lesson)
[Images](/documentation/tutorials/quick_start/ticks_and_labels/images)
[Configuration](/documentation/tutorials/quick_start/ticks_and_labels/configuration)

### circos.conf

    
    
    # 1.2 IDEOGRAM LABELS, TICKS, AND MODULARIZING CONFIGURATION
    #
    # In this tutorial, I will add tick marks, tick labels and ideogram
    # labels to the previous image. This will require the use of a <ticks>
    # block and expanding the <ideogram> block. 
    #
    # To make the configuration more modular, the tick and ideogram
    # parameters will be stored in different files and imported using the
    # <<include>> directive.
    
    karyotype = data/karyotype/karyotype.human.txt
    
    # The chromosomes_unit value is used as a unit (suffix "u") to shorten
    # values in other parts of the configuration file. Some parameters,
    # such as ideogram and tick spacing, accept "u" suffixes, so instead of
    #
    # spacing = 10000000
    #
    # you can write
    #
    # spacing = 10u
    #
    # See ticks.conf for examples.
    
    chromosomes_units = 1000000
    
    <<include ideogram.conf>>
    
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>                
    </image>
    
    <<include etc/colors_fonts_patterns.conf>> 
    
    <<include etc/housekeeping.conf>> 
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    # Ideogram position, fill and outline
    radius           = 0.90r
    thickness        = 20p
    fill             = yes
    stroke_color     = dgrey
    stroke_thickness = 2p
    
    # Minimum definition for ideogram labels.
    
    show_label       = yes
    # see etc/fonts.conf for list of font names
    label_font       = default 
    label_radius     = dims(image,radius) - 60p
    label_size       = 30
    label_parallel   = yes
    
    </ideogram>
    
    

  

* * *

### ticks.conf

    
    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = 1r
    color            = black
    thickness        = 2p
    
    # the tick label is derived by multiplying the tick position
    # by 'multiplier' and casting it in 'format':
    #
    # sprintf(format,position*multiplier)
    #
    
    multiplier       = 1e-6
    
    # %d   - integer
    # %f   - float
    # %.1f - float with one decimal
    # %.2f - float with two decimals
    #
    # for other formats, see https://perldoc.perl.org/functions/sprintf.html
    
    format           = %d
    
    <tick>
    spacing        = 5u
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 25u
    size           = 15p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    </ticks>
    

  

* * *

