---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Links & Rules
---

## Links & Rules
### lesson
The first data track we will add are links. Links represent an association
between two genomic positions (e.g. similarity, difference, fusion, etc) by
curves or straight lines.

Links can be visually formatted using rules, which compose a decision tree of
expressions that are evaluated for every link. Rules test links based on data
value, and can therefore dynamically change how a link appears based on its
position, size, or other parameter.

But before adding links to the image from the previous tutorial, I want to
show you another way of changing the colors of ideograms that is more helpful
if you want to reuse the custom colors for other elements in the image.

#### custom colors
If you look in the human karyotype file linked to above, you'll see that each
chromosome's color is `chrN` where `N` is the number of the chromosome. Thus,
chromosome `hs1` has color `chr1`, `hs2` has color `chr2` and so on. For
convenience, a color can be referenced using `chr` and `hs` prefixes (`chr1`
and `hs1` are the same color).

Because the color and chromosome name is the same for human genome data (or
any data set in which you use `chr` or `hs` as the chromosome prefix), you can
color a data point by using its chromosome name.

In the previous tutorial, I used `chromosomes_colors` to change the color of
the ideograms. This approach works well when the only thing you want to do is
change the color of the segments, because although the color of `hs1` on the
image has changed, the definition of color `hs1` remains the same.

```    
    chromosomes_color = hs1=red,hs2=orange,hs3=green,hs4=blue
```
To change the color of the ideogram and color of the same name, you need to
redefine the value of the color in the `<colors>` block. This block is
included below from the `colors_fonts_patterns.conf` file, which contains all
the default definitions. To overwrite colors, use a `*` suffix and provide a
new value, which can be a lookup to another color.

```    
    <colors>
    chr1* = red
    chr2* = orange
    chr3* = green
    chr4* = blue
    </colors>
```
#### links
Links are defined in `<link>` blocks enclosed in a `<links>` block. The links
start at a radial position defined by `radius` and have their control point
(adjusts curvature) at the radial position defined by `bezier_radius`. In this
example, I use the segmental duplication data set, which connects regions of
similar sequence (90%+ similarity, at least 1kb in size).

```    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.8r
    bezier_radius = 0r
    color         = black_a4
    thickness     = 2
    </link>
    
    </links>
```
#### rules
Rule blocks can be added to any  or  block and form a decision chain that
changes how data points (e.g. links, histogram bins, scatter plot glyphs, etc)
are formatted.

The decision chain is composed of one or more `<rule>` blocks enclosed by a
`<rules>` block.

```    
    <rules>
    
    <rule>
    ...
    </rule>
    
    <rule>
    ...
    </rule>
    
    ...
    
    </rules>
```
Each rule has a condition, formatting statements and an optional `flow`
statement. If the condition is true, the rule is applied to the data point and
no further rules are checked (unless flow=continue). If the condition is
false, the next rule is checked.

`var(X)` referrs to the value of variable `X` for the data point. Here
`intrachr` means intra-chromosomal.

```    
    <rule>
    condition     = var(intrachr)
    # Any links that are intra-chromosomal will not be shown. Further rules are not tested.
    show          = no
    </rule>
```
A rule with `condition=1` is applied to all remaining links, since its
condition is always true.

The color of the link is set to the 2nd chromosome in the link coordinate
(link's end). Here `eval()` is required so that the expression `var(chr2)` is
evaluated (we want the result of `var(chr2)`, not the color named
`"var(chr2)"`). Note that for conditions, evaluation is automatic, but
required for all other parameters.

```    
    <rule>
    condition     = 1
    color         = eval(var(chr2))
    # After this rule is applied, the rule chain continues.
    flow          = continue
    </rule>
```
The remaining two rules each change the radius of the start and end of a link,
respectively, if it starts or ends on `hs1`.

```    
    <rule>
    # If the link's start is on hs1...
    condition     = from(hs1)
    # ...set the radial position of the link's start to be close to the ideogram.
    radius1       = 0.99r
    </rule>
    
    <rule>
    # Same as the rule above, but applies to the end of the link.
    condition     = to(hs1)
    # 'radius2' (like chr2, start2, end2) refers to the variable 'radius' of the end of the link.
    radius2       = 0.99r
    </rule>
```
#### more on rules
Rules are evaluated in order of appearance. You can move a rule up in the
decision tree by either moving its `<rule>` block up, or adding the
`importance` parameter. Rules with this parameter will be tested first, in
descending value of the parameter, followed by rules without the parameter.

```    
    <rules>
    
    <rule>
    # 2nd
    </rule>
    
    <rule>
    # 3rd
    </rule>
    
    <rule>
    # 1st 
    importance = 10
    </rule>
    
    </rules>
```
If the `condition` of a rule is true, the rule is applied and the rule chain
stops for the current data point. If you want to change this behaviour, use
the `flow` parameter. Optionally, you can make the `flow` control dependent on
the outcome of the `condition` by using `if true` or `if false`.

To force the testing to continue,

```    
    flow = continue {if true|false}
```
The default behaviour is

```    
    flow = continue if false
```
To force the testing to stop,

```    
    flow = stop {if true|false}
```
You can restart the testing (only once though, to avoid endless loops)

```    
    flow = restart {if true|false}
```
Finally, you can assign a `tag` to a rule and then jump to it from another.

```    
    <rule>
    flow = goto special_rule if true
    ...
    </rule>
    
    <rule>
    tag = special_rule
    ...
    </rule>
```### images
![Circos tutorial image - Links &
Rules](/documentation/tutorials/quick_start/links_and_rules/img/01.png)
### configuration
#### circos.conf
```    
    # 1.4 LINKS AND RULES
    #
    # The first data track we will add are links. By using rules, which
    # are expressions that are evaluated for every link, the formatting
    # can be dynamically changed based on data values.
    #
    # I will also show you how to change the definition of colors, if you
    # would like to assign different chromosome color scheme to your
    # figure.
    
    karyotype = data/karyotype/karyotype.human.txt
    chromosomes_units = 1000000
    
    chromosomes_display_default = no
    chromosomes                 = /hs[1-4]$/
    chromosomes_reverse         = /hs[234]/
    chromosomes_scale           = hs1=0.5r,/hs[234]/=0.5rn
    chromosomes_radius          = hs4:0.9r
    
    # In the previous tutorial (1.3), I used chromosomes_colors to change
    # the color of the ideograms. This approach works well when the only
    # thing you want to do is change the color of the segments. 
    #
    # Another way to achieve this is to actually redefine the colors which
    # are used to color the ideograms. The benefit of doing this is that
    # whenever you refer to the color (which you can use by using the name
    # of the chromosome), you get the custom value.
    #
    # If you look in the human karyotype file linked to above, you'll see
    # that each chromosome's color is chrN where N is the number of the
    # chromosome. Thus, hs1 has color chr1, hs2 has color chr2, and so
    # on. For convenience, a color can be referenced using 'chr' and 'hs'
    # prefixes (chr1 and hs1 are the same color).
    #
    # Colors are redefined by overwriting color definitions, which are
    # found in the <colors> block. This block is included below from the
    # colors_fonts_patterns.conf file, which contains all the default
    # definitions. To overwrite colors, use a "*" suffix and provide a new
    # value, which can be a lookup to another color.
    
    <colors>
    chr1* = red
    chr2* = orange
    chr3* = green
    chr4* = blue
    </colors>
    
    # Links are defined in <link> blocks enclosed in a <links> block. The
    # links start at a radial position defined by 'radius' and have their
    # control point (adjusts curvature) at the radial position defined by
    # 'bezier_radius'. In this example, I use the segmental duplication
    # data set, which connects regions of similar sequence (90%+
    # similarity, at least 1kb in size).
    
    <links>
    
    <link>
    file          = data/5/segdup.txt
    radius        = 0.8r
    bezier_radius = 0r
    color         = black_a4
    thickness     = 2
    
    # Rule blocks can be added to any <link> or <plot> block and form a
    # decision chain that changes how data points (e.g. links, histogram
    # bins, scatter plot glyphs, etc) are formatted.
    
    <rules>
    
    # The decision chain is composed of one or more <rule> blocks.
    
    <rule>
    
    # Each rule has a condition, formatting statements and an optional
    # 'flow' statement. If the condition is true, the rule is applied to
    # the data point and no further rules are checked (unless
    # flow=continue). If the condition is false, the next rule is checked.
    #
    # var(X) referrs to the value of variable X for the data point. Here 'intrachr' means intra-chromosomal.
    
    condition     = var(intrachr)
    
    # Any links that are intra-chromosomal will not be shown. Further rules are not tested.
    
    show          = no
    
    </rule>
    
    <rule>
    
    # This rule is applied to all remaining links, since its condition is always true.
    
    condition     = 1
    
    # The color of the link is set to the 2nd chromosome in the link
    # coordinate (link's end). Here eval() is required so that the
    # expression var(chr2) is evaluated (we want the result of var(chr2),
    # not the color named "var(chr2)"). Note that for conditions,
    # evaluation is automatic, but required for all other parameters.
    
    color         = eval(var(chr2))
    
    # After this rule is applied, the rule chain continues.
    
    flow          = continue
    </rule>
    
    <rule>
    
    # If the link's start is on hs1...
    
    condition     = from(hs1)
    
    # ...set the radial position of the link's start to be close to the ideogram.
    
    radius1       = 0.99r
    </rule>
    
    <rule>
    
    # Same as the rule above, but applies to the end of the link.
    
    condition     = to(hs1)
    
    # 'radius2' (like chr2, start2, end2) refers to the variable 'radius' of the end of the link.
    
    radius2       = 0.99r
    
    </rule>
    
    </rules>
    
    </link>
    
    </links>
    
    <<include ideogram.conf>>
    
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>                
    </image>
    
    <<include etc/colors_fonts_patterns.conf>> 
    
    <<include etc/housekeeping.conf>> 
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    # Ideogram position, fill and outline
    radius           = 0.90r
    thickness        = 20p
    fill             = yes
    stroke_color     = dgrey
    stroke_thickness = 2p
    
    # Minimum definition for ideogram labels.
    
    show_label       = yes
    # see etc/fonts.conf for list of font names
    label_font       = default 
    label_radius     = dims(image,radius) - 60p
    label_size       = 30
    label_parallel   = yes
    
    </ideogram>
``````
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = 1r
    color            = black
    thickness        = 2p
    
    # the tick label is derived by multiplying the tick position
    # by 'multiplier' and casting it in 'format':
    #
    # sprintf(format,position*multiplier)
    #
    
    multiplier       = 1e-6
    
    # %d   - integer
    # %f   - float
    # %.1f - float with one decimal
    # %.2f - float with two decimals
    #
    # for other formats, see https://perldoc.perl.org/functions/sprintf.html
    
    format           = %d
    
    <tick>
    spacing        = 5u
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 25u
    size           = 15p
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
