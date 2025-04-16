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

## 6\. Spacing and Axis Breaks

[Lesson](/documentation/tutorials/ideograms/spacing_breaks/lesson)
[Images](/documentation/tutorials/ideograms/spacing_breaks/images)
[Configuration](/documentation/tutorials/ideograms/spacing_breaks/configuration)

### ideogram spacing

Spacing between ideograms derived from different chromosomes is controlled by
the `default` parameter in <ideogram><spacing> block.

#### absolute spacing

This parameter may be set relative to chromosome units (suffixed with `u`).
For example, if `chromosomes_units=1000000` and the spacing value is `10u`,
then the actual spacing in the image will be 10Mb.

    
    
    <ideogram>
     <spacing>
      default = 10u
     </spacing>
    </ideogram>
    

#### relative spacing

You can also set the parameter to be relative to the total size of ideograms
in the image (suffix with `r`). This is useful if you would like to maintain a
fixed spacing between ideograms as you add/remove ideograms from the image.

    
    
    <ideogram>
     <spacing>
      default = 0.01r
     </spacing>
    </ideogram>
    

In this example, the spacing will be 1% of the size of all ideograms. This
will be close to 1% of the circumference of the image.

Use the absolute value format (e.g. `10u`), when you have created your
ideogram layout and want to adjust the spacing value to be visually compatible
with adjacent tick marks. For example, if you have major ticks every 5Mb, you
may want to set the spacing value to this.

Use the relative value format (e.g. `0.01r`), when you anticipate that you
will be adding/removing/cropping ideograms from the image but do not want the
spacing value to fluctuate.

### changing spacing between specific ideograms

Spacing between specific ideograms can be adjusted in <pairwise> block.

    
    
    <ideogram>
     <spacing>
      default = 10u
    
      <pairwise hs1>
       spacing = 5u
      </pairwise>
    
      <pairwise hs3 hs4>
       spacing = 0.25r
      </pairwise>
    
     </spacing>
    </ideogram>
    

When you specify the name of one ideogram, spacing on either side of it will
be affected. The first pairwise block creates `5u` spacing around `hs1`.

When you specify the names of two ideograms, the spacing between them is
affected. If you use relative spacing, it is interpreted to be relative to the
default spacing. Thus, `spacing=0.25r` between `hs3` and `hs4` will be 2.5u
(i.e. 25% of `10u`).

#### making room for a legend

To make room for a track legend, use the <pairwise> block to adjust spacing
between the ideograms at the top of the image and then `angle_offset` to
rotate the image to center the spacing along the vertical line.

    
    
    # ideogram.conf
    <ideogram>
     <spacing> 
      # spacing between ideograms is 0.1% of image
      default = 0.001r 
    
      <pairwise hsY hs1>
       # spacing between hsY and hs1 is 50x 0.1% of image
       spacing = 50r 
      </pairwise>
    
     </spacing>
    </ideogram>
    
    # circos.conf
    <image>
     # override angle_offset defined in etc/image.conf 
     angle_offset* = -82
     <<include etc/image.conf>>
    </image>
    

This example assumes that `hsY` and `hs1` are the last and first ideograms in
your image, flanking the 12 o'clock position.

By default, `angle_offset=-90`, which makes ideograms start at 12 o'clock
position. The image is rotated slightly clockwise by reducing this offset.
You'll need to determine this offset yourself—start at `-85` and then vary the
value up/down as required.

### axis breaks

When only a subregion of a chromosome is drawn, you have the option to place
axis breaks on the ideogram to indicate that the chromosome extent is larger
than shown in the figure.

There are two axis break styles, with style properties defined in
`break_style` blocks. The size of the axis break is controlled by the break
parameter and can be defined in absolute units (`u`) or relative to the
default spacing (`r`).

    
    
    <ideogram>
      block(spacing>
    
      default = 10u
      break   = 2u
    
      axis_break         = yes
      axis_break_style   = 2
      axis_break_at_edge = yes
    
      <break_style 1>
        stroke_color = black
        fill_color   = blue
        thickness    = 0.25r
        stroke_thickness = 2
      </break_style>
    
      <break_style 2>
        stroke_color     = black
        stroke_thickness = 3
        thickness        = 1.5r
      </break_style>
    
      </spacing>
    </ideogram>
    

If an ideogram does not begin at its chromosome start or end, you can choose
to place an axis break at the edge with `axis_break_at_edge=yes`.

The thickness parameter defines the radial extent of the break and can be
expressed relative to the thickness of the ideogram (e.g. `0.25r`) or in in
absolute pixel size (e.g. `100p`). Typically, break style 1 should have a
thickness <`1r` and style 2 should have a thickness >`1r`.

The axis break defined by style 1 uses a rectangle to join the ideogram across
the break. Style 2 uses two radial lines to indicate a break. The size of the
break is independent of spacing between two ideograms. Thus, if two
neighbouring ideograms have breaks at neighbouring ends, then the total space
between them is the sum of break sizes and ideogram spacing.

