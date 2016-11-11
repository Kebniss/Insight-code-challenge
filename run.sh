#!/usr/bin/env bash

# example of the run script for running the fraud detection algorithm with a python file,
# but could be replaced with similar files from any major language

# I'll execute my programs, with the input directory paymo_input and output the files in the directory paymo_output
PROJECT_PATH=$(dirname ${BASH_SOURCE})

cut -d , -f 2,3 ${PROJECT_PATH}/paymo_input/batch_payment.txt > ${PROJECT_PATH}/paymo_input/batch_payment_trimmed.txt
cut -d , -f 2,3 ${PROJECT_PATH}/paymo_input/stream_payment.txt > ${PROJECT_PATH}/paymo_input/stream_payment_trimmed.txt


python ${PROJECT_PATH}/src/antifraud.py --input_batch ${PROJECT_PATH}/paymo_input/batch_payment_trimmed.txt --input_stream ${PROJECT_PATH}/paymo_input/stream_payment_trimmed.txt --distance_limit 1 --output ${PROJECT_PATH}/paymo_output/output1.txt --log_file ${PROJECT_PATH}/log1.txt

python ${PROJECT_PATH}/src/antifraud.py --input_batch ${PROJECT_PATH}/paymo_input/batch_payment_trimmed.txt --input_stream ${PROJECT_PATH}/paymo_input/stream_payment_trimmed.txt --distance_limit 2 --output ${PROJECT_PATH}/paymo_output/output2.txt --log_file ${PROJECT_PATH}/log2.txt

python ${PROJECT_PATH}/src/antifraud.py --input_batch ${PROJECT_PATH}/paymo_input/batch_payment_trimmed.txt --input_stream ${PROJECT_PATH}/paymo_input/stream_payment_trimmed.txt --distance_limit 4 --output ${PROJECT_PATH}/paymo_output/output3.txt --log_file ${PROJECT_PATH}/log3.txt


rm ${PROJECT_PATH}/paymo_input/batch_payment_trimmed.txt
rm ${PROJECT_PATH}/paymo_input/stream_payment_trimmed.txt
