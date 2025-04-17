---
author: DoubleCat
date: 2025-04-11
layout: post
category: image_maps
title: Image Maps
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

# 11 — Image Maps

## 4\. Clickable Highlights and Data

[Lesson](/documentation/tutorials/image_maps/highlights_data/lesson)
[Images](/documentation/tutorials/image_maps/highlights_data/images)
[Configuration](/documentation/tutorials/image_maps/highlights_data/configuration)

In addition to ideograms, bands and ticks, data elements such as highlights,
scatter plots, histograms, text and ribbons can be associated with a link. The
mechanism very similar to that of ideograms and bands.

### defining url elements for highlights, plots and links

To associate an element with a URL, define a url parameter in its block. Here
are some examples

    
    
    <highlights>
    
    <highlight>
    ...
    url              = script?type=highlight&start=[start]&end=[end]&chr=[chr]
    </highlight>
    
    </highlights>
    
    <plots>
    
    <plot>
    ...
    url              = script?type=plot&start=[start]&end=[end]
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    ...
    url              = script?type=ribbon&start=[start]&end=[end]
    </link>
    
    </links>
    

As soon as the url parameter is defined in a block, all data points (or
ribbons or highlights) for that block have links. You can use the following
parameters

  * chr 
  * start 
  * start1 (ribbons) 
  * start2 (ribbons) 
  * end 
  * end1 (ribbons) 
  * end2 (ribbons) 
  * size1 (ribbons) 
  * size2 (ribbons) 
  * color 
  * fill_color 
  * stroke_color 
  * stroke_thickness 
  * glyph (scatter) 
  * glyph_size (scatter) 
  * value (scatter, histogram, heatmap, text) 
  * id (for data points that have this element defined in the input file) 

The example image in this tutorial shows a an image with many types of
elements, each with its own url definition. Notice that for places where link
areas overlap, the element that was drawn last is the one that responds to
clicking.

### using rules to adjust URLs

Rules can be used to adjust the `url` parameter. This works in the same manner
as for any other adjustable parameter.

    
    
    <plot>
    type = text
    ...
    <rules>
    <rule>
    # any label that contains M will have a different URL
    condition  = var(value) =~ /M/
    url        = special?label=[label]
    </rule>
    </rules>
    </plot>
    

