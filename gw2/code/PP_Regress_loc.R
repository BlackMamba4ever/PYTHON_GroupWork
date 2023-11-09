rm(list = ls())
MyDF <- as.data.frame(read.csv("../data/EcolArchives-E089-51-D1.csv"))
require(tidyverse)
library(tidyverse)

lm_models_data <- MyDF %>%
  group_by(Location) %>%
  do(model = lm(Predator.mass ~ Prey.mass, data = .)) %>%
  reframe(
    Location,
    intercept = summary(model)$coefficients[1],
    slope = summary(model)$coefficients[2],
    r_squared = summary(model)$r.squared,
    f_statistic = as.numeric(summary(model)$fstatistic[1]),
    p_value = summary(model)$coefficients[2,4]
  )

write.csv(lm_models_data, "../results/PP_Regress_loc_Results.csv", row.names = F)







