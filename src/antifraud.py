import os
from features import *
from Graph import Graph
import logging

cur_path = os.path.dirname('__file__')

logger = logging.getLogger()
hdlr = logging.FileHandler(os.path.join(cur_path, 'antifraud.log'))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

input_batch = os.path.relpath('..\\paymo_input\\batch_payment_trimmed.csv', cur_path)

connections = Graph()

i = 0
with open(input_batch, 'r') as f:
    for line in f:
        # skip header
        if i == 0:
            i += 1
            continue

        input_line = line.split(',')
        try:
            user_1 = int(input_line[0].strip())
        except:
            logger.error('Could not parse {0} at line {1}'.format(input_line[0], i))
            continue

        try:
            user_2 = int(input_line[1].strip())
        except:
            logger.error('Could not parse {0} at line {1}'.format(input_line[1], i))
            continue

        i += 1

        connections.add_edge(user_1, user_2)

input_stream = os.path.relpath('..\\paymo_input\\stream_payment_trimmed.csv', cur_path)

i = 0
output1 = []

output_stream = os.path.relpath('..\\paymo_output\\output1.txt', cur_path)

with open(output_stream, 'w') as fout:
    with open(input_stream, 'r') as fin:
        for line in fin:
            if i == 0:
                i += 1
                continue
            if i % 10000 == 0:
                logger.info("Working on row " + str(i) )

            input_line = line.split(',')
            try:
                user_1 = int(input_line[0].strip())
            except:
                logger.error('Could not parse {0} at line {1}'.format(input_line[0], i))
                continue

            try:
                user_2 = int(input_line[1].strip())
            except:
                logger.error('Could not parse {0} at line {1}'.format(input_line[1], i))
                continue

            i += 1
            fout.write(feature_1(connections, user_1, user_2) + "\n")

            connections.add_edge(user_1, user_2)

logger.info("Done!")
