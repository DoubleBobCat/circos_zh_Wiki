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

## 5\. Visualizing Tabular Data

[Lesson](/documentation/tutorials/utilities/visualizing_tables/lesson)
[Images](/documentation/tutorials/utilities/visualizing_tables/images)

## motivation

For details about the methodology behind the use of Circos to visualize
tabular data, see the article [Visualizing Tabular
Data](/presentations/articles/vis_tables1).

For an in-depth description of the configuration syntax for tableviewer script
set, see [Visualizing Tabular Data - Part
II](/presentations/articles/vis_tables2).

## script location

    
    
    tools/tableviewer
    

## script usage

    
    
    > cd tools/tableviewer
    # create an image of a basic sample table
    > ./makeimage-basic
    # create an image of a sample table with row/col order information
    > ./makeimage-ordered
    # create an image of a sample table with row/col order an color information
    > ./makeimage-ordered-colored
    

The tableviewer is composed of three parts

  * make-table - creates a random table (helpful for debugging and exploration) 
  * parse-table - parses a table into an intermediate state 
  * make-conf - uses output of parse-table and creates Circos data files and configuration files 

To get the full manpage, use -man.

    
    
    > cd tools/tableviewer
    > bin/make-table -man
    > bin/parse-table -man
    > bin/make-conf -man
    

Adjust the configuration files in etc/ to suit your needs.

## details

The scripts in tableviewer/ (make-table, parse-table, make-conf) generate a
Circos image of tabular data. For more information about how tabular data is
represented, see the [online tableviewer](https://mk.bcgsc.ca/tableviewer).
The online version limits you to 15 columns and rows and with the scripts
described here you can process tables of any size.

There are three scripts that compose the tableviewer package

  * make-table - Create a table filled with random values. Useful when you need to debug or explore visualization for tables with specific properties. You don't need this script if you only want to exclusively work with your own data. 
  * parse-table - Parses a table file (your own or generated with make-table) and generates a parsed data stream that is used by make-conf 
  * make-conf - Uses output of parse-table to create data files and configuration files used by Circos to visualize the table 

### make-table

This script is helpful to generate random data to test-drive the rest of the
tableviewer package. For example, you can generate a small table

    
    
    > bin/make-table -row 3 -brief
     lbl    A    B    C
       A   80  387  112
       B    1   30   61
       C   96  146   29
    

or a large one

    
    
    > bin/make-table -row 15 -brief
     lbl    A    B    C    D    E    F    G    H    I    J    K    L    M    N    O
       A  376   78  367   75   72  184  452  285  310  142  469  215  107  106   95
       B   38   33   36   55   53   68   77   35   59   20   52   36   19   23   19
       C  108   79  121   47  120   95   65   30   89  125   78   99   39  166   82
       D   90   78   77   63  153   35   97  133  213  129  137  159   40   65  100
       E   99   52  129  139  129   27   95  129   36   90   32   73   82  110  131
       F  145  162  104  121   84   67  125   98  146   11  156   62  153   72  167
       G   67  123   53   39    6  108   36   77  118   96   92   97  119  142  142
       H   55   74   92   33   77   43  109   39  166  182   92    1  115   91   85
       I  135  168  101   78   21   85   76   94  105   18  144  174  135  120  168
       J   98   94   32   76   44    9   45  133  132   42   64   29   57   92  141
       K   74   71  117   98  118   88  104   80  168  127   33   46    5  110   68
       L   65  179   54   73   93  110  123   81  156  109   58   72  131   59   76
       M   93   73   60  226   59   55  140  124  210  136   59   79   80  106  204
       N  143  150   92   67   94  239   48  125  214  119   84   76  121   72   92
       O  134  122   83  223  101   74  161  155  151  159  183  154   15   48  145
    

You can use -row and -col to independently set the number of rows and columns
in the table.

By using -unique, you can request that row and column labels are all
different.

    
    
    > bin/make-table -row 3 -brief -uniq
     lbl    D    E    F
       A  288   40  245
       B   52   52   33
       C  139   76   85
    

Uniquely labeled rows and columns generate an image in which each row and
column has its own segment, since segments are keyed by label. If your table
represents relationships between a set of items, then row/column labels will
be the same. However, if your table represents relationshpis between two
disjoint sets, then the labels will be different.

Notice that make-table creates output with a leading space in each line. The
configuration file for make-table defines the precise format of the output
line and here you can adjust the width of each field. When parsing this output
using parse-table (see below), you should always set strip_leading_space=yes
(this is the default) in parse-table.conf so that any leading space in lines
is removed.

### parse-table

This script parses the table file and generates row, column, and cell
statistics and data values that are subsequently used to create configuration
and input files using make-conf.

This part of the tableviewer suite is the most complex and has the largest
number of configuration settings, since this is the script that determines the
position and color of all the elements in the final image.

Please read the etc/parse-table.conf configuration file for an explanation of
what the parameters do. It's likely that you will find the configuration file
overwhelming at first - do not dispair! By learning how the elements of the
configuration file affect the final image, you will be able to tweak the
output image to best represent your data. You can control nearly every aspect
of how the table is shown. Parameters such as col/row order can be either
manually set (via order rows and columns in the input file) or automatically
determined (based on label value or row/column size).

To help you experiment, you should construct two simple tables using the make-
table tool - one with unique labels and one with shared column/row labels

    
    
    > bin/make-table -rows 5 -seed 123 -brief -uniq  > samples/table-basic-unique.txt
    > bin/make-table -rows 5 -seed 123 -brief        > samples/table-basic-shared.txt
    

and then play with parse-table.conf settings as you draw each table

    
    
    cat samples/table-unique.txt | bin/parse-table | bin/make-conf -dir data/
    ../../bin/circos -conf etc/circos.conf
    

Take a look at the example images associated with this tutorial to get a
feeling for the kind of variety that is possible.

### make-conf

The only option to make-conf is the directory to which it should write the
data files.

    
    
    > cat samples/table-basic.txt | bin/parse-table | bin/make-conf **-dir data/**
    

Make sure that paths in the etc/circos.conf file correctly reflect the
location to which the data files were written.

