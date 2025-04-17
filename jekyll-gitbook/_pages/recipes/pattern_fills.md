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

## 15\. Pattern Fills

[Lesson](/documentation/tutorials/recipes/pattern_fills/lesson)
[Images](/documentation/tutorials/recipes/pattern_fills/images)
[Configuration](/documentation/tutorials/recipes/pattern_fills/configuration)

Ribbons, heatmaps and histograms can be drawn with a pattern fill by setting
the `pattern` parameter.

    
    
    <link>
    ...
    ribbon = yes
    pattern = checker
    ...
    </link>
    

### Patterns

The following patterns are available

  * solid 
  * hline 
  * hline-sparse 
  * vline 
  * vline-sparse 
  * checker 
  * checker-sparse 
  * dot 
  * dot-sparse 

Like fonts, patterns are named in their own block and imported from another
configuration file. The file that defines patterns is `etc/patterns.conf`. The
bitmaps for the patterns are found in `etc/tiles`.

    
    
    # etc/pattern.conf
    vline        = tiles/vlines.png
    vline-sparse = tiles/vlines-sparse.png
    ...
    

The configuration file `etc/colors_fonts_patterns.conf` takes care of
importing all the pattern definitions.

    
    
    <<include etc/colors_fonts_patterns.conf>>
    

You can add your own patterns by creating a PNG file and adding it to the
pattern block. Use an 8-bit PNG. Transparency is not supported for tiles.

If you do not specify a color for a pattern (see below), the pattern will be
used as it appears in the PNG file, without any change in colors.

### Colored Patterns

A pattern's colors can be remapped using the color parameter. The predefined
patterns are black-on-white, but you can remap a pattern's color by defining a
list of `old:new` colors.

    
    
    color = white:red,black:orange
    

To invert a black and white pattern,

    
    
    color = white:black,black:white
    

To replace all the colors in a pattern that are not the same as the image's
background color, set the `color` value to a single word. For example, on an
image whose background is black

    
    
    color = red
    

will color all non-black pixels in the pattern red.

In this tutorial, the links originally are defined with a color.

    
    
    hs11 27363982 47363982 hs8 1 12346012 color=chr11
    hs11 113293528 133293528 hs21 24848956 44848956 color=chr11
    hs10 27542441 47542441 hs20 33053889 53053889 color=chr10
    

A rule is set up so that for 50% of the ribbons, a colored pattern is
selected.

For about 25% of the links, only a pattern is selected. Because each link
already has a color, the pattern is colored by the existing color (in this
case, chromosome color).

### Patterns with Transparency

This is not supported by GD. Regardless of whether your PNG file has
transparency or not, the tiled pattern will not have transparent components.

