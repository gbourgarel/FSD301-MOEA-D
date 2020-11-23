import matplotlib.pyplot as plt
plt.scatter(*ref_dirs.T)
plt.xlabel('Objective 0')
plt.ylabel('Objective 1')
plt.title('Subproblems weights')
plt.show()

# each point defines a subproblem.
# a subproblem is based on weights of each objective.
# it is important to keep subproblems even spread, to get a pareto front with no gap

