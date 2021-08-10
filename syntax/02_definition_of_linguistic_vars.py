        
def tnorm(a,b,type="min"):
    if(tnorm=="min"):
        p = np.fmin(a, b)
    else:
        p = np.fmax(0,(a+b-1))
    return p 

for parameter in parameters:
    print(parameter)
    #parameter="loudness"

    ########################################################################################################3
    #calculate stats
    data_parameter=data_euthymia[[parameter]]
    min_for_universe = data_parameter.min()[parameter]
    max_for_universe=np.max([np.max(data_euthymia[[parameter]])[parameter],np.max(data_hipomania[[parameter]])[parameter],np.max(data_mania[[parameter]])[parameter]])/2
    #data_parameter.max()[parameter]
    a=min_for_universe
    b = data_parameter.quantile(0.95)[parameter]
    #b = df4.value.quantile(0.95)

    first_quartile = np.percentile(data_parameter, 25)
    median_quartile = np.percentile(data_parameter, 50)
    third_quartile = np.percentile(data_parameter, 75)
    
    if(clusters):
#        data_clusters=prototypes[[parameter]][1:4]
        data_clusters=prototypes[[parameter]]
        first_quartile = np.percentile(data_clusters, 25)
        median_quartile = np.percentile(data_clusters, 50)
        third_quartile = np.percentile(data_clusters, 75)
    
    ########################################################################################################3
    
    if(parameter=="energy"):
        energy = np.arange(a,max_for_universe, 0.00001)
        if(ling_var == "interval"):
            energy_low = fuzz.trapmf(energy,[a, a,a + (b-a)/4,a + (b-a)/2])
            energy_medium = fuzz.trapmf(energy,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            energy_high = fuzz.trapmf(energy,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            energy_low = fuzz.trapmf(energy, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            energy_medium = fuzz.trimf(energy, [first_quartile, median_quartile, third_quartile])
            energy_high = fuzz.trapmf(energy, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="energy"
            ax0.plot(energy, energy_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(energy, energy_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(energy, energy_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="loudness"):
        loudness = np.arange(a,max_for_universe, 0.001)
        if(ling_var == "interval"):
            loudness_low = fuzz.trapmf(loudness,[a, a,a + (b-a)/4,a + (b-a)/2])
            loudness_medium = fuzz.trapmf(loudness,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            loudness_high = fuzz.trapmf(loudness,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            loudness_low = fuzz.trapmf(loudness, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            loudness_medium = fuzz.trimf(loudness, [first_quartile, median_quartile, third_quartile])
            loudness_high = fuzz.trapmf(loudness, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="loudness"
            ax0.plot(loudness, loudness_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(loudness, loudness_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(loudness, loudness_high, 'gray', linewidth=3, label=name_param+' high')
            #ax0.set_title(name_param +" - " +ling_var)
            ax0.set_title("loudness level")
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="f0final"):
        f0final = np.arange(a,max_for_universe, 0.001)
        if(ling_var == "interval"):
            f0final_low = fuzz.trapmf(f0final,[a, a,a + (b-a)/4,a + (b-a)/2])
            f0final_medium = fuzz.trapmf(f0final,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            f0final_high = fuzz.trapmf(f0final,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            f0final_low = fuzz.trapmf(f0final, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            f0final_medium = fuzz.trimf(f0final, [first_quartile, median_quartile, third_quartile])
            f0final_high = fuzz.trapmf(f0final, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="f0final"
            ax0.plot(f0final, f0final_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(f0final, f0final_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(f0final, f0final_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="f0env"):
        f0env = np.arange(a,max_for_universe, 0.001)
        #f0env = np.arange(180,220, 0.001)
        #min_for_universe=180
        #max_for_universe=220
        if(ling_var == "interval"):
            f0env_low = fuzz.trapmf(f0env,[a, a,a + (b-a)/4,a + (b-a)/2])
            f0env_medium = fuzz.trapmf(f0env,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            f0env_high = fuzz.trapmf(f0env,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            f0env_low = fuzz.trapmf(f0env, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            f0env_medium = fuzz.trimf(f0env, [first_quartile, median_quartile, third_quartile])
            f0env_high = fuzz.trapmf(f0env, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="f0env"
            ax0.plot(f0env, f0env_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(f0env, f0env_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(f0env, f0env_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="spectralflux"):
        spectralflux = np.arange(a,max_for_universe, 0.0001)
        if(ling_var == "interval"):
            spectralflux_low = fuzz.trapmf(spectralflux,[a, a,a + (b-a)/4,a + (b-a)/2])
            spectralflux_medium = fuzz.trapmf(spectralflux,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            spectralflux_high = fuzz.trapmf(spectralflux,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            spectralflux_low = fuzz.trapmf(spectralflux, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            spectralflux_medium = fuzz.trimf(spectralflux, [first_quartile, median_quartile, third_quartile])
            spectralflux_high = fuzz.trapmf(spectralflux, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="spectralflux"
            ax0.plot(spectralflux, spectralflux_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(spectralflux, spectralflux_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(spectralflux, spectralflux_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="spectralcentroid"):
        spectralcentroid = np.arange(a,max_for_universe, 0.001)
        if(ling_var == "interval"):
            spectralcentroid_low = fuzz.trapmf(spectralcentroid,[a, a,a + (b-a)/4,a + (b-a)/2])
            spectralcentroid_medium = fuzz.trapmf(spectralcentroid,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            spectralcentroid_high = fuzz.trapmf(spectralcentroid,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            spectralcentroid_low = fuzz.trapmf(spectralcentroid, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            spectralcentroid_medium = fuzz.trimf(spectralcentroid, [first_quartile, median_quartile, third_quartile])
            spectralcentroid_high = fuzz.trapmf(spectralcentroid, [median_quartile, third_quartile, max_for_universe, max_for_universe])    
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="spectralcentroid"
            ax0.plot(spectralcentroid, spectralcentroid_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(spectralcentroid, spectralcentroid_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(spectralcentroid, spectralcentroid_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="spectralharmonicity"):
        spectralharmonicity = np.arange(a,max_for_universe, 0.001)
        if(ling_var == "interval"):
            spectralharmonicity_low = fuzz.trapmf(spectralharmonicity,[a, a,a + (b-a)/4,a + (b-a)/2])
            spectralharmonicity_medium = fuzz.trapmf(spectralharmonicity,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            spectralharmonicity_high = fuzz.trapmf(spectralharmonicity,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            spectralharmonicity_low = fuzz.trapmf(spectralharmonicity, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            spectralharmonicity_medium = fuzz.trimf(spectralharmonicity, [first_quartile, median_quartile, third_quartile])
            spectralharmonicity_high = fuzz.trapmf(spectralharmonicity, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="spectralharmonicity"
            ax0.plot(spectralharmonicity, spectralharmonicity_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(spectralharmonicity, spectralharmonicity_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(spectralharmonicity, spectralharmonicity_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="jitterlocal"):
        jitterlocal = np.arange(a,max_for_universe, 0.0001)
        if(ling_var == "interval"):
            jitterlocal_low = fuzz.trapmf(jitterlocal,[a, a,a + (b-a)/4,a + (b-a)/2])
            jitterlocal_medium = fuzz.trapmf(jitterlocal,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            jitterlocal_high = fuzz.trapmf(jitterlocal,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            jitterlocal_low = fuzz.trapmf(jitterlocal, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            jitterlocal_medium = fuzz.trimf(jitterlocal, [first_quartile, median_quartile, third_quartile])
            jitterlocal_high = fuzz.trapmf(jitterlocal, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="jitterlocal"
            ax0.plot(jitterlocal, jitterlocal_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(jitterlocal, jitterlocal_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(jitterlocal, jitterlocal_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()


    
    if(parameter=="jitterddp"):
        jitterddp = np.arange(a,max_for_universe, 0.001)
        if(ling_var == "interval"):
            jitterddp_low = fuzz.trapmf(jitterddp,[a, a,a + (b-a)/4,a + (b-a)/2])
            jitterddp_medium = fuzz.trapmf(jitterddp,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            jitterddp_high = fuzz.trapmf(jitterddp,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            jitterddp_low = fuzz.trapmf(jitterddp, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            jitterddp_medium = fuzz.trimf(jitterddp, [first_quartile, median_quartile, third_quartile])
            jitterddp_high = fuzz.trapmf(jitterddp, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="spectralcentroid"
            ax0.plot(jitterddp, jitterddp_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(jitterddp, jitterddp_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(jitterddp, jitterddp_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    if(parameter=="shimmerlocal"):
        shimmerlocal = np.arange(a,max_for_universe, 0.001)
        if(ling_var == "interval"):
            shimmerlocal_low = fuzz.trapmf(shimmerlocal,[a, a,a + (b-a)/4,a + (b-a)/2])
            shimmerlocal_medium = fuzz.trapmf(shimmerlocal,[a + (b-a)/4, a + (b-a)/2,a + (b-a)/2,a + (b-a)*3/4])
            shimmerlocal_high = fuzz.trapmf(shimmerlocal,[a + (b-a)/2 , a + (b-a)*3/4, max_for_universe, max_for_universe])
        if(ling_var == "quartiles"):
            shimmerlocal_low = fuzz.trapmf(shimmerlocal, [min_for_universe, min_for_universe, first_quartile, median_quartile])
            shimmerlocal_medium = fuzz.trimf(shimmerlocal, [first_quartile, median_quartile, third_quartile])
            shimmerlocal_high = fuzz.trapmf(shimmerlocal, [median_quartile, third_quartile, max_for_universe, max_for_universe])
        if if_plot: 
            #exec(open(path_scripts + '02_plot_linguistic_vars.py').read())
            fig, (ax0) = plt.subplots(nrows=1, figsize=(6, 3))
            name_param="shimmerlocal"
            ax0.plot(shimmerlocal, shimmerlocal_low, 'b', linewidth=3, label=name_param+' low')
            ax0.plot(shimmerlocal, shimmerlocal_medium, 'g', linewidth=3, label=name_param+' medium')
            ax0.plot(shimmerlocal, shimmerlocal_high, 'gray', linewidth=3, label=name_param+' high')
            ax0.set_title(name_param +" - " +ling_var)
            ax0.legend()
            ax0.set_ylim([0, 1.05])
            fig.savefig(path_plots + patient_id +  "_ling_variable_"+name_param+ling_var+".pdf", bbox_inches='tight')
            plt.close()
    
    


