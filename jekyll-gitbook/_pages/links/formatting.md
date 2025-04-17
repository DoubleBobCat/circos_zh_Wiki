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

# 6 — Links and Relationships

## 3\. Link Formatting

[Lesson](/documentation/tutorials/links/formatting/lesson)
[Images](/documentation/tutorials/links/formatting/images)
[Configuration](/documentation/tutorials/links/formatting/configuration)

In this example, the image will be created using multiple data sources for
links. I'm also going to subvert the record_limit setting, and in combination
with z depth, to sample different links from the same data file.

In general, if you have multiple data files, each is associated with its own
<link> block.

    
    
    <links>
    
     # global parameters here
     ...
    
     <link>
      file = /path/to/file
      # local parameters for this data set
      ...
     </link>
    
     <link>
      file = /path/to/file
      # local parameters for this data set
      ...
     </link>
    
     ...
    
    </links>
    

When combining multiple link data sets in one image, there are a few things to
keep in mind.

First, set the z depth for each data set accordingly. Data sets with a higher
the z depth value are drawn on top of data sets with a lower value. In this
example, I draw the first 10,000 records from segdup.txt in very light grey
(z=5), then the first 2,500 records in light grey (z=10, thus on top of any
z<10 data), then the first 1,000 records in grey (z=15, thus on top of any
z<15 data), and so on.

Second, you can adjust link geometry for each data set. In this example, I've
modified the crest and bezier radius purity for links drawn from the three
`segdup.bundle*.txt` files.

Finally, thickness and color can be effectively used to help layer the data. I
typically draw links with a lower z value in a light shade of a color and with
thin lines.

