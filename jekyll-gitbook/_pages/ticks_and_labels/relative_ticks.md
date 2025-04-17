---
author: DoubleCat
date: 2025-04-11
layout: post
category: ticks_and_labels
title: Tick Marks, Grids and Labels
---

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

# 5 — Tick Marks, Grids and Labels

## 7\. Relative Ticks

[Lesson](/documentation/tutorials/ticks_and_labels/relative_ticks/lesson)
[Images](/documentation/tutorials/ticks_and_labels/relative_ticks/images)
[Configuration](/documentation/tutorials/ticks_and_labels/relative_ticks/configuration)

Ticks can be spaced and/or labeled in relative units, with respect to the
length of the ideogram to which they belong. Up to now, you've seen how to
label and space ticks in absolute distances (e.g. every 10 Mb), and this
tutorial shows you how to space your ticks in relative distances (e.g. every
1% along ideogram).

There are two independent relative tick settings: relative spacing and
relative labels. Relative spacing is used to set the tick period to be
relative to the ideogram (e.g. every 1%). Relative labels are used to format
the label of the tick to be relative to the length of the ideogram. These two
settings are independent. You can have ticks spaced relatively, but labeled by
their absolute position, and vice versa.

### Relative Spacing

To space ticks relatively, use the rspacing and spacing_type parameter in the
block. For example, to place ticks every 1% along the ideogram,

    
    
    <ticks>
    <tick>
    spacing_type = relative
    rspacing     = 0.01
    ...
    </tick>
    ...
    </ticks>
    

Note that relative spacing parameters do not collide with absolute spacing,
which is defined by the "spacing" parameter. This means that you can have both
"spacing" and "rspacing" defined, and then toggle between relative and
absolute spacing by defining the value of spacing_type.

    
    
    <ticks>
    # this tick is relatively spaced
    <tick>
    spacing      = 10u
    rspacing     = 0.01
    spacing_type = relative
    ...
    </tick>
    
    # this tick is absolutely spaced
    <tick>
    spacing      = 10u
    rspacing     = 0.01
    spacing_type = absolute
    ...
    </tick>
    ...
    </ticks>
    

Since each tick definition is independent, you can mix relatively spaced ticks
with absolutely spaced ticks. For example, you can have ticks every 10Mb and
every 10% if you like.

    
    
    <ticks>
    # these ticks are every 1Mb (assumes chromosome_units=1000000)
    <tick>
    spacing      = 1u
    spacing_type = absolute
    ...
    </tick>
    
    # these ticks are every 1% of ideogram 
    <tick>
    rspacing     = 0.01
    spacing_type = relative
    ...
    </tick>
    ...
    </ticks>
    

In the first example image, there are three layers of ticks: absolute spacing
every 1Mb, relative spacing every 0.01 and relative spacing every 0.1. Notice
that the labels for each tick layer are absolute. This works well for
absolutely spaced ticks, but looks awkward for relatively spaced ticks (e.g.
first tick in relative layer 0.1 is "24").

### Relative Labels

When ticks are relatively spaced (e.g. every 1%), it makes more sense that
their labels are relative too (e.g. appear as 1% rather than the corresponding
absolute amount, such as 24.72 for chr1). To set the tick label to be
relative, use the label_relative and rmultiplier settings.

    
    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    format         = %.2f
    ...
    </tick>
    

You can define a relative multiplier for the label so that relative labels
like "0.07" can be displayed as "7".

    
    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    format         = %.2f # labels will be 0.01 0.02 0.03 ...
    ...
    </tick>
    

With these settings, the tick labels will read 0.01, 0.02, ... 0.99. The
"rmultiplier" works just like "multiplier", but is reserved for labels of
relatively spaced ticks. If rmultiplier was set to 100, the tick labels would
be 1.00, 2.00, ... 99.00. For example, to have ticks every 1% labeled 1%, 2%,
... 99%, use

    
    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    rmultiplier    = 100 # labels will be 1 2 3 4 ... 
    format         = %d
    </tick>
    

By adding a suffix, you can construct labels such as "6%" or "2/10".

    
    
    <tick>
    spacing_type   = relative
    rspacing       = 0.01
    label_relative = yes
    rmultiplier    = 100 
    format         = %d
    suffix         = %  # labels will be 1% 2% 3% ... 
    </tick>
    
    <tick>
    spacing_type   = relative
    rspacing       = 0.1
    label_relative = yes
    rmultiplier    = 10 
    format         = %d
    suffix         = "/10" # labels will be 1/10 2/10 3/10 ...
    </tick>
    

### relative ticks - relative to chromsomes or ideograms

If a chromosome is represented by a single ideogram in its entirety, then the
default relative tick settings, which are relative to chromosome size, are
appropriate.

However, if you are displaying a fraction of a chromosome, or are splitting it
up into multiple ideograms, you may wish to make tick marks relative to the
ideogram and not the chromosome. To do this, set the rdivisor.

    
    
    <tick>
    spacing_type   = relative
    rspacing       = 0.1
    rdivisor       = ideogram
    </tick>
    

With this block, ticks will be spaced every 1/10th of the ideogram they belong
to.

