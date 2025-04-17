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

## 5\. <image> block

You are strongly encouraged to use the default image block from the Circos
distribution (`etc/image.conf`), rather than rolling your own. Override any
parameters with the `*` suffix.

    
    
    ################################################################
    # circos.conf
    <image>
    <<include etc/image.conf>>
    # now override as necessary
    radius*           = 750p
    auto_alpha_steps* = 10
    </image>
    

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

  

`dir` R

Output file directory  
VALUE `DIR`

`.`  
`/tmp`

  

`file` R

Output file name. Appropriate extension will be added.  
VALUE `FILE`

`repeats.png`

  

`png` R

Toggles creation of PNG file. To suppress this on the command line, use
`-nopng`.  
VALUE `yes|no`  
DEFAULT `yes`

  

`svg` R

Toggles creation of SVG file. To suppress this on the command line, use
`-nosvg`.  
VALUE `yes|no`  
DEFAULT `yes`

  

`radius` R

Size of the image based on radius of inscribed circle. For a radius `r`, the
image will be `2r×2r`.  
VALUE `INT`

`1500p`  
`3000p`

  

`angle_offset` R

Angle offset of the start of the first segment in the circle. `0` corresponds
to 3 o'clock and `-90` to 12 o'clock.  
VALUE `FLOAT`

`0`  
`-90`

  

`angle_orientation`

Scale and ideogram progression in the image.  
VALUE `clockwise|counterclockwise`  
DEFAULT `clockwise`

  

`auto_alpha_colors`

Toggles automatic definition and allocation of transparent colors  
VALUE `yes|no`  
REQUIRED BY `auto_alpha_steps`

  

`auto_alpha_steps`

Number of transparency steps for each automatically allocated color. When
defined to `N`, colors `COLOR_a1` ... `COLOR_aN` are available for each named
`COLOR`.  
VALUE `yes|no`  
REQUIRES `auto_alpha_colors`

`5`

  

`background` R

Background of the image. This can be either a color or a PNG file.  
VALUE `COLOR|FILE`  
DEFAULT `white`

`white`  
`background.png`

  

