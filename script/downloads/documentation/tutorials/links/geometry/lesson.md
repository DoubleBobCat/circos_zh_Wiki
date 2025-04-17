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

## 2\. Link geometry

[Lesson](/documentation/tutorials/links/geometry/lesson)
[Images](/documentation/tutorials/links/geometry/images)
[Configuration](/documentation/tutorials/links/geometry/configuration)

Link geometry is defined by four parameters: radius, bezier_radius,
bezier_radius_purity and crest. An additional set of parameters in the
perturb* name space permits random adjustment to some of these parameters.

### radius

This value sets the radial position of the termini of the links and may be
defined as a relative or absolute value.

    
    
    # 50% of inner ideogram radius
    radius = 0.5r 
    
    # 50 pixels inside inner ideogram radius
    radius = 1r - 50p
    
    # 25 pixels outside inner ideogram radius
    # careful - links will overlap with ideogram
    radius = 1r + 25p
    
    # links terminate 750 pixels from image center
    radius = 750p
    

I suggest that you set the radius value to be relative, to make it easier to
later resize the figure without having to adjust the radius value.

A combination of relative and absolute values permits an overall relative
position with a fixed margin.

### bezier_radius

The bezier_radius controls the radial position of the control point used to
accentuate the curvature in the link. Without any additional parameters, each
link will have its control point placed at the same radial position,
regardless of the location of the start and end points of the link.

### crest

Two additional Bezier control points can be set by using the crest parameter.
When defined, points p3 and p4 are added. These points lie at the same angular
position as the start and end link termini and have the radial position

    
    
    p3r,p4r = radius +/- |bezier_radius - radius| * crest
    

In the crest=0 extreme, p3 and p4 are at the same position as p0,p1. In this
case, crest has no effect. When crest=1, p3,p4 are at the radial position of
p2, the control point set by bezier_radius. Keep in mind the difference
between p2 and p3,p4 control points - p2 is placed along the radius that
bisects angle formed by p0,center,p1 whereas p3,p4 are placed along the same
radius as p0,p1.

The purpose of the crest parameter is to make the links terminate
perpendicularly to the ideogram radius. Cresting works only if bezier_radius
is defined.

### bezier_radius_purity

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

### perturb

A set of parameters can be used to randomly adjust bezier_radius,
bezier_radius_purity, and crest parameters to give the links a more
disorganized, organic feel. By perturbing each link you can also show
additional texture in the data among links which would have ordinarily
overlapped.

Each parameter's perturbation amount is defined as a pair of values -
pmin,pmax. These are the minimum and maximum multipliers by which the value
can be perturbed.

Given a perturbation (pmin,pmax), the modification is defined by

    
    
    new_value = value * [ pmin + (pmax-pmin)*urd ]
    

where urd is a uniform random deviate in the range [0,1). Thus, the new value
will be sampled uniformly from the range [value*pmin, value*pmax].

For example, if you define

    
    
    perturb               = yes
    perturb_crest         = 0
    perturb_bezier_radius = 0.5,1.2
    perturb_bezier_radius_purity = 0.5,1
    

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

