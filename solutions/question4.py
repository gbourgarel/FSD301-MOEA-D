plot = get_visualization('scatter')
for prob_neighbor_mating in [.0, .5, 1.]:
    moead = MOEAD(
        ref_dirs = ref_dirs,
        n_neighbors=20,
        decomposition='tchebi',
        prob_neighbor_mating=prob_neighbor_mating,
        sampling=get_sampling("perm_random"),
        crossover=get_crossover("perm_erx", prob=.9),
        mutation=get_mutation("perm_inv"),
    )
    res_moead = minimize(problem, moead, termination=('n_eval', 1000))
    plot.add(res_moead.F, label='prob_neighbor_mating: {}'.format(prob_neighbor_mating))
plot.legend=True
plot.show()

