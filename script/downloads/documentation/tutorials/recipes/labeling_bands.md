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

## 3\. Labeling Karyotype Bands

[Lesson](/documentation/tutorials/recipes/labeling_bands/lesson)
[Images](/documentation/tutorials/recipes/labeling_bands/images)
[Configuration](/documentation/tutorials/recipes/labeling_bands/configuration)

This tutorial show syou how to add a narrow band of text labels to your
figure. We'll label the cytogenetic bands on the ideograms for the example.

First, we'll extract the position and names of the bands from the human
karyotype file that is included with Circos
(`data/karyotype/karyotype.human.txt`).

    
    
    > cat data/karyotype.human.txt | grep band | awk '{print $2,$5,$6,$3}'
    hs1 0 2300000 p36.33
    hs1 2300000 5300000 p36.32
    hs1 5300000 7100000 p36.31
    ...
    

This data file to populate a text track. In this example, I've placed the band
labels immediately outside the ideogram circle, which required that I shift
the ticks outward.

    
    
    <plot>
    
    type  = text
    color = red
    file  = data/8/text.bands.txt
    
    r0 = 1r
    r1 = 1r+300p
    
    label_size = 12
    label_font = condensed
    
    show_links     = yes
    link_dims      = 0p,2p,6p,2p,5p
    link_thickness = 2p
    link_color     = black
    
    label_snuggle        = yes
    max_snuggle_distance = 1r
    snuggle_tolerance    = 0.25r
    snuggle_sampling     = 2
    snuggle_refine       = yes
    
    </plot>
    
    

### adjusting text color

One way to adjust the color of the text is to use rules. For example, the
three rules below adjust the color of the text based on chromosome, position
and text label, respectively.

    
    
    <rules>
    <rule>
    condition  = on(hs1)
    color      = blue
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(start) > 50mb && var(end) < 100mb
    color      = green
    flow       = continue
    </rule>
    
    <rule>
    condition  = var(value) =~ /[.]\d\d/
    color      = grey
    </rule>
    
    </rules>
    

You can also adjust the color of the label (or any other format parameter) by
including the corresponding variable/value pairs directly in the data file.

    
    
    hs10 111800000 114900000 q25.2 color=orange
    hs10 114900000 119100000 q25.3 color=orange
    hs10 119100000 121700000 q26.11 color=purple
    hs10 121700000 123100000 q26.12 color=purple
    hs10 123100000 127400000 q26.13 label_size=24p
    hs10 127400000 130500000 q26.2 label_size=18p
    hs10 130500000 135374737 q26.3 label_size=14p
    

Remember that rules will override these settings, unless `overwrite=no` is set
in a rule.

