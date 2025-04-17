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

## 11\. Heat Map Links

[Lesson](/documentation/tutorials/recipes/heatmap_links/lesson)
[Images](/documentation/tutorials/recipes/heatmap_links/images)
[Configuration](/documentation/tutorials/recipes/heatmap_links/configuration)

You can color links by an associated value to create a heatmap effect.

Heatmaps were discussed in [2d Tracks—Heatmap
tutorial](//documentation/tutorials/2d_tracks/heatmaps).

### assigning value to links

At this time there is no way to associate a value with a link in the same way.
However, you can subvert one of the link parameters to do so. For example, use
a `value` parameter.

    
    
    hs12 117427133 132349534 hs2 94056542 114056542 value=2
    hs22 33232924 49691432 hs4 88399610 108399610 value=5
    

### coloring links by value

Now that each link has a value, it's time to use it to set its color. Rules
are used for this.

To reference the link's value, use `var(value)`.

The first rule maps the "url" value onto a list of colors. In this example,
the "url" value is in the range [0,4]. To map the value to a color, you will
need to use an eval() block and write a Perl one-liner to sample a list. If
the list contains entries that do not have a space (e.g. single word colors),
you can use the qw() operator which turns words into a list.

    
    
    qw(red orange green blue purple)
    

Perl's syntax to sample an element of a list is

    
    
    ( ...list here...)[i]
    

Combining these

    
    
    (qw(red orange green blue purple))[i]
    

In this case the value of `i` is the `value` parameter, reference by
`var(value)`.

    
    
    <rules>
    
    <rule>
    # always trigger this rule
    condition  = 1
    # use the link's value to sample from a list of colors
    color      = eval((qw(red orange green blue purple))[ var(value) ])
    # continue parsing other rules
    flow       = continue
    </rule>
    
    <rule>
    # always trigger this rule
    condition  = 1
    # add _a3 to the color of the ribbon, giving it 50% transparency (3/6)
    color      = eval(sprintf("%s_a3",var(color)))
    </rule>
    
    </rules>
    

