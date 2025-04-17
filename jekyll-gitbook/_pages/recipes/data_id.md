---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: ID Fields
---

### lesson
In this tutorial, I will demonstrate how to apply formatting to data based on
its identifier stored in the `id` field.

As you've seen, each data point can have values set for format parameters such
as `color`, `stroke_thickness`, `fill_color`, and so on. These elements can be
defined in (a) the data file itself, independently for each data point (b) in
rule blocks or (c) as global settings for the entire data set.

However, it may be convenient to assign an annotation to your data points and
then calculate format values based on the annotation. This is where the `id`
field is useful—this field does not directly impact the way the data point is
displayed, but tags it with a string which you can use in rule blocks.

#### Formatting Tiles
In the first example, I'll show you how to dynamically format tiles.

There is a variety of repeat element types (LINE, SINE, Satellite, simple,
etc) and these may be stored as follows

```    
    ...
    chr21 30003462 30003712 AluSx SINE Alu
    chr21 30003734 30003925 L1MD LINE L1
    chr21 30004082 30004207 L1ME4a LINE L1
    chr21 30004229 30004286 AT_rich Low_complexity Low_complexity
    chr21 30004378 30004615 L1ME4a LINE L1
    chr21 30004781 30004872 AT_rich Low_complexity Low_complexity
    chr21 30004942 30005099 CT-rich Low_complexity Low_complexity
    chr21 30005358 30005634 MER7A DNA MER2_type
    chr21 30006113 30006265 L1ME4a LINE L1
    ...

with each element having multiple, independent classifications (e.g. AluSx,
SINE, Alu). To use these classifications, you will need to parse the data and
associate a `id` parameter with each data point. The value of the `id`
parameter is up to you. I used this script

```    
    #!/usr/bin/perl
    use strict;
    $,=" ";
    $\="\n";
    while(<>) {
        chomp;
        my $id;
        s/chr/hs/;
        if(/L(\d+)/) {
            $id = "LINE$1";
        } elsif (/S(\d+)/ || /SINE(\d?)/) {
            #my $num = $1 || 0;
            $id = "SINE" . ($1||0);
        } elsif (/low/i || /simple/i) {
            $id = "SIMPLE";
        } elsif (/LTR/) {
            $id = "LTR";
        } else {
            $id = "OTHER";
        }
        my @tok = split;
        print @tok[0..2],"id=$id";
    }

to transform the data file above into the following

```    
    ...
    hs21 30003462 30003712 id=SINE0
    hs21 30003734 30003925 id=LINE1
    hs21 30004082 30004207 id=LINE1
    hs21 30004229 30004286 id=SIMPLE
    hs21 30004378 30004615 id=LINE1
    hs21 30004781 30004872 id=SIMPLE
    hs21 30004942 30005099 id=SIMPLE
    hs21 30005358 30005634 id=OTHER
    hs21 30006113 30006265 id=LINE1
    ...

Define a tile block to show these elements

```    
    <plot>
    type = tile
    file = repeats.withid.txt
    r0   = 0.8r
    r1   = 0.98r
    orientation = in
    layers      = 50
    thickness   = 20p
    padding     = 6p
    margin      = 0.001u
    color       = black
    # for very small tiles a stroke is useful because
    # it ensures that tiles associated with very small
    # spans will be visible
    stroke_thickness = 2p
    stroke_color = black
    
    # RULES WILL GO HERE
    
    </plot>
``````
With this block, all repeat tiles will have the same formatting. To apply
formatting specific to `id` values, use

```    
    # test with regular expression
    condition = var(id) =~ /LINE/
```
or

```    
    # test string equality
    condition = var(id) eq "LINE"
```
For example, this set of rules applies different formatting to elements with
`id` LINE, SINE, SIMPLE and OTHER. For LINE elements, fill color is set to
green, but LINE1 and LINE2 elements have an additional stroke_color condition.

```    
    <plot>
    
    ...
    
    <rules>
    
    <rule>
    condition    = var(id) =~ /LINE/
    color        = green
    flow         = continue
    </rule>
    
    <rule>
    condition    = var(id) =~ /LINE[12]/
    stroke_color = red
    </rule>
    
    <rule>
    condition    = var(id) =~ /SINE/
    color        = blue
    stroke_color = blue
    </rule>
    
    <rule>
    condition    = var(id) =~ /SIMPLE/
    color        = dgrey
    </rule>
    
    <rule>
    condition    = var(id) =~ /OTHER/
    color        = lgrey
    </rule>
    
    </rules>
    
    </plot>
```
The first rule makes use of the `flow=continue` directive, which prevents the
rule chain from terminating if this rule matches. This allows a rule for LINE
and another rule for the more specific LINE1 or LINE2 test. To read more about
rule flow, see [Basic Rules Tutorial](/documentation/tutorials/links/rules1).

#### Formatting Links
Let's look how link formatting can be adjusted in the same way.

Suppose you have links which have an `id` field that contains your annotation.
In this example, I use an annotation in the format `number-number` (e.g.
87-69). This format is arbitrary and will serve to show how regular
expressions in rules can be used to extract values.

```    
    ...
    linkid5 hs21 30772491 30777591 id=87-69
    linkid5 hs21 30602230 30607330 id=87-69
    linkid6 hs21 30257977 30263077 id=60-22
    linkid6 hs21 30367808 30372908 id=60-22
    linkid7 hs21 30079003 30084103 id=54-90
    linkid7 hs21 30771970 30777070 id=54-90
    ...
```
We will first set the thickness of the link based on the first number in the
`id` field.

```    
    <rule>
    # make sure that the id field matches the required number-number format
    condition  = var(id) =~ /(\d+)-(\d+)/
    # extract the two number in 'id' to @match and use remap() function to map
    # the first number in the range 1..100 to thickess in the range 1..10.
    thickness  = eval( my @match = var(id) =~ /(\d+)-(\d+)/; remap($match[0],1,100,1,10) )
    # so that other rules can trigger too
    flow = continue
    </rule>
```
Let expand the rule to remap the z-value (depth), color and transparency as
well.

```    
    <rule>
    # make sure that the id field matches the required number-number format
    condition  = var(id) =~ /(\d+)-(\d+)/
    # extract the two number in 'id' to @match and use remap_int() function to map
    # the first number in the range 1..100 to integer thickess in the range 1..10.
    thickness  = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; remap_int($match[0],1,100,1,10) )
    
    # use the first number as the z-value (i.e. thick links will be drawn on top)
    z          = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; $match_int[0] )
    
    # use the second number for the color and transparency
    color      = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/;  
                       sprintf("spectral-9-div-%d_a%d", remap_int($match[1],1,100,1,9),  
                                                        remap_int($match[1],1,100,5,1 ) ) )
    </rule>
```
Notice that the `id` field, which is text, is set in quotes. This is required
so that the Perl expression for evaluation is

```    
    # correct - "87-69" treated as string
    my @match = "87-69" =~ /(\d+)-(\d+)/
```
rather than

```    
    # incorrect - 87-69 treated as literal
    my @match = 87-69 =~ /(\d+)-(\d+)/
```
Remember that you can use `-debug_group rules` as a command-line parameter
when running Circos to obtain debug information about how rules are parsed.

#### Formatting Text
To format text labels based on the `id` field the recipe is the same. If your
text data looks like this

```    
    ...
    hs21 30829740 30829740 tb id=64
    hs21 30405360 30405360 oe id=31
    hs21 30112849 30112849 ps id=74
    hs21 30721834 30721834 dg id=25
    hs21 30325022 30325022 sj id=22
    ...
```
then the rules to change the color and label size based on the `id` field
would be

```    
    <rule>
    condition  = 1
    color      = eval(sprintf("set2-4-qual-%d",remap_int(var(id),1,100,1,4)))
    label_size = eval(sprintf("%dp",remap_int(var(id),1,100,12,48)))
    </rule>
```
In this case, I've set `condition=1` to apply the rule without checking that
the `id` field matches the right format. Also, the `id` string does not
require quotes because the value of the parameter is a number, which does not
need to be quoted (quoting it won't hurt, though).
### images
![Circos tutorial image - ID
Fields](/documentation/tutorials/recipes/data_id/img/image-01.png) ![Circos
tutorial image - ID
Fields](/documentation/tutorials/recipes/data_id/img/image-02.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ticks.conf>>
    <<include ideogram.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    chromosomes = hs21:29.99-31.01
    
    <plots>
    
    <plot>
    file = data/8/repeats.withid.txt
    r0   = 0.8r
    r1   = 0.98r
    orientation = in
    type        = tile
    layers      = 50
    thickness   = 25p
    padding     = 5p
    margin      = 0.001u
    color       = black
    stroke_thickness = 2p
    stroke_color = black
    
    <rules>
    
    <rule>
    condition    = var(id) =~ /line/i
    color        = green
    flow         = continue
    </rule>
    
    <rule>
    condition    = var(id) =~ /line[12]/i
    stroke_color = red
    </rule>
    
    <rule>
    condition    = var(id) =~ /sine/i
    color        = blue
    stroke_color = blue
    </rule>
    
    <rule>
    condition    = var(id) =~ /simple/i
    color        = dgrey
    </rule>
    
    <rule>
    condition    = var(id) =~ /other/i
    color        = lgrey
    </rule>
    
    </rules>
    
    </plot>
    
    <plot>
    
    type = text
    file = data/8/textid.txt
    
    color      = black
    
    label_font = bold
    label_size = 36p
    r0         = 0.51r
    r1         = 0.7r
    
    padding    = 15p
    rpadding   = 15p
    
    <rules>
    
    <rule>
    condition  = 1
    color      = eval(sprintf("set2-4-qual-%d",remap_int(var(id),1,100,1,4)))
    label_size = eval(sprintf("%dp",remap_int(var(id),1,100,12,48)))
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <links>
    
    <link>
    
    file = data/8/linkid.txt
    
    bezier_radius = 0r
    radius        = 0.50r
    crest         = 0.25
    
    color     = dgrey
    thickness = 2
    
    <rules>
    <rule>
    # make sure that the id field matches the required number-number format
    condition  = var(id) =~ /(\d+)-(\d+)/
    thickness  = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; remap($match[0],1,100,1,10) )
    z          = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; $match[0] )
    color      = eval( my @match = "var(id)" =~ /(\d+)-(\d+)/; sprintf("spectral-9-div-%d_a%d", remap($match[1],1,100,1,9), remap($match[1],1,100,5,1 ) ) )
    </rule>
    </rules>
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
    band_transparency     = 3
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    break   = 0.5r
    
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
    stroke_thickness = 2
    thickness        = 1.5r
    </break>
    
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
    label_radius     = dims(image,radius) - 50p
    label_size       = 36
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.85r
    thickness        = 30p
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
    
    grid_start         = dims(ideogram,radius_inner)-0.5r
    grid_end           = dims(ideogram,radius_outer)+100
    
    <ticks>
    skip_first_label     = no
    skip_last_label      = no
    radius               = dims(ideogram,radius_outer)
    label_offset     = 2p
    multiplier = 1e-6
    color = black
    size  = 20p
    thickness = 4p
    
    <tick>
    spacing        = .005u
    color          = black
    show_label     = no
    label_size     = 8p
    label_offset   = 0p
    format         = %2.f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    
    <tick>
    spacing        = .05u
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 10p
    format         = %.2f
    grid           = yes
    grid_color     = grey
    grid_thickness = 1p
    </tick>
    
    <tick>
    spacing        = .25u
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 10p
    format         = %.2f
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    </tick>
    </ticks>
```
  

* * *
