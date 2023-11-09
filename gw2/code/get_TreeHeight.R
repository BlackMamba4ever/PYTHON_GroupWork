# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

args <- commandArgs(trailingOnly = T)
trees <- read.csv(args)
TreeHeight <- function(degrees, distance) {
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  return (height)
}
num <- nrow(trees)
all_trees_height <- sapply(1:nrow(trees) , function(i) TreeHeight(trees$Angle.degrees[i], trees$Distance.m[i]))
TreeHts <- cbind(trees, Tree.Height.m = all_trees_height)
filename_without_extension <- sub(".csv", "", basename(args))
p <- paste0("../results/", filename_without_extension, "_treeheights.csv")
write.csv(TreeHts, file = p, row.names = FALSE)


