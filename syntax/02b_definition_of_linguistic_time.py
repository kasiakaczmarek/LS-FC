time = np.arange(0,1, 0.01)
a =  0
b =  1

time_beginning = fuzz.trapmf(time ,[a, a, 0.25 ,0.5])
time_middle = fuzz.trapmf(time ,[0.25, 0.5, 0.5,0.75])
time_ending = fuzz.trapmf(time ,[0.5, 0.75, b, b])

# different time phases
# time_beginning = fuzz.trapmf(time ,[a, a, 0.10 ,0.30])
# time_middle = fuzz.trapmf(time ,[0.20, 0.40, 0.60,0.80])
# time_ending = fuzz.trapmf(time ,[0.70, 0.90, b, b])

fig, (ax0) = plt.subplots(nrows=1, figsize=(8, 9))
ax0.plot(time, time_beginning, 'b', linewidth=1.5, label='time_beginning')
ax0.plot(time, time_middle, 'g', linewidth=1.5, label='time_middle')
ax0.plot(time, time_ending, 'r', linewidth=1.5, label='time_ending')
ax0.set_title('Time')
ax0.legend()
ax0.set_ylim([0, 1.05])
fig.savefig(path_plots + patient_id + parameter + state +"_time.pdf", bbox_inches='tight')
plt.close()