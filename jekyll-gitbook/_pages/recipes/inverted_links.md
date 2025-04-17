---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Recipes
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

# 9 — Recipes

## 12\. Inverted Links

[Lesson](/documentation/tutorials/recipes/inverted_links/lesson)
[Images](/documentation/tutorials/recipes/inverted_links/images)
[Configuration](/documentation/tutorials/recipes/inverted_links/configuration)

In this tutorial, I will show how to write rules that format inverted links.

A link is considered inverted if the orientation of its two ends is inverted
with respect to one another. For example, given a link defined by the two ends
`chrA:start1-end1` and `chrB:start2-end2`, the link is inverted if

    
    
    start1 < end1 && start2 > end2
    
    or
    
    start1 > end1 && start2 < end2
    

The interpretation of the case

    
    
    start1 > end1 && start2 > end2
    

depends on your application.

### link geometry

Recall that links are defined by specifing the position and orientation of
their ends. When links are drawn as ribbons, the relative orientation of the
link's ends affects whether the ribbon has a twist (see [Link—Twists
tutorial](//documentation/tutorials/links/twists)).

In that tutorial, you saw that you can make a link ribbon flat (i.e. without a
twist), regardless of the orientation of the link, by setting

    
    
    flat = yes
    

in the link block. By adding the `twist` parameter to the link, the ribbon
could be made to twist even if `flat=yes` was set.

    
    
    hs1 100 200 hs2 100 200
    # this link's ribbon will be twisted, even if flat=yes is set
    hs3 100 200 hs4 100 200 twist=1
    

Adding the `inverted` parameter to one of the link's ends in the data file
swaps its start and end coordinates. This parameter is useful if you want to
keep start < end for all your links, but still store information about the
orientation.

    
    
    hs1 100 200 hs2 100 200
    # when a link end has inverted*=1, its start/end coordinates
    # are reversed. For the start of the link use inverted1 and
    # for the end inverted2.
    hs3 100 200 hs4 100 200 inverted1=1
    

The difference between the `twist` and `inverted` parameters is that `twist`
is meant to affect how a link's ribbon is drawn and `inverted` is meant to
actually alter how a link is defined.

Keep in mind that the orientation of the link's ideograms has an effect on the
link's twist. Link ribbons, by default, have their corners drawn in the order
start1 -> end1 -> end2 -> start2, which results in a twist for a link with
start < end for both ends when the ideograms are oriented in the same
direction.

### testing for inversion

To test whether a link is inverted, use the `var(rev1)` and `var(rev2)`
keywords in a rule. Each of these strings evaluate to 1 if the start and end
of the link are inverted, respectively.

For example, this rule will color orange all links which have their ends
inverted.

    
    
    <rule>
    condition  = var(rev2)
    color      = orange
    </rule>
    

You can test one or both ends for inversion, though if both ends of a link are
inverted the link itself could be consider as not inverted. It is up to you
how to interpret this case.

    
    
    <rule>
    condition  = var(rev1) && var(rev2)
    color      = red
    </rule>
    
    <rule>
    condition  = var(rev1)
    color      = green
    </rule>
    
    <rule>
    condition  = var(rev2)
    color      = orange
    </rule>
    

### defining inverted links

To indicate that a link is inverted, you can either reverse the coordinates of
one of its ends, or assign it the `inverted` parameter.

    
    
    # this is a normal link
    chr1 100 200 chr2 100 200
    
    # this is an inverted link - its first end is inverted
    chr1 200 100 chr2 100 200
    
    # this is an inverted link - its first end is inverted using the 'inverted' flag
    chr1 100 200 chr2 100 200 inverted1=1
    
    # this is an inverted link - its second end is inverted
    chr1 100 200 chr2 200 100
    
    # this is an inverted link - its second end is inverted using the 'inverted' flag
    chr1 100 200 chr2 100 200 inverted2=1
    

How you choose to store information about inversion is up to you. Unless you
are using the link input file in other analysis that requires strictly that
`start<=end`, I suggest you use explicit coordinate inversion.

