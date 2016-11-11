import os
import inspect
from Graph import Graph
import logging
import argparse

script_path = os.path.abspath(inspect.getsourcefile(lambda:0))
src_dir = os.path.dirname(script_path)
project_dir = os.path.dirname(src_dir)

parser = argparse.ArgumentParser(description='Insight Antifraud')
parser.add_argument('-ib','--input_batch', help="Batch input to seed the graph's starting point", required=True)
parser.add_argument('-is','--input_stream', help="Stream input to run the algo on, step by step", required=True)
parser.add_argument('-d','--distance_limit', help="Maximum distance between two users that does not raise a warning", required=True)
parser.add_argument('-o','--output', help="Output for the first challenge", required=True)
parser.add_argument('-l','--log_file', help="Path to the logger (if not provided, no logging happens)", required=False)
args = vars(parser.parse_args()) # args is a dictionary, with everything represented as string

if args["log_file"]:
    log_path = os.path.join(project_dir,
                            os.path.relpath(args['log_file'])
                            )
    logger = logging.getLogger()
    hdlr = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

input_batch_path = os.path.join(project_dir,
                                os.path.relpath(args['input_batch'])
                                )
input_stream_path = os.path.join(project_dir,
                                os.path.relpath(args['input_stream'])
                                )
distance_limit = int(args['distance_limit'])
output_path = os.path.join(project_dir,
                                os.path.relpath(args['output'])
                                )
# Instanciate the graph object
connections = Graph()

i = 0
with open(input_batch_path, 'r') as f:
    for line in f:
        # skip header
        if i == 0:
            i += 1
            continue

        input_line = line.split(',')
        try:
            user_1 = int(input_line[0].strip())
        except:
            if args["log_file"]:
                logger.error('Could not parse {0} at line {1}'.format(input_line[0], i))
            continue

        try:
            user_2 = int(input_line[1].strip())
        except:
            if args["log_file"]:
                logger.error('Could not parse {0} at line {1}'.format(input_line[1], i))
            continue

        i += 1
        # Fill it with all the connections in Batch
        connections.add_edge(user_1, user_2)

# Now in Stream we perform these operations in this order:
# 1. Perform inference about the transaction: is it within *distance_limit*?
# 2. Add edge considering the transaction valid and remember for future transactions

i = 0
with open(output_path, 'w') as fout:
    with open(input_stream_path, 'r') as fin:
        for line in fin:
            if i == 0:
                i += 1
                continue
            if i % 10000 == 0 and "log_file" in args:
                logger.info("Working on row " + str(i) )

            input_line = line.split(',')
            try:
                user_1 = int(input_line[0].strip())
            except:
                if args["log_file"]:
                    logger.error('Could not parse {0} at line {1}'.format(input_line[0], i))
                continue

            try:
                user_2 = int(input_line[1].strip())
            except:
                if args["log_file"]:
                    logger.error('Could not parse {0} at line {1}'.format(input_line[1], i))
                continue

            i += 1
            s = "trusted" if connections.bi_bfs_until(user_1, user_2, distance_limit) else "unverified"
            fout.write(s + "\n")

            connections.add_edge(user_1, user_2)

if args["log_file"]:
    logger.info("Done!")
