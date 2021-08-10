def Degree_of_truth_ext(d, Q="majority", P="loudness_medium", R="",tnorm="min"):
    """
    Degree of truth for extended protofors
    """

    if(tnorm=="min"):
        p = np.fmin(d[P], d[R])
    else:
        p = np.fmax(0,(d[P]+d[R]-1))
    
    r = d[R]
    t = np.sum(p) / np.sum(r)
    
    if np.sum(r) == 0:
        t = 0
    else:
        t = np.sum(p) / np.sum(r)

    return quantifier(t)[Q]

def Degree_of_truth(d, Q="minority", P="loudness_low", P2=""):
    """
    Degree of truth for short protofors
    """
    if P2 == "":
        p = np.mean(d[P])
    else:
        p = np.mean(np.fmin(d[P], d[P2]))

 #       p = np.fmax(0,(d[P]+d[R]-1))

    return quantifier(p)[Q]

def all_protoform(d, state="mania", ending=" compared to the state of euthymia."):
    """
    Function aggregating summaries of short and extended form for all groups of parameters
    """
    pp = ["loudness_low", "loudness_medium", "loudness_high"]
    rr = ["tone_low", "tone_medium", "tone_high"]
    qq = ["spectrum_low", "spectrum_medium", "spectrum_high"]
    zz = ["quality_low", "quality_medium", "quality_high"]

    protoform = np.empty(240, dtype="object")
    DoT = np.zeros(240)
    Type = np.zeros(240)
    k = 0
    for i in range(len(pp)):
        DoT[k] = Degree_of_truth(d=d, Q="majority", P=qq[i])
        protoform[k] = "Most calls "+"in "+state +" are "+ qq[i] +ending
        Type[k] = 1
        k += 1
        DoT[k] = Degree_of_truth(d=d, Q="majority", P=pp[i])
        protoform[k] = "Most calls "+"in "+state +" are "+pp[i]+ending
        Type[k] = 1
        k += 1
        DoT[k] = Degree_of_truth(d=d, Q="majority", P=rr[i])
        protoform[k] = "Most calls "+"in "+state +" are "+ rr[i]+ending
        Type[k] = 1
        k += 1
        DoT[k] = Degree_of_truth(d=d, Q="majority", P=zz[i])
        protoform[k] = "Most calls "+"in "+state +" are "+ zz[i] +ending
        Type[k] = 1
        k += 1
        
        DoT[k] = Degree_of_truth(d=d, Q="minority", P=qq[i])
        protoform[k] = "Minority of calls "+"in "+state +" are "+ qq[i] +ending
        Type[k] = 1
        k += 1
        DoT[k] = Degree_of_truth(d=d, Q="minority", P=pp[i])
        protoform[k] = "Minority of calls "+"in "+state +" are "+pp[i]+ending
        Type[k] = 1
        k += 1
        DoT[k] = Degree_of_truth(d=d, Q="minority", P=rr[i])
        protoform[k] = "Minority of calls "+"in "+state +" are "+ rr[i]+ending
        Type[k] = 1
        k += 1
        DoT[k] = Degree_of_truth(d=d, Q="minority", P=zz[i])
        protoform[k] = "Minority of calls "+"in "+state +" are "+ zz[i] +ending
        Type[k] = 1
        k += 1

    for i in range(len(pp)):
        for j in range(len(rr)):
            #i=1
            #j=1
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=qq[j], R=pp[i])
            protoform[k] = "Most " + pp[i] + " calls "+"in "+state +" are "+ qq[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=qq[j], R=pp[i])
            protoform[k] = "Minority of " + pp[i] + " calls "+"in "+state +" are "+ qq[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=rr[j], R=pp[i])
            protoform[k] = "Most " + pp[i] + " calls "+"in "+state +" are "+ rr[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=rr[j], R=pp[i])
            protoform[k] = "Minority of " + pp[i] + " calls "+"in "+state +" are "+ rr[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=zz[j], R=pp[i])
            protoform[k] = "Most " + pp[i] + " calls "+"in "+state +" are "+ zz[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=zz[j], R=pp[i])
            protoform[k] = "Minority of " + pp[i] + " calls "+"in "+state +" are "+ zz[j]+ending
            Type[k] = 2
            k += 1
    for i in range(len(pp)):
        for j in range(len(rr)):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=qq[j], R=rr[i])
            protoform[k] = "Most " + rr[i] + " calls "+"in "+state +" are "+ qq[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=qq[j], R=rr[i])
            protoform[k] = "Minority of " + rr[i] + " calls "+"in "+state +" are "+ qq[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=pp[j], R=rr[i])
            protoform[k] = "Most " + rr[i] + " calls "+"in "+state +" are "+ pp[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=pp[j], R=rr[i])
            protoform[k] = "Minority " + rr[i] + " calls "+"in "+state +" are "+ pp[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=zz[j], R=rr[i])
            protoform[k] = "Most " + rr[i] + " calls "+"in "+state +" are "+ zz[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=zz[j], R=rr[i])
            protoform[k] = "Minority of " + rr[i] + " calls "+"in "+state +" are "+ zz[j]+ending
            Type[k] = 2
            k += 1

    for i in range(len(pp)):
        for j in range(len(rr)):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=rr[j], R=qq[i])
            protoform[k] = "Most " + qq[i] + " calls "+"in "+state +" are "+ rr[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=rr[j], R=qq[i])
            protoform[k] = "Minority of " + qq[i] + " calls "+"in "+state +" are "+ rr[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=pp[j], R=qq[i])
            protoform[k] = "Most " + qq[i] + " calls "+"in "+state +" are "+ pp[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=pp[j], R=qq[i])
            protoform[k] = "Minority of " + qq[i] + " calls "+"in "+state +" are "+ pp[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=zz[j], R=qq[i])
            protoform[k] = "Most " + qq[i] + " calls "+"in "+state +" are "+ zz[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=zz[j], R=qq[i])
            protoform[k] = "Minority of " + qq[i] + " calls "+"in "+state +" are "+ zz[j]+ending
            Type[k] = 2
            k += 1

    for i in range(len(pp)):
        for j in range(len(rr)):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=rr[j], R=zz[i])
            protoform[k] = "Most " + zz[i] + " calls "+"in "+state +" are "+ rr[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=rr[j], R=zz[i])
            protoform[k] = "Minority of " + zz[i] + " calls "+"in "+state +" are "+ rr[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=pp[j], R=zz[i])
            protoform[k] = "Most " + zz[i] + " calls "+"in "+state +" are "+ pp[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=pp[j], R=zz[i])
            protoform[k] = "Minority of " + zz[i] + " calls "+"in "+state +" are "+ pp[j]+ending
            Type[k] = 2
            k += 1

        for j in range(3):
            DoT[k] = Degree_of_truth_ext(d=d, Q="majority", P=qq[j], R=zz[i])
            protoform[k] = "Most " + zz[i] + " calls "+"in "+state +" are "+ qq[j]+ending
            Type[k] = 2
            k += 1

            DoT[k] = Degree_of_truth_ext(d=d, Q="minority", P=qq[j], R=zz[i])
            protoform[k] = "Minority of " + zz[i] + " calls "+"in "+state +" are "+ qq[j]+ending
            Type[k] = 2
            k += 1

    dd = {"protoform": protoform,
          "DoT": DoT,
          "Type": Type}
    dd = pd.DataFrame(dd)
    return dd[['protoform', "DoT", "Type"]]



d = characteristic_table(data)
d['id'] = name_of_run

csvFilePath = path_results + patient_id  + "_characteristic_table.csv"
append_df_to_csv_void(d, csvFilePath, False, sep=";")


Degree_of_truth(d=d, Q="majority", P="loudness_high")
Degree_of_truth(d=d, Q="minority", P="loudness_high")

#Degree_of_truth(d=d, Q="majority", P="duration_short")
#Degree_of_truth(d=d, Q="majority", P="duration_short", P2="dynamics_decreasing")
#Degree_of_truth_ext(d=d, Q="majority", P="duration_long", R="dynamics_increasing")



pd.set_option('max_colwidth', 70)
df_protoform = all_protoform(d, state)

df_protoform['id'] = name_of_run
csvFilePath = path_results + patient_id +  "_protoforms"+name_of_run+".csv"
append_df_to_csv_void(df_protoform, csvFilePath, sep=";")
