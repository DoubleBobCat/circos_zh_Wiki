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

## 4\. Links & Rules

[Lesson](/documentation/tutorials/quick_start/links_and_rules/lesson)
[Images](/documentation/tutorials/quick_start/links_and_rules/images)
[Configuration](/documentation/tutorials/quick_start/links_and_rules/configuration)

### circos.conf

    
    
    # 1.4 LINKS AND RULES
    #
    # The first data track we will add are links. By using rules, which
    # are expressions that are evaluated for every link, the formatting
    # can be dynamically changed based on data values.
    #
    # I will also show you how to change the definition of colors, if you
    # would like to assign different chromosome color scheme to your
    # figure.
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1-4]$/
    chromosomes_reverse         = /hs[234]/
    chromosomes_scale           = hs1=0.5r,/hs[234]/=0.5rn
    chromosomes_radius          = hs4:0.9r
    
    # In the previous tutorial (1.3), I used chromosomes_colors to change
    # the color of the ideograms. This approach works well when the only
    # thing you want to do is change the color of the segments. 
    #
    # Another way to achieve this is to actually redefine the colors which
    # are used to color the ideograms. The benefit of doing this is that
    # whenever you refer to the color (which you can use by using the name
    # of the chromosome), you get the custom value.
    #
    # If you look in the human karyotype file linked to above, you'll see
    # that each chromosome's color is chrN where N is the number of the
    # chromosome. Thus, hs1 has color chr1, hs2 has color chr2, and so
    # on. For convenience, a color can be referenced using 'chr' and 'hs'
    # prefixes (chr1 and hs1 are the same color).
    #
    # Colors are redefined by overwriting color definitions, which are
    # found in the <colors> block. This block is included below from the
    # colors_fonts_patterns.conf file, which contains all the default
    # definitions. To overwrite colors, use a "*" suffix and provide a new
    # value, which can be a lookup to another color.
    
    <colors>
    chr1* = red
    chr2* = orange
    chr3* = green
    chr4* = blue
    </colors>
    
    # Links are defined in <link> blocks enclosed in a <links> block. The
    # links start at a radial position defined by 'radius' and have their
    # control point (adjusts curvature) at the radial position defined by
    # 'bezier_radius'. In this example, I use the segmental duplication
    # data set, which connects regions of similar sequence (90%+
    # similarity, at least 1kb in size).
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.8r
    bezier_radius = 0r
    color         = black_a4
    thickness     = 2
    
    # Rule blocks can be added to any <link> or <plot> block and form a
    # decision chain that changes how data points (e.g. links, histogram
    # bins, scatter plot glyphs, etc) are formatted.
    
    <rules>
    
    # The decision chain is composed of one or more <rule> blocks.
    
    <rule>
    
    # Each rule has a condition, formatting statements and an optional
    # 'flow' statement. If the condition is true, the rule is applied to
    # the data point and no further rules are checked (unless
    # flow=continue). If the condition is false, the next rule is checked.
    #
    # var(X) referrs to the value of variable X for the data point. Here 'intrachr' means intra-chromosomal.
    
    condition     = var(intrachr)
    
    # Any links that are intra-chromosomal will not be shown. Further rules are not tested.
    
    show          = no
    
    </rule>
    
    <rule>
    
    # This rule is applied to all remaining links, since its condition is always true.
    
    condition     = 1
    
    # The color of the link is set to the 2nd chromosome in the link
    # coordinate (link's end). Here eval() is required so that the
    # expression var(chr2) is evaluated (we want the result of var(chr2),
    # not the color named "var(chr2)"). Note that for conditions,
    # evaluation is automatic, but required for all other parameters.
    
    color         = eval(var(chr2))
    
    # After this rule is applied, the rule chain continues.
    
    flow          = continue
    </rule>
    
    <rule>
    
    # If the link's start is on hs1...
    
    condition     = from(hs1)
    
    # ...set the radial position of the link's start to be close to the ideogram.
    
    radius1       = 0.99r
    </rule>
    
    <rule>
    
    # Same as the rule above, but applies to the end of the link.
    
    condition     = to(hs1)
    
    # 'radius2' (like chr2, start2, end2) refers to the variable 'radius' of the end of the link.
    
    radius2       = 0.99r
    
    </rule>
    
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

