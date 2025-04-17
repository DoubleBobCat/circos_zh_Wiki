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

## 5\. Link Rules - Part II

[Lesson](/documentation/tutorials/links/rules2/lesson)
[Images](/documentation/tutorials/links/rules2/images)
[Configuration](/documentation/tutorials/links/rules2/configuration)

Rules are worth learning—they allow you to customize the layering and
formating your links.

In the previous tutorial, we saw how links can be identified by changing their
color based on chromosome assignment.

In this tutorial, I extend the example and show you how you can layer and
format links based not only on which chromosomes they connect, but also based
on position and link end size.

## multiple conditions

A rule can have multiple condition parameters. They are evaluated using
**AND** , i.e. all conditions must be satisfied for the rule to pass. This
rule tests for links that are interchromosomal and whose start size is greater
than 40kb.

    
    
    <rule>
    condition = var(interchr)
    condition = var(size1) > 40kb
    ...
    </rule>
    

While you can always combine the conditions in one parameter,

    
    
    condition = var(interchr) && var(size1) > 40kb
    

it is more modular and transparent to take advantage of multiple conditions.
Just remember: the conditions are combined with AND, **not OR**.

## helper functions

There are several helper functions that simplify testing data point position.

  * `on(CHR)` returns 1 if data point on chromosome `CHR`, for links tests both ends 
  * `from(CHR)` returns 1 if start of link is on chromosome `CHR`, used for links only 
  * `to(CHR)` returns 1 if start of link is on chromosome `CHR`, used for links only 
  * `between(CHR1,CHR2)` returns 1 if link is between `CHR1` and `CHR2`, regardless of orientation, used for links only 
  * `fromto(CHR1,CHR2)` returns 1 if link is from `CHR1` to `CHR2`, used for links only 
  * `tofrom(CHR1,CHR2)` returns 1 if link is from `CHR2` to `CHR1`, used for links only 

The `on()` function has a variant that tests for both chromosome and
coordinate.

  * `on(CHR,START,END)` returns 1 if data point is on chromosome CHR and intersects coordinate START-END, for links tests both ends 

To test that the data point coordinate falls entirely within the interval, use
`within()`.

  * `within(CHR,START,END)` returns 1 if data point is on chromosome CHR and falls entirely within START-END, for links tests both ends 

## 5-rule example

The first rule, colors any interchromosomal links whose either end falls on
hs2:65-75Mb.

The next four rules change the color and thickness based on the maximum size
of the link ends. The links with the largest ends (> 40kb) are made green and
thick and successive rules retest with a lower maximum size cutoff.  #
multiple conditions are combined with AND  # i.e. all conditions must be
satisfied condition = var(interchr) condition = on(hs2,65Mb,75Mb) z = 60 color
= red thickness = 5  condition = max(var(size1),var(size2)) > 40kb z = 50
color = green thickness = 5  condition = max(var(size1),var(size2)) > 10kb z =
45 color = dgrey thickness = 4  condition = max(var(size1),var(size2)) > 5kb z
= 40 color = grey thickness = 3  condition = max(var(size1),var(size2)) > 1000
z = 35 color = lgrey thickness = 2

Notice that I did not set flow = continue for these rules, since they were
designed to short-circuit. The first rule that matches is the only rule that I
want to affect the format parameters.

