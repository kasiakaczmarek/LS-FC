# basic operations on csv file

def append_df_to_csv_void(df, csv_file_path, if_rownames=False, sep=";"):
    import os
    if not os.path.isfile(csv_file_path):
        df.to_csv(csv_file_path, mode='a', index=if_rownames, sep=sep)
    elif len(df.columns) != len(pd.read_csv(csv_file_path, nrows=1, sep=sep).columns):
        raise Exception("Columns do not match!! Dataframe has " + str(len(df.columns)) + " columns. CSV file has " + str(len(pd.read_csv(csv_file_path, nrows=1, sep=sep).columns)) + " columns.")
    elif not (df.columns == pd.read_csv(csv_file_path, nrows=1, sep=sep).columns).all():
        raise Exception("Columns and column order of dataframe and csv file do not match!!")
    else:
        df.to_csv(csv_file_path, mode='a', index=False, sep=sep, header=False)


#################################################################################################3
# Definition of the quantifiers
def quantifier(x):
    range_for_quantifier = np.arange(0, 1.01, 0.001)

    majority = fuzz.trapmf(range_for_quantifier, [0.45, 0.6, 1, 1])
    minority = fuzz.trapmf(range_for_quantifier, [0, 0, 0.25, 0.5])
    almost_all = fuzz.trapmf(range_for_quantifier, [0.7, 0.8, 1, 1])

    quantifier_majority = fuzz.interp_membership(range_for_quantifier, majority, x)  # Depends from Step 1
    quantifier_minority = fuzz.interp_membership(range_for_quantifier, minority, x)
    quantifier_almost_all = fuzz.interp_membership(range_for_quantifier, almost_all, x)

    return dict(majority=quantifier_majority, minority=quantifier_minority,
                almost_all=quantifier_almost_all)

#################################################################################################3
# Functions to fuzzify acoustic data about phone calls
def loudness_category(loudness_in=0, energy_in=0):

    loudness_cat_low = tnorm(fuzz.interp_membership(loudness, loudness_low, loudness_in)
    ,fuzz.interp_membership(energy, energy_low, energy_in),type="luk")
    loudness_cat_medium = tnorm(fuzz.interp_membership(loudness, loudness_medium, loudness_in)
    ,fuzz.interp_membership(energy, energy_medium, energy_in),type="luk")
    loudness_cat_high = tnorm(fuzz.interp_membership(loudness, loudness_high, loudness_in)
    ,fuzz.interp_membership(energy, energy_high, energy_in),type="luk")

    return pd.DataFrame([[loudness_cat_low, loudness_cat_medium, loudness_cat_high]],
                        columns=["loudness_low", "loudness_medium", "loudness_high"])

def loudness_table(df):
    n = df.shape[0]
    for i in range(n):
        if i == 0:
            #i=0
            d = loudness_category(df.loudness[i],df.energy[i])
        else:
            d = d.append(loudness_category(df.loudness[i],df.energy[i]),
                         ignore_index=True)
    return d

#fuzz.interp_membership(loudness, loudness_low, 0.16)
#fuzz.interp_membership(energy, energy_low, 0.01)

#df=data_mania
#loudness_in=df.loudness[1]
#loudness_category(6.81231115,4.8)

#####################################################################################################3
def tone_category(f0final_in=0, f0env_in=0):

    tone_cat_low = tnorm(fuzz.interp_membership(f0final, f0final_low, f0final_in)
    ,fuzz.interp_membership(f0env, f0env_low, f0env_in),type="luk")
    tone_cat_medium = tnorm(fuzz.interp_membership(f0final, f0final_medium, f0final_in)
    ,fuzz.interp_membership(f0env, f0env_medium, f0env_in),type="luk")
    tone_cat_high = tnorm(fuzz.interp_membership(f0final, f0final_high, f0final_in)
    ,fuzz.interp_membership(f0env, f0env_high, f0env_in),type="luk")

    return pd.DataFrame([[tone_cat_low, tone_cat_medium, tone_cat_high]],
                        columns=["tone_low", "tone_medium", "tone_high"])

def tone_table(df):
    n = df.shape[0]
    for i in range(n):
        if i == 0:
            #i=0
            d = tone_category(df.f0final[i],df.f0env[i])
        else:
            d = d.append(tone_category(df.f0final[i],df.f0env[i]),
                         ignore_index=True)
    return d


#################################################################################################3
#def spectrum_category(spectralflux_in=0, spectralcentroid_in=0):
def spectrum_category(spectralflux_in=0, spectralharmonicity_in=0):
    spectrum_cat_low = fuzz.interp_membership(spectralflux, spectralflux_low, spectralflux_in)
    #spectrum_cat_low = tnorm(fuzz.interp_membership(spectralflux, spectralflux_low, spectralflux_in)
    #,fuzz.interp_membership(spectralcentroid, spectralcentroid_low, spectralcentroid_in),type="luk")
    #,fuzz.interp_membership(spectralharmonicity, spectralharmonicity_low, spectralharmonicity_in),type="luk")
    #spectrum_cat_medium = tnorm(fuzz.interp_membership(spectralflux, spectralflux_medium, spectralflux_in)
    spectrum_cat_medium = fuzz.interp_membership(spectralflux, spectralflux_medium, spectralflux_in)
    #,fuzz.interp_membership(spectralcentroid, spectralcentroid_medium, spectralcentroid_in),type="luk")
    #,fuzz.interp_membership(spectralharmonicity, spectralharmonicity_medium, spectralharmonicity_in),type="luk")
    #spectrum_cat_high = tnorm(fuzz.interp_membership(spectralflux, spectralflux_high, spectralflux_in)
    spectrum_cat_high = fuzz.interp_membership(spectralflux, spectralflux_high, spectralflux_in)
    #,fuzz.interp_membership(spectralcentroid, spectralcentroid_high, spectralcentroid_in),type="luk")
    #,fuzz.interp_membership(spectralharmonicity, spectralharmonicity_high, spectralharmonicity_in),type="luk")
    return pd.DataFrame([[spectrum_cat_low, spectrum_cat_medium, spectrum_cat_high]],
                        columns=["spectrum_low", "spectrum_medium", "spectrum_high"])

def spectrum_table(df):
    n = df.shape[0]
    for i in range(n):
        if i == 0:
#            d = spectrum_category(df.spectralflux[i],df.spectralcentroid[i])
            d = spectrum_category(df.spectralflux[i],df.spectralharmonicity[i])
        else:
#            d = d.append(spectrum_category(df.spectralflux[i],df.spectralcentroid[i]),ignore_index=True)
            d = d.append(spectrum_category(df.spectralflux[i],df.spectralharmonicity[i]),ignore_index=True)
    return d

#################################################################################################3
def quality_category(jitterlocal_in=0, shimmerlocal_in=0):
    quality_cat_low = tnorm(fuzz.interp_membership(jitterlocal, jitterlocal_low, jitterlocal_in)
    ,fuzz.interp_membership(shimmerlocal, shimmerlocal_low, shimmerlocal_in),type="luk")
    quality_cat_medium = tnorm(fuzz.interp_membership(jitterlocal, jitterlocal_medium, jitterlocal_in)
    ,fuzz.interp_membership(shimmerlocal, shimmerlocal_medium, shimmerlocal_in),type="luk")
    quality_cat_high = tnorm(fuzz.interp_membership(jitterlocal, jitterlocal_high, jitterlocal_in)
    ,fuzz.interp_membership(shimmerlocal, shimmerlocal_high, shimmerlocal_in),type="luk")
    return pd.DataFrame([[quality_cat_low, quality_cat_medium, quality_cat_high]],
                        columns=["quality_low", "quality_medium", "quality_high"])

def quality_table(df):
    n = df.shape[0]
    for i in range(n):
        if i == 0:
            d = quality_category(df.jitterlocal[i],df.shimmerlocal[i])
        else:
            d = d.append(quality_category(df.jitterlocal[i],df.shimmerlocal[i]),ignore_index=True)
    return d


#################################################################################################3

# Function to gather all charcteristics
def characteristic_table(df):
    d1 = loudness_table(df)
    d2 = tone_table(df)
    d3 = spectrum_table(df)
    d4 = quality_table(df)
    return pd.concat([d1, d2, d3, d4], axis=1)