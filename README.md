# useful_functions
Can be used across different projects.
Contains plotly graphs, short cuts to access to AWS S3 buckets and simple date-time functions.

## plotly_graphs.py
Draws a multi line graph given a numerical pandas data frame. Index is the x axis. Columns are taken as lines. 
Draws a graph from a dictionary with the following format.
dict_data = {
        'x': random_x,
        'y' : {
           'v1': random_y0,
           'v2': random_y1,
           'v3': random_y2,
        } ,
    }

## s3_utils.py
Reading and writing from Amazon ( AWS ) S3 buckets

Reads and writes a pandas data frame as json or csv
Reads and writes a python dictionary as json 
Reads and writes a text to s3 path
Lists file in a s3 path

## general_utils.py
Takes dates in string format, does simple date additions and substrations and returns text dates.
'%Y-%m-%d'  format : example: 2019-01-25



