#!/bin/bash


URL="http://localhost:8080"  
NUM_REQUESTS=100             
CONCURRENCY=10               


for ((i=1; i<=$NUM_REQUESTS; i++)); do
    (curl -s -o /dev/null -w "%{http_code}" $URL &)   
    if (( $i % $CONCURRENCY == 0 )); then
        wait  
    fi
done
wait
