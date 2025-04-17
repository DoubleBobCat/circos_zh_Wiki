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

## 7\. Link Rules - Part IV

[Lesson](/documentation/tutorials/links/rules4/lesson)
[Images](/documentation/tutorials/links/rules4/images)
[Configuration](/documentation/tutorials/links/rules4/configuration)

Rules can be used to set formatting values based on a function of
characteristics of the link. For example, you can define the thickness of the
link line to be proportional to the size of the link's spans.

In previous examples, rules assigned constants to format parameters, such as

    
    
    <rule>
    ...
    thickness = 2
    color     = red
    </rule>
    

To assign a value based on characteristics of the link, use `eval()`. The
expression within `eval()` must be valid Perl.

    
    
    <rule>
    ...
    thickness = eval(max(1,round(var(size1)/1000)))
    </rule>
    

The argument to `eval()` will be parsed and its output value will be assigned
to the format parameter. In the above example, thickness will the size of the
link's first span, divided by 1000. If the span is 28kb, the thickness will be
28. In case the link is smaller than 500 bp, I've set the minimum thickness to
be 1 by using `max(1,...)`.

For the image in this example, I've set up four expressions that use `eval()`
to assign variable values to the thickness, radius, color and z-depth of
links.

    
    
    <rule>
    condition  = 1
    thickness  = eval(sprintf("%d",remap_round(max(var(size1),var(size2)),1,25000,2,6)))
    radius     = eval(sprintf("%fr",remap(min(var(size1),var(size2)),1,25000,0.5,0.999)))
    color      = eval(sprintf("spectral-11-div-%d",remap_round(scalar min(var(size1),var(size2)),1,25000,1,11)))
    z          = eval(int(max(var(size1),var(size2))/100))
    </rule>
    

This single rule applies to all links, since the condition is always true. For
each formatting parameter, an expression that is a function of the size of the
link's spans is evaluated to obtain a value for the parameter.

Thickness is scaled with the size of the larger span. Here
`max(var(size1),var(size2))` returns the larger of the two values and is a
Perl function. You can also use `min()`, if you need the smaller value. The
helper function `remap_round()` remaps the maximum size from a range of
[1,25000] to [2,6], which is assigned to the thickness.

Similar remappings are applied to the radius and color. In the case of color,
the target range is [1,11], which is the range of colors in the Brewer
spectral-11-div palette.

I have also assigned z-depth a value based on the link's span size. This has
the effect of drawing the links with larger spans last \- these would be the
blue and purple links, as formatted by the expression that assigns color. The
z-depth expression effectively divides links into 100 bp bins based on the
larger span size, with links in bins associated with smaller spans drawn
first. Avoid having too many bins - it can take a long time for Circos to
iterate through all the requested z-depths. In fact, the rule in this example
could just as well have been

    
    
    z          = eval(int(max(var(size1),var(size2))/500))
    

or

    
    
    z          = eval(int(max(var(size1),var(size2))/1000))
    

likely without much impact on the final image.

