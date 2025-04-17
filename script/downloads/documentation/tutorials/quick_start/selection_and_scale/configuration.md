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

## 3\. Ideogram Selection, Scale, Color & Orientation

[Lesson](/documentation/tutorials/quick_start/selection_and_scale/lesson)
[Images](/documentation/tutorials/quick_start/selection_and_scale/images)
[Configuration](/documentation/tutorials/quick_start/selection_and_scale/configuration)

### circos.conf

    
    
    # 1.3 IDEOGRAM SELECTION, SCALE, COLOR AND ORIENTATION
    #
    # This tutorial shows you how to select which chromosomes to draw and
    # flexibly arrange them in the image by applying custom scaling and
    # colors.
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    # The default behaviour is to display all chromosomes defined in the
    # karyotype file. In this example, I select only a subset.
    #
    # The 'chromosomes' parameter has several uses, and selecting which
    # chromosomes to show is one of them. You can list them
    #
    # hs1;hs2;hs3;hs4
    #
    # or provide a regular expression that selects them based on a successful match
    #
    # /hs[1-4]$/
    #
    # The $ anchor is necessary, otherwise chromosomes like hs10, hs11 and
    # hs20 are also matched.
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1-4]$/
    
    # The size of the ideogram on the figure can be adjusted using an
    # absolute or relative magnification. Absolute scaling,
    #
    # hs1=0.5
    #
    # shrinks or expands the ideogram by a fixed factor. When the "r"
    # suffix is used, the magnification becomes relative to the
    # circumference of the figure. Thus, 
    #
    # hs1=0.5r 
    #
    # makes hs1 to occupy 50% of the figure. To uniformly distribute
    # several ideogram within a fraction of the figure, use a regular
    # expression that selects the ideograms and the "rn" suffix (relative
    # normalized).
    #
    # /hs[234]/=0.5rn
    #
    # Will match hs2, hs3, hs4 and divide them evenly into 50% of the figure. Each ideogram will be about 16% of the figure.
    
    chromosomes_scale   = hs1=0.5r,/hs[234]/=0.5rn
    
    # By default, the scale progression is clockwise. You can set the
    # global angle progression using 'angle_orientation' in the <image>
    # block (clockwise or counterclockwise). To reverse it for one or
    # several ideograms, use 'chromosomes-reverse'
    
    chromosomes_reverse = /hs[234]/
    
    # The color of each ideogram is taken from the karyotype file. To
    # change it, use 'chromosomes_color'.
    
    chromosomes_color   = hs1=red,hs2=orange,hs3=green,hs4=blue
    
    # The default radial position for all ideograms is set by 'radius' in
    # the <ideogram> block (see ideogram.conf). To change the value for
    # specific ideograms, use chromosomes_radius.
    
    chromosomes_radius  = hs4:0.9r
    
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
    label_radius     = 1.075r  # if ideogram radius is constant, and you'd like labels close to image edge, 
                               # use the dims() function to access the size of the image
                               # label_radius  = dims(image,radius) - 60p
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

