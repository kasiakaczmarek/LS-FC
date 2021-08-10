# packages ----------------------------------------------------------------

pkgs <- c("plotly","readxl","lubridate","haven","dplyr","ggplot2"
          ,"reshape2","stringdist","RODBC","openxlsx", "readr","readxl","stringr" ,"purrr"
          ,"gdata", "tidyverse", "readxl", "rlist", "stringi", "data.table", "gdata", "splitstackshape",  "tidyr", "lubridate",
          "data.table", "zoo", "openxlsx", "readr", "funModeling","DALEX",
          "mlr", "lubridate", "stringr", "caret", "hashids", "vroom", "lintr", "DataExplorer", "qwraps2", "ParamHelpers", "rio",
          "httr", "RcppRoll", "Hmisc", "corrplot") 


for (pkg in pkgs) {
  if (!(pkg %in% rownames(installed.packages())))
  {install.packages(pkg, dependencies = TRUE)
    library(pkg, character.only = TRUE)}
  else
  {library(pkg, character.only = TRUE)}
}

library("readr")
library("DataCombine")

install.packages("RColorBrewer")
library("RColorBrewer")
display.brewer.all()
col=brewer.pal(n = 3, name = "RdBu")

library(dplyr)

# prepare data of protoforms --------------------------
protoforms <- read.csv("linguistic_summaries/results/1472/loudness_sma3/_protoforms.csv", sep = ";"
                       # , col.names = c("protoform", "DoT", "id", "label")
)

if(nrow(protoforms) != nrow(unique(protoforms))){
  protoforms <- protoforms %>% group_by(id, protoform) %>% 
    mutate(n = row_number()) %>% 
    filter(n == 1) %>% 
    ungroup() %>% 
    select(-n)
} else{print("no duplicates")}

protoforms$id %>% unique() %>% length()

protoforms$protoform <- gsub(',', '', protoforms$protoform)
protoforms$protoform <- gsub(' ', '_', protoforms$protoform)

protoforms <- protoforms %>% 
  mutate(protoform = ifelse(Type == 1, paste0("short_", protoform), paste0("extended_", protoform)))

protoforms <- protoforms %>% pivot_wider(id_cols = c(id, label),
                                         names_from = protoform,
                                         values_from = DoT,
                                         names_glue = "protoforms_{.value}_{protoform}") 


# rfe -----------------------------------------
target <- factor(protoforms$label)
control <- rfeControl(functions = rfFuncs, method = "cv", number = 5)

lst <- rfe(
  protoforms[, 3:ncol(protoforms)],
  target,
  sizes = 10,
  metric = "Accuracy",
  rfeControl = control
)
  
variables <- predictors(lst)[1:10]



# histograms ----------------------------------
# plot density plots
for(i in 1:length(variables)){
  
  name <- variables[i]
  df <- cbind(protoforms[variables[i]], protoforms["label"])
  
  ggplot(df, aes(get(variables[i]), fill = label)) + geom_density(alpha = 0.2) +xlab(name)
  ggsave(paste0("linguistic_summaries/plots/1472/loudness_sma3/histograms_of_rfe/histogram_relative_",name,".pdf"), width = 16, height = 8)    
  
}
