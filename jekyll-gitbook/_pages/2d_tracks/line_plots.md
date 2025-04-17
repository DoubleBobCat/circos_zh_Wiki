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

## 2\. Line Plots

[Lesson](/documentation/tutorials/2d_tracks/line_plots/lesson)
[Images](/documentation/tutorials/2d_tracks/line_plots/images)
[Configuration](/documentation/tutorials/2d_tracks/line_plots/configuration)

The line plot differs from the scatter plot in that there are no glyphs drawn
at each point position. Rather the points are joined by a line.

The line plot is formatted very similarly to the scatter plot, with the
following differences.

  * `type=line`
  * no glyphs - there are no glyph parameters - glyph and glyph_size do not apply. 
  * `stroke_thickness` and `stroke_color` are replaced by `thickness` and `color`, since the line isn't really outlined 
  * adjacent points whose distance is greater than `max_gap` are not joined by a line - this is useful to avoid drawing lines across large gaps (e.g. centromere) in data 

Points that fall outside of the `min/max` data range are placed at the
`min/max` extremes. Thus, if you have many adjacent points that fall outside
the data range the connecting line may run along the bottom or top of the plot
track.

If you want to explicitly remove these points from the data set, use a rule
that sets `show=no`. For example, if your `min/max` values are 0/0.5, then
this rule set will remove points falling outside the range from influencing
how the connecting line is drawn.

    
    
    <rules>
    <rule>
    condition  = var(value) < 0 || var(value) > 0.5
    show       = no
    </rule>
    </rules>
    

