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

## 6\. Manipulating Histograms

[Lesson](/documentation/tutorials/recipes/complex_histograms/lesson)
[Images](/documentation/tutorials/recipes/complex_histograms/images)
[Configuration](/documentation/tutorials/recipes/complex_histograms/configuration)

### mapping value to histogram fill

The fill of histogram bins can be changed based on the histogram bin value
using a rule like the following.

    
    
    # remap the histogram value from the range [-0.6,0.6] onto the index [0,5], then
    # use the index to select the color from the list
    # dorange orange lorange lblue blue dblue
    # 
    # Perl syntax for referencing an element of a list is qw(a b c d)[index]
    # where index starts at 0.
    <rule>
    condition  = 1
    fill_color = eval(qw(dorange orange lorange lblue blue dblue)[remap_int(var(value),-0.6,0.6,0,5)])
    </rule>
    

### layered background color and macros

Recall that you can use `conf()` to reference a configuration parameter. This
is described in detail in the [Automation and Macros
tutorial](//documentation/tutorials/quick_start/automation_and_macros).

In this example, I create a background for the histogram track that has six
colored layers: tones of blue for positive values and tones of orange for
negative values. Both cutoffs for the layers and colors will be defined as
parameters within the <plot> block.

Each separate colored layer in the background is defined by its own
<background> block.

    
    
    <plot>
    ...
    # define background color cutoffs
    bgy1 = 0.2    # first cutoff
    bgy2 = 0.5    # second cutoff
    bgc1 = orange # bg color for negative values
    bgc2 = blue   # bg color for positive values
    ...
    
    <backgrounds>
    # use the parameters above using conf(.,param)
    <background>
    color = lconf(.,bgc2)
    y0    = conf(.,bgy2)
    </background>
    <background>
    color = vlconf(.,bgc2)
    y1    = conf(.,bgy2)
    y0    = conf(.,bgy1)
    </background>
    <background>
    color = vvlconf(.,bgc2)
    y1    = conf(.,bgy1)
    y0    = 0
    </background>
    <background>
    color = vvlconf(.,bgc1)
    y1    = 0
    y0    = -conf(.,bgy1)
    </background>
    <background>
    color = vlconf(.,bgc1)
    y1    = -conf(.,bgy1)
    y0    = -conf(.,bgy2)
    </background>
    <background>
    color = lconf(.,bgc1)
    y1    = -conf(.,bgy2)
    </background>
    </backgrounds>
    
    </plot>
    

### y-axis grid and macros

The axis grid can also reference the histogram cutoff values.

    
    
    <axes>
    
    # every 25% with low transparency
    <axis>
    color     = grey_a1
    thickness = 2
    spacing   = 0.25r
    
    # every 5% with higher transparency
    <axis>
    color     = grey_a3
    thickness = 1
    spacing   = 0.05r
    </axis>
    
    # thick line at y=0
    <axis>
    color     = grey_a1
    thickness = 5
    position  = 0
    </axis>
    
    # at each background cutoff, a thick white line
    <axis>
    color     = white
    thickness = 5
    position  = -conf(.,bgy2),-conf(.,bgy1),conf(.,bgy1),conf(.,bgy2)
    </axis>
    
    </axes>
    

