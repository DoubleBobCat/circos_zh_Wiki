---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Recipes
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

# 9 — Recipes

## 7\. Variable Radius Link Ends

[Lesson](/documentation/tutorials/recipes/variable_link_ends/lesson)
[Images](/documentation/tutorials/recipes/variable_link_ends/images)
[Configuration](/documentation/tutorials/recipes/variable_link_ends/configuration)

Using entries in the link data file, or rules, you can independently
manipulate the radial position of each end of a link. One application of this
is to move link ends out of the way of another data track.

This is done by setting `radius1` and `radius2` values, which are the radial
positions of the link ends associated with the first and second data point,
respectively.

The first way to achieve this is to associate a radius value with one or both
of the ends.

    
    
    hs1 486 76975 hs15 100263879 100338121 radius1=0.5r
    hs1 342608 393885 hs15 100218755 100268630 radius2=0.5r
    hs1 576306 626811 hs15 100218755 100268630 radius=0.75r
    

Link ends for which radius is not defined will use the `radius` value defined
in the <link> or <links> blcok.

The second way to adjust radius values is to use a rule and set `radius1` and
`radius2` variables.

    
    
    <rules>
    
    # if a rule is triggered, continue testing with other rules
    flow       = continue
    
    # remap the color of the link to the first chromosome
    <rule>
    condition  = 1
    color      = eval(sprintf("%s_a4",var(chr1)))
    </rule>
    
    # Alter radial position of one or both ends of a link, depending
    # on its position. The function on(RX) tests whether a link
    # is on a chromosome matching the regular expression RX.
    
    # to/from hs1
    <rule>
    # the trailing $ (end of string anchor) is required so that 
    # chromosome names like hs10, hs11, hs12, etc don't match
    condition  = on(hs1$)
    radius     = 0.85r
    </rule>
    
    # to hs10, hs11 or hs12
    <rule>
    condition  = to(hs1[012])
    radius2    = 0.75r
    </rule>
    
    # from hs10, hs11, hs12
    <rule>
    condition  = from(hs1[012])
    radius1    = 0.75r
    </rule>
    
    # from hs14 and has start beyond 100mb
    <rule>
    condition  = from(hs14) && var(start1) > 100mb
    radius1    = 1r+50p
    z          = 5
    thickness  = 3
    color      = blue
    </rule>
    
    # to hs5 and has end within 50mb of position 100mb
    <rule>
    condition  = to(hs5) && abs(var(start2) - 100mb) < 50mb
    radius2    = 1r+50p
    z          = 5
    thickness  = 3
    color      = red
    </rule>
    
    </rules>
    

