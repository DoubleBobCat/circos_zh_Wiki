---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Naming Names
---

## Naming Names
### lesson
One of the first uses of Circos in popular print was Jonathan Corum's [Naming
Names](https://www.nytimes.com/interactive/2007/12/15/us/politics/DEBATE.html)
graphic in the New York Times, which visualized the names used by major
presidential candidates in the series of Democratic and Republican debates
leading up to the Iowa caucuses.

This tutorial shows you how to create this kind of image.

#### not just for genomics
[Jonathan Corum describes the use of Circos for this
graphic](https://www.nytimes.com/2008/02/25/business/media/25asktheeditors.html?pagewanted=5&_r=1):

_The circle design was created with an impressive piece of software called
Circos, which was originally built to visualize genomic data. To make it work
I had to encode the entire series of debates as if it was a genome. So each
presidential candidate was a chromosome, and each debate was a chromosome
band, and each spoken word was a nucleotide. It sounds a bit ridiculous, but
that was all behind the scenes. The end result is a fairly simple interactive
graphic, but hopefully one that caught the eye and allowed readers to find
patterns across the long series of debates._

The most difficult part of creating a Circos image—any visualization for that
matter—is deciding what data to show. Chances are your data is too complex to
show (e.g. its native format doesn't have a trivial visual encoding, such as a
scatter plot).

Mapping data onto a Circos figure requires that you identify what patterns in
your data are (a) likely to be important and (b) likely to be present, and
create a figure that exposes such patterns. Remember, if the pattern exists,
you can't afford to miss it. If it doesn't exist, you can't afford to be
fooled into thinking that it's there, or left wondering whether it's occluded
by other data.

If you don't know where to start when creating Circos images from genomic and
non-genomic data, look through [published examples from the
literature](/images/scientific_literature/). Find images whose patterns map
onto your data types.

Don't think necessarily from the point of view of how to construct input
files. First, identify what you want to show and how. Make a sketch of the
kind of figure you want to make. This is the hard part.

#### karyotype file
In the [Ideograms Tutorial](/documentation/tutorials/ideograms/ideograms/) I
have briefly mentioned that ideograms can be used to depict any axis, not just
a stretch of sequence like a chromosome or contig. In this example, the
segments correspond to a candidate's total word delivery during all debates.

The karyotype file defines these segments. For example, we'll say that Obama
delivered 2,000 words, Richardson 1,000 words, and so on. The actual values
would probably be much higher.

```    
    # karyotype.txt
    chr - obama obama 0 2000 dem
    chr - richardson richardson 0 1000 dem
    chr - clinton clinton 0 1500 dem
    chr - mccain mccain 0 1000 rep
    chr - romney romney 0 1750 rep
    chr - huckabee huckabee 0 1250 rep
```
The last field sets the color of the segments, according to the typical
blue/red scheme for republicans and democrats. I've used the RGB values used
by Jonathan.

```    
    <<include etc/colors_fonts_patterns.conf>>
    
    # append to the colors block
    <colors>
    rep = 211,121,111
    dem = 85,143,190
    </colors>
```
#### segment slices
Each segment is divided into slices. The slice represents the number of words
delivered in a specific debate.

```    
    # slices.txt
    obama 0 300     # Obama's 1st debate words
    obama 301 750   #         2nd
    obama 751 950   #         3rd
    obama 951 1250  #         4th
    obama 1251 1500 #         5th
    obama 1501 2000 #         6th
```
These slices are drawn as hollow highlights on top of the ideograms, with a
thick white outline.

```    
    <plot>
    file  = slices.txt
    type  = highlight
    r0    = dims(ideogram,radius_inner)
    r1    = dims(ideogram,radius_outer)
    fill_color       = undef
    stroke_color     = white
    stroke_thickness = 5
    </plot>
```
#### naming names
When a candidate mentions the name of another candidate during his speech, we
draw a link. The link starts at the debate slice in which the other candidate
name is mentioned. The link ends at the center of the segment of the mentioned
candidate.

```    
    # links.txt
    # Obama mentions Clinton in his 1st debate
    obama 150 150 clinton 750 750
    # McCain mentions Clinton in his 3rd debate
    mccain 875 875 clinton 750 750
    # Huckabee mentions Clintin in his 2nd debate
    huckabee 525 525 clinton 750 750
```
By default, the link color is set to `rep`, which is the republican red.

```    
    <link>
    file      = links.txt
    radius    = dims(ideogram,radius_inner)
    bezier_radius = 0r
    thickness = 5
    color     = rep 
    ...
```
A rule is added to change the link color to `dem` if the refering candidate is
a democrat.

```    
    <rules>
    <rule>
    # set dem color if start is on a democrat
    condition = var(chr1) =~ /obama|richardson|clinton/
    color     = dem
    </rule>
    </rules>
```
#### focusing on a candidate
To show links from a given candidate, use the `from()` function which returns
the name of the starting segment.

```    
    <rule>
    # only links from obama are shown (all others are hidden by setting show=no)
    # the condition test is equivalent to
    #   var(chr1) ne "obama"
    condition = ! from(obama)  
    show      = no
    </rule>
```
Or, to test the identity of the segment at the end of the link, use the `to()`
function.

```    
    <rule>
    # only links to mccain are shown (all others are hidden by setting show=no)
    # the condition test is equivalent to
    #   var(chr2) ne "mccain"
    condition = ! to(mccain)
    show      = no
    </rule>
```
Use the `fromto()` function to test both ends

```    
    <rule>
    # only links from obama to mccain are shown (all others are hidden by setting show=no)
    # the condition test is equivalent to
    #   var(chr1) ne "obama" || var(chr2) ne "mccain"
    condition = ! fromto(obama,mccain)
    show      = no
    </rule>
```### images
![Circos tutorial image - Naming
Names](/documentation/tutorials/recipes/naming_names/img/00.png)
### configuration
#### circos.conf
```    
    <<include etc/colors_fonts_patterns.conf>>
    
    <colors>
    rep = 211,121,111
    dem = 85,143,190
    </colors>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    chromosomes_units           = 1
    chromosomes_display_default = yes
    
    karyotype = karyotype.txt
    
    <links>
    <link>
    file      = links.txt
    radius    = dims(ideogram,radius_inner)
    bezier_radius = 0r
    thickness = 5
    color     = rep # make it republican, by default
    <rules>
    <rule>
    # set dem color if start is on a democrat
    condition = var(chr1) =~ /obama|richardson|clinton/
    color     = dem
    </rule>
    </rules>
    </link>
    
    </links>
    
    <plots>
    
    <plot>
    file  = slices.txt
    type  = highlight
    r0    = dims(ideogram,radius_inner)
    r1    = dims(ideogram,radius_outer)
    fill_color       = undef
    stroke_color     = white
    stroke_thickness = 5
    </plot>
    
    <plot>
    z    = 10
    type = highlight
    file = axis.txt
    r0   = dims(ideogram,radius_outer) - 2p
    r1   = dims(ideogram,radius_outer) + 3p
    fill_color = black
    </plot>
    </plots>
    
    <<include etc/housekeeping.conf>>
    track_defaults* = undef
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    
    default = 0.01r
    
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-70p
    label_with_tag   = yes
    label_size       = 40
    label_parallel   = yes
    label_case       = upper
```
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.90r
    thickness        = 150p
    fill             = yes
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius           = dims(ideogram,radius_outer)
    multiplier       = 1
    color            = black
    thickness        = 4p
    size             = 20p
    
    <tick>
    spacing        = 100u
    </tick>
    
    </ticks>
```
  

* * *
