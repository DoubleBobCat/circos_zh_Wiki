---
author: DoubleCat
date: 2025-04-11
layout: post
category: reference
title: Reference
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

# 12 — Circos Reference

## 4\. Configuration Parameters

### syntax

Below is a block template for a general configuration file. Not all blocks are
required. For some, duplicate blocks will be merged (e.g. `<colors>`), while
others will be stored as a list (e.g. `<tick>`).

    
    
    <colors>
    </colors>
    
    <fonts>
    </fonts>
    
    <patterns>
    </patterns>
    
    <zooms>
    
      <zoom>
      </zoom>
    
      <zoom>
      </zoom>
    
      ...
    
    </zooms>
    
    <ideogram>
    
      <spacing>
    
        <pairwise>
        </pairwise>
    
        <pairwise>
        </pairwise>
    
        ...
    
      </spacing>
    
      <break_style>
      </break_style>
    
      <break_style>
      </break_style>
    
      ...
    
      <rules>
    
        <rule>
        </rule>
    
        <rule>
        </rule>
    
        ...
    
      </rules>
    
    </ideogram>
    
    <ticks>
    
      <tick>
      </tick>
    
      <tick>
      </tick>
    
      ...
    
    </ticks>
    
    <highlights>
    
      <highlight>
        <rules>
          <rule>
          </rule>
          <rule>
          </rule>
          ...
        </rules>
      </highlight>
    
      <highlight>
      </highlight>
    
      ...
    
    </highlights>
    
    <plots>
    
      <plot>
        <rules>
          <rule>
          </rule>
          <rule>
          </rule>
          ...
        </rules>
    
        <axes>
          <axis>
          </axis>
          <axis>
          </axis>
          ... 
        </axes>
    
        <backgrounds>
          <background>
          </background>
          <background>
          </background>
          ...
        </backgrounds>
      </plot>
    
      <plot>
      </plot>
    
      ...
    
    </plots>
    
    <links>
    
      <link>
        <rules>
          <rule>
          </rule>
          <rule>
          </rule>
          ...
        </rules>
      </link>
    
      <link>
      </link>
    
      ...
    
    </links>
    

### includes

A configuration file can be included in another with the `<<include FILE`>>
directive.

    
    
    ################################################################
    # circos.conf
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    ################################################################
    # ideogram.conf
    <ideogram>
     ...
    </ideogram>
    
    ################################################################
    # ticks.conf
    <ticks>
     ...
    </ticks>
    

When including the file, a relative file name will be interpreted relative to
the location of the file in which it is being included. If it is not found
there, the Circos distribution directory will be searched. For example,

    
    
    <<include etc/housekeeping.conf>>
    

will include `etc/housekeeping.conf` from the Circos distribution.

### parameters

Parameters are defined as variable/value pairs.

    
    
    param = value
    

In some cases the parameter accepts a list (usually comma-delimited, but not
always).

    
    
    param = value,value,...
    

In a very few cases the parameter accepts multiple instances.

    
    
    radius = 0.9r
    radius = 0.8r
    

If you attempt multiple definitions for a parameter that does not allow this,
you'll see an error.

#### units

Circos understands three units: `p` (pixel), `r` (relative) and `u`
(chromosome units). Depending on a parameter, one or more of these units can
be used. In some cases, in an arithmetic expression (e.g. `0.5r+10p`).

Parameters with the relative unit, `r`, are evaluated relative to the value of
another parameter. For example, expressing the ideogram position in relative
units determines the position relative to the size of the image.

Parameters that specify axis position or spacing typically use the `u` unit.
When this unit is used, the value is expressed as a multiple of
`chromosomes_units`. This helps shorten values of parameters (e.g. `10u` vs
`10000000`) such as `spacing` in `<tick>` blocks.

#### references to other parameters

Anywhere in the configuration file you can refer to the value of another
parameter using the `conf()` function.

To access configuration parameters from the root of the configuration file,

    
    
    show_histogram = yes
    ...
    <plots>
     <plot>
      show = conf(show_histogram)
      type = histogram
      ...
    

To access configuration parameters from anywhere in the configuration file,
include the list of blocks before the parameter name.

    
    
    <plots>
     show_histogram = yes
     <plot>
      show = conf(plots,show_histogram)
      type = histogram
      ...
    

To refer to a parameter in the current block and perform a search up the block
hierarchy, specify "`.`" for the path.

    
    
    <plots>
     <plot>
      type = histogram
      r0   = 0.5r
      r1   = conf(.,r0)+50p
      ...
    

The search is useful in rules

    
    
    <plots>
     <plot>
      x    = 10
      ...
    
      <rules>
       <rule>
       # x is not defined in this  block, but it will
       # be found from the outer  block
       condition = conf(.,x) == 10
       ...
    

### accessing data properties

###

In rules, to access a data point's property, such as position or value, use
`var()`.

    
    
    <rule>
    color = var(id)
    

If you are using the value as a part of an expression, make sure you pass it
through `eval()` (see below).

### evaluating parameters

You can express a parameter using Perl code. Use `eval()` to make sure that it
is evaluated. This is common in rules.

    
    
    <rule>
     condition = on(hs1)
     value     = eval(log(var(value))/log(2))
    </rule>
    

The `condition` parameter in `<rule>` blocks is automatically evaluated.

#### overriding values

Generally most parameters do not accept multiple instances. The following is
not allowed and will produce an error

    
    
    <ideogram>
    position = 0.9r
    position = 0.8r
    ...
    </ideogram>
    

However, if you add the `*` suffix to one of the parameter names, it will be
used to override the previously defined value of the parameter.

    
    
    <ideogram>
    position = 0.9r
    position* = 0.8r # this value will be used
    ...
    </ideogram>
    

You can use as many `*` in the suffix as you want — the parameter with the
largest number of `*` will be the one used. This facility is useful in
overriding parameters from included files (see below).

### block structure and merging

Blocks logically group parameters and help name collisions.

#### multiple blocks

Certain blocks can have multiple instances, as indicated by the flags in the
table below.

Some blocks define lists of objects, such as `<plot>` or `<tick>`. In these
cases multiple entries will be stored as a list. In others, such as `<color>`,
multiple instances will be merged into a single block.

    
    
    # two <color> blocks are ...
    <color>
    color1 = 255,100,100
    </color>
    <color>
    color2 = 255,255,100
    </color>
    
    # ... merged into one
    
    <color>
    color1 = 255,100,100
    color2 = 255,255,100
    </color>
    

#### merging and overriding

You can take advantage of merging by adding or overriding parameters in blocks
which were included from another file.

    
    
    # default <colors> block with pre-defined colors
    <<include etc/colors_fonts_patterns.conf>>
    
    # to add more colors, define them in a second <colors> block, 
    # which will be merged
    <colors>
    mycolor = 255,100,100
    </colors>
    

When overriding parameters, use the `*` suffix.

    
    
    # suppose you are including your <ideogram> block from a file
    <<include ideogram.conf>>
    
    # to change the position parameter with in this block, you can 
    # override it without having to edit ideogram.conf
    <ideogram>
    position* = 0.95r
    </ideogram>
    

### blocks

Block flags: R required, M multiple blocks will be merged, + multiple blocks
allowed.

#### system

block

inheritance

description

comment

  

<colors> R M

PARENT  
root  

Color and color lists.

Include this using `etc/colors_fonts_patterns.conf`.

  

<fonts> R M

PARENT  
root  

Font names and TTF file associations.

Include this using `etc/colors_fonts_patterns.conf`.

  

<patterns> M

PARENT  
root  

Fill patterns.

Include this using `etc/colors_fonts_patterns.conf`.

  

* * *

#### layout

block

inheritance

description

comment

  

<ideogram> R M

PARENT  
root  
CHILDREN  
`<spacing>`

Position, spacing and format of ideograms.

  

<spacing> R

PARENT  
`<ideogram>`  
CHILDREN  
`<pairwise>`

Spacing between ideograms.

  

<pairwise> +

PARENT  
`<spacing>`  

Spacing between specific ideogram pairs.

  

<image> R

PARENT  
root  

Size, background and format of output image.

Import default image settings from `etc/image.conf` and override as necessary.

  

<ticks>

PARENT  
root  

Position, spacing and format of ideogram scale ticks.

  

<tick> +

PARENT  
`<ticks>`  

A tick group, defined by uniform spacing or specific position.

  

<zooms>

PARENT  
root  
CHILDREN  
`<zoom>`

Regions with magnified or condensed scale.

  

<zoom> +

PARENT  
`<zooms>`  

Region with magnified or condensed scale.

  

* * *

#### data tracks

block

inheritance

description

comment

  

<highlights> M

PARENT  
root  
CHILDREN  
`<highlight>`

Highlight tracks.

Import default image settings from `etc/image.conf` and override as necessary.

  

<plots> M

PARENT  
root  
CHILDREN  
`<plot>`

Data tracks.

  

<links> M

PARENT  
root  
CHILDREN  
`<link>`

Link tracks.

  

<highlight> +

PARENT  
`<highlights>`  

Highlight track, composed of colored segment displayed under axes, grids and
other tracks.

Import default image settings from `etc/image.conf` and override as necessary.

  

<plot> +

PARENT  
`<plots>`  
CHILDREN  
`<rules>`, `<axes>`, `<backgrounds>`

A data track, such as scatter plot, histogram, heat map or text.

  

<link> +

PARENT  
`<links>`  
CHILDREN  
`<rules>`

Link track, composed of connections drawn as Bezier curves between ideogram
positions.

  

* * *

#### annotations and rules

block

inheritance

description

comment

  

<rules>

PARENT  
`<plot>`, `<link>`, `<highlight>`, `<ideogram>`  
CHILDREN  
`<rule>`

Track rules.

  

<rule> +

PARENT  
`<rules>`  

A rule, which changes how a data point is displayed subject to conditions
based on value, position and property.

  

<axes>

PARENT  
`<plot>`  
CHILDREN  
`<axis>`

Track y-axes.

  

<axis> +

PARENT  
`<axes>`  

Track y-axis, a group of axis grids defined by uniform spacing or specific
position.

  

<backgrounds>

PARENT  
`<plot>`  
CHILDREN  
`<background>`

Track backgrounds.

  

<background> +

PARENT  
`<backgrounds>`  

Track background, which is a colored region between axis ranges within the
track.

  

