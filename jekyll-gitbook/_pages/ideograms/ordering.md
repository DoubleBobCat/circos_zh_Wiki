---
author: DoubleCat
date: 2025-04-11
layout: post
category: ideograms
title: Ordering
---

### lesson
Ideograms are ordered using the chromosomes_order field.

#### default order
The default order of ideogram display is the order of appearance in the
karyotype definition file. Display of individual ideograms can be toggled
using the chromosome field (see previous tutorial), but this field does not
influence the order of display. For this, the chromosomes_order field is used.

#### custom order - part 1 - absolute order
The simplest way to specify a new order is to exhaustively list the new order
of ideograms. For example,

```    
    chromosomes       = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    chromosomes_order = hs2,hs3,hs1,hs5,hs4,hs8,hs7,hs6
```
The new order is 2 3 1 5 4 8 7 6.

Note that the delimiter for the order field is a comma (,), whereas a
semicolon (;) is used for the list of ideograms to draw. The reason for this
will be explained later.

If you have a small number of ideograms, or your custom order is always fixed
then a full ordered list is practical. In cases where you want to adjust order
by specifying the position of one ideogram relative to another, a more complex
syntax for chromosomes_order is used.

#### custom order - part 2 - relative order
You can specify ideogram order for a subset of ideograms by specifying local
order. For example, to specify that hs4 should follow hs5,

```    
    chromosomes_order = hs5,hs4
```
In this case, the order is 1 2 3 6 5 4 7 8, which you may find surprising (the
fact that 6 comes before 5). When Circos parses a relative order, such as
hs5,hs4, it looks at the first named ideogram, in this case hs5, and uses that
as an anchor for ordering remaining ideograms in the order list. Since hs4 is
specified after hs5, Circos places hs4 immediately after hs5, but does not
move the original location of hs5. Since hs4 has been moved, the next ideogram
(hs6) takes its place.

In order to achieve order 1 2 3 5 4 6 7 8, you need to anchor on hs3.

```    
    chromosomes_order = hs3,hs5,hs4
```
Remember, the first named entry in the order list will be the anchor and this
should correspond to the ideogram that you don't want to move. The remaining
ideograms in the list will be relocated relative to the anchor.

#### custom order - part 3 - relative order with spacing
Instead of the chromosome ID, you can enter "-" in an order list to indicate
the next available ideogram. Here, the sense of "next" is relative to default
order.

The purpose of the wildcard "-" entry is to allow for additional flexibility
on ordering the ideograms. For example, to specify that hs2 should be the next
neighbour after hs3,

```    
    chromosomes_order = hs3,-,hs2
```
This order list would produce the order 4 5 3 1 2 6 7 8. Again, the result may
be a little surprising. What has happened is that the order request used hs3
as the anchor ideogram. Thus, the position of hs3 in the final order is not
altered (it comes 3rd). The next ideogram is "-", which is a wildcard that
indicates the next available ideogram, or hs1 since this is the first ideogram
that has not been specifically mentioned in the order list. Thus the local
order in the vicinity of hs3 is hs3, hs1, hs2. Since hs3 is 3rd, the first two
slots are replaced by the first available ideograms, hs4 and hs5.

If you want two ideograms to separate hs3 and hs2, then

```    
    chromosomes_order = hs3,-,-,hs2
```
would produce the order 5 6 3 1 4 2 7 8, anchoring on hs3. If however you
enter

```    
    chromosomes_order = hs2,-,-,hs3
```
then the anchor is hs2 and the order is 5 2 1 4 3 6 7 8.

You can intersperse wildcards with specific ideograms. For example

```    
    chromosomes_order = hs1,-,hs2,-,hs3
```
would produce 1 4 2 5 3 6 7 8. The wildcards are filled by the first available
ideograms that were not specifically ordered - these are hs4 and hs5.

You can place a wildcard as the first entry, to force an ideogram to appear
before your anchor. For example,

```    
    chromosomes_order = -,hs1,-,hs2,-,hs3
```
yields 4 1 5 2 6 3 7 8. In this case, the rule that the anchor's (here hs1)
position is unchanged is overridden by the fact that you've requested an
ideogram to appear in front of the anchor. Effectively, you have forced the
insertion of the first available ideogram before hs1.

#### custom order - part 4 - anchors
In addition to the "-" wildcard in the order list, you can use two additional
metacharacters: the ^ and anchors.indicatesthebeginningofthecircularmapand
indicates the end. Thus, to have hs5 appear as the first ideogram, it is
enough to say

```    
    chromosomes_order = ^,hs5
```
and the order will be 5 1 2 3 4 6 7 8. If you would like hs5 to appear last,

```    
    chromosomes_order = hs5,$
```
and now the order will be 1 2 3 4 6 7 8 5.

#### custom order - part 5 - multiple groups
Multiple order groups can be specified by using '|' as a delimiter. Each group
affects order local to its anchor (the first specified ideogram within the
group).

Consider the following order string,

```    
    chromosomes_order = hs3,hs2,|,hs8,hs1
```
and note the '|' that separates the two groups hs3,hs2 and hs8,hs1. The anchor
for the first group is hs3 and hs2 is ordered relative to it. The anchor for
the second group is hs8 and hs1 is ordered relative to it. The final order is
4 5 3 2 6 7 8 1.

When using multiple groups, wildcards can add additional flexibility. Consider
the following order string

```    
    chromosomes_order = hs3,-,hs2,|,-,hs8,hs1
```
Each group is evaluated independently, but in order of appearance. Thus, the
first wildcard is filled by hs4, which is the first ideogram that hasn't been
explicitly placed. The wildcard in the second group is the next available
ideogram, and that is hs5 (since hs4 has already been used by the previous
wildcard). The final order is 6 7 3 4 2 5 8 1.

The strength of specifying multiple groups is realized when you have a lot of
ideograms to draw, and want to specify order for several local sets of
ideograms without having to write down the order for all ideograms.

#### custom order - part 6 - multiple groups with anchors
Finally, you can combine wildcards, multiple groups and anchors in one string.
This can quickly yield a complex order string.

```    
    chromosomes_order = ^,-,hs5,hs2,|,hs4,hs3,|,hs7,$
```
The final order is 1 5 2 4 3 6 8 7.

When constructing a string with multiple groups, wildcards and anchors, each
individual rule must be fulfilled, or Circos exists with an error. It is your
responsibility to write down rules that describe a consistent global order.
For example, if the number of wildcards and ideograms in your order string is
larger than the number of ideograms you are drawing, Circos will produce an
error. For example, this string requires at least 8 ideograms

```    
    chromosomes_order = ^,-,hs5,hs2,|,hs4,-,-,hs3,|,hs7,$
```
and works with our example to produce an order 1 5 2 4 6 8 3 7\. However, if
one more wildcard is added

```    
    chromosomes_order = ^,-,hs5,hs2,|,hs4,-,-,-,hs3,|,hs7,$
```
we run out of ideograms to place and get an error

```    
    fatal error - chromosomes_order string cannot be processed because group hs7 
                  cannot be placed in the display. This may be due to more tags in 
                  the chromosomes_order field than ideograms.
```### images
![Circos tutorial image -
Ordering](/documentation/tutorials/ideograms/ordering/img/01.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    
    # to explicitly define what is drawn
    chromosomes                 = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    
    # absolute order - specify the order for all ideograms
    chromosomes_order           = hs2,hs3,hs1,hs5,hs4,hs8,hs7,hs6
    
    # relative order - 1 2 3 6 5 4 7 8
    # why does hs6 appear before hs5? The order requires that hs4 
    # come after hs5. In turn, the position of hs5 is its original position 
    # (i.e. 5th ideogram). Since the position of hs4 has been reserved
    # to come after hs5, the next unordered ideogram (hs6) is placed before
    # hs5 to make hs5 the 5th ideogram.
    #chromosomes_order = hs5,hs4
    
    # relative order - 1 2 3 5 4 6 8 7
    #chromosomes_order = hs3,hs5,hs4,hs6,hs8
    
    # relative order 4 2 3 5 6 7 8 1
    # chromosomes_order = ^,hs4,|,hs1,$
    
    # relative order 4 2 6 7 5 3 8 1
    #chromosomes_order = ^,hs4,|,hs5,hs3,|,hs1,$
    
    # line below will give an error because there are more entries (9)
    # in this ordered list than ideograms (8)
    # chromosomes_order = ^,-,hs5,hs2,|,hs4,-,-,-,hs3,|,hs7,$
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 4
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.0025r
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
    label_font       = bold
    # labels outside circle
    #label_radius     = dims(ideogram,radius) + 0.05r
    #labels inside circle
    label_radius     = dims(ideogram,radius) - 0.15r
    label_with_tag   = yes
    label_size       = 48
    label_parallel   = yes
    label_case       = upper
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
    skip_first_label = no
    skip_last_label  = no
    radius           = dims(ideogram,radius_outer)
    tick_separation  = 3p
    label_separation = 1p
    multiplier       = 1e-6
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 1u
    show_label     = no
    thickness      = 2p
    color          = dgrey
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = no
    thickness      = 3p
    color          = vdgrey
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 20p
    label_offset   = 10p
    format         = %d
    grid           = yes
    grid_color     = dgrey
    grid_thickness = 1p
    grid_start     = 0.5r
    grid_end       = 0.999r
    </tick>
    
    </ticks>
```
  

* * *
