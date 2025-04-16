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

# 9 — Recipes

## 5\. Image Transparency and Background

[Lesson](/documentation/tutorials/recipes/transparency_background/lesson)
[Images](/documentation/tutorials/recipes/transparency_background/images)
[Configuration](/documentation/tutorials/recipes/transparency_background/configuration)

In addition to the colors you define in color.conf, an additional color called
"transparent" is automatically defined for you. Therefore, if you try to
define your own color of this name, your definition will be ignored.

## making background transparent

To create an image with a transparent background, set the background color to
"transparent".

    
    
    <image>
    ...
    background = transparent
    </image>
    

## using another image as background

To draw the image on a existing image, specify the input image file for the
background parameter. This works only for PNG images.

    
    
    <image>
    ...
    background = data/8/background.png
    </image>
    

The input image must be of the same size as the output Circos image (it must
be square and have dimensions 2*radius x 2*radius, where radius is specified
in the <image> block).

Instead of drawing on an existing image, you can compose a Circos image with a
transparent background together with a custom background during post-
processing. However, having the ability to draw the Circos image on any
background is useful when you automate Circos image generation and require a
watermark or logo on each image.

