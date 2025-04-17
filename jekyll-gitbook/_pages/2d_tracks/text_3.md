---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: 2D Data Tracks
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

# 7 — 2D Data Tracks

## 8\. Text—Rules

[Lesson](/documentation/tutorials/2d_tracks/text_3/lesson)
[Images](/documentation/tutorials/2d_tracks/text_3/images)
[Configuration](/documentation/tutorials/2d_tracks/text_3/configuration)

This tutorial shows you how to use rules with the text track. All tracks allow
for rules and using rules works the same way for each track. The [previous
tutorial](/documentation/tutorials/2d_tracks/text_2) used rules to color text.

We'll draw some sequence on the image and color the base pairs. We'll use a
monospaced font using

    
    
    label_font = mono
    

There are two data files used in this example, `data/6/sequence.txt` (20,000
entries)

    
    
    # sequence.txt
    ...
    hs1 2 2 C
    hs1 3 3 A
    hs1 4 4 A
    ...
    

and `data/6/sequence.long.txt` (100,000 entries).

    
    
    # sequence.long.txt
    ...
    hs1 1 1 A
    hs1 1 1 C
    hs1 1 1 A
    hs1 1 1 G
    hs1 2 2 T
    hs1 2 2 A
    hs1 2 2 C
    hs1 2 2 T
    ...
    

The ideogram in the image is `hs1:0-20kb`, but it's a good idea to start with
a smaller interval to see how things work, e.g. `hs1:0-1`. A track with
100,000 bases can take a very long time to draw—the code that determines the
character layout has not been optimized.

### applying text rules

A good way to include rules is using the <<include ... >> directive to read
them from another file. This keeps the configuration file tidy and allows you
to reuse the same rules for other tracks.

    
    
    <plots>
    
    # default values for all <plot> blocks
    type       = text
    color      = black
    label_font = mono
    label_size = 32
    # radial padding
    rpadding   = 0.2r
    
    <plot>
    
    file       = data/6/sequence.txt
    r1         = 0.9r
    r0         = 0.3r
    label_size = 16
    # angular padding
    padding    = -0.25r 
    
    <rules>
    <<include rule.textcolor.conf>>
    </rules>
    
    </plot>
    
    </plots>
    
    

The `rule.textcolor.conf` file is

    
    
    <rule>
    condition = var(value) eq "A"
    color     = red
    </rule>
    <rule>
    
    condition = var(value) eq "T"
    color     = blue
    </rule>
    <rule>
    
    condition = var(value) eq "C"
    color     = green
    </rule>
    

The text label is referenced using `var(value)` and the conditions check
whether the text is `A`, `T` or `C`. The default track coloring assumes the
label is `G`, so we don't have to check for this condition.

### adjusting text size

With rules, you can adjust any attribute of the text characters. For example,
you can adjust the size of the letters in the label by setting `label_size`.
This is done in the tracks immediately inside and outside the circle.

    
    
    <rule>
    # If the text is not A, then hide it. When this rule triggers,
    # other rules are not evaluated.
    condition  = var(value) ne "A"
    show       = no
    </rule>
    
    # This rule is applied to any text that didn't pass the previous
    # rule (i.e. only A). The label is set to a random value between
    # 12 and 48. The rand() function returns a uniformly sampled
    # random value in the interval [0,1).
    
    <rule>
    condition  = 1
    label_size = eval(12+32*rand())
    </rule>
    

