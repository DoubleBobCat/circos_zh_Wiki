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

## 14\. Directed Links

[Lesson](/documentation/tutorials/recipes/directed_links/lesson)
[Images](/documentation/tutorials/recipes/directed_links/images)
[Configuration](/documentation/tutorials/recipes/directed_links/configuration)

Circos draws links without orientation. To indicate the direction of the link,
you need to compose the link track with another track, which will provide an
indication of which end of the link is its end (or start, if you wish).

To do so, the best way is to use a scatter plot with a triangular glyph. The
glyph will act as a natural arrowhead at the end of the link.

To prepare your data, create a scatter plot data file that contains the
coordinates of the ends of the links. For example, if your links are

    
    
    hs1 102024400 102025440 hs3 111883743 111884767
    hs1 152617218 152618252 hs3 111883745 111884756
    hs1 158502674 158503718 hs3 111883744 111884768
    ...
    

the list of ends might be

    
    
    hs1 102024400 102025440 0
    hs1 152617218 152618252 0
    hs1 158502674 158503718 0
    ...
    

I've selected the second coordinate of the link as its end (arbitrarily, for
this example), and set the y-value of the associated data point to 0.

The scatter track that adds the arrow head would be defined like this

    
    
    <plots>
    
    <plot>
    
    type  = scatter
    file  = linkends.txt
    
    glyph      = triangle
    glyph_size = 24p
    
    min = 0
    max = 1
    r0  = 0.99r
    r1  = 0.99r
    
    fill_color = black
    
    <rules>
    
    <rule>
    condition  = 1
    fill_color = eval(lc "chr".substr(var(chr),2))
    </rule>
    
    </rules>
    
    </plot>
    
    </plots>
    

I've added a rule that colors the glyph by the color of the chromosome on
which it lies.

The scatter plot is placed at `radius=0.99r`, which is just before where the
links end, to seamlessly join the triangular glyphs to the link line.

You can use other tracks to indicate the end of the link, such as a highlight
track, to give the link a thicker base, or a text track (to give the end of
the link a name).

