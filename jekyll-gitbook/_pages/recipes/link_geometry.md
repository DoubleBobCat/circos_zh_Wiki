---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Link Geometry - Detailed Bezier Control
---

## Link Geometry - Detailed Bezier Control
### lesson
The raison d'etre of Circos is the ability to draw links. Links are covered in
tutorial 5. Link geometry is controlled by many parameters (see tutorial 5.2).

Below, I'll walk through some geometry recipes to help illustrate how the
parameters interact.

#### straight lines
To draw links with straight lines, keep bezier_radius undefined. Below I set
the link radius to be nearly at the inner ideogram radius (0.98r). I also hide
links associated with smaller segmental duplications (<1.5kb), set the
thickness based on the size of the segmental duplication (scaled exponentially
in the range 1-6), and color red those links that eminate from a region on
chromosome 2.

```    
    radius = 0.98r
    # comment out bezier_radius, or leave out
    #bezier_radius        = 0.9r
    
    <link segdup>
    color        = vdgrey
    thickness    = 2
    file         = data/5/segdup.txt
    </link>
    
    <rules>
    
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.75kb || _SIZE2_ < 1.75kb
    show       = no
    </rule>
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
``````
Notice that you can use common suffixes like kb and Mb to indicate a value
multiplier.

#### bezier curves
Straight lines are not always the best way to draw links, especially for links
that join two closely spaced points. The bezier_radius parameter, when
defined, controls the curvature of the line by establishing a third control
point of the line at an angle that bisects the position of the start and end
of the link.

The bezier_radius specifies the radius at this control point. Using the start
and end of the link, and the control point, a bezier curve is drawn. Note that
the bezier curve generally does not pass through the control point, but merely
comes close.

Thus, the larger the bezier radius, the greater the affinity of the middle of
the link line to the ideogram circle. A bezier_radius of zero, on the other
hand, will result in great affinity of each link to the center of the circle.

You generally will be setting the bezier_radius as a relative value. It will
be relative to the inner ideogram radius.

```    
    bezier_radius = 0.25r
```
You can set the bezier_radius to be negative, which will result in some weird
link layouts (the control point will be placed at the same radial position but
on the other side of the circle).

#### dynamically altering geometry parameters
You can use rules to adjust the bezier_radius. For example, links between
closely spaced points on the same ideogram should get a large bezier radius to
avoid the link from being drawn too far into the circle, only to double back
on itself. In the rule below, any intrachromosomal links with ends within 50Mb
will have a bezier_radius of 0.75r (vs all other links with bezier_radius of
0.5r, for example).

```    
    <rules>
    <rule>
    importance    = 95
    condition     = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 50Mb
    bezier_radius = 0.75r
    flow          = continue
    </rule>
    </rules>
```
You can also dynamically remap the bezier_radius using an eval() condition.
For example, the rule below will adjust it to range from 0.5r to 0.9r smoothly
(links 100Mb apart will have a bezier_radius of 0.5r which will increase to
0.9r as the link ends fall closer). The unit "r" has to be explicitly
concatenated onto the new bezier_radius in the eval() expression.

```    
    <rule>
    importance     = 95
    condition      = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 100Mb
    bezier_radius  = eval( (0.5 + 0.4*( 1 - abs(_START1_-_START2_) / 100Mb )) . "r" )
    flow           = continue
    </rule>
```
The choice of parameters in the rules (0.5, 0.4, and 100Mb) are arbitrary and
guided by desired esthetics of the final image.

#### making link ends perpendicular to ideograms
As you can see from the images in the previous examples, links with ends that
are far apart impinge on the ideogram at a shallow angle.

If you would like the link lines to be perpendicular to the ideogram,
additional curve control points are necessary. To do this, the crest parameter
is used to set two additional control points at the same angular position as
the link start and end, but at a radial position closer to the center of the
circle (see tutorial 5.2).

The crest parameter is automatically relative to the link radius and bezier
radius. When crest = 0 (no effect), the crest control point is at the same
radial position as the link start/end. When crest = 1, the control point is
placed at the bezier_radius (see [this
image](https://mk.bcgsc.ca/circos/tutorials/5/2/image-04.png) from tutorial
5.2).

#### isolating interchromosomal links
Rules make it easy to hide links that are do not fit a condition. For example,
to draw only interchromosomal links (between different chromosomes), hide all
intrachromosomal links

```    
    <rule>
    importance = 100
    condition  = _CHR1_ eq _CHR2_
    show       = no
    </rule>
```
You can deal with interchromosomal and intrachromosomal links separately by
either (a) setting up two tracks with two different hide rules (one track will
have interchromosomal links hidden, the other intrachromosomal links hidden)
or (b) setting up two sets of rules (one or more rules for interchromosomal
links and one or more rules for intrachromosomal links).

```    
    <rules>
    
    # intrachromosomal links with ends within 40 Mb placed outside circle
    
    <rule>
    importance = 90
    condition  = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 40Mb
    radius        = 1r+125p
    bezier_radius = 1r+225p
    crest         = 1
    color         = red
    </rule>
    
    # all other intrachromosomeal links hidden
    
    <rule>
    importance = 80
    condition  = _CHR1_ eq _CHR2_
    show       = no
    </rule>
    
    # interchromosomeal links involving start
    # of chromosome are inside circle
    
    <rule>
    importance = 70
    condition  = _CHR1_ ne _CHR2_ && (_START1_ < 20Mb || _START2_ < 20Mb)
    color      = black
    radius     = 0.99r
    bezier_radius = 0.5r
    crest         = 1
    </rule>
    
    # all remaining links are hidden
    
    <rule>
    importance = 10
    condition  = 1
    show       = no
    </rule>
    
    </rules>
``````
#### bulging links with bezier_radius and crest
Some combinations of bezier_radius and crest values result in links that
appear to bulge. That is, they run radially for quite a distance from the
ideograms and then swing around the center of the image.

For a given bezier_radius value, the crest value that generates this behaviour
is 1/(1-bezier_radius). For example, for a bezier_radius of 0.75r, a crest
value of 4 will yield bulging links. Crest values significantly larger than
this can create undesirable loops in the curves.

Large negative crest values produce links that look like the rings of Saturn.
Small negative crest values yield undulating links for links with closely
spaced ends.
### images
![Circos tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/01.png) ![Circos
tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/02.png) ![Circos
tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/03.png) ![Circos
tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/04.png) ![Circos
tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/05.png) ![Circos
tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/06.png) ![Circos
tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/07.png) ![Circos
tutorial image - Link Geometry - Detailed Bezier
Control](/documentation/tutorials/recipes/link_geometry/img/08.png)
### configuration
#### circos.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest         = 2.5
    bezier_radius = 0.5r
    
    <link segdup>
    show         = yes
    color        = grey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _CHR1_ eq _CHR2_ 
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && _CHR2_ eq "hs4" && abs(_START1_ - 90Mb) < 30Mb) || (_CHR2_ eq "hs2" && _CHR1_ eq "hs4" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    thickness  = eval(_thickness_*2)
    z          = 5
    
    crest         = 2
    bezier_radius = 0.5r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs3" && abs(_START1_ - 160Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs3" && abs(_START2_ - 160Mb) < 20Mb)
    color      = blue
    thickness  = eval(_thickness_*2)
    z          = 10
    crest         = 4
    bezier_radius = 0.75r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs2" && abs(_START1_ - 10Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs2" && abs(_START2_ - 10Mb) < 20Mb)
    color      = orange
    thickness  = eval(_thickness_*2)
    z          = 15
    crest         = 5
    bezier_radius = 0.8r
    
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### circos.image-01.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    #crest  = 0.25
    #bezier_radius        = 0.9r
    #bezier_radius_purity = 0.5
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    #record_limit = 500
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next rule must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the next color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### circos.image-02.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    #bezier_radius         = 0r
    #bezier_radius         = 0.25r
    bezier_radius         = 0.5r
    #bezier_radius         = 0.75r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next rule must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the next color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### circos.image-03.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    bezier_radius         = 0.5r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 95
    condition  = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 100Mb
    #bezier_radius = 0.75r
    bezier_radius = eval( (0.5 + 0.4*(1-abs(_START1_-_START2_) / 100Mb)) . "r")
    flow = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### circos.image-04.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest = 2.5
    bezier_radius         = 0.5r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _SIZE1_ < 1.5kb || _SIZE2_ < 1.5kb
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 95
    condition  = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 100Mb
    #bezier_radius = 0.75r
    bezier_radius = eval( (0.5 + 0.4*(1-abs(_START1_-_START2_) / 100Mb)) . "r")
    flow = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && abs(_START1_ - 100Mb) < 20Mb) || (_CHR2_ eq "hs2" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    </rule>
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### circos.image-05.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    
    # adjust thickness for all links
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    # closely spaced intrachromosomal links
    # go outside ideogram circle
    
    <rule>
    importance = 90
    condition  = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 40Mb
    radius        = 1r+125p
    bezier_radius = 1r+225p
    crest         = 1
    color         = red
    </rule>
    
    # all other intrachromosomeal links hidden
    
    <rule>
    importance = 80
    condition  = _CHR1_ eq _CHR2_
    show       = no
    </rule>
    
    # interchromosomeal links involving start
    # of chromosome are inside circle
    
    <rule>
    importance = 70
    condition  = _CHR1_ ne _CHR2_ && (_START1_ < 20Mb || _START2_ < 20Mb)
    color      = black
    radius     = 0.99r
    bezier_radius = 0.5r
    crest         = 1
    </rule>
    
    # all remaining links are hidden
    
    <rule>
    importance = 10
    condition  = 1
    show       = no
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### circos.image-06.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest = 2.5
    bezier_radius         = 0.5r
    
    <link segdup>
    show         = yes
    color        = vdgrey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _CHR1_ eq _CHR2_
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance    = 95
    condition     = _CHR1_ eq _CHR2_ && abs(_START1_-_START2_) < 100Mb
    bezier_radius = eval( (0.5 + 0.4*(1-abs(_START1_-_START2_) / 100Mb)) . "r")
    flow          = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && _CHR2_ eq "hs4" && abs(_START1_ - 90Mb) < 30Mb) || (_CHR2_ eq "hs2" && _CHR1_ eq "hs4" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    thickness  = eval(_thickness_*2)
    z          = 5
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs3" && abs(_START1_ - 160Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs3" && abs(_START2_ - 160Mb) < 20Mb)
    color      = blue
    thickness  = eval(_thickness_*2)
    z          = 10
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### circos.image-07.conf
```    
    <colors>
    <<include etc/colors.conf>>
    </colors>
    
    <fonts>
    <<include etc/fonts.conf>>
    </fonts>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype.human.txt
    
    <image>
    dir = /tmp
    file  = circos-tutorial.png
    # radius of inscribed circle in image
    radius         = 1500p
    background     = white
    # by default angle=0 is at 3 o'clock position
    angle_offset   = -90
    </image>
    
    chromosomes_units = 1000000
    chromosomes       = hs1;hs2;hs3;hs4
    chromosomes_display_default = no
    
    <links>
    
    radius = 0.98r
    
    crest         = 2.5
    bezier_radius = 0.5r
    
    <link segdup>
    show         = yes
    color        = grey
    thickness    = 2p
    file         = data/5/segdup.txt
    
    <rules>
    <rule>
    importance = 110
    condition  = _CHR1_ eq _CHR2_ 
    show       = no
    </rule>
    # the next two rules must contain flow=continue because it 
    # always matches and you do not want it to terminate
    # the rule chain (otherwise the color rule would
    # never be checked)
    <rule>
    importance = 100
    condition  = 1
    thickness  = eval(max(1,min(6,exp(_SIZE1_/50000))))
    flow       = continue
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs2" && _CHR2_ eq "hs4" && abs(_START1_ - 90Mb) < 30Mb) || (_CHR2_ eq "hs2" && _CHR1_ eq "hs4" && abs(_START2_ - 100Mb) < 20Mb)
    color      = red
    thickness  = eval(_thickness_*2)
    z          = 5
    
    crest         = 2
    bezier_radius = 0.5r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs3" && abs(_START1_ - 160Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs3" && abs(_START2_ - 160Mb) < 20Mb)
    color      = blue
    thickness  = eval(_thickness_*2)
    z          = 10
    crest         = 4
    bezier_radius = 0.75r
    
    </rule>
    
    <rule>
    importance = 90
    condition  = (_CHR1_ eq "hs1" && _CHR2_ eq "hs2" && abs(_START1_ - 10Mb) < 20Mb) || (_CHR2_ eq "hs1" && _CHR1_ eq "hs2" && abs(_START2_ - 10Mb) < 20Mb)
    color      = orange
    thickness  = eval(_thickness_*2)
    z          = 15
    crest         = 5
    bezier_radius = 0.8r
    
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    anglestep       = 0.5
    minslicestep    = 10
    beziersamples   = 40
    debug           = no
    warnings        = no
    imagemap        = no
    
    # don't touch!
    units_ok        = bupr
    units_nounit    = n
``````
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 5u
    break   = 1u
    
    axis_break_at_edge = yes
    axis_break         = yes
    axis_break_style   = 2
    
    <break_style 1>
    stroke_color = black
    fill_color   = blue
    thickness    = 0.25r
    stroke_thickness = 2
    </break>
    
    <break_style 2>
    stroke_color     = black
    stroke_thickness = 3
    thickness        = 1.5r
    </break>
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 100p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = yes
    label_with_tag = yes
    label_font     = condensedbold
    label_radius   = dims(ideogram,radius) + 0.075r
    label_size     = 60p
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    <tick>
    spacing        = 5u
    size           = 5p
    thickness      = 2p
    color          = black
    show_label     = no
    label_size     = 16p
    label_offset   = 0p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    size           = 8p
    thickness      = 2p
    color          = black
    show_label     = yes
    label_size     = 20p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
