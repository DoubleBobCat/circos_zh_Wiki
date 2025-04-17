---
author: DoubleCat
date: 2025-04-11
layout: post
category: highlights
title: Highlights
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

# 4 — Highlights

## 7\. Recipe 2 - Focusing on a Genome Region

[Lesson](/documentation/tutorials/highlights/recipe2/lesson)
[Images](/documentation/tutorials/highlights/recipe2/images)
[Configuration](/documentation/tutorials/highlights/recipe2/configuration)

In many of the examples in this series of tutorials, the highlights were used
to draw data sets, such as gene position. Highlights are very useful for
drawing data because you have a high degree of control in formatting each
highlight wedge.

In other cases, highlights are useful to help the eye focus on a part, or
parts, of your diagram.

All other data types, as well as tick mark grids, are placed on top of the
highlights.

### continuing with the chromosome color scheme

For the first image in this section, I've prepared two highlight files. The
first file, recapitulates the chromosome size and uses the chromosome color
scheme.

    
    
    hs1 0 247249719 fill_color=chr1
    hs2 0 242951149 fill_color=chr2
    hs3 0 199501827 fill_color=chr3
    hs4 0 191273063 fill_color=chr4
    hs5 0 180857866 fill_color=chr5
    hs6 0 170899992 fill_color=chr6
    hs7 0 158821424 fill_color=chr7
    hs8 0 146274826 fill_color=chr8
    hs9 0 140273252 fill_color=chr9
    hs10 0 135374737 fill_color=chr10
    hs11 0 134452384 fill_color=chr11
    hs12 0 132349534 fill_color=chr12
    hs13 0 114142980 fill_color=chr13
    hs14 0 106368585 fill_color=chr14
    hs15 0 100338915 fill_color=chr15
    hs16 0 88827254 fill_color=chr16
    hs17 0 78774742 fill_color=chr17
    hs18 0 76117153 fill_color=chr18
    hs19 0 63811651 fill_color=chr19
    hs20 0 62435964 fill_color=chr20
    hs21 0 46944323 fill_color=chr21
    hs22 0 49691432 fill_color=chr22
    hsX 0 154913754 fill_color=chrX
    hsY 0 57772954 fill_color=chrY
    

Using this file, I can recreate the ideogram size in chromosome-specific color
anywhere in the image. I've drawn two highlight tracks using this file.

The first track is drawn in side the circle from 0.5 to 1.0 times the inner
ideogram radius.

    
    
    <highlight>
    file       = data/3/chr.highlights.txt
    r0 = 0.5r
    r1 = 1r
    </highlight>
    

The second track is drawn outside the circle, and includes a black stroke.

    
    
    <highlight>
    file       = data/3/chr.highlights.txt
    stroke_thickness = 2
    stroke_color = black
    r0 = 1.1r
    r1 = 1.15r
    </highlight>
    

The second file stores the position of cytogenetic bands classified as
centromeres and stalks in the karyotype. This is a union of all coordinates
whose bands were labeled as acen or stalk.

    
    
    hs1 121100000 128000000
    hs10 38800000 42100000
    hs11 51400000 56400000
    hs12 33200000 36500000
    hs13 3800000 8300000
    hs13 13500000 18400000
    hs14 3100000 6700000
    hs14 13600000 19100000
    hs15 3500000 7900000
    hs15 14100000 18400000
    hs16 34400000 40700000
    hs17 22100000 23200000
    hs18 15400000 17300000
    hs19 26700000 30200000
    hs2 91000000 95700000
    hs20 25700000 28400000
    hs21 2900000 6300000
    hs21 10000000 13200000
    hs22 3000000 6600000
    hs22 9600000 16300000
    hs3 89400000 93200000
    hs4 48700000 52400000
    hs5 45800000 50500000
    hs6 58400000 63400000
    hs7 57400000 61100000
    hs8 43200000 48100000
    hs9 46700000 60300000
    hsX 56600000 65000000
    hsY 11200000 12500000
    

This set of highlights is drawn on top of the previous, outer track and filled
white, effectively splitting the highlights along centromeres and stalks.

    
    
    <highlight>
    file       = data/3/chr.hetero.highlights.txt
    stroke_thickness = 2
    stroke_color = black
    fill_color = white
    r0 = 1.1r
    r1 = 1.15r
    z = 10
    </highlight>
    

### focus on genomic regions

If you have a figure in which certain genomic areas are of interest,
highlights are the best way to guide your audience's eyes.

For this example, I've created a data file with just a few highlights.

    
    
    hs1 15000000 50000000
    hs2 100000000 150000000
    hs3 50000000 60000000
    hs3 80000000 90000000
    hs3 100000000 105000000
    hs14 0 106368585
    

Using this data set, I've drawn three sets of highlights that isolate these
regions. These are shown in the second image in this section. The first set of
highlights is light grey and spans 0.5r-1.0r radial region. These second falls
outside of the ideogram circle and is light yellow from 1.0r to 1.1r. The last
is light grey again from 1.1r to 1.15r.

Note that unless you are using ideogram highlights, Circos does not support
highlights that cross the circle of ideograms. I strongly advise against
setting r0<1 and r1>1 for a set of highlights :)

