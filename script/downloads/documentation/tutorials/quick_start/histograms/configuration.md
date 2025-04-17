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

## 5\. Histograms

[Lesson](/documentation/tutorials/quick_start/histograms/lesson)
[Images](/documentation/tutorials/quick_start/histograms/images)
[Configuration](/documentation/tutorials/quick_start/histograms/configuration)

### circos.conf

    
    
    # 1.5 HISTOGRAMS
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1234]$/
    chromosomes_radius          = hs4:0.9r
    
    <colors>
    chr1* = red
    chr2* = orange
    chr3* = green
    chr4* = blue
    </colors>
    
    chromosomes_reverse = /hs[234]/
    chromosomes_scale   = hs1=0.5r,/hs[234]/=0.5rn
    
    # Histograms are a type of track that displays 2D data, which
    # associates a value with a genomic position. Line plots, scatter
    # plots and heat maps are examples of other 2D tracks.
    #
    # The data format for 2D data is 
    #
    # #chr start end value [options]
    # ...
    # hs3 196000000 197999999 71.0000
    # hs3 198000000 199999999 57.0000
    # hs4 0 1999999 28.0000
    # hs4 2000000 3999999 40.0000
    # hs4 4000000 5999999 59.0000
    # ...
    #
    # Each histogram is defined in a <plot> block within an enclosing <plots> block.
    
    <plots>
    
    <plot>
    
    # The type sets the format of the track.
    
    type = histogram
    file = data/5/segdup.hs1234.hist.txt
    
    # The track is confined within r0/r1 radius limits. When using the
    # relative "r" suffix, the values are relative to the position of the
    # ideogram.
    
    r1   = 0.88r
    r0   = 0.81r
    
    # Histograms can have both a fill and outline. The default outline is 1px thick black. 
    
    fill_color = vdgrey
    
    # To turn off default outline, set the outline thickness to zero. If
    # you want to permanently disable this default, edit
    # etc/tracks/histogram.conf in the Circos distribution.
    
    #thickness = 0p
    
    # Do not join histogram bins that do not abut.
    
    extend_bin = no
    
    # Like for links, rules are used to dynamically alter formatting of
    # each data point (i.e. histogram bin). Here, I include the <rule>
    # block from a file, which contains the following
    #
    # <rule>
    # condition = on(hs1)
    # show      = no
    # </rule>
    #
    # to avoid displaying any data on hs1. The rule is included from a
    # file because it is reused again in the track below.
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    </plot>
    
    # Below I define another histogram. This will be a stacked histogram,
    # which will show several values for a given position by stacking
    # bins. This is a special kind of 2D data track which uses the data
    # format
    #
    # #chr start end value,value,value,... [options]
    # ...
    # hs3 196000000 197999999 0.0000,7.0000,64.0000,0.0000
    # hs3 198000000 199999999 21.0000,6.0000,18.0000,12.0000
    # hs4 0 1999999 5.0000,3.0000,1.0000,19.0000
    # hs4 2000000 3999999 1.0000,6.0000,16.0000,17.0000
    # hs4 4000000 5999999 1.0000,13.0000,25.0000,20.0000
    # ...
    #
    # Circos will automatically format the track as a stacked histogram
    # when type=histogram and multiple values in the data file are found.
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.stacked.txt
    r1   = 0.99r
    r0   = 0.92r
    
    # The fill_color for a stacked histogram is expected to be a list of
    # colors, each corresponding to a given value. For example, for the data line
    #
    # hs3 198000000 199999999 21.0000,6.0000,18.0000,12.0000
    #
    # the colors for the bins will be hs1 (21.0000), hs2 (6.0000), hs3 (18.0000), hs4 (12.0000).
    
    fill_color  = hs1,hs2,hs3,hs4
    
    # A histogram can be oriented out or in. 
    
    orientation = in
    extend_bin  = no
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.8r
    bezier_radius = 0r
    color         = black_a4
    thickness     = 2
    
    <rules>
    <<include rules.link.conf>>
    </rules>
    
    </link>
    
    </links>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>                
    </image>
    
    <<include etc/colors_fonts_patterns.conf>> 
    <<include etc/housekeeping.conf>> 
    data_out_of_range* = trim
    

  

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

### rule.exclude.hs1.conf

    
    
    <rule>
    condition = on(hs1)
    show      = no
    </rule>
    

  

* * *

### rules.link.conf

    
    
    <rule>
    condition     = var(intrachr)
    show          = no
    </rule>
    <rule>
    condition     = 1
    color         = eval(var(chr2))
    flow          = continue
    </rule>
    <rule>
    condition     = from(hs1)
    radius1       = 0.99r
    </rule>
    <rule>
    condition     = to(hs1)
    radius2       = 0.99r
    </rule>
    

  

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

