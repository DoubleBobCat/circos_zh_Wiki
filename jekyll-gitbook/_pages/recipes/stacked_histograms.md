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

## 8\. Stacked Histograms

[Lesson](/documentation/tutorials/recipes/stacked_histograms/lesson)
[Images](/documentation/tutorials/recipes/stacked_histograms/images)
[Configuration](/documentation/tutorials/recipes/stacked_histograms/configuration)

### stacking data sets

Stacked histograms are an extenstion of the histogram track. To plot stacked
histograms, the only adjustment you require is to provide a series of values
for each histogram bin in your data file.

For example, here is a part of a data file for a stacked histogram in which 5
data sets are stacked.

    
    
    ...
    hs7 65000000 69999999 0.388090,0.070074,0.547485,0.842239,0.525658
    hs7 70000000 74999999 0.886542,0.321023,0.145677,0.897684,0.264217
    hs7 75000000 79999999 0.854199,0.567889,0.574767,0.656331,0.418385
    hs7 80000000 84999999 0.286509,0.201049,0.552485,0.876529,0.999801
    hs7 85000000 89999999 0.154836,0.515471,0.389453,0.440168,0.475127
    ...
    

The first value will appear at the bottom of the bin's stack, then the second,
then third, and so on.

### formatting stacked data sets

Individual format parameters (`color`, `thickness` `fill_color`, `pattern`)
for each data sets can be specified by providing a list of comma-separated
values.

For example, to make each data set filled with a different color, provide five
different values for `fill_color`.

    
    
    fill_color = red,orange,yellow,green,blue
    

If you provide parameter values than data sets, they will be cycled.

Assigning individual values for color and thickness can produce useful
displays, particularly when `color=white` and `thickness` is varied.

    
    
    color      = white
    fill_color = red,orange,yellow,green,blue
    fill_under = yes
    thickness  = 1,2,3,4,5
    

### colors and patterns

You can independently cycle bins' color and pattern.

    
    
    fill_color = red,grey,black
    pattern    = checker,solid
    

will create the following bins

    
    
      color  pattern
      red    checker
      grey   solid
      black  checker
      red    solid
      grey   checker
      black  solid
      ...    ...
    

### adjusting stack order

By default, the bins are stacked in order of appearance of their values in the
data file. Thus, given the colors

    
    
    fill_color = red,orange,yellow,green,blue
    

the data line

    
    
    hs1 0 4999999 0.237788,0.291066,0.845814,0.152208,0.585537
    

the bins will stack in the following order

  * 0.237788 (red) 
  * 0.291066 (orange) 
  * 0.845814 (yellow) 
  * 0.152208 (green) 
  * 0.585537 (blue) 

However, when

    
    
    sort_bin_values = yes
    

is used, the bins will be stacked by decreasing value

  * 0.845814 (yellow) 
  * 0.585537 (blue) 
  * 0.291066 (orange) 
  * 0.237788 (red) 
  * 0.152208 (green) 

