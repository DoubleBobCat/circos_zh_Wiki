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

## 16\. Automating Heatmaps

[Lesson](/documentation/tutorials/recipes/automating_heatmaps/lesson)
[Images](/documentation/tutorials/recipes/automating_heatmaps/images)
[Configuration](/documentation/tutorials/recipes/automating_heatmaps/configuration)

Before reading this tutorial, make sure that you understand how dynamic
configuration parameters work (see [Configuration Files
Tutorial](/documentation/tutorials/configuration/configuration_files/)) and
have read through the [Automating Tracks
Tutorial](/documentation/tutorials/recipes/automating_tracks/).

For this tutorial, I have created an image with 100 heat map tracks. The data
for these tracks are gene densities computed across differently sized windows
(0.5-50 Mb). The higest resolution file is `data/8/17/genes.0.txt` which
samples density every 500kb. The lowest resolution file is
`data/8/17/genes.99.txt` which samples density every 50,000kb (1/100th
resolution of `genes.0.txt`).

The gene densities were designed so that each heat map interval occupies the
same number of pixels along the map's circumference.

### changing heat map color

The color of the heat map is specified using a list of colors

    
    
    color = red,green,blue
    

or a color list

    
    
    color = spectral-11-div
    

For more about color lists, see the [Configuration Files
Tutorial](/documentation/tutorials/configuration/configuration_files/).

The track counter can be used to dynamically change the color scheme. For
example, as the track counter increases from 0 to 99, the definition

    
    
    color = eval(sprintf("spectral-%d-div",remap_round(counter(plot),0,99,11,3)))
    

will assign a list to a track based on the counter. The assignment will range
from `spectral-11-div` for the outer-most track, progressing through
`spectral-10-div`, ..., and end at `spectral-3-div` for the inner-most track.

You can combine multiple color maps. Here, an orange sequential color list is
added to a reversed blue sequential one.

    
    
    color = eval(sprintf("blues-%d-seq-rev,oranges-%d-seq-rev",
                         remap_round(counter(plot),0,99,9,3),
                         remap_round(counter(plot),0,99,9,3)))
    

Given the reduced resolution of the inner-most track, reducing the number of
colors in its heat map can make the figure more legible.

### adjusting log scaling

The `scale_log_base` parameter controls how heat map values are mapped onto
colors. The default value of this parameter is `scale_log_base = 1`, which
corresponds to a linear mapping. For more details about this parameter, see
the [Heat Map Tutorial](/documentation/tutorials/2d_tracks/heat_maps/).

Keeping the color list constant, but varying the `scale_log_base`, you can
increase the dynamic range of color sampling for small values (if
`log_scale_base < 1`) or large values (if `log_scale_base > 1`).

    
    
    color          = spectral-11-div
    # 0.05, 0.10, 0.15, ..., 5.00
    scale_log_base = eval(0.05*(1+counter(plot)))
    

