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

## 6\. <ideogram> block

You are strongly encouraged to use the default image block from the Circos
distribution (`etc/image.conf`), rather than rolling your own. Override any
parameters with the `*` suffix.

    
    
    ################################################################
    # circos.conf
    <<include ideogram.conf>>
    
    ################################################################
    # ideogram.conf
    <ideogram>
     ...
    </ideogram>
    

### syntax

    
    
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
    

### block parameters

**Flags** R required, + multiple instances allowed.

**Units** Parameters that require units (`p` pixel, `r` relative, `u` value of
`chromosomes_units`) have acceptable units listed in brackets (e.g. `[p]`,
`[pr]`).

**Expressions** All parameters can be defined by an expression or code to be
evaluated with `eval()`.

**Defaults** Default values will be used for any required parameters that are
missing. If no default value is available, Circos will exit with an error.

parameter

description

examples

  

`<spacing>` R

Ideogram spacing.  
PARENT  
`<ideogram>`  
CHILDREN  
`<pairwise>`, `<break_style>`  

  

`spacing`

Spacing between ideogram pair defined by the block.  
VALUE `FLOAT [ur]`

`0.25u`  
`0.5r`

  

`<break_style>` R

Axis break styles.  
PARENT  
`<ideogram>`

  

`<rules>`

Format rules.  
PARENT  
`<ideogram>`  
CHILDREN  
`<rule>`  

  

parameter

description

examples

  

`show` R

Toggle the display of ideograms. If ideograms are not shown, neither are ticks
or grids.  
VALUE `yes|no`  
DEFAULT `yes`

  

`radius` R

Radial position of ideograms. Relative position is relative to image size.  
VALUE `INT [pr]`

`0.9r`  
`750p`

  

`thickness` R

Radial thickness of ideogram segments. Relative thickness is relative to image
size.  
VALUE `FLOAT [pr]`

`15p`  
`0.02r`

  

`thickness`

Radial extent of axis break. Relative extent is relative to ideogram
thickness.  
VALUE `INT [rp]`

`25p`  
`2r`

  

`fill` R

Toggles fill of ideogram segments using color defined in karytoype file.  
VALUE `yes|no`  
DEFAULT `yes`  
TUTORIALS [ideograms/karyotype](/documentation/tutorials/ideograms/karyotype)  

  

`stroke_color`

Color of outline for ideogram segments.  
VALUE `COLOR`  
REQUIRES `stroke_thickness`  
REQUIRED BY `stroke_thickness`

`black`

  

`stroke_color`

Color of stroke on axis break.  
VALUE `COLOR`  
REQUIRES `stroke_thickness`  
REQUIRED BY `stroke_thickness`

`dgrey`

  

`stroke_thickness`

  
VALUE `INT [p]`  
REQUIRES `stroke_color`  
REQUIRED BY `stroke_color`

`2p`

  

`stroke_thickness`

Thickness of stroke on axis break.  
VALUE `INT [p]`  
REQUIRES `stroke_color`  
REQUIRED BY `stroke_color`

`2p`

  

### cytogenetic bands

parameter

description

examples

  

`show_bands`

Toggles the display of cytogenetic bands. Bands are defined in the karytoype
file.  
VALUE `yes|no`

  

`fill_bands`

Toggles fill of the cytogenetic bands using the color defined in the karyotype
file.  
VALUE `yes|no`

  

`band_transparency`

Transparency of cytogenetic band fill.  
VALUE `INT`  
TUTORIALS [ideograms/karyotype](/documentation/tutorials/ideograms/karyotype)  

  

`band_stroke_thickness`

Thickness of outline for cytogenetic bands.  
VALUE `INT [p]`  
REQUIRES `band_stroke_color`  
REQUIRED BY `band_stroke_color`

`2p`

  

`band_stroke_color`

Color of outline for cytogenetic bands.  
VALUE `COLOR`  
REQUIRES `band_stroke_thickness`  
REQUIRED BY `band_stroke_thickness`

`dgrey`

  

### ideogram label

parameter

description

examples

  

`show_label`

Toggles the display of ideogram labels.  
VALUE `yes|no`  
TUTORIALS [ideograms/labels](/documentation/tutorials/ideograms/labels)  

  

`label_radius`

Radial position of ideogram label.  
VALUE `FLOAT [rp]`

`1.1r`  
`1r+50p`  
`800p`  
`dims(image,radius)-25p`

  

`label_size`

Size of ideogram label, in pixels.  
VALUE `INT`

`24`

  

`label_font`

Font of ideogram label.  
VALUE `FONT`  
DEFAULT `default`

`default`  
`bold`  
`condensed`

  

`label_parallel`

Toggles the ideogram label to be parallel to the ideogram segment.  
VALUE `yes|no`

  

`label_with_tag`

Toggles presence of ideogram tag in the label. Tags uniquely identify
ideograms from the same chromosome and are defined in the `chromosomes`
parameter.  
VALUE `yes|no`

  

`label_case`

Case of ideogram label.  
VALUE `upper|lower`

  

`label_format`

Format of ideogram label.  
VALUE `EXPR`

`eval(sprintf("chr%s",var(label)))`

  

### axis breaks

**Tutorial** [Spacing & Axis
Breaks](/documentation/tutorials/ideograms/spacing_breaks).

parameter

description

examples

  

`axis_break`

Toggles display of axis breaks.  
VALUE `yes|no`  
REQUIRES `<break_style`>  
TUTORIALS [ideograms/cropping](/documentation/tutorials/ideograms/cropping),
[ideograms/spacing_breaks](/documentation/tutorials/ideograms/spacing_breaks)  

  

`axis_break_style`

Axis break style to use.  
VALUE `1|2`  
REQUIRES `<break_style`>  
TUTORIALS [ideograms/cropping](/documentation/tutorials/ideograms/cropping),
[ideograms/spacing_breaks](/documentation/tutorials/ideograms/spacing_breaks)  

  

`axis_break_at_edge`

Toggles display of axis break at edge of cropped ideogram.  
VALUE `yes|no`  
REQUIRES `<break_style`>  
TUTORIALS [ideograms/cropping](/documentation/tutorials/ideograms/cropping),
[ideograms/spacing_breaks](/documentation/tutorials/ideograms/spacing_breaks)  

  

### <spacing> block

**Tutorial** [Spacing & Axis
Breaks](/documentation/tutorials/ideograms/spacing_breaks).

parameter

description

examples

  

`<pairwise>` R

Ideogram spacing for specific ideogram pairs.  
PARENT  
`<spacing>`

  

`default` R

Spacing between ideograms. Relative spacing is relative to circumference of
ideogram circle.  
VALUE `FLOAT [ur]`  
TUTORIALS
[ideograms/spacing_breaks](/documentation/tutorials/ideograms/spacing_breaks)  

`0.5u`  
`0.01r`

  

`break` R

Size of axis break. Relative size is relative to ideogram spacing.  
VALUE `FLOAT [ur]`  
TUTORIALS
[ideograms/spacing_breaks](/documentation/tutorials/ideograms/spacing_breaks)  

`0.25u`  
`0.5r`

  

### <pairwise> block

**Tutorial** [Spacing & Axis
Breaks](/documentation/tutorials/ideograms/spacing_breaks).

The name of the block defines to which ideogram pair the spacing applies.

    
    
    # adjust spacing between chr1 and chr2
    <pairwise chr1 chr2>
    </pairwise>
    
    # adjust spacing around chr1
    <pairwise chr1>
    </pairwise>
    

parameter

description

examples

  

`<spacing>` R

Ideogram spacing.  
PARENT  
`<ideogram>`  
CHILDREN  
`<pairwise>`, `<break_style>`  

  

`spacing`

Spacing between ideogram pair defined by the block.  
VALUE `FLOAT [ur]`

`0.25u`  
`0.5r`

  

### <break_style> block

**Tutorial** [Spacing & Axis
Breaks](/documentation/tutorials/ideograms/spacing_breaks).

This block defines one of two types of axis break styles.

    
    
    # style 1 definition
    <break_style 1>
    </break_style>
    
    # style 2 definition
    <break_style 2>
    </break_style>
    

The style to be used is defined by `axis_break_style`.

parameter

description

examples

  

`stroke_thickness`

Thickness of stroke on axis break.  
VALUE `INT [p]`  
REQUIRES `stroke_color`  
REQUIRED BY `stroke_color`

`2p`

  

`stroke_color`

Color of stroke on axis break.  
VALUE `COLOR`  
REQUIRES `stroke_thickness`  
REQUIRED BY `stroke_thickness`

`dgrey`

  

`thickness`

Radial extent of axis break. Relative extent is relative to ideogram
thickness.  
VALUE `INT [rp]`

`25p`  
`2r`

  

`fill_color`

Fill color of axis break. Used for <break_style 1>.  
VALUE `COLOR`

`black`

  

