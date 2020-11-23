# You can choose different termination criterions:
termination = ('n_eval', 10000)
#termination = ('n_gen', 100)
#termination = ('time', 10) # time in seconds

res_nsga2 = minimize(problem, nsga2, termination=termination)
res_moead = minimize(problem, moead, termination=termination)
plot = get_visualization('scatter')
plot.add(res_nsga2.F, label='NSGA2')
plot.add(res_moead.F, label='MOEA-D')
plot.legend=True
plot.show()
