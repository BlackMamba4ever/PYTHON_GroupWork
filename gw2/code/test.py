import pandas as pd
import math


def tree_height(degrees, distance):
    radians = degrees * math.pi / 180
    height = distance * math.tan(radians)
    return height


df = pd.read_csv('../data/trees.csv')
col_names = df.columns.tolist()
print(type(col_names))
print(col_names)
trees = df.values.T.tolist()
num_of_trees = len(trees[0])
all_trees_height = [tree_height(trees[2][i], trees[1][i]) for i in range(num_of_trees)]
trees.append(all_trees_height)
