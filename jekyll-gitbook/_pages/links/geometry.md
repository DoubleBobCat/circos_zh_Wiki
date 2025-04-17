---
author: DoubleCat
date: 2025-04-11
layout: post
category: links
title: Link Geometry
---

## Link Geometry
### lesson
Link geometry is defined by four parameters: radius, bezier_radius,
bezier_radius_purity and crest. An additional set of parameters in the
perturb* name space permits random adjustment to some of these parameters.

#### radius
This value sets the radial position of the termini of the links and may be
defined as a relative or absolute value.

```    
    # 50% of inner ideogram radius
    radius = 0.5r 
    
    # 50 pixels inside inner ideogram radius
    radius = 1r - 50p
    
    # 25 pixels outside inner ideogram radius
    # careful - links will overlap with ideogram
    radius = 1r + 25p
    
    # links terminate 750 pixels from image center
    radius = 750p
```
I suggest that you set the radius value to be relative, to make it easier to
later resize the figure without having to adjust the radius value.

A combination of relative and absolute values permits an overall relative
position with a fixed margin.

#### bezier_radius
The bezier_radius controls the radial position of the control point used to
accentuate the curvature in the link. Without any additional parameters, each
link will have its control point placed at the same radial position,
regardless of the location of the start and end points of the link.

#### crest
Two additional Bezier control points can be set by using the crest parameter.
When defined, points p3 and p4 are added. These points lie at the same angular
position as the start and end link termini and have the radial position

```    
    p3r,p4r = radius +/- |bezier_radius - radius| * crest
```
In the crest=0 extreme, p3 and p4 are at the same position as p0,p1. In this
case, crest has no effect. When crest=1, p3,p4 are at the radial position of
p2, the control point set by bezier_radius. Keep in mind the difference
between p2 and p3,p4 control points - p2 is placed along the radius that
bisects angle formed by p0,center,p1 whereas p3,p4 are placed along the same
radius as p0,p1.

The purpose of the crest parameter is to make the links terminate
perpendicularly to the ideogram radius. Cresting works only if bezier_radius
is defined.

#### bezier_radius_purity
The bezier_radius parameter is constant for all links. Therefore, regardless
of a link's start/end position, the p2 control point will always be at the
same radial position, as determined by the bezier_radius value. This has the
effect of making links that have nearby start/end termini highly curved.

To mitigate this, bezier_radius_purity allows you to define an effective
bezier radius, which is a function of the distance between the link's
start/end termini.

The bezier_radius_purity adjusts the position of p2 for each link. The p2
control point will move along the line formed by the original p2 location and
the intersection of p0-p1 and the bisecting radius. When purity = 1, p2' = p2.
When purity = 0, p2' = midpoint(p0,p1).

If bezier_radius_purity is defined, crest will use the new bezier radius
control point (p2').

#### perturb
A set of parameters can be used to randomly adjust bezier_radius,
bezier_radius_purity, and crest parameters to give the links a more
disorganized, organic feel. By perturbing each link you can also show
additional texture in the data among links which would have ordinarily
overlapped.

Each parameter's perturbation amount is defined as a pair of values -
pmin,pmax. These are the minimum and maximum multipliers by which the value
can be perturbed.

Given a perturbation (pmin,pmax), the modification is defined by

```    
    new_value = value * [ pmin + (pmax-pmin)*urd ]
```
where urd is a uniform random deviate in the range [0,1). Thus, the new value
will be sampled uniformly from the range [value*pmin, value*pmax].

For example, if you define

```    
    perturb               = yes
    perturb_crest         = 0
    perturb_bezier_radius = 0.5,1.2
    perturb_bezier_radius_purity = 0.5,1
```
then crest will remain unperturbed, and bezier radius and radius purity will
be randomly scaled between 50-120% and 50-100% of their original values,
respectively.

By using pmin<0, you can force some values to become negative at times. For
example, if crest = 0.5, then perturb_crest = -1,2 would perturb crest to lie
in the range [-0.5,1).

Experiment with the values, starting small unless you want _very_ organic
images. The curves.repeated.txt data set bundled with this tutorial provides a
data set with 7 identical sets of 24 links. By applying perturbation, each
links from a set will be drawn differently, exposing the effect of parameter
adjustment on the final curve.
### images
![Circos tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/01.png) ![Circos
tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/02.png) ![Circos
tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/03.png) ![Circos
tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/04.png) ![Circos
tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/05.png) ![Circos
tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/06.png) ![Circos
tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/07.png) ![Circos
tutorial image - Link
Geometry](/documentation/tutorials/links/geometry/img/08.png)
### configuration
#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1;hs2;hs3
    
    <links>
    
    z      = 0
    radius = 0.90r
    crest  = 0.9
    bezier_radius        = 0.9r
    bezier_radius_purity = 0.5
    
    perturb               = yes
    perturb_crest         = 0
    perturb_bezier_radius = 0.8,1.2
    perturb_bezier_radius_purity = 0.5,1.5
    
    <link>
    color        = vvdgrey
    thickness    = 2
    file         = data/5/curves.repeated.txt
    </link>
    
    </links>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 0
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.01r
    break   = 0.5r
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(ideogram,radius) + 0.075r
    label_with_tag   = yes
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 100p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    
    <tick>
    spacing        = 1u
    show_label     = no
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
