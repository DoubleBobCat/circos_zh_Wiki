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

## 1\. Microbial Genome

[Lesson](/documentation/tutorials/recipes/microbial_genomes/lesson)
[Images](/documentation/tutorials/recipes/microbial_genomes/images)
[Configuration](/documentation/tutorials/recipes/microbial_genomes/configuration)

Circos is suitable for creating images of genomes that only have one
chromosome, such as circular bacterial genomes. This example mentions a few
tips in creating such images.

### structures crossing origin

First, and perhaps ironically, Circos doesn't actually understand the concept
of a circular chromosome. In other words, a chromosome, which is represented
by one or more ideograms, must have a beginning and an end which are
explicitly defined.

This means that on circular chromosomes, structures (e.g. clone, gene) that
cross the origin must be defined by two entries. For example, if you have a 1
Mb genome, and wish to have a highlight from `950,000` to `50,000` you must
define two highlights: `950,000-1,000,000` and then another `1-50,000`.

### ideogram breaks

To achieve an image with an ideogram that appears circular, set the ideogram
spacing values to `0`. This is done in the <ideogram><spacing> found in the
`ideogram.conf` file (which is linked to the main `circos.conf` file via the
`<<include ideogram.conf>>` directive.

    
    
    <ideogram>
     <spacing>
      default = 0u
      break   = 0u
     </ideogram>
    </spacing>
    

If you would like to decompose the chromosome into multiple ideograms, you
still need to maintain a zero-separation between the ideograms containing the
end and beginning of the chromosome. One of the images in this example shows
how to introduce three axis breaks into the image in this manner, using the
<pairwise> block.

