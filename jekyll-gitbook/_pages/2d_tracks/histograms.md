---
author: DoubleCat
date: 2025-04-11
layout: post
category: 2d_tracks
title: Histograms
---

### lesson
Circos' histograms are a variation on the line plot. In a line plot, adjacent
points are connected by a straight line whereas in a histogram the points form
a step-like trace. To make a histogram, set `type=histogram`.

In line and scatter plots, the data point is placed at the midpoint of the
point's span. Thus, if you define a data point

```    
    hs1 1000 2000 0.5
```
the point will be plotted at position 1500. If your data associates a value
with a specific base pair position, set the start and end position to be the
same. For example,

```    
    hs1 1500 1500 0.5
```
In the histogram plot, however, the entire range 1000-2000 is used to define a
histogram bin with a value of 0.5.

#### extending bins
If you set `extend_bin=yes`, the bin's left and right sides are extended to
the mid-point between this and the neighbouring bin. This behaviour, in which
bins are extended to meet their neighbours, is the default setting. Explicitly
setting `extend_bin=yes` is not necessary (but useful if you want to toggle
this feature later).

For example, if you have data points

```    
    hs1 1000 2000 0.5
    hs1 5000 5500 0.25
    hs1 9000 9250 0.75
```
you set `extend_bin=yes`, the middle bin 5000-5500 will have its left side
extended to `avg(2000,5000)=3500` and its right side to `avg(5500,9000)=7250`.
Thus, even though the data spans are not contiguous, the histogram trace will
be contiguous across the three bins.

If you use `extend_bin=no`, then the histogram will have three bins, each
rising from the baseline of the plot.

The sample image for this tutorial section contains many histograms with a
variety of combinations of `extend_bin` and `fill_color`. You'll notice that
even if you set `extend_bin=no`, bins which abut (start/end are within 1bp of
each other) will be joined. This makes `extend_bin=no` useful to distinguish
regions where you have no data.

If your data set is very dense, the histogram can become very busy and
difficult to interpret. The histogram and line plots are most useful when the
angular distance between adjacent data points spans at least several pixels.

The histogram plot type is very effective for data sets which assign a
floating point to a span rather than a single genomic point. If your data is
very dense relative to your output scale, however, I suggest using the line
plot.

#### skipping data points
You can write a rule that skips certain data points using Perl's modulo `%`
operator. For example, if you have data points whose start/end coordinates
being every 250kb, but want to draw points only every 1Mb, you would set up a
rule like this

```    
    <rule>
    condition  = var(start) % 1Mb
    show       = no
    </rule>
```
The condition is the remainder of the bin's start value (250kb, 500kb, 750kb,
...) when divided by 1Mb. If `start` is a multiple of 1Mb, then the remainder
is zero and the rule fails. However, if `start` is not a multiple of 1Mb, the
remainder is positive and the rule applies show=no to the point, effectively
hiding the point. In order for this approach to work, your `start` must have a
common divisor.

#### coping with sampling rate
Regardless whether you create a bitmap or SVG image, it is not useful to draw
more data on the image than can be resolved given the image size. For example,
if your ideogram radius is 1000 pixels, the circumference at the ideograms is
about 6000 pixels. Thus, you have only 6000 distinguishable positions at which
data can be drawn (e.g. scatter plot, line plot, histogram, etc). If you
consider sub-pixels sampling that is made possible with anti-aliasing, then at
most you have about 12,000 positions. If your data samples values at more than
12,000 different locations, it will be be visible.

If your data set samples positions much more frequently than this maximum
resolvable number (e.g. at 1,000,000 different positions vs 12,000
distinguishable positions) you can easily run into trouble because (a) data
points or lines will stack and occlude each other or (b) Circos will run out
of memory. The reason why (b) can happen is because Circos is not optimized to
manage large amounts (millions) of data inputs.

To better manage large data sets within Circos, you can write a rule that
draws data at positions that are multiples of a value (e.g. 100kb). However,
Circos will still read in all the data values and try to store them in memory.

To avoid reading in all the data, use `skip_run` and `min_value_change`
parameters. The `skip_run` parameter, when set, makes Circos read in only the
first data point of a consecutive set of points with the same value. For
example,

```    
    <plot>
    skip_run = yes
    ...
    </plot>
``````    
    # data input
    chr1 100 200 0.25 # read in
    chr1 200 300 0.1  # read in
    chr1 300 400 0.1  # not read in
    chr1 400 500 0.1  # not read in
    chr1 500 600 0.1  # not read in
    chr1 600 700 0.3  # read in
```
The `min_value_change` parameter works similarly and requires that the nth
value that is read in must have its value difference (absolute difference is
used) by at least min_value_change from the (n-1)th value that is read in. For
example,

```    
    <plot>
    min_value_change = 5
    ...
    </plot>
``````    
    # data input
    chr1 100 200 1   # read in
    chr1 200 300 2   # not read in (difference = 1 < 5)
    chr1 300 400 5   # not read in (difference = 4 < 5)
    chr1 400 500 6   # read in     (difference = 5 >= 5)
    chr1 500 600 3   # not read in (difference = 3 < 5)
    chr1 600 700 13  # read in     (difference = 7 >= 5)
    chr1 
```
Note that even though the difference between the data points with values 3 and
13 is greater than min_value_change, because the data point with value 6 is
read in, the data point with value 3 is not because it does not pass the
minimum difference cutoff with the previously accepted value (6).

Even though these primitive data sampling methods are available, I strongly
suggest that you filter and average your data yourself, before using it as
input to Circos. You'll have complete control over what is displayed (e.g., in
the above example you might argue that the data point with value 3 should also
be displayed ... and I would tend to agree).

#### setting axis range
If you do not specify the axis range using `min/max` values, then the axis
will be scaled to span the full range of the data. You can set the axis range
explicitly. For example

```    
    min=-1
    max=0
```
will effectively hide any values outside this range.

#### hiding values
You can crop data values by setting the axis range, as shown above. For
example, if your data is in the range `[-1,1]` and you set

```    
    min=0
    max=1
```
then only the data in the subrange `[0,1]` will be shown. However, if you
would like to keep the original axis range, and supress display of a data
range you should use rules. The rule below will hide the display of negative
data.

```    
    <rules>
    <rule>
    condition  = var(value) < 0
    show       = no
    </rule>
    </rules>
```
#### axis orientation
By default, the y-axis is oriented outward. This means that smaller values are
closer to the center of the circle than larger ones. For histograms, the net
effect is that bins for positive values point outward and bins for negative
values point inward. This is a direct result of the fact that bins always drop
to y=0, if within display range, or to the axis end closer to y=0.

You can adjust the direction of the y-axis by using the orientation setting.
To make the y-axis point inward (larger values are closer to the center), use

```    
    orientation = in
```
The effect will be the same as flipping the sign on all your data values.

#### filling histograms
You can fill under the connecting line in a histogram by using `fill_color`.

```    
    fill_color = red
```
By combining two histograms together, one each for negative and positive data,
with different background colors, you can achieve visually appealing
separation between negative and positive values.

#### filling extended bins
Extended bins are filled and stroked according to the format of the original
bins. When bins are extended, those corresponding to the same signed value
(positive, or negative) abut. No stroke appears between this interface.
### images
![Circos tutorial image -
Histograms](/documentation/tutorials/2d_tracks/histograms/img/01.png) ![Circos
tutorial image -
Histograms](/documentation/tutorials/2d_tracks/histograms/img/03.png) ![Circos
tutorial image -
Histograms](/documentation/tutorials/2d_tracks/histograms/img/04.png) ![Circos
tutorial image -
Histograms](/documentation/tutorials/2d_tracks/histograms/img/05.png)
### configuration
#### circos.2.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    file* = circos.2.png
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1
    chromosomes_breaks          = -hs1:120-140
    
    #chromosomes_reverse = hs2
    
    # lots of histograms here - let's take it one at a time
    
    <plots>
    
    # tall histogram immediately inside the ideogram circle
    # background* parameters define a colored backdrop for this histogram
    # axes* define y-axes
    
    <plot>
    
    type      = histogram
    file      = data/6/histogram.rand.txt
    
    r1        = 0.9r
    r0        = 0.7r
    max       = 1
    min       = -1
    
    stroke_type = outline
    thickness   = 4
    color       = vdgrey
    extend_bin  = no
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    spacing   = 0.1r
    color     = lgrey
    thickness = 2
    </axis>
    </axes>
    
    <rules>
    <rule>
    use       = no
    condition = var(value) < 0
    show      = no
    </rule>
    <rule>
    #condition  = var(value) < 0
    condition  = 1
    #fill_color = lred
    fill_color = eval(sprintf("spectral-9-div-%d",remap_int(var(value),-1,1,1,9)))
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### circos.3.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    karyotype   = data/karyotype/karyotype.human.hg19.txt
    
    <image>
    <<include etc/image.conf>>
    file* = circos.3.png
    </image>
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1;hs2;hs3;hs4;hs5;hs6
    
    <plots>
    
    # Make all shared parameters central by including
    # them in the outer <plots> block. These values are
    # inherited by each <plot> block, where they can
    # be further overridden.
    
    type       = histogram
    extend_bin = no
    color      = black
    fill_under = yes
    thickness  = 2
    
    <plot>
    file = data/6/histogram.txt
    r0   = 0.8r
    r1   = 0.9r
    min  = 0.15
    max  = 0.3
    fill_color       = green
    background_color = lgreen
    <<include axis.conf>>
    <<include background.conf>>
    
    </plot>
    
    <plot>
    file = data/6/histogram.txt
    r0   = 0.6r
    r1   = 0.7r
    min  = -0.3
    max  = -0.15
    fill_color       = red
    background_color = lred
    <<include axis.conf>>
    <<include background.conf>>
    
    </plot>
    
    <plot>
    file = data/6/histogram.txt
    r0  = 0.7r
    r1  = 0.8r
    min = -0.15
    max = 0.15
    fill_color       = orange
    background_color = lorange
    <<include axis.conf>>
    <<include background.conf>>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### circos.4.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    file* = circos.4.png
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1
    chromosomes_breaks          = -hs1:120-140
    
    #chromosomes_reverse = hs2
    
    # lots of histograms here - let's take it one at a time
    
    <plots>
    
    # tall histogram immediately inside the ideogram circle
    # background* parameters define a colored backdrop for this histogram
    # axes* define y-axes
    
    <plot>
    
    type      = histogram
    file      = data/6/histogram.rand.txt
    
    r1        = 0.9r
    r0        = 0.7r
    max       = 1
    min       = -1
    
    stroke_type = outline
    thickness   = 4
    color       = vdgrey
    extend_bin  = no
    
    <backgrounds>
    <background>
    y1    = -0.5
    color = lred
    </background>
    <background>
    y0    = 0.5
    color = lgreen
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    spacing   = 0.1r
    color     = lgrey
    thickness = 2
    </axis>
    </axes>
    
    <rules>
    use = no
    <rule>
    condition  = var(value) < -0.5
    fill_color = red
    </rule>
    <rule>
    condition  = var(value) > 0.5
    fill_color = green
    </rule>
    </rules>
    
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
```
  

* * *

#### circos.conf
```    
    <<include colors_fonts_patterns.conf>>
    
    <<include ideogram.conf>>
    <<include ticks.conf>>
    
    <image>
    <<include etc/image.conf>>
    </image>
    
    karyotype   = data/karyotype/karyotype.human.txt
    
    chromosomes_units           = 1000000
    chromosomes_display_default = no
    chromosomes                 = hs1
    
    #chromosomes_reverse = hs2
    
    # lots of histograms here - let's take it one at a time
    
    <plots>
    
    type      = histogram
    thickness = 2
    
    # tall histogram immediately inside the ideogram circle
    # background* parameters define a colored backdrop for this histogram
    # axes* define y-axes
    
    <plot>
    
    show    = yes
    
    max_gap = 5u
    file    = data/6/snp.density.250kb.txt
    #file = hist.txt
    color   = vdgrey
    min     = 0
    max     = 0.015
    r0      = 0.8r
    r1      = 0.975r
    
    #fill_color  = red
    
    stroke_type = bin # outline | bin | both
    
    <backgrounds>
    <background>
    color = vvlgrey
    </background>
    </backgrounds>
    
    <axes>
    <axis>
    spacing = 0.1r
    color   = lgrey
    thickness = 2
    </axis>
    </axes>
    
    # color the histogram by value value and
    # only plot points every 2Mb
    
    <rules>
    
    <rule>
    condition    = var(value) > 0.006
    color        = dgreen
    fill_color   = green
    </rule>
    
    <rule>
    condition    = var(value) < 0.002
    color        = dred
    fill_color   = red
    </rule>
    
    </rules>
    
    </plot>
    
    # Dense histogram outside ideogram circle
    
    <plot>
    
    show    = yes
    
    file    = data/6/snp.density.txt
    z       = 5
    max_gap = 5u
    color   = black
    min     = 0
    max     = 0.015
    r0      = 1.075r
    r1      = 1.175r
    </plot>
    
    # precomputed average of previous histogram, drawn
    # underneath and filled under. The fill color is
    # adjusted based on value
    
    <plot>
    
    show       = yes
    
    file       = data/6/snp.density.1mb.txt
    max_gap    = 1u
    fill_under = yes
    fill_color = lgrey
    thickness  = 0
    min        = 0
    max        = 0.015
    r0         = 1.075r
    r1         = 1.175r
    
    <rules>
    <rule>
    condition  = var(value) > 0.006
    fill_color = lgreen
    </rule>
    <rule>
    condition  = var(value) > 0.004
    fill_color = lorange
    </rule>
    <rule>
    condition  = var(value) > 0.003
    fill_color = lred
    </rule>
    
    </rules>
    </plot>
    
    # histograms with randomly assigned values and
    # bin sizes, illustrating how Circos handles
    # variable-sized bins
    
    # simple outline - bins are not extended
    
    <plot>
    
    file       = data/6/hist.random.txt
    extend_bin = no
    color      = black
    min        = 0
    max        = 1
    r0         = 0.75r
    r1         = 0.79r
    </plot>
    
    # simple outline - bins are extended
    
    <plot>
    
    file  = data/6/hist.random.txt
    color = black
    min   = 0
    max   = 1
    r0    = 0.7r
    r1    = 0.74r
    </plot>
    
    # colored by value - bins are not extended
    
    <plot>
    
    file       = data/6/hist.random.2.txt
    extend_bin = no
    color      = black
    min        = 0
    max        = 1
    r0         = 0.65r
    r1         = 0.69r
    <rules>
    <rule>
    condition = var(value) > 0.9
    color = green
    </rule>
    <rule>
    condition = var(value) < 0.1
    color = red
    </rule>
    <rule>
    condition = var(value) > 0.45 && var(value) < 0.55
    color = orange
    </rule>
    </rules>
    </plot>
    
    # colored by value - bins are extended
    
    <plot>
    
    file  = data/6/hist.random.2.txt
    color = black
    min   = 0
    max   = 1
    r0    = 0.6r
    r1    = 0.64r
    <rules>
    <rule>
    condition = var(value) > 0.9
    color = green
    </rule>
    <rule>
    condition = var(value) < 0.1
    color = red
    </rule>
    <rule>
    condition = var(value) > 0.45 && var(value) < 0.55
    color = orange
    </rule>
    </rules>
    </plot>
    
    # filled under with grey, oriented out (default)
    
    <plot>
    
    file       = data/6/hist.random.3.txt
    z          = 5
    extend_bin = no
    color      = black
    fill_under = yes
    fill_color = lgrey
    min        = 0
    max        = 1
    r0         = 0.55r
    r1         = 0.59r
    </plot>
    
    # filled under with grey, oriented out (default) - bins are extended
    
    <plot>
    
    file       = data/6/hist.random.3.txt
    z          = 5
    color      = black
    fill_under = yes
    fill_color = lgrey
    min        = 0
    max        = 1
    r0         = 0.5r
    r1         = 0.54r
    </plot>
    
    # filled under with grey, oriented in
    
    <plot>
    file        = data/6/hist.random.4.txt
    z           = 5
    orientation = in
    color       = black
    fill_under  = yes
    fill_color  = lblue
    min         = 0
    max         = 1
    r0          = 0.46r
    r1          = 0.5r
    </plot>
    
    # filled under with orange, oriented out, 
    # complementary to the previous histogram
    #
    # here, I've used the previous histogram data
    # and remapped its value using a rule which
    # assigns a new data value new=1-old
    #
    # this remapping has the effect of making the
    # the histograms fit into one another (peak of one
    # fits exactly into valley of other)
    
    <plot>
    file       = data/6/hist.random.4.txt
    z          = 5
    color      = black
    fill_under = yes
    fill_color = orange
    min        = 0
    max        = 1
    r0         = 0.46r
    r1         = 0.5r
    <rules>
    <rule>
    condition  = 1
    value      = eval(1-var(value))
    </rule>
    </rules>
    </plot>
    
    # another random histogram, oriented in
    
    <plot>
    file        = data/6/hist.random.5.txt
    orientation = in
    color       = black
    fill_under  = yes
    fill_color  = orange
    min         = 0
    max         = 1
    r0          = 0.42r
    r1          = 0.46r
    </plot>
    
    <plot>
    file        = data/6/hist.random.5.txt
    orientation = in
    color       = black
    extend_bin  = no
    fill_under  = yes
    fill_color  = orange
    min         = 0
    max         = 1
    r0          = 0.36r
    r1          = 0.41r
    </plot>
    
    </plots>
    
    <<include etc/housekeeping.conf>>
    data_out_of_range* = trim
```
  

* * *

#### axis.conf
```    
    axis           = yes
    axis_color     = dgrey
    axis_thickness = 2
    axis_spacing   = 0.1
```
  

* * *

#### background.conf
```    
    background                  = yes
    background_stroke_color     = black
    background_stroke_thickness = 2
```
  

* * *

#### bands.conf
```    
    show_bands            = yes
    fill_bands            = yes
    band_stroke_thickness = 2
    band_stroke_color     = white
    band_transparency     = 0
```
  

* * *

#### ideogram.conf
```    
    <ideogram>
    
    <spacing>
    default = 0.01r
    break   = 0.5r
    </spacing>
    
    <<include ideogram.position.conf>>
    <<include ideogram.label.conf>>
    <<include bands.conf>>
    
    radius*       = 0.825r
    
    </ideogram>
``````
  

* * *

#### ideogram.label.conf
```    
    show_label       = yes
    label_font       = default
    label_radius     = dims(image,radius)-30p
    label_size       = 24
    label_parallel   = yes
    label_case       = lower
    label_format     = eval(sprintf("chr%s",var(label)))
``````
  

* * *

#### ideogram.position.conf
```    
    radius           = 0.775r
    thickness        = 30p
    fill             = yes
    fill_color       = black
    stroke_thickness = 2
    stroke_color     = black
```
  

* * *

#### rules.conf
```    
    <rules>
    <rule>
    condition  = var(value) < -0.5
    fill_color = red
    color      = dred
    </rule>
    <rule>
    condition  = var(value) < 0
    fill_color = orange 
    color      = dorange
    </rule>
    <rule>
    condition  = var(value) < 0.5
    fill_color = green
    color      = dgreen
    </rule>
    </rules>
```
  

* * *

#### ticks.conf
```    
    show_ticks          = yes
    show_tick_labels    = yes
    
    <ticks>
    
    radius           = dims(ideogram,radius_outer)
    orientation      = out
    label_multiplier = 1e-6
    color            = black
    size             = 20p
    thickness        = 3p
    label_offset     = 5p
    format           = %d
    
    <tick>
    spacing        = 1u
    show_label     = no
    size           = 10p
    </tick>
    
    <tick>
    spacing        = 5u
    show_label     = yes
    label_size     = 20p
    size           = 15p
    </tick>
    
    <tick>
    spacing        = 10u
    show_label     = yes
    label_size     = 24p
    </tick>
    
    </ticks>
```
  

* * *
