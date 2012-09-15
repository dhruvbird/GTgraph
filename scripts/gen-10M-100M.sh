#!/bin/bash
#PBS -q shared
# specify your project allocation
#PBS -A sun104
# number of nodes and number of processors per node requested
#PBS -l nodes=1:ppn=32
# requested Wall-clock time.
#PBS -l walltime=01:00:00
# name of the standard out file to be "output-file".
#PBS -o bfs-graph-gen-op
# name of the job
#PBS -N bfs-graph-gen
#PBS -V

cd ./GTgraph/R-MAT/
./GTgraph-rmat -c config.me -o /dev/stdout | python rmat-2-custom.py 1000 > ../scripts/graph-10M-100M-1k.in
