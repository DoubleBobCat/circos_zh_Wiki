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

# 1 — Configuration and Installation

## 10\. PNG Output

[Lesson](/documentation/tutorials/configuration/png_output/lesson)
[Images](/documentation/tutorials/configuration/png_output/images)
[Configuration](/documentation/tutorials/configuration/png_output/configuration)

Circos is capable of producing both PNG (24-bit) and
[SVG](/documentation/tutorials/configuration/svg_output) images. This section
discusses PNG files, as well as the <image> block which controls the location,
size and other characteristics of the output file.

### <image> block

I suggest that you always import the default image settings.

    
    
    <image>
    # import defaults from Circos distribution
    <<include etc/image.conf>>
    </image>
    

The settings define the output file to be 3,000 x 3,000 pixels, with white
background, named `circos.png`, which will be placed in the current directory.

Take a look at `etc/image.conf` in the Circos distribution to see the
parameter definitions. You'll find that this file is actually composed of two
additional includes, a practise common in Circos to try to modularize
configuration as much as possible.

    
    
    # etc/image.conf
    <<include image.generic.conf>>
    <<include background.white.conf>>
    
    # image.generic.conf
    dir                = .
    file               = circos.png
    png                = yes
    svg                = yes
    radius             = 1500p
    angle_offset       = -90
    #angle_orientation = counterclockwise
    auto_alpha_colors  = yes
    auto_alpha_steps   = 5
    
    # background.white.conf
    background         = white
    

If you would like to overwrite any of these parameters, use the `*` suffix
syntax.

    
    
    # circos.conf
    <image>
    <<include etc/image.conf>>
    file*   = myfile.png
    radius* = 1000p
    </image>
    

### 24-bit images

PNG files are created in 24-bit mode. The `24bit` flag previously found in the
<image> block has been deprecated.

### image size

Output image directory and filename are defined in the `dir` and `file`
parameters of the <image> block. The produced image is always square, and its
size set by the `radius` parameter (this is the size of the inscribed circle).
If `radius=1500p`, then the image will be 3,000 x 3,000 pixels in size.

### image background

Image background is controlled using the `background` parameter, which may be
set to `transparent` or an image location. For more details, see the [Image
Transparency
Tutorial](/documentation/tutorials/recipes/transparency_background/)

### angle offset

You can adjust the angle offset of the circular layout using the
`angle_offset` parameter. The value of this parameter determines where the
start of the first ideogram appears. By default, the value is set to
`angle_offset=-90` to make the first ideogram start at the top of the image.

This is the prefered way to rotate the image, rather than in post-production,
because it will maintain legibility of all all text labels, which will be
oriented right-side-up. If you rotate the image yourself, some labels may be
upside-down.

### scale orientation

You can orient all the ideogram directions to point counterclockwise by
setting `angle_orientation=counterclockwise`. By default, everything is
oriented `clockwise`.

### PNG dpi image resolution

There's often confusion about what "dpi" means—I hope to clear this up here.

The default settings in Circos generate PNG images at 3,000 x 3,000 pixels,
which provides you with enough pixels for most journal size/resolution
requirements.

The PNG output doesn't have any inherent dpi resolution. When loaded into an
application like Photoshop, this lack of value will be replaced by the default
72 dpi, which itself is both historic and useless. Let's just call it a
default. You might see this 72 dpi value and think that it's too low for your
needs, because the journal requirements stipulate "at least 300 dpi".

When journals say 300 dpi, what they really mean is "give us enough pixels so
that when we go to print, we have at least 300 pixels for every inch of
figure". To know whether you have enough "dots" per "inch", you need to not
only know how many "dots" you have (pixels), but also how many "inches" the
pixels will map to. Without having this physical size in mind, dpi resolution
is meaningless.

Let's look at an example.

Nature's two-column figure is 7.2" wide (183 mm) as described in their
[Guidelines to Authors](https://www.nature.com/nature/authors/gta/#a5.9). To
achieve 300 dpi resolution (at least 300 pixels per inch of figure), you'll
need a figure that is

    
    
    300 * 7.2 = 2,160 pixels
    

in each dimension. The default Circos 3,000 x 3,000 pixel output is sufficient
(it is 417 dpi if the output is 7.2").

Using the `radius` parameter in the <image> block, you control the output
pixel size of the image. Match this to the size of the physical image in the
journal. It usually doesn't hurt to have an image that exceeds the minimum
resolution.

### Limitations in PNG output

If you susspect there may be a problem with drawing images, please run

    
    
    bin/gddiag
    

and look at the output `gddiag.png`. It should look like the second image in
this tutorial.

Circos uses perl's GD module to draw its graphics, which in turn depends on
the [gd library](https://www.libgd.org) for its core implementation.

### anti-aliasing bug in `libgd`

If you find artefacts in your image (e.g. squares or elements in unexpected
places), it is likely that your libgd is one of the versions which has an
anti-aliasing bug. Please turn anti-aliasing off by toggling the
`anti_aliasing` parameter in `etc/housekeeping.conf`.

You can overwrite this parameter in `circos.conf`, right after importing
`etc/housekeeping`,

    
    
    # in circos.conf
    <<include etc/housekeeping.conf>>
    anti_aliasing* = no
    

or change it permanently in `etc/housekeeping.conf`,

    
    
    # etc/housekeeping.conf
    anti_aliasing = no
    

### other anti-aliasing limitations

As of libgd 2.0.35, antialiasing for lines is not supported when the line is
drawn at a thickness >1 or with a color that has an alpha channel. The
consequence is that you cannot have thick antialiased lines, or partially
transparent antialiased lines.

Until these features are implemented in gd, the solution is to create an image
magnified by a factor of _x_ (e.g. 2 _x_) and use a command-line image
manipulation tool like
[ImageMagick's](https://www.imagemagick.org/script/index.php) convert to
shrink the image back to its desired size. The process of resizing the image
will subsample the pixels and give the effect of antialiasing.

