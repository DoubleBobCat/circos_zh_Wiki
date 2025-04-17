---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Links and Relationships
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

# 6 — Links and Relationships

## 8\. Link Rules - Part V

[Lesson](/documentation/tutorials/links/rules5/lesson)
[Images](/documentation/tutorials/links/rules5/images)
[Configuration](/documentation/tutorials/links/rules5/configuration)

In the previous examples of rules, I triggered rules to adjust format
parameters of links or data points based on their position (start, end,
chromosome) or y-value (for plots). In this example, I'll show how to trigger
rules based on values of format parameters. This may seem a little strange at
first, but trust me, it's useful!

The input data set for this example is a subset of segmental duplications.
I've formatted the links by randomly assigning one of the following formats to
the data lines

  * `color = red`
  * `color = blue`
  * `thickness = 5`

Here's an excerpt of the data file

    
    
    segdup00002 hs1 486 76975
    segdup00002 hs15 100263879 100338121
    segdup00011 hs1 71096 76975 thickness=5
    segdup00011 hs1 388076 393885 thickness=5
    ...
    segdup00062 hs1 120975 125718 color=blue
    segdup00062 hs1 220708073 220712741 color=blue
    segdup00071 hs1 129327 166636 color=red
    segdup00071 hs1 665046 702417 color=red
    ...
    

There are four kinds of links, therefore, those with: no additional format,
red color, blue color and thickness 5.

I'll show you how to write rules that adjust parameters of the links based on
these format parameters. Consider these two rules

    
    
    <rule>
    condition  = var(thickness) == 4
    condition  = rand() < 0.25
    thickness  = 10
    color      = green
    z          = 15
    </rule>
    
    <rule>
    condition  = var(color) eq "red"
    thickness  = 4
    z          = 10
    flow       = restart
    </rule>
    
    <rule>
    condition  = var(color) ne "grey" && var(thickness) == 2
    z          = 5
    </rule>
    

The first rule applies to any links with a thickness of 4 red and assigns them
a thickness of 10, colors them green and sets their z-depth to 15. The second
condition applies the rule to only 25% of these links, since the value of
`rand()` is smaller than 0.25 this fraction of the time.

The next rule sets the thickness and z-depth of red links and then restarts
the rule chain. Thus, red links which are made thicker can be further modified
by the first rule, on the second loop through the rule chain. A rule can
restart the rule chain only once in order to avoid an endless loop.

The final rule sets the z-depth of any non-grey links whose thickness is 2.

