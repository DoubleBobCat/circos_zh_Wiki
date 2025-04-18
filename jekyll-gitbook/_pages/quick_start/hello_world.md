---
author: DoubleCat
date: 2025-04-11
layout: post
category: quick_start
title: Hello World
---

### lesson
This is the first of a series of tutorials that show you how to build a Circos
image from scratch. Whereas other tutorials (e.g.
[ideograms](//documentation/tutorials/ideograms),
[scaling](//documentation/tutorials/scaling),
[highlights](//documentation/tutorials/highlights),
[highlights](//documentation/tutorials/highlights), [2D
data](//documentation/tutorials/2d_tracks),
[links](//documentation/tutorials/links)) detail the functions of Circos, here
I take a more pedagogical approach, similar to what you will find in the
[Circos course](//documentation/course).

This first section shows the _minimum practical Circos configuration_ required
to obtain an image. I include the word _practical_ because there are some
parameters that have built-in default values in the code and these _could_ be
left out. The built-in defaults, however, are a measure of safety, not
convenience. Even if parameters do have default values, there are some that
you should explicitly include for clarity.

The minimum configuration image will show the 24 human chromosomes as colored
segments. As this tutorial progresses, we will be adding optional elements
like cytogenetic bands, labels, ticks and, of course, data.

#### minimum configuration
```    
    # circos.conf
    
    karyotype = data/karyotype/karyotype.human.txt
    
    <ideogram>
    
    <spacing>
    default = 0.005r
    </spacing>
    
    radius    = 0.9r
    thickness = 20p
    fill      = yes
    
    </ideogram>
    
    ################################################################
    # The remaining content is standard and required. It is imported 
    # from default files in the Circos distribution.
    #
    # These should be present in every Circos configuration file and
    # overridden as required. To see the content of these files, 
    # look in etc/ in the Circos distribution.
    
    <image>
    # Included from Circos distribution.
    <<include etc/image.conf>>
    </image>
    
    # RGB/HSV color definitions, color lists, location of fonts, fill patterns.
    # Included from Circos distribution.
    <<include etc/colors_fonts_patterns.conf>>
    
    # Debugging, I/O an dother system parameters
    # Included from Circos distribution.
    <<include etc/housekeeping.conf>>
```
#### karyotype
The karyotype file is always required. It defines the names, sizes and colors
of chromosomes that you will use in the image.

Because Circos can display any data, the _meaning_ of this file is not
restricted to chromosomes. Axis segments can be sequence contigs, genes,
indexed positions, blocks of time, or any quantity that has an integer-based
coordinate system.

Circos ships with several predefined karyotype files for common sequence
assemblies: human, mouse, rat, and drosophila. These files are located in
`data/karyotype` within the Circos distribution. ([karyotype file
details](//documentation/tutorials/ideograms/karyotypes)).

When a parameter, such as `karyotype` defines the location of a file, the file
path can be relative or absolute. If it is relative, and it is not found
relative to the configuration file, the Circos distribution tree is searched
for the file. This is why here the directory `data/karyotype` finds the file,
even though there is no `data/` directory in this tutorial.

#### ideograms
Once Circos has a list of the chromosomes that can be drawn, the only other
parameters required to create an image are those that define where on the
image the ideograms should appear.

This is accomplished with the `<ideogram>` block and the parameters `radius`,
`thickness` and `fill`. In addition, you will need the `<spacing>` that
defines the separation between ideograms on the figure.

For a figure to be clear and informative, the position and format of the
ideograms is important to get just right. I dedicate a full [tutorial section
for ideograms](//documentation/tutorials/ideograms), where you can learn how
to adjust spacing, labeling, sizing, cropping and radial position of
ideograms.
### images
![Circos tutorial image - Hello
World](/documentation/tutorials/quick_start/hello_world/img/01.png)
### configuration
#### circos.conf
```    
    # 1.1 MINIMUM CIRCOS CONFIGURATION 
    #
    # This is a 'hello world' Circos tutorial. 
    #
    # Only required configuration elements are included.
    #
    # Subsequent tutorials in this section build on this example to
    # generate a representative image with common elements found in Circos
    # figures in the literature.
    
    # Chromosome name, size and color definition
    karyotype = data/karyotype/karyotype.human.txt
    
    # The <ideogram> block defines the position, size, labels and other
    # properties of the segments on which data are drawn. These segments
    # are usually chromosomes, but can be any integer axis.
    
    <ideogram>
    
    <spacing>
    # Spacing between ideograms. Suffix "r" denotes a relative value. It
    # is relative to circle circumference (e.g. space is 0.5% of
    # circumference).
    default = 0.005r
    
    # You can increase the spacing between specific ideograms.
    #<pairwise hsY;hs1>
    #spacing = 20r
    #</pairwise>
    
    </spacing>
    
    # Ideogram position, thickness and fill. 
    #
    # Radial position within the image of the ideograms. This value is
    # usually relative ("r" suffix).
    radius           = 0.90r
    
    # Thickness of ideograms, which can be absolute (e.g. pixels, "p"
    # suffix) or relative ("r" suffix). When relative, it is a fraction of
    # image radius.
    thickness        = 20p
    
    # Ideograms can be drawn as filled, outlined, or both. When filled,
    # the color will be taken from the last field in the karyotype file,
    # or set by chromosomes_colors. Color names are discussed in
    #
    # https://www.circos.ca/documentation/tutorials/configuration/configuration_files
    #
    # When stroke_thickness=0p or if the parameter is missing, the ideogram is
    # has no outline and the value of stroke_color is not used.
    
    fill             = yes  
    stroke_color     = dgrey
    stroke_thickness = 2p   
    
    </ideogram>
    
    ################################################################
    # The remaining content is standard and required. It is imported from
    # default files in the Circos distribution.
    #
    # These should be present in every Circos configuration file and
    # overridden as required. To see the content of these files, 
    # look in etc/ in the Circos distribution.
    #
    # It's best to include these files using relative paths. This way, the
    # files if not found under your current directory will be drawn from
    # the Circos distribution. 
    #
    # As always, centralize all your inputs as much as possible.
    
    <image>
    # Included from Circos distribution.
    <<include etc/image.conf>>                
    </image>
    
    # RGB/HSV color definitions, color lists, location of fonts, fill
    # patterns. Included from Circos distribution.
    #
    # In older versions of Circos, colors, fonts and patterns were
    # included individually. Now, this is done from a central file. Make
    # sure that you're not importing these values twice by having
    #
    # *** DO NOT DO THIS ***
    # <colors>
    # <<include etc/colors.conf>>
    # <colors>
    # **********************
    <<include etc/colors_fonts_patterns.conf>> 
    
    # Debugging, I/O an dother system parameters
    # Included from Circos distribution.
    <<include etc/housekeeping.conf>> 
```
  

* * *
