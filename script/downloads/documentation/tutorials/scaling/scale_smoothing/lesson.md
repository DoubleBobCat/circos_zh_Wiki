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

## 6\. Smoothing Scale

[Lesson](/documentation/tutorials/scaling/scale_smoothing/lesson)
[Images](/documentation/tutorials/scaling/scale_smoothing/images)
[Configuration](/documentation/tutorials/scaling/scale_smoothing/configuration)

In the last example, I created a series of regions with gradually
increasing/decreasing scale in order to avoid large changes in scale over
short distances.

To automate scale smoothing, each zoom block supports a smooth_distance and
smooth_steps parameters. When using the smoothing feature, you define the zoom
setting for your region of interest and then the number of smoothing steps and
distance over which the scale smoothing is applied. Flanks around your zoomed
region will have their scale progressively grow/shrink from the scale of your
zoomed region to 1.

    
    
    <zoom>
    chr    = hs1
    start  = 120u
    end    = 125u
    scale  = 10
    smooth_distance = 2r
    smooth_steps    = 10
    </zoom>
    

In this block, I define a 5Mb region on chromosome 1 that is expanded to 10x
scale. The smoothing distance is 2r = 10Mb (here the "r" is relative to the
size of the zoomed region) and smoothing is applied over 10 steps. Each
smoothing step is 10Mb/10 = 1Mb and the scale decreases linearly across the
smoothing regions.

You can define the smooth_distance parameter in relative units (r), chromosome
units (u) or bases (b).

