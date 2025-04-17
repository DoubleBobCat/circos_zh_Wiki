---
author: DoubleCat
date: 2025-04-11
layout: post
category: scaling
title: Axis Scaling
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

# 8 — Axis Scaling

## 4\. Creating Zoomed Regions

[Lesson](/documentation/tutorials/scaling/zooming/lesson)
[Images](/documentation/tutorials/scaling/zooming/images)
[Configuration](/documentation/tutorials/scaling/zooming/configuration)

Local scale adjustment is one of the coolest features of Circos. In the first
two examples in this tutorial section you saw how to adjust local scale by
splitting a chromosome into multiple ideograms and assigning each ideogram a
different scale value. This worked, but required that you create multiple
ideograms. Sometimes this is the right approach, especially if you need to
both crop and zoom your data domain.

Local adjustment of scale is for cases when you want to zoom parts of your
data domain without cropping. If you think of the ideogram as a rubber band,
applying a local scale adjustment is analogous to locally stretching or
compressing the rubber band. The effect is that you still see the entire
rubber band, but the length scale across it is variable.

You can adjust length scale locally by using the <zooms> block. For example,

    
    
    <zooms>
     <zoom>
     chr = hs1
     start = 100u
     end   = 120u
     scale = 5
     </zoom>
     <zoom>
     chr = hs1
     start = 120u
     end   = 130u
     scale = 10
     </zoom>
    </zoom>
    

will locally stretch the region 100-120Mb of hs1 by 5x and the region
120-130Mb of hs1 by 10x. Remember that the "u" is a unit designation that
specifies the value to be in units of the value of chromosomes_units, which I
set to 1,000,000.

Notice that zoom definitions are independent of the "chromosomes" and
"chromosomes_breaks" parameters. In effect, you define length scales for
regions independently of the definition of which regions to draw. Obviouly,
zoom settings will only have an effect on your image if they apply to regions
of the genome that are drawn.

In this example, I have defined several zoom regions on hs1 and hs2. On hs1
the scale is increased, zooming into a part of the chromosome. On hs2 the
scale is decreased, collapsing certain regions. I've added a heatmap to the
image to help see the regions that are affected.

Both ideograms in the image in this example are internally demarcated into
regions with the following scale.

    
    
                                      START       END
    zoomregion ideogram 0 chr hs1         0  99999999 scale  1.00 absolutescale  1.00
    zoomregion ideogram 0 chr hs1  99999999 119999999 scale  2.00 absolutescale  2.00
    zoomregion ideogram 0 chr hs1 119999999 129999999 scale  3.00 absolutescale  3.00
    zoomregion ideogram 0 chr hs1 129999999 139999999 scale  5.00 absolutescale  5.00
    zoomregion ideogram 0 chr hs1 139999999 142500001 scale 10.00 absolutescale 10.00
    zoomregion ideogram 0 chr hs1 142500001 247249719 scale  1.00 absolutescale  1.00
    zoomregion ideogram 1 chr hs2         0  99999999 scale  1.00 absolutescale  1.00
    zoomregion ideogram 1 chr hs2  99999999 119999999 scale  0.50 absolutescale  2.00
    zoomregion ideogram 1 chr hs2 119999999 139999999 scale  0.25 absolutescale  4.00
    zoomregion ideogram 1 chr hs2 139999999 160000001 scale  0.10 absolutescale 10.00
    zoomregion ideogram 1 chr hs2 160000001 180000001 scale  0.25 absolutescale  4.00
    zoomregion ideogram 1 chr hs2 180000001 200000001 scale  0.50 absolutescale  2.00
    zoomregion ideogram 1 chr hs2 200000001 242951149 scale  1.00 absolutescale  1.00
    

### defining zoomed regions

In this example the regions to which zooming was applied did not overlap (e.g.
100-120Mb, 120-140Mb, 140-160Mb, and so on). In the next example you'll see
what happens when you define overlapping regions with different zoom levels.
Hint: the largest absolute zoom wins.

