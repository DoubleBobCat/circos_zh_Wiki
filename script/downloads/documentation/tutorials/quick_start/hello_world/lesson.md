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

# 2 — Quick Start

## 1\. Hello World

[Lesson](/documentation/tutorials/quick_start/hello_world/lesson)
[Images](/documentation/tutorials/quick_start/hello_world/images)
[Configuration](/documentation/tutorials/quick_start/hello_world/configuration)

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

### minimum configuration

    
    
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
    

### karyotype

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

### ideograms

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

