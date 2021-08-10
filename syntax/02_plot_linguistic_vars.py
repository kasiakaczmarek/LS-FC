

########################################################################################################3
fig, (ax0) = plt.subplots(nrows=1, figsize=(4, 2))
ax0.plot(loudness, loudness_low, 'b', linewidth=3, label='loudness_low')
ax0.plot(loudness, loudness_medium, 'g', linewidth=3, label='loudness_medium')
ax0.plot(loudness, loudness_high, 'gray', linewidth=3, label='loudness_high')
ax0.set_title('loudness - '+ling_var)
ax0.legend()
ax0.set_ylim([0, 1.05])
fig.savefig(path_plots + patient_id +  "_ling_variables_"+"_loudness_"+ling_var+".pdf", bbox_inches='tight')
plt.close()
########################################################################################################3

