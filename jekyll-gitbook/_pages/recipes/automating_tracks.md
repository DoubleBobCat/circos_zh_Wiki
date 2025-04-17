---
author: DoubleCat
date: 2025-04-11
layout: post
category: recipes
title: Automating Tracks
---

## Automating Tracks
### lesson
If you are displaying a large number of similar tracks (e.g. 20 histograms),
which are similarly formatted, you can automate the generation of these tracks
using dynamic configuration variables and counters. This situation applies to
figures created from multiple samples (e.g. 20 cancer genomes), which each
have the same kind of data type (e.g. CNV).

This is an advanced method, but well worth studying. It will save you time and
keep the configuration files sane. An exciting feature!

Before you continue, make sure that you're familiar with the include()
mechanism in configuration files, which imports content from other files. This
is briefly mentioned in the [Best Practices
Tutorial](/documentation/tutorials/reference/best_practices/) and in detail in
the [Configuration File
Tutorial](/documentation/tutorials/configuration/configuration_files/).

#### Dynamic Configuration Variables
In order to use counters, you will need to know how to refer to configuration
file parameters by name within the configuration file. For example, if you
have a configuration parameter named `myparameter`, you need to know how to
use its value in another parameter.

This is done using `conf()` function. Anywhere in the configuration file,
values of other parameters can be accessed using this function. For example,

```    
    param1 = 10
    # assigns value of param1 to param2
    param2 = conf(param1)
```
The argument to the `conf()` function is the full block path of the parameter,
provided as a comma-delimited list. To access the value of a parameter
`param1` in <myblock>, you would use `conf(myblock,param1)`.

```    
    <myblock>
    param1 = 10
    </myblock>
    
    <anotherblock>
    param2 = conf(myblock,param1)
    </myblock>
```
If your parameter is buried several blocks deep, list the path like this
`conf(myblock1,myblock1a,myblock1aa,param1)`.

```    
    <myblock1>
     <myblock1a>
      <myblock1aa>
       param1 = 10
      </myblock1aa>
     </myblock1a>
    </myblock1>
```
#### evaluatable configuration parameters
Configuration parameters can be based on an expression. To evaluate the value
of a parameter as an expression (Circos won't automatically detect whether a
parameter value is an expression), you need to wrap the parameter value in
`eval()`

```    
    color = eval("b"."l"."u"."e")
```
These can be combined using

```    
    <myblock>
     global_color = blue
    </myblock>
    
    color = eval(conf(myblock,global_color) . "_a5")
```
The expression is expected to be Perl code.

#### Counters
##### Automatic Counters
When <plot>, <link> and <highlight> blocks are parsed by Circos, you have
access to the index of each track through a counter accessed by
`counter(TYPE)`, where `TYPE` is one of `plot`, `link`, or `highlight`. The
counter value starts at `0` for the first block of a given `TYPE` and is
incremented by `1`.

The `counter(TYPE)` function is a shortcut for `conf(counter,TYPE)`.

The counter variables are provided to you automatically.

For example,

```    
    <plots>
    
    <plot>
    # value of counter(plot) = 0
    ...
    </plot>
    
    <plot>
    # value of counter(plot) = 1
    ...
    </plot>
    
    <plot>
    # value of counter(plot) = 2
    ...
    </plot>
    
    ... 
    
    </plots>
    
    <links>
    
    <link>
    # value of counter(link) = 0
    ...
    </link>
    
    <link>
    # value of counter(link) = 1
    ...
    </link>
    
    <link>
    # value of counter(link) = 2
    ...
    </link>
    
    ...
    
    </links>
``````
These counters can be used to dynamically adjust the track parameters based on
their order of appearance in the configuration file. This is extremely useful
for stacking multiple tracks—you only need to define track width and spacing
and the position of the first track, and the rest will be automatically
placed.

By default, the automated counters are incremented by 1 (remember that their
count starts at `0`). If you want to change the increment, use

```    
    <plot>
    post_increment_counter = 2
    ...
    </plot>
```
This is the value that the `plot` counter will be incremented once this
particular <plot> has been parsed. Thus,

```    
    <plots>
    
    <plot>
    # counter(plot) = 0
    ...
    post_increment_counter = 2
    </plot>
    
    <plot>
    # counter(plot) = 2
    ...
    post_increment_counter = 5
    </plot>
    
    <plot>
    # counter(plot) = 7
    ...
    </plot>
    
    <plot>
    # counter(plot) = 14
    ...
    </plot>
    
    </plots>
```
If you specify `post_increment_counter`, this value will be used for all other
blocks of the same `TYPE`, unless you redefine the value.

You can play tricks by setting this increment to a random value. Here the
counter increment will be 1, 2 or 3.

```    
    <plot>
    post_increment_counter = eval(1+int(rand(3)))
    ...
    </plot>
```
Counters are available for all blocks. Typically, you'll use counters in
<plot>, <link> and <highlight> blocks. In the case where you only have a
single block (e.g. <ideogram>), the counter value is always 0.

##### Custom Counters
You can set and change custom counters within any block using the following
parameters

  * `init_counter = counter_name:value`
  * `pre_set_counter = counter_name:value`
  * `post_set_counter = counter_name:value`
  * `pre_increment_counter = counter_name:value_increment`
  * `post_increment_counter = counter_name:value_increment`

If you omit `counter_name`, Circos will assume that you are refering to the
block's default counter (e.g. plot, link or highlight).

For example,

```    
    <plots>
    
    <plot>
    
    # set the value of the counter before this block is parsed
    pre_set_counter = mycounter:5
    
    # inside the block
    # counter(mycounter) = 5
    
    # set the value after parsing this block
    post_set_counter = mycounter:10
    ...
    </plot>
    
    <plot>
    
    # counter(mycounter)=11 before this block is parsed (previous value +1)
    pre_increment_counter = mycounter:1
    
    # counter(mycounter) = 11
    
    # set the increment to add to counter after parsing this block
    post_increment_counter = mycounter:2
    ...
    </plot>
    
    <plot>
    
    # counter(mycounter) = 13
    ...
    
    </plot>
    
    ...
    
    </plots>
```
The purpose of custom counters is allow more than one counter.

To set a counter value initially, use `init_counter`. This initalization will
only happen the first time it is seen—it does nothing if the counter is
already defined. To change the value of a counter that has already been
defined, use `pre_set_counter` or `post_set_counter`.

#### Automating Track Placement and Formatting
Let's create a figure with 16 histograms. Each will be automatically
incrementally placed and formatted.

First, I created 16 different random data files `histogram.0.txt` ...
`histogram.15.txt` to act as source data files.

I'd like the first track to start at `0.925r`, and each track to have a width
of `0.055r` with track baselines separated by `0.06`. These variables are
defined in the root of the configuration file.

```    
    track_width   = 0.055
    track_start   = 0.925
    track_step    = 0.06
```
The actual definition of each track will be the same, because all parameters
will be automatically generated using the plot counter.

Below is the track definition. It looks complicated. Each parameter is an
expression in terms of the automatic counter `counter(plot)` and the custom
counter `counter(thickness)`.

Above each definition, I list the values of the parameter for each successive
plot block.

```    
    <plot>
    # histogram.0.txt, histogram.1.txt, histogram.2.txt, ...
    file    = data/8/16/histogram.counter(plot).txt
    
    # 0.925, 0.925-0.06, 0.0925-2*0.06, ...
    r0      = eval(sprintf("%fr",conf(track_start) -
    			     counter(plot) * conf(track_step) ))
    
    # 0.925+0.055, 0.925+0.55-0.06, 0.0925+0.55-2*0.06, ...
    r1      = eval(sprintf("%fr",conf(track_start) +
     	                     conf(track_width) - 
    			     counter(plot) * conf(track_step)))
    
    # in, out, in, out, ...
    orientation = eval( counter(plot) % 2 ? "in" : "out" )
    
    # spectral-11-div-1, spectral-11-div-2, spectral-11-div-3, ...
    fill_color  = eval(sprintf("spectral-11-div-%d",counter(plot)%11+1))
    
    # 8, 8, 7, 7, 6, 6, ...
    thickness   = eval(max(1,8-int(counter(thickness))))
    # 0, 0.5, 1, 1.5, ...
    post_increment_counter = thickness:0.5
    # vvvlgrey, vvlgrey, vlgrey, ...
    background_color = eval((qw(vvvlgrey vvlgrey vlgrey lgrey grey dgrey vdgrey vvdgrey))[counter(plot) % 8])
    
    <rules>
    <rule>
    condition  = var(value) > 0.25 && var(value) < 0.75
    show = no
    </rule>
    </rules>
    
    </plot>
```
Because each plot track definition is the same, it is convenient to store this
in a separate configuration file (e.g. `plot.conf`) and include as many copies
of this block in the main configuration as required

```    
    <plots>
    # global settings
    ...
    
    # multiple plot block definitions
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    ...
    
    </plots>
``````### images
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_tracks/img/image-01.png)
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_tracks/img/image-02.png)
![Circos tutorial image - Automating
Tracks](/documentation/tutorials/recipes/automating_tracks/img/image-03.png)
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
    
    chromosomes = hs1;hs2;hs3;hs4;hs5;hs6
    
    track_width   = 0.055
    track_start   = 0.925
    track_step    = 0.06
    
    <plots>
    
    type       = histogram
    color      = black
    extend_bin = no
    min        = 0
    max        = 1
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    <<include plot.conf>>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### file.conf
```    
    file = data/8/16/histogram.counter(plot).txt
```
  

* * *

#### fillcolor.conf
```    
    fill_color = eval(sprintf("spectral-11-div-%d",counter(plot)%11+1))
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    show = no
    
    <spacing>
    
    default = 0u
    
    </spacing>
    
    # thickness (px) of chromosome ideogram
    thickness        = 20p
    stroke_thickness = 2
    # ideogram border color
    stroke_color     = black
    fill             = yes
    # the default chromosome color is set here and any value
    # defined in the karyotype file overrides it
    fill_color       = black
    
    # fractional radius position of chromosome ideogram within image
    radius         = 0.85r
    show_label     = no
    label_with_tag = yes
    label_font     = default
    label_radius   = dims(ideogram,radius) + 0.075r
    label_size     = 60p
    
    # cytogenetic bands
    band_stroke_thickness = 2
    
    # show_bands determines whether the outline of cytogenetic bands
    # will be seen
    show_bands            = yes
    # in order to fill the bands with the color defined in the karyotype
    # file you must set fill_bands
    fill_bands            = yes
    
    </ideogram>
``````
  

* * *

#### plot.conf
```    
    <plot>
    
    post_increment_counter = 1 # applies to default block counter (i.e. plot)
    init_counter           = thickness:0
    thickness              = eval(max(1,8-int(counter(thickness))))
    post_increment_counter = thickness:0.5
    
    <<include file.conf>>
    <<include r0r1.conf>>
    <<include fillcolor.conf>>
    <<include rules.conf>>
    
    <backgrounds>
    <background>
    color       = eval((qw(vvvlgrey vvlgrey vlgrey lgrey grey dgrey vdgrey vvdgrey))[counter(plot) % 8])
    </background>
    </backgrounds>
    </plot>
```
  

* * *

#### r0r1.conf
```    
    r0      = eval(sprintf("%fr",conf(track_start)-counter(plot)*conf(track_step)))
    r1      = eval(sprintf("%fr",conf(track_start)+conf(track_width)-counter(plot)*conf(track_step)))
    orientation = eval( counter(plot) % 2 ? "in" : "out" )
```
  

* * *

#### rules.conf
```    
    <rules>
    
    # If you wish, you can generate the random
    # values for each histogram automatically
    # using this rule. Don't forget to set
    # flow=continue so that rule testing
    # doesn't short-circuit.
    #<rule>
    #condition  = 1
    #value      = eval(rand())
    #flow       = continue
    #</rule>
    
    <rule>
    condition  = var(value) > 0.25 && var(value) < 0.75
    #fill_color = white
    show = no
    </rule>
    </rules>
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    radius               = dims(ideogram,radius_outer)
    multiplier           = 1e-6
    
    <tick>
    spacing        = 5u
    size           = 10p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 24pp
    label_offset   = 5p
    format         = %d
    </tick>
    
    <tick>
    spacing        = 20u
    size           = 16p
    thickness      = 3p
    color          = black
    show_label     = yes
    label_size     = 30p
    label_offset   = 5p
    format         = %d
    </tick>
    
    </ticks>
```
  

* * *
