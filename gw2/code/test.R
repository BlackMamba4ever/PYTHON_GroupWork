args <- commandArgs(trailingOnly = T)
cat("Received command line arguments:\n")
cat(args)
filename_without_extension <- sub(".csv", "", basename(args))
p <- paste0("../data/", filename_without_extension, "_treeheights.csv")
p
# trees <- read.csv(args)


# write.csv(args, file = "../results/_treeheights.csv", row.names = FALSE)
