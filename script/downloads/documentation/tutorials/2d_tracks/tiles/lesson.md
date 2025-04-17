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

## 4\. Tiles

[Lesson](/documentation/tutorials/2d_tracks/tiles/lesson)
[Images](/documentation/tutorials/2d_tracks/tiles/images)
[Configuration](/documentation/tutorials/2d_tracks/tiles/configuration)

Tile tracks are used to show spans such as genomic regions (genes, exons,
duplications) or coverage elements (clones, sequence reads). Tiles will stack
within their track to avoid overlap. The stacking process is controlled by
several parameters, which are the topic of this example.

The image for this example has 5 different tile tracks. From outside in, these
are: assembly clones (black/red), gene regions (green), copy-number
polymorphism regions (blue), segmental duplications (orange) and conservation
regions (purple). Each track is formatted slightly differently to illustrate
various formatting options.

### how tiles stack

Tiles are stacked in layers, which are annuli within the tile track. The
parameters that define the tile track position, layers and direction of
stacking are (in the case of the assembly track for this example)

    
    
    r1 = 0.98r
    r0 = 0.86r
    
    layers      = 15
    margin      = 0.02u
    orientation = out
    
    thickness   = 15
    padding     = 8
    

This track is placed within the radial extent defined by `[0.86r,0.98r]`
(these are radial values relative to the inner ideogram radius). The `r0/r1`
values define the baseline from which the tiles are stacked.

When `orientation=out`, tiles stack from `r0` out towards `r1`. When
`orientation=in`, tiles stack from `r1` in towards `r0`. When
`orientation=center`, tiles stack from the midpoint between `r0/r1` in an
alternating fashion towards `r0` and `r1`.

Each tile element has a radial width of 15 pixels with 8 pixels of padding
between elements.

Tiles will stack in layers to avoid overlap and each tile is given a margin to
control the distance of neighbouring tiles within the same layer.

The full extent of tile elements is defined by the layers parameter. In this
case, there are 15 layers that are allowed. The value of `layers_overflow`
controls what happens when additional layers are needed to accomodate tiles.
It's important to realize that it is the layers parameter that controls the
radial extent of the track, and not the `r0/r1` values. The radius `r0/r1`
values are used to define the baselines of the track whereas the combination
of `layers/thickness/padding` controls how far in the image the tiles stack.

The illustrations associated with this example explain the tile stacking
process.

### handling overflow

When tiles cannot fit into the number of layers you have specified using
`layers`, Circos looks to `layers_overflow` to determine how to handle the
overflow tiles.

When `layers_overflow=hide`, overflow tiles are not drawn. Use this setting
for the overflow option with caution, since Circos will not alert you to the
fact that not all of your tiles are drawn.

When `layers_overflow=collapse`, overflow tiles are drawn on the first layer.
The position of the first layer depends on the track orientation.

When `layers_overflow=grow`, new layers are added as required. There is no
limit to how many layers may be added.

To help inform you that overflow actions have been taken, you may set the fill
color of overflow tiles to a specific color using `layers_overflow_color`. If
you set this value to be different than the tiles' default color, overflow
tiles will be obvious.

Several images in this example show how overflow can be handled.

### applying rules

Rules apply to tiles just like for other data points. For example, you may
format tile color by its size.

    
    
    <rules>
    <rule>
    condition  = var(size) > 100kb
    color      = red
    </rule>
    
    <rule>
    condition  = var(size) > 50kb
    color      = orange
    </rule>
    
    <rule>
    condition  = var(size) > 20kb
    color      = yellow
    </rule>
    

