
"""
Create linguistic summaries using prototypes from DISSFCM
@author KKM
"""

path_scripts = r'c:/Users/Kasia/Documents/GitHub/MLC_for_CHAD/future_generation/syntax/'
exec(open(path_scripts+'00_config.py').read())

patient_id = "1472/"

parameters = ["loudness"
             ,"energy"
             ,"f0final"
             ,"f0env"
             ,"spectralflux"
             ,"spectralcentroid"
             ,"spectralharmonicity"
             ,"jitterlocal"
             ,"jitterddp"
             ,"shimmerlocal"]

#for parameter in parameters:
#    print(parameter)   
#parameter=parameters[1]             

# selection of variant for ling var creation
#ling_var = "interval"
ling_var = "quartiles"
clusters = True

#name_of_run = "only spectralflux - Quartiles"
date="20210630"
name_of_run = date+" only chunks6-8 "+ling_var

# EUTHYMIA ----------------------------------------------
state = "euthymia"
#path_ids = path_data+patient_id+state

#importa data
data_euthymia=pd.read_csv(path_data+'agg_data_euthymia.csv')
data_mania=pd.read_csv(path_data+'agg_data_mania.csv')
data_hipomania=pd.read_csv(path_data+'agg_data_hipomania.csv')

prototypes=pd.read_csv(path_data+'prototypes_euthymia.csv',sep=";")

#config
first = True
if_plot = True

n = len(data_euthymia)+len(data_hipomania)+len(data_mania)
standarization=False
# n = 5

#first = False

# EUTHYMIA ----------------------------------------------
table_name = path_results + name_of_run

# set linguistic variables
data=data_euthymia
exec(open(path_scripts + '02_definition_of_linguistic_vars.py').read())

exec(open(path_scripts + '03_def_of_functions.py').read())

# MANIA ----------------------------------------------
state = "mania"
data=pd.read_csv(path_data+'agg_data_mania.csv')
exec(open(path_scripts+'04_gen_linguistic_summaries.py').read())

# HIPOMANIA ----------------------------------------------
state = "hipomania"
data=pd.read_csv(path_data+'agg_data_hipomania.csv')
exec(open(path_scripts+'04_gen_linguistic_summaries.py').read())

