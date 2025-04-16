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

# 3 — Drawing Ideograms

## 5\. Cropping

[Lesson](/documentation/tutorials/ideograms/cropping/lesson)
[Images](/documentation/tutorials/ideograms/cropping/images)
[Configuration](/documentation/tutorials/ideograms/cropping/configuration)

If you do not wish to have the entire ideogram drawn, you can choose to create
an axis break and remove a region from the display. This can be achieved in
two ways: specify what to draw, or specify what not to draw.

You should never use the [karyotype
file](https://mk.bcgsc.ca/circos/tutorials/lessons/ideograms/karyotypes) to
crop the ideograms. In other words, in the karyotype file the chromosome
start/end positions should reflect the physical chromosome size, not the
regions you wish to draw.

### specifying chromosome ranges

To specify what regions of an ideogram to draw, use the following syntax

    
    
    chromosomes = ...;ID:START-END;...
    

For example,

    
    
    chromosomes_units = 1000000
    chromosomes       = hs1:0-100;hs2:50-150;hs3:50-100;hs4;hs5;hs6;hs7;hs8
    

Will draw all 8 chromosomes, but only 0-100 Mb of hs1, 50-150Mb of hs2 and
50-100 Mb of hs3. The start and end ranges are given in units of
chromosomes_units.

### chromosomes_units

This parameter defines a multiplier which can be applied to many other
variable values within the configuration files. Some values have this
multiplier automatically applied (e.g. the display ranges in the chromosomes
parameter, like shown above). Other values require the use of the "u" suffix.
For example,

    
    
    spacing = 5u
    
    

In this case, this tick's spacing is 5u. If chromosomes_units=1000000, then
the tick spacing is 5Mb.

The chromosome units value can be defined in absolute terms, such as 1000000
(1Mb), or in relative terms, such as 0.005r. The relative definition is
calculated relative to the total size of all ideograms in the image. For
example, you show the entire human genome (3Gb) in the image, and use
chromosome_units=0.001r, then this is equivalent to a chromosome_units value
of 3Mb (0.001 * 3Gb).

The reason why the relative value is useful is to maintain relatively constant
(and sane!) spacing between elements that use the chromosomes_unit value (such
as ticks) when the number and size of ideograms changes in the image.

Let's look at a quick example. Suppose that you show the entire human genome
and you set chromosomes_units=0.001r. The unit multiplier is 0.001=1/1000 and
you are effectively dividing the image into 1000 slices (every 1Mb). If your
major ticks are spaced every 10u, then you will have a major tick every 10Mb
and there will be about 300 major ticks around your image. Now consider what
happens when you change the ideogram set to display, and let's say that you're
now showing only one ideogram whose size is 100Mb. If chromosomes_unit was
constant (1Mb) , then the tick mark spacing would still be 10Mb and you would
only have 10 major ticks. This may be too coarse a scale. However, if your
chromosomes_units value is relative (e.g. 0.001r), then your major tick marks
will be spaced every 10u = 10*(100*0.001) = 1Mb and you will have 100 major
ticks. Thus, even though you radically changed the extent of the data domain,
spacing of elements in the image relative to the image dimensions is
maintained.

### axis breaks

Axis breaks are defined in the <ideogram> block and will be covered in another
tutorial section. For now, take a look at the ideogram.conf file associated
with this section for a preview of how breaks are defined.

### supressing ranges

Instead of specifying what to draw, you can supress a range by using
chromosomes_breaks

    
    
    chromosomes = hs1;hs2;hs3;hs4;hs5;hs6;hs7;hs8
    chromosomes_breaks = -hs1:100-200;-hs2:0-50;-hs2:150-);-hs3:0-50
    

Each of the entries in chromosomes_breaks must be preceeded by a "-" and
specifies a range to exclude from the final image. You can specify multiple
ranges for a chromosome. Use ")" to indicate the end of the chromosome (e.g.,
-hs2:150-) supresses drawing from 150 Mb to the end of the chromosome).

### combining region declarations

You can combine region declarations in "chromosomes" and "chromosomes_breaks"
fields. For example,

    
    
    chromosomes = hs1:0-100;hs2:0-100;hs3:0-100;hs4:0-100;hs5;hs6;hs7;hs8
    chromosomes_breaks = -hs1:25-75;-hs2:25-75;-hs3:25-75;-hs4:25-75;-hs5:75-);-hs6:75-);-hs7:75-);-hs8:75-)
    

