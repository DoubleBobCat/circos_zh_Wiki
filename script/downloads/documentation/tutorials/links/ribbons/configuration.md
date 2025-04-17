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

# 6 — Links and Relationships

## 9\. Ribbons

[Lesson](/documentation/tutorials/links/ribbons/lesson)
[Images](/documentation/tutorials/links/ribbons/images)
[Configuration](/documentation/tutorials/links/ribbons/configuration)

### circos.conf

    
    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes                 = hs1[a]:0-0.8;hs1[b]:16.6-17.2;hs1[c]:141.5-148;hs1[d]:220.6-222.4;hs2[e]:90.8-95.2;hs2[f]:132.3-132.8;hs2[g]:242.5-)
    chromosomes_breaks          = -hs1:142.3-143.9;-hs1:144.2-144.7;-hs1:145-146;-hs1:220.8-222;-hs2:91.8-94.6
    chromosomes_display_default = no
    
    #chromosomes_radius = hs2:0.8r;a:0.9r;b:1.0r
    
    <links>
    
    radius = 0.99r
    crest  = 1
    ribbon           = yes
    flat             = yes
    stroke_color     = vdgrey
    stroke_thickness = 2
    color            = grey_a3
    
    bezier_radius        = 0r
    bezier_radius_purity = 0.5
    
    <link>
    
    file       = data/5/segdup.txt
    
    <rules>
    
    flow       = continue
    
    <rule>
    condition  = var(intrachr) && abs(var(pos1)-var(pos2)) < 10Mb
    show       = no
    </rule>
    
    <rule>
    condition  = max(var(size1),var(size2)) < 10kb
    show       = no
    </rule>
    
    <rule>
    condition  = 1
    z          = eval(int(max(var(size1),var(size2))/5000))
    </rule>
    
    <rule>
    condition    = var(intrachr) 
    condition    = (from(hs1) && var(start1) < 1Mb) || (to(hs1) && var(start2) < 1Mb)
    color        = orange
    stroke_color = dorange
    </rule>
    
    <rule>
    condition    = var(intrachr)
    condition    = (from(hs1) && var(start1) > 16Mb && var(start1) < 17Mb) || (to(hs1) && var(start2) > 16Mb && var(start2) < 17Mb)
    color        = lblue
    stroke_color = dblue
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
    band_transparency     = 0
    

  

* * *

### ideogram.conf

    
    
    <ideogram>
    
    <spacing>
    default = 0.02r
    break   = 0.25r
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    radius*       = 0.875r
    label_radius* = dims(ideogram,radius) + 0.125r
    
    </ideogram>
    
    

  

* * *

### ideogram.label.conf

    
    
    show_label       = yes
    label_font       = default
    label_radius     = dims(ideogram,radius) + 0.075r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
    

  

* * *

### ideogram.position.conf

    
    
    radius           = 0.90r
    thickness        = 100p
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
    
    <tick>
    spacing        = 0.01u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 0.05u
    show_label     = yes
    label_size     = 16p
    format         = %.2f
    </tick>
    
    <tick>
    spacing        = 0.2u
    show_label     = yes
    label_size     = 24p
    format         = %.2f
    </tick>
    
    </ticks>
    

  

* * *

