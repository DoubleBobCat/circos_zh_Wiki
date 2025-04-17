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

# 2 — Quick Start

## 3\. Ideogram Selection, Scale, Color & Orientation

[Lesson](/documentation/tutorials/quick_start/selection_and_scale/lesson)
[Images](/documentation/tutorials/quick_start/selection_and_scale/images)
[Configuration](/documentation/tutorials/quick_start/selection_and_scale/configuration)

In this section, we will adjust which chromosomes are drawn and change their
scale, color and orientation.

Getting the ideogram layout right is important. For example, making all
chromosomes appear to be the same size can emphasize the comparison between
relative positions in patterns.

### ideogram selection

The default behaviour is to display all chromosomes defined in the karyotype
file, in order of appearance.

To select a subset of chromosomes, set `chromosomes_display_default=no`

    
    
    chromosomes_display_default = no
    

and then use the `chromosomes` parameter to provide either a list

    
    
    chromosomes                 = hs1;hs2;hs3;h4
    

or regular expression in

    
    
    chromosomes                 = /hs[1-4]$/
    

to specify which chromosomes to show. You can combine these methods

    
    
    chromosomes                 = /hs[1-4]$/;hs10;hs11
    

and use `-` prefix to specify that you don't want a chromosome to be drawn

    
    
    chromosomes                 = /hs[1-4]$/;-hs3
    

Note that the list uses `;` as the delimiter. The reason why `,` is not used
is because the chromosome entry can include a list of chromosome regions to
draw, such as

    
    
    chromosomes                 = hs1:(-100,120-);hs2;hs3;h4
    

The regular expression can match a partial string, so don't forget to include
a trailing `$` anchor if you don't mean to match hs10,hs11,...

### ideogram scale

The size of the ideogram on the figure can be adjusted using an absolute or
relative magnification.

Absolute scale applies a fixed magnification to an ideogram

    
    
    # hs1 0.25x zoom
    # hs2 2.00x zoom
    chromosomes_scale   = hs1=0.25,hs2=2.0
    

Relative scale defines the size of the ideogram relative to image
circumference

    
    
    # hs1 25% of figure
    # hs2 50% of figure
    chromosomes_scale   = hs1=0.25r,hs2=0.50r
    

Normalized relative scale distributes several ideograms evenly within a
fraction of the figure.

    
    
    # hs1,hs2 distributed evenly within 50% of figure (each is 25%)
    chromosomes_scale   = /hs[12]/=0.5rn
    

A useful idiom is to select all ideograms and distribute them across entire
figure.

    
    
    # all ideograms distributed evenly within entire figure
    chromosomes_scale   = /./=1rn
    

### scale progression

By default, the scale progression is clockwise. You can set the global angle
progression using `angle_orientation` in the `<image>` block

    
    
    <image>
    # The * suffix is used to overwrite a parameter. In this case, the 
    # angle_orientation imported from etc/image is assigned a different value.
    angle_orientation* = counterclockwise
    <<include etc/image>>
    </image>
    

To reverse it for one or several ideograms, use `chromosomes-reverse`

    
    
    chromosomes_reverse = /hs[234]/
    

In this case the regular expression did not require a trailing `$` because it
applies only to those chromosomes that are displayed. Thus, even though
`/hs[234]/` does match `hs20`, it does not matter because this chromosome is
not shown.

### ideogram color

The color of each ideogram is taken from the karyotype file. To change it, use
`chromosomes_color`

    
    
    chromosomes_color   = hs1=red,hs2=orange,hs3=green,hs4=blue
    

### ideogram radial position

By default, all ideograms are placed at the same radial position, as defined
by the `radius` parameter in the `<ideogram>` block. You can selectively move
one or more of the ideograms radially by definining a new radial position
using `chromosomes_radius`.

Probably the most convenient way to do this is to use relative coordinates
(`r` suffix), which are interpreted relative to the default ideogram radius.
For example,

    
    
    chromosomes_radius  = hs4:0.9r
    

would place chromosome 4 at `0.9x` the radius of all other chromosomes.

