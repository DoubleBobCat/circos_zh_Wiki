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

## 3\. Histograms

[Lesson](/documentation/tutorials/2d_tracks/histograms/lesson)
[Images](/documentation/tutorials/2d_tracks/histograms/images)
[Configuration](/documentation/tutorials/2d_tracks/histograms/configuration)

### circos.2.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    file* = circos.2.png
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1
    chromosomes_breaks          = -hs1:120-140
    
    #chromosomes_reverse = hs2
    
    # lots of histograms here - let's take it one at a time
    
    <plots>
    
    # tall histogram immediately inside the ideogram circle
    # background* parameters define a colored backdrop for this histogram
    # axes* define y-axes
    
    <plot>
    
    type      = histogram
    file      = data/6/histogram.rand.txt
    
    r1        = 0.9r
    r0        = 0.7r
    max       = 1
    min       = -1
    
    stroke_type = outline
    thickness   = 4
    color       = vdgrey
    extend_bin  = no
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    spacing   = 0.1r
    color     = lgrey
    thickness = 2
    </axis>
    </axes>
    
    <rules>
    <rule>
    use       = no
    condition = var(value) < 0
    show      = no
    </rule>
    <rule>
    #condition  = var(value) < 0
    condition  = 1
    #fill_color = lred
    fill_color = eval(sprintf("spectral-9-div-%d",remap_int(var(value),-1,1,1,9)))
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### circos.3.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.hg19.txt
    
    <image>
    <<include etc/image.conf>>
    file* = circos.3.png
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1;hs2;hs3;hs4;hs5;hs6
    
    <plots>
    
    # Make all shared parameters central by including
    # them in the outer <plots> block. These values are
    # inherited by each <plot> block, where they can
    # be further overridden.
    
    type       = histogram
    extend_bin = no
    color      = black
    fill_under = yes
    thickness  = 2
    
    <plot>
    file = data/6/histogram.txt
    r0   = 0.8r
    r1   = 0.9r
    min  = 0.15
    max  = 0.3
    fill_color       = green
    background_color = lgreen
    <<include axis.conf>>
    <<include background.conf>>
    
    </plot>
    
    <plot>
    file = data/6/histogram.txt
    r0   = 0.6r
    r1   = 0.7r
    min  = -0.3
    max  = -0.15
    fill_color       = red
    background_color = lred
    <<include axis.conf>>
    <<include background.conf>>
    
    </plot>
    
    <plot>
    file = data/6/histogram.txt
    r0  = 0.7r
    r1  = 0.8r
    min = -0.15
    max = 0.15
    fill_color       = orange
    background_color = lorange
    <<include axis.conf>>
    <<include background.conf>>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### circos.4.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    file* = circos.4.png
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1
    chromosomes_breaks          = -hs1:120-140
    
    #chromosomes_reverse = hs2
    
    # lots of histograms here - let's take it one at a time
    
    <plots>
    
    # tall histogram immediately inside the ideogram circle
    # background* parameters define a colored backdrop for this histogram
    # axes* define y-axes
    
    <plot>
    
    type      = histogram
    file      = data/6/histogram.rand.txt
    
    r1        = 0.9r
    r0        = 0.7r
    max       = 1
    min       = -1
    
    stroke_type = outline
    thickness   = 4
    color       = vdgrey
    extend_bin  = no
    
    <backgrounds>
    <background>
    y1    = -0.5
    color = lred
    </background>
    <background>
    y0    = 0.5
    color = lgreen
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    spacing   = 0.1r
    color     = lgrey
    thickness = 2
    </axis>
    </axes>
    
    <rules>
    use = no
    <rule>
    condition  = var(value) < -0.5
    fill_color = red
    </rule>
    <rule>
    condition  = var(value) > 0.5
    fill_color = green
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    

  

* * *

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1
    
    #chromosomes_reverse = hs2
    
    # lots of histograms here - let's take it one at a time
    
    <plots>
    
    type      = histogram
    thickness = 2
    
    # tall histogram immediately inside the ideogram circle
    # background* parameters define a colored backdrop for this histogram
    # axes* define y-axes
    
    <plot>
    
    show    = yes
    
    max_gap = 5u
    file    = data/6/snp.density.250kb.txt
    #file = hist.txt
    color   = vdgrey
    min     = 0
    max     = 0.015
    r0      = 0.8r
    r1      = 0.975r
    
    #fill_color  = red
    
    stroke_type = bin # outline | bin | both
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    spacing = 0.1r
    color   = lgrey
    thickness = 2
    </axis>
    </axes>
    
    # color the histogram by value value and
    # only plot points every 2Mb
    
    <rules>
    
    <rule>
    condition    = var(value) > 0.006
    color        = dgreen
    fill_color   = green
    </rule>
    
    <rule>
    condition    = var(value) < 0.002
    color        = dred
    fill_color   = red
    </rule>
    
    </rules>
    
    </plot>
    
    # Dense histogram outside ideogram circle
    
    <plot>
    
    show    = yes
    
    file    = data/6/snp.density.txt
    z       = 5
    max_gap = 5u
    color   = black
    min     = 0
    max     = 0.015
    r0      = 1.075r
    r1      = 1.175r
    </plot>
    
    # precomputed average of previous histogram, drawn
    # underneath and filled under. The fill color is
    # adjusted based on value
    
    <plot>
    
    show       = yes
    
    file       = data/6/snp.density.1mb.txt
    max_gap    = 1u
    fill_under = yes
    fill_color = lgrey
    thickness  = 0
    min        = 0
    max        = 0.015
    r0         = 1.075r
    r1         = 1.175r
    
    <rules>
    <rule>
    condition  = var(value) > 0.006
    fill_color = lgreen
    </rule>
    <rule>
    condition  = var(value) > 0.004
    fill_color = lorange
    </rule>
    <rule>
    condition  = var(value) > 0.003
    fill_color = lred
    </rule>
    
    </rules>
    </plot>
    
    # histograms with randomly assigned values and
    # bin sizes, illustrating how Circos handles
    # variable-sized bins
    
    # simple outline - bins are not extended
    
    <plot>
    
    file       = data/6/hist.random.txt
    extend_bin = no
    color      = black
    min        = 0
    max        = 1
    r0         = 0.75r
    r1         = 0.79r
    </plot>
    
    # simple outline - bins are extended
    
    <plot>
    
    file  = data/6/hist.random.txt
    color = black
    min   = 0
    max   = 1
    r0    = 0.7r
    r1    = 0.74r
    </plot>
    
    # colored by value - bins are not extended
    
    <plot>
    
    file       = data/6/hist.random.2.txt
    extend_bin = no
    color      = black
    min        = 0
    max        = 1
    r0         = 0.65r
    r1         = 0.69r
    <rules>
    <rule>
    condition = var(value) > 0.9
    color = green
    </rule>
    <rule>
    condition = var(value) < 0.1
    color = red
    </rule>
    <rule>
    condition = var(value) > 0.45 && var(value) < 0.55
    color = orange
    </rule>
    </rules>
    </plot>
    
    # colored by value - bins are extended
    
    <plot>
    
    file  = data/6/hist.random.2.txt
    color = black
    min   = 0
    max   = 1
    r0    = 0.6r
    r1    = 0.64r
    <rules>
    <rule>
    condition = var(value) > 0.9
    color = green
    </rule>
    <rule>
    condition = var(value) < 0.1
    color = red
    </rule>
    <rule>
    condition = var(value) > 0.45 && var(value) < 0.55
    color = orange
    </rule>
    </rules>
    </plot>
    
    # filled under with grey, oriented out (default)
    
    <plot>
    
    file       = data/6/hist.random.3.txt
    z          = 5
    extend_bin = no
    color      = black
    fill_under = yes
    fill_color = lgrey
    min        = 0
    max        = 1
    r0         = 0.55r
    r1         = 0.59r
    </plot>
    
    # filled under with grey, oriented out (default) - bins are extended
    
    <plot>
    
    file       = data/6/hist.random.3.txt
    z          = 5
    color      = black
    fill_under = yes
    fill_color = lgrey
    min        = 0
    max        = 1
    r0         = 0.5r
    r1         = 0.54r
    </plot>
    
    # filled under with grey, oriented in
    
    <plot>
    file        = data/6/hist.random.4.txt
    z           = 5
    orientation = in
    color       = black
    fill_under  = yes
    fill_color  = lblue
    min         = 0
    max         = 1
    r0          = 0.46r
    r1          = 0.5r
    </plot>
    
    # filled under with orange, oriented out, 
    # complementary to the previous histogram
    #
    # here, I've used the previous histogram data
    # and remapped its value using a rule which
    # assigns a new data value new=1-old
    #
    # this remapping has the effect of making the
    # the histograms fit into one another (peak of one
    # fits exactly into valley of other)
    
    <plot>
    file       = data/6/hist.random.4.txt
    z          = 5
    color      = black
    fill_under = yes
    fill_color = orange
    min        = 0
    max        = 1
    r0         = 0.46r
    r1         = 0.5r
    <rules>
    <rule>
    condition  = 1
    value      = eval(1-var(value))
    </rule>
    </rules>
    </plot>
    
    # another random histogram, oriented in
    
    <plot>
    file        = data/6/hist.random.5.txt
    orientation = in
    color       = black
    fill_under  = yes
    fill_color  = orange
    min         = 0
    max         = 1
    r0          = 0.42r
    r1          = 0.46r
    </plot>
    
    <plot>
    file        = data/6/hist.random.5.txt
    orientation = in
    color       = black
    extend_bin  = no
    fill_under  = yes
    fill_color  = orange
    min         = 0
    max         = 1
    r0          = 0.36r
    r1          = 0.41r
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
    

  

* * *

### axis.conf

    
    
    axis           = yes
    axis_color     = dgrey
    axis_thickness = 2
    axis_spacing   = 0.1
    

  

* * *

### background.conf

    
    
    background                  = yes
    background_stroke_color     = black
    background_stroke_thickness = 2
    

  

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

### rules.conf

    
    
    <rules>
    <rule>
    condition  = var(value) < -0.5
    fill_color = red
    color      = dred
    </rule>
    <rule>
    condition  = var(value) < 0
    fill_color = orange 
    color      = dorange
    </rule>
    <rule>
    condition  = var(value) < 0.5
    fill_color = green
    color      = dgreen
    </rule>
    </rules>
    

  

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
    format           = %d
    
    <tick>
    spacing        = 1u
    show_label     = no
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    size           = 15p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
    

  

* * *

