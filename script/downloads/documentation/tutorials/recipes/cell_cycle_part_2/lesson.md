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

## 21\. Cell Cycle — Part 2

[Lesson](/documentation/tutorials/recipes/cell_cycle_part_2/lesson)
[Images](/documentation/tutorials/recipes/cell_cycle_part_2/images)
[Configuration](/documentation/tutorials/recipes/cell_cycle_part_2/configuration)

This tutorial will show you how to use Circos to create a diagram of a
[typical cell cycle](https://en.wikipedia.org/wiki/Cell_cycle) (G1, S, G2, M)
and annotate it with links and text.

This is the second part of the tutorial, continuing from [Cell Cycle — Part
1](/documentation/tutorials/recipes/cell_cycle_part_1).

This tutorial shows a more advanced way to define the phase axes. Depending on
how you wish to define your coordinate system (e.g. relative to cycle, not
phase), the approach taken by this tutorial may be more helpful.

In general, this tutorial should be of interest to anyone who wishes to use
Circos for display of data that is not based on sequence coordinates.

### cycle segment

There are four phases in the cell cycle: gap 1 (G1), synthesis (S), gap 2 (G2)
and mitosis (M). There's also a senescence phase (gap 0, G0), into which the
cell can pass to/from G1. I'll ignore G0 in this example.

Instead of defining one axis per phase, like in [Cell Cycle — Part
1](/documentation/tutorials/recipes/cell_cycle_part_1), I will create an axis
segment for the whole cycle.

    
    
    # cycle.txt
    chr - cycle cycle 0 100 greys-6-seq-5
    

### phases as cycle segment ideograms — using cropping

Each phase will be defined as a cropped region of the cycle axis.

    
    
    karyotype   = cycle.txt
    chromosomes = cycle[g1]:0-45;cycle[s]:45-80;cycle[g2]:80-95;cycle[m]:95-100
    

The spacing between the cropped regions is defined by the `break` parameter in
<spacing> block

    
    
    <ideogram>
    <spacing>
    default = 0.005r
    break   = 1r
    </spacing>
    </ideogram>
    

### segment colors

Colors are defined in the same way as [Cell Cycle — Part
1](/documentation/tutorials/recipes/cell_cycle_part_1), except now the
arguments to `chromosomes_color` are the ideogram tags, not axis names.

    
    
    palette  = greys-6-seq
    <phases>
    g1 = 3
    s  = 4
    g2 = 5
    m  = 6
    </phases>
    # g1, s, g2, m are tags defined in 'chromosomes' above
    chromosomes_color = g1=conf(palette)-conf(phases,g1),
                        s=conf(palette)-conf(phases,s),
                        g2=conf(palette)-conf(phases,g2),
                        m=conf(palette)-conf(phases,m)
    

### tick marks

There are two options in this tutorial for tick marks.

The `ticks.absolute.conf` file defines them across the full cycle (e.g. first
tick on G2 is 80%). Nothing special needs to be done in this case, because
ticks are automatically generated relative to the original axis segment, and
not to any cropped regions. The tick labels will run from the start of the
segment (position 0 on `cycle` axis) to the end (position 100 on `cycle`
axis).

The `ticks.relative.conf` defines them relative to each ideogram (e.g. first
tick on G2 is 0%). The definition is almost identical to that of [Cell Cycle —
Part 1](/documentation/tutorials/recipes/cell_cycle_part_1) except for the
`rdivisor = ideogram` parameter, which tells Circos to label the ticks
relative to their position on the cropped ideogram and not on the underlying
axis segment.

