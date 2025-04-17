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

# 10 — Helper Tools

## 7\. Visualizing Categorical Data

[Lesson](/documentation/tutorials/utilities/categorical_data/lesson)
[Images](/documentation/tutorials/utilities/categorical_data/images)

## script location

    
    
    tools/categoryviewer
    

## script usage

    
    
    > cd tools/categoryviewer
    # use canned data
    > ./makeimage
    # which runs
    > cat data/individuals.txt | bin/parse-category -conf etc/parse-category.conf > data/links.txt 2> data/karyotype.txt
    > ../../bin/circos -conf etc/circos.conf
    

The input data must be tab delimited. The individuals.txt file is an example
of a randomly generated set of eye color, hair color, height and sex of 1000
individuals.

The output of parse-category is the link file, sent to STDOUT (redirect with
>), and the karyotype file, sent to STDERR (redirect with 2>).

## details

This utility tool is similar to the table viewer ([Tutorial
9.5](https://mk.bcgsc.ca/circos/?tutorials&id=9&section=5) tools/tableviewer),
but instead of tabular data (stored as a matrix of rows and columns), this
tool generates images of categorical data which is supplied as one record per
line. This utility tool is useful in analyzing survey data, relationship
between multiple choice answers, and any data in which a record is associated
with two or more partitioned values (partitions can be categories, codes, or
intervals).

### sample data set

For the example data set, I have randomly generated a putative survey
responses of 1000 individuals that asked questions about sex, hair color, eye
color and height. Each record corresponds to a respondent's answers.

    
    
    0       female  f       red     3       green   2       165
    1       female  f       blonde  0       blue    1       156
    2       female  f       brown   1       grey    3       157
    3       male    m       brown   1       green   2       165
    4       female  f       black   2       blue    1       164
    5       female  f       brown   1       green   2       158
    ...
    996     male    m       red     3       grey    3       179
    997     female  f       red     3       green   2       163
    998     female  f       black   2       brown   0       161
    999     female  f       brown   1       brown   0       160
    

Each responses is given in full (e.g. green) as well as a code. The codes for
hair are blonde=0, brown=1, black=2 and red=3. The codes for eyes are brown=0,
blue=1, green=2 and grey=3. Height is in centimeters.

The data were geneated using a probability model in which used the frequency
of hair color in the population and the probabilistic relationship between
hair and eye color. This is a primitive model with manufactured parameters,
but serves to illustrate the benefits of Circos visualizations of categorical
data.

### hair and eye color

The first sample configuration file, etc/parse-category.conf, generates an
image that compares hair and eye color. The start of the links are defined by
column 4 (0-index). This is the column that contains the hair code (0-3). The
color parameter defines the color of the segments from which the links will
start.

    
    
    <link_start>
    id  = hair
    col = 4
    min = 0
    max = 3
    rx  = \d
    color = orange
    </link_start>
    

Link ends are defined by the eye color code, found in column 6. Eye color
segments will be green.

    
    
    <link_start>
    id  = eye
    col = 6
    min = 0
    max = 3
    rx  = \d
    color = green
    </link_start>
    

Once the categories for the start and end of the links are defined, the data
file is parsed and turned into a format that Circos can use. One set of
segments will correspond to hair color, with a segment for each distinct hair
color code (value found in column 4). Another set of segments will correspond
to eye color. Links between them will encode the number of records with a
given hair/eye color combination.

In the first example image, the color of the links is determined by the value
in column 2, which contains either "m" (male) or "f" (female). The values
block defines the link format values for each value in this column.

    
    
    <link_coding sex>
    order = 2
    use   = yes
    col   = 2
    <values>
    m = color=black_a4
    f = color=black_a8
    </values>
    </link_coding>
    

You can add more coding blocks, which are evaluated in order of the value of
the order parameter. For example,

    
    
    <link_coding height>
    order = 1
    use   = yes
    col   = 7
    <values>
    158 = stroke_color=green,stroke_thickness=3p
    159 = stroke_color=green,stroke_thickness=3p
    160 = stroke_color=green,stroke_thickness=3p
    161 = stroke_color=green,stroke_thickness=3p
    162 = stroke_color=green,stroke_thickness=3p
    168 = stroke_color=red,stroke_thickness=3p
    169 = stroke_color=red,stroke_thickness=3p
    170 = stroke_color=red,stroke_thickness=3p
    171 = stroke_color=red,stroke_thickness=3p
    172 = stroke_color=red,stroke_thickness=3p
    </values>
    </link_coding>
    

The rules for link formatting are simple: (1) rules triggered later (based on
order parameter) overwrite any formatting set by previous rules, and (2)
records with the same formatting form independent ribbons. The consequence of
(2) is that you can subdivide a group of records for a given start/end
category value (e.g. blonde hair/blue eye) into smaller groups based on other
values (e.g. blonde/blue males and females, or blonde/blue males 170cm and
blonde/blue females 160cm).

### ribbon order

The order of the start and end of the ribbons on each segment is controlled by
the <link_order> blocks. The following ways of ordering ribbons are supported

  * by size - ribbons are placed in decreasing order of thickness (number of records) 
  * by coding - ribbons are placed in alphanumeric order of the code used to determine their format characteristics through the <link_coding> blocks 
  * by other end - ribbons are placed to limit the number of crossing ribbons, and this order scheme can only be used for one of the two ends 
  * by radius - ribbons are placed in increasing order of the radius of their end 

Ribbon order is defined in the <link_order> block and specified for the start
and end of the ribbon. For example,

    
    
    <link_order>
    start = otherend
    end   = size
    </link_order>
    

### ribbon radius

The radial position of a ribbon can be adjusted based on any column value.
This is done using <radius> blocks within the <link_start> and <link_end>
blocks. The radius of the ribbon is mapped onto radius min-max range (rmin-
rmax) based on the value of a column (possibly remapped) and a range of
acceptable values (min-max).

For example, the block

    
    
    <link_start>
    ...
    <radius>
    use   = yes
    col   = 7
    remap = int((190-int(x))/5)
    min   = 0
    max   = 10
    rmin  = 0.7
    rmax  = 0.98
    </radius>
    </link_start>
    

will place the start of the ribbon at a radius proportional to a remapped
height value. The height value is sampled from column 7 and remapped according
to the remap parameter. The effect of the remap parameter as shown here is to
map the height values, which range 144-189, to a range 0-9.

Just like for formatting, radial values are used to split the record set. If
you have a large number of possible radial values, you will wind up with a
large number of thin ribbons, since it's likely that no more than a few
records will have the same radial value. It is therefore a good idea to bin
adjacent radial values together to reduce the number of ribbons and avoid
having a busy, uninterpretable figure.

