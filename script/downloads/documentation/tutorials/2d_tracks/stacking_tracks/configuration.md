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

## 12\. Putting It All Together

[Lesson](/documentation/tutorials/2d_tracks/stacking_tracks/lesson)
[Images](/documentation/tutorials/2d_tracks/stacking_tracks/images)
[Configuration](/documentation/tutorials/2d_tracks/stacking_tracks/configuration)

### circos.conf

    
    
    show_scatter   = yes
    show_line      = yes
    show_histogram = yes
    show_heatmap   = yes
    show_tile      = yes
    show_highlight = yes
    use_rules      = yes
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype         = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    chromosomes_display_default = no
    
    # to see how reversing ideograms work - comment out the chromosomes
    # line below
    chromosomes       = hs2
    
    # and uncomment the two definitions below
    # - first split hs2 into three ideograms
    # - now reverse the ideogram with tag "b"
    #chromosomes       = hs2[a]:0-60;hs2[b]:70-140;hs2[c]:150-)
    #chromosomes_reverse = b
    
    #chromosomes        = hs2[a]:0-30;hs2[b]:50-80;hs2[c]:100-130;hs2[d]:150-180;hs2[e]:190-200;hs2[f]:210-)
    #chromosomes_radius = a:0.95r;b:0.9r;c:0.85r;d:0.8r;e:0.75r;f:0.7r
    
    <plots>
    
    show = no
    
    <plot>
    show             = conf(show_heatmap)
    type             = heatmap
    color            = spectral-5-div
    stroke_thickness = 1
    scale_log_base   = 0.25
    stroke_color     = black
    file             = data/6/snp.number.1mb.txt
    r0               = 1.075r
    r1               = 1.075r+50p
    </plot>
    
    <plot>
    show             = conf(show_heatmap)
    type             = heatmap
    color            = spectral-5-div
    file             = data/6/variation.heatmap.txt
    stroke_thickness = 0
    scale_log_base   = 0.25
    r0               = 0.925r
    r1               = 0.925r+50p
    </plot>
    
    <plot>
    show             = conf(show_heatmap)
    type             = heatmap
    color            = spectral-5-div
    file             = data/6/rand.1.txt
    r0               = 0.6r
    r1               = 0.6r+30p
    
    <rules>
    use = conf(use_rules)
    <rule>
    condition  = rand() < 0.2 || var(value) < 0.5
    show       = no
    </rule>
    </rules>
    </plot>
    
    <plot>
    show             = conf(show_heatmap)
    type             = heatmap
    color            = spectral-5-div
    file             = data/6/rand.2.txt
    r0               = 0.6r+40p
    r1               = 0.6r+70p
    
    <rules>
    use = conf(use_rules)
    <rule>
    condition = rand() < 0.2 || var(value) > 0.5
    show      = no
    </rule>
    </rules>
    </plot>
    
    <plot>
    show             = conf(show_heatmap)
    type             = heatmap
    color            = spectral-5-div
    file             = data/6/rand.3.txt
    r0               = 0.6r+80p
    r1               = 0.6r+110p
    
    <rules>
    use = conf(use_rules)
    <rule>
    condition  = rand() < 0.2 || (var(value) > 0.25 && var(value) < 0.75)
    show       = no
    </rule>
    </rules>
    </plot>
    
    <plot>
    show         = conf(show_scatter)
    type         = scatter
    file         = data/6/conservation.avg.txt
    glyph        = circle
    glyph_size   = 8
    orientation  = out
    fill_color   = black
    r0           = 0.80r
    r1           = 0.90r
    z            = 5
    </plot>
    
    <plot>
    show         = conf(show_line)
    type         = line
    file         = data/6/conservation.p5.txt
    orientation  = out
    thickness    = 3
    color        = green
    r0           = 0.80r
    r1           = 0.90r
    z = 15
    </plot>
    
    <plot>
    show         = conf(show_line)
    type         = line
    file         = data/6/conservation.p95.txt
    orientation  = out
    thickness    = 3
    color        = red
    r0           = 0.80r
    r1           = 0.90r
    z = 15
    </plot>
    
    <plot>
    show         = conf(show_histogram)
    type         = histogram
    file         = data/6/snp.number.500kb.txt
    thickness    = 2
    color        = black
    fill_under   = yes
    fill_color   = red
    r0           = 0.80r
    r1           = 0.90r
    max_gap      = 5u
    z = 10
    </plot>
    
    <plot>
    show         = conf(show_histogram)
    type         = histogram
    file         = data/6/snp.number.250kb.txt
    orientation  = in
    thickness    = 1
    color        = black
    fill_under   = yes
    fill_color   = red
    r0           = 0.65r
    r1           = 0.75r
    max_gap      = 5u
    z = 10
    </plot>
    
    <plot>
    show         = conf(show_heatmap)
    type         = heatmap
    file         = data/6/snp.number.1mb.txt
    scale_log_base = 0.25
    min          = 1500
    color        = spectral-5-div
    r0           = 0.75r
    r1           = 0.80r
    </plot>
    
    <plot>
    show         = conf(show_tile)
    type         = tile
    file         = data/6/variation.txt
    color        = orange
    stroke_color = black
    stroke_thickness = 0
    r0           = 0.50r
    r1           = 0.65r
    orientation  = out
    layers       = 11
    margin       = 0.25u
    padding      = 4
    thickness    = 10
    z = 10
    
    <rules>
    use = conf(use_rules)
    <rule>
    condition  = var(size) < 25000
    show = no
    </rule>
    </rules>
    </plot>
    
    <plot>
    show         = conf(show_tile)
    type         = tile
    file         = data/6/tiles.rand.1.txt
    color        = black
    r0           = 0.05r
    r1           = 0.35r
    orientation  = center
    layers       = 11
    margin       = 0.25u
    padding      = 4
    thickness    = 10
    z = 10
    
    <rules>
    use = conf(use_rules)
    <rule>
    condition  = abs(var(start) - 20Mb) < 10Mb
    color      = red
    </rule>
    <rule>
    condition  = abs(var(start) - 60Mb) < 10Mb
    color      = orange
    </rule>
    <rule>
    condition  = abs(var(start) - 160Mb) < 10Mb
    color      = green
    </rule>
    <rule>
    condition  = rand() < 0.1
    color      = blue
    </rule>
    <rule>
    condition  = rand() < 0.1
    show = no
    </rule>
    <rule>
    condition  = rand() < 0.1
    color      = orange
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    show         = conf(show_tile)
    type         = tile
    file         = data/6/assembly.txt
    color        = black
    stroke_thickness = 1
    r0           = 0.30r
    r1           = 0.49r
    orientation  = in
    layers       = 11
    margin       = 0.25u
    padding      = 4
    thickness    = 10
    z = 10
    
    <rules>
    use = conf(use_rules)
    <rule>
    condition = var(size) < 50000
    show = no
    </rule>
    </rules>
    
    </plot>
    
    <plot>
    show = conf(show_highlight)
    type = highlight
    file = data/6/highlights.txt
    r0   = 0.98r
    r1   = 0.0r
    z    = 2
    
    <rules>
    use = conf(use_rules)
    <rule>
    condition  = 1
    fill_color = eval(var(fill_color)."_a4")
    </rule>
    </rules>
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
    

  

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

