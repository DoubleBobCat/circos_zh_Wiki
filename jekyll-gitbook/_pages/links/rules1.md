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

## 4\. Link Rules - Part I

[Lesson](/documentation/tutorials/links/rules1/lesson)
[Images](/documentation/tutorials/links/rules1/images)
[Configuration](/documentation/tutorials/links/rules1/configuration)

Rules are special blocks within <plot> or <link> blocks which redefine how
data (e.g. links) are displayed based on position, value, format or any other
property associated with the data.

The general form is

    
    
    # for 2D plots
    <plots>
    
     <plot>
    
     ...
    
     <rules>
      <rule>
      ...
      </rule>
    
      <rule>
      ...
      </rule>
    
      ...
    
     </rules>
    
     </plot>
    
    </plots>
    
    # for links
    <links>
    
     <link>
    
     ...
    
     <rules>
      <rule>
      ...
      </rule>
    
      <rule>
      ...
      </rule>
    
      ...
    
     </rules>
    
     </link>
    
    </links>
    

Each <link> block may have an associated <rules> block, which in turn contains
one or more <rule> blocks. Each <rule> block contains a test condition and
format parameters. When a link passes the test condition, the format
parameters of the rule block are applied to the link.

## data points are tested independently

Rules are applied to each data point in your data set independently. The data
point can be a highlight, histogram bar, scatter point or link. When a rule is
being applied to a point, you have access to properties of the data point, but
_not_ to other data points. In other words, there is no _direct_ mechanism of
adjusting a data point based on its neighbours. You can hack this by
associating a coe(prev) and `next` parameter with a data point and testing for
those

    
    
    hs1 0 9 0.25 next=0.5
    hs1 10 19 0.5 prev=0.25,next=0.75
    hs1 20 29 0.75 prev=0.5,next=1.00
    ...
    

## rule syntax

Each rule must contain a `condition` parameter which defines the test applied
to the data. Each data point is tested.

### rule condition

The format of the condition is Perl code and is automatically evaluated (no
need for `eval()`). A few helper functions are available to simplify testing
multiple parameters (e.g. `between()`, see below). You can suffix any
numerical value in a condition expression with `kb`, `mb`, or `gb` to indicate
a base pair multiplier.

There are certain keywords that are parsed at runtime and substituted with
values based on the link that is being tested. For example, individual data
point properties are accessible via the `var(FIELD)` function, where `FIELD`
is one of

  * `CHRn` chromosome of span n in the link (e.g. `var(chr1)`) 
  * `STARTn` start position of span n in the link (e.g. `var(start2)`) 
  * `ENDn` end position of span n in the link (e.g. `var(end2)`) 
  * `POSn` middle position of span n in the link (e.g. `var(position1)`) 
  * `SIZEn` size of span n in the link (e.g. `var(size1)`) 
  * `REVn` returns 1 if the link end is reversed (e.g. start > end) 
  * `INV` returns 1 if the link is inverted (i.e. one of its ends is reversed). If both ends are reversed, the link is _not_ inverted 
  * `INTERCHR` returns 1 if the link ends are on different chromosomes, otherwise returns 0 (e.g. `var(interchr)`) 
  * `INTRACHR` returns 1 if the link ends are on the same chromosome, otherwise returns 0 (e.g. `var(intrachr)`) 

The numerical suffix (e.g. `var(start1)` vs `var(start2)`) applies to links
only and is used to test the start or end of the link. Data types associated
with a single coordinate span do not use the suffix (e.g. `var(start)`).

Examples of conditions are

    
    
    condition = var(chr1) eq "hs1"  # link starts on hs1
    condition = var(size1) < 1mb    # link start span is shorter than 1Mb
    condition = 1                   # always true for any link
    

### rule condition testing

Rules are applied in the following order.

First, any rules that contain the `importance` parameter are applied, in
descending order of `importance`. Second, any rules that do not contain the
`importance` parameter are applied, in order of appearance. The `importance`
parameter allows you to prioritize rules without having to move their blocks.

When a rule passes (e.g. its `condition` parameter evalutes to true), it is
applied to the data point. At this point, the rule chain may or may not
terminate, depending on the `flow` parameter (see below). By default, the
first rule that passes terminates the rule chain (i.e. no further rules are
applied to the data point and the next data point is tested).

When a rule fails, the next rule is tested on the data point. This continues
until a rule passes or all rules have been tested.

## rule cascade

By default, when a rule passes, it terminates the chain.

    
    
    <rule>
    # if this rule passes
    </rule>
    
    <rule>
    # all subsequent rules are not tested
    </rule>
    
    ...
    

You can change this behaviour by setting the `flow` parameter. If `flow =
continue`, then a rule that passes no longer short-circuits the cascade.
Subsequent rules are tested and if they pass, can overwrite data point
properties.

    
    
    <rule>
    ...
    flow = continue # if this rule passes, continue testing
    </rule>
    

The `flow` parameter can take on four different values, with an optional
optional `if true` or `if false`.

    
    
    # continue testing
    flow = continue { if true|false }
    # continue testing, but start at top of rule chain
    flow = restart  { if true|false }
    # stop testing
    flow = stop     { if true|false }
    # goto rule associated with tag=TAG
    flow = goto TAG { if true|false }
    

You can have multiple `flow` parameters for different evantualities.

    
    
    <rule>
    ...
    flow = stop if false
    flow = goto otherrule if true
    </rule>
    
    <rule>
    tag = otherrule
    ...
    </rule>
    

A rule may lack a condition if a flow directive exists. You can short-circuit
all rules using

    
    
    <rule>
    flow = stop
    </rule>
    

Use the `goto` form to skip to bypass rules you don't want to test.

    
    
    <rule>
    flow = goto myrule
    </rule>
    
    ... rules you don't want to use
    
    <rule>
    tag = myrule
    ...
    </rule>
    

## 3-rule example

Here's a simple example, where segmental duplication links are displayed and
tested with 3 rules.

The first rule turns off the display of intrachromosomal links by setting
`show=no` when `var(intrachr)` is true.

The second rule colors all links between `hs1` and `hs2` green and makes them
drawn on top of other links, by setting their `z` parameter higher. Recall
that by default `z = 0` for all data points. The `flow = continue` parameter
continues testing other rules, even if this rule passes.

The final rule colors links between `hs2` and `hs3` blue, makes them thicker
and increases their `z` value further.

    
    
    <link>
    
     <link>
    
     file       = data/5/segdup.txt
    
     <rules>
    
      <rule>
       condition  = var(intrachr)
       show       = no
      </rule>
    
      <rule>
       condition  = between(hs1,hs2)
       color      = green
       z          = 10
       flow       = continue
      </rule>
    
      <rule>
       condition  = between(hs2,hs3)
       color      = blue
       thickness  = 2
       z          = 15
      </rule>
    
     </rules>
    
     </link>
    
    </links>
    

