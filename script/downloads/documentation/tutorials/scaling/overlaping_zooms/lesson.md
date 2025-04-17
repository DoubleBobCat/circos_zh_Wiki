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

## 5\. Overlapping Zoomed Regions

[Lesson](/documentation/tutorials/scaling/overlaping_zooms/lesson)
[Images](/documentation/tutorials/scaling/overlaping_zooms/images)
[Configuration](/documentation/tutorials/scaling/overlaping_zooms/configuration)

When overlapping zoom regions are defined, the zoom level at an ideogram
position is taken to be the highest (in absolute terms) zoom of any
overlapping regions.

For example, if you define the following regions

    
    
    100-200Mb - 2x
    150-180Mb - 3x
    160-170Mb - 5x
    

then the net effect will be as if you defined

    
    
    100-150Mb - 2x
    150-160Mb - 3x
    160-170Mb - 5x
    170-180Mb - 3x
    180-200Mb - 2x
    

The zoom precedence is defined by the absolute zoom level, which is taken to
be max(scale,1/scale) For example, a scale of 0.1 (absolute zoom = 1/0.1 =
10x) overrides any zoom setting with an absolute zoom level smaller than 10x.

