# Cloud Computing

Data of all the accidents in the state of New York was collected. This data contains over 900,000 records and is almost 175MB in size.
Using the Hadoop Streaming API, we built mapper and reducer scripts that analyze the data and summarizes counts for each type of vehicle 
involved. If the vehicle was involved in an accident more than once in an accident, we are counting the vehicle multiple times for 
consistency.

# Overview

Hadoope Cluster uses the concept of divide and conquer in Computer science. The part of the program that we use to divide is called the mapper,
and the part of the program used to "conquer" is called reducer.

## Mapper
This script/program is used to divide the provided data into chunks reducing the load on the cluster. For example, if you were 
supposed to take the mean of 100 million numbers, the mapper would reduce it chunks of a million each. This makes it simpler as only dataset
as big as a million is stored in the RAM at one point.

## Reducer
