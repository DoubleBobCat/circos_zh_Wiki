---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Links and Relationships
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

# 6 — Links and Relationships

## 1\. Drawing Basic Links

[Lesson](/documentation/tutorials/links/basic_links/lesson)
[Images](/documentation/tutorials/links/basic_links/images)
[Configuration](/documentation/tutorials/links/basic_links/configuration)

One of the core uses of Circos is to show the relationships between positions
on axes. Axes might be chromosomes and might indicate translocations. Or the
axes could be categories or entities (e.g. countries) and indicate some
relationship between them, such as migration of people.

A lot of the syntax for defining parameters that control how links are defined
carry over directly from the syntax for highlights.

### <links> block

All link data sets are defined within the <links> block. Typically this block
contains global parameter settings in its root - these values become the
default values for all link data.

Individual link data sets are defined within <link> blocks.

    
    
    <links>
    
     # global parameters here
    
     <link>
     ...
     </link>
    
     <link>
     ...
     </link>
    
    </links>
    

### data format

Link data files are composed of position pairs defined on one line.

    
    
    ...
    hs1 100 200 hs2 250 300
    hs1 400 550 hs3 500 750
    hs1 600 800 hs4 150 350
    ...
    

#### two-line format

Links may also be defined across two lines. The lines are associated together
using a link `id`, which is unique for each pair. You must also have exactly
two lines for each link `id`.

    
    
    ...
    segdup00010 hs1 100 200 
    segdup00010 hs2 250 300
    segdup00011 hs1 400 550
    segdup00011 hs3 500 750
    segdup00012 hs1 600 800
    segdup00012 hs4 150 350
    ...
    

The two-line format is deprecated and may not be supported in future versions.

#### link options

As with highlights, you can add an optional field to specify link-specific
options.

    
    
    ...
    hs1 100 200 hs2 250 300 color=blue
    hs1 400 550 hs3 500 750 color=red,thickness=5p
    hs1 600 800 hs4 150 350 color=black
    ...
    

### example

In this example, I draw data from a file of coordinates defined by segmental
duplications. Each coordinate pair defines two regions of the genome that are
defined as segmental duplications (>1kb in length, >90% similarity).

    
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    color         = black_a5
    radius        = 0.95r
    bezier_radius = 0.1r
    thickness     = 1
    </link>
    
    </links>
    
    

#### links with custom karyotype files

If you need to draw links on segments for which the karyotype is not available
— when the segments are not chromosomes from a common species — you'll need to
[create your own karyotype
file](/documentation/tutorials/ideograms/karyotype).

For example, if you had 3 contigs of size 1000, 1500 and 2500 bp, you might
create this file

    
    
    # karyotype.txt
    chr - contig1 1 0 1000 black
    chr - contig2 2 0 1500 blue
    chr - contig3 3 0 2500 red
    

and in `circos.conf` use

    
    
    karyotype = karyotype.txt
    

Your link file might look like this

    
    
    contig1 10 20 contig2 500 520 
    contig3 50 80 contig3 750 760
    ...
    

Here the first link defines connections between `contig1:10-20` and
`contig2:500-520` and the second between `contig3:50-80` and
`contig3:750-760`.

#### link parameters

The basic parameters for links are

  * `radius` — this is the radial position of the termination of the link; for relative values, if `radius` < 1 then it is defined in terms of the inner ideogram radius, otherwise it is defined in terms of the outer ideogram radius 
  * `bezier_radius` — the radial position of the third control point (in addition to the two positions defined by the link coordinates) used to draw the Bezier curve; if this parameter is not defined then straight lines will be used 
  * `color` — color of the link line 
  * `thickness` — thickness of the link line (note that this is not stroke_thickness, since the line isn't technically stroked) 
  * `record_limit` — if this is defined, the number of records read from the file is capped; coordinate records are sampled from the start of the file; useful for debugging 

### link defaults

All track types have default values. For links, these are

    
    
    ribbon           = no
    color            = black
    thickness        = 1
    radius           = 0.40r
    bezier_radius    = 0r
    crest                = 0.5
    bezier_radius_purity = 0.75
    

and loaded from `etc/tracks/link.conf` in the Circos distribution. This file
is set by the `track_defaults` parameter, which is set normally in
`etc/housekeeping.conf`. You can override defaults by setting the parameter to
`undef`

    
    
    <link>
     ...
     crest = undef
     ...
    </link>
    

or undefining `track_defaults`

    
    
    <<include etc/housekeeping.conf>>
    track_defaults* = undef
    

Note that the `*` syntax is required because you are overriding a parameter
which is already defined at the same level in the configuration file.

### bezier curves

Links can be drawn as straight lines or as [quadratic Bezier
curves](https://en.wikipedia.org/wiki/B%C3%A9zier_curve).

For the latter, the start `p1` and end `p3` control points are defined by the
coordinate positions (angularly) and the radius parameter (radially). The
middle control point `p2` is defined by the mid point between the coordinates
(angularly) and `bezier_radius` parameter (radially).

The Bezier curve is drawn to have its tangent at `p1` defined by the line
`p1-p2` and at `p3` defined by the line `p2-p3` (see the image associated with
this tutorial).

