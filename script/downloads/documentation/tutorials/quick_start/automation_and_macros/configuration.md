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

## 9\. Automation & Macros

[Lesson](/documentation/tutorials/quick_start/automation_and_macros/lesson)
[Images](/documentation/tutorials/quick_start/automation_and_macros/images)
[Configuration](/documentation/tutorials/quick_start/automation_and_macros/configuration)

### circos.conf

    
    
    # 1.9 MODULAR CONFIGURATION, MACROS
    
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
    
    <plots>
    
    <plot>
    type  = text
    file  = data/6/genes.labels.txt
    r1    = 0.8r
    r0    = 0.6r
    label_font = light
    label_size = 12p
    rpadding   = 5p
    show_links     = no
    link_dims      = 0p,2p,5p,2p,2p
    link_thickness = 2p
    link_color     = black
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    <rule>
    condition  = var(value) =~ /a/i
    label_font = bold
    flow       = continue
    </rule>
    <rule>
    condition  = var(value) =~ /b/i
    color      = blue
    </rule>
    </rules>
    
    </plot>
    
    # By using counters and automatic track placement, we can
    # create 4 heatmaps with identical configurations (heatmap.conf).
    # The conf() function is used within heatmap.conf to reference
    # configuration parameters.
    
    h0 = 0.88 # start of heatmap tracks 
    hw = 0.01 # width of heatmap track (-'ve if tracks progress inward)
    hp = 0    # padding between heatmap tracks
    
    # Look in heatmap.conf for explanation.
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    <<include heatmap.conf>>
    </plot>
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.hist.txt
    r1   = 0.88r
    r0   = 0.81r
    fill_color = vdgrey
    extend_bin = no
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    <<include backgrounds.conf>>
    </plot>
    
    <plot>
    type = histogram
    file = data/5/segdup.hs1234.stacked.txt
    r1   = 0.99r
    r0   = 0.92r
    fill_color  = hs1,hs2,hs3,hs4
    orientation = in
    extend_bin  = no
    <rules>
    <<include rule.exclude.hs1.conf>>
    </rules>
    <<include axes.conf>>
    </plot>
    
    </plots>
    
    <links>
    <link>
    file          = data/5/segdup.txt
    radius        = 0.6r
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

### axes.conf

    
    
    <axes>
    # Show axes only on ideograms that have data for this track
    show = data
    
    thickness = 1
    color     = lgrey
    <axis>
    spacing   = 0.1r
    </axis>
    <axis>
    spacing   = 0.2r
    color     = grey
    </axis>
    <axis>
    position  = 0.5r
    color     = red
    </axis>
    <axis>
    position  = 0.85r
    color     = green
    thickness = 2
    </axis>
    
    </axes>
    

  

* * *

### backgrounds.conf

    
    
    <backgrounds>
    # Show the backgrounds only for ideograms that have data
    show  = data
    <background>
    color = vvlgrey
    </background>
    <background>
    color = vlgrey
    y0    = 0.2r
    y1    = 0.5r
    </background>
    <background>
    color = lgrey
    y0    = 0.5r
    y1    = 0.8r
    </background>
    <background>
    color = grey
    y0    = 0.8r
    </background>
    
    </backgrounds>
    

  

* * *

### heatmap.conf

    
    
    type           = heatmap
    file           = data/5/segdup.hs1234.heatmap.txt
    
    # The 'c' parameter (arbitrarily named) is referenced
    # within heatmap.conf as conf(.,c). conf(x) retrieves
    # the value of parameter 'x' in the current block and
    # conf(.,x) looks up the configuration tree until
    # it finds x.
    
    c = eval(sprintf("hs%d",counter(heatmap)+1))
    
    # track_r0(counter,start,width,padding) 
    # track_r1(counter,start,width,padding) 
    # are helper functions that return the start/end radius of a track
    # formatted as float+"r", e.g. 0.925r
    # 
    # r0 = start + counter * (width + padding) 
    # r1 = start + counter * (width + padding) + width
    #
    # The calls to conf(.,x) reference the <plot> block's h0, hw and hp
    # parameters. The counter(heatmap) is an 0-start automatically incremented
    # index, which is incremented by 1 for each type=heatmap plot.
    #
    r1    = eval(track_r1(counter(heatmap),conf(.,h0),conf(.,hw),conf(.,hp)))
    r0    = eval(track_r0(counter(heatmap),conf(.,h0),conf(.,hw),conf(.,hp)))
    
    # conf(.,c) references the <plot> block's 'c' parameter
    color          = conf(.,c)_a5,conf(.,c)_a4,conf(.,c)_a3,conf(.,c)_a2,conf(.,c)_a1,conf(.,c)
    scale_log_base = 0.25
    
    <rules>
    <<include rule.exclude.hs1.conf>>
    <rule>
    condition = var(id) ne "conf(.,c)"
    show      = no
    </rule>
    </rules>
    

  

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

