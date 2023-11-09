#!/usr/bin/env python3

"""Some functions exemplifying the use of control statements"""
# docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.
__author__ = 'Pu Zhao (pu.zhao@imperial.ac.uk)'
__version__ = '0.0.1'

import os
import sys
import math
import pandas as pd


def load_data(filename):
    read_csv = pd.read_csv(filename)
    col_names = read_csv.columns.tolist()
    col_names.append('Tree.Height.m')
    trees = read_csv.values.T.tolist()
    return trees, col_names


def tree_height(degrees, distance):
    radians = degrees * math.pi / 180
    height = distance * math.tan(radians)
    return height


def get_all_tree_height(trees):
    num_of_trees = len(trees[0])
    all_trees_height = [tree_height(trees[1][i], trees[2][i]) for i in range(num_of_trees)]
    trees.append(all_trees_height)
    return trees


def output_file(trees, column_names, op_file_name):
    trees_df = pd.DataFrame(trees)
    trees_df = trees_df.transpose()
    trees_df.columns = column_names
    trees_df.to_csv(op_file_name, index=False)


def main(ip_file_name, op_file_name):
    trees, col_names = load_data(ip_file_name)
    trees2 = get_all_tree_height(trees)
    output_file(trees2, col_names, op_file_name)
    return 0


if __name__ == "__main__":
    input_file_name, extension = os.path.splitext(os.path.basename(sys.argv[1]))
    output_file_name = "../results/" + input_file_name + "_treeheights.csv"
    sys.exit(main(sys.argv[1], output_file_name))
