from pymoo.model.problem import Problem
import numpy as np

class MOTSP(Problem):
    
    def __init__(self, n_cities, n_obj):
        # lower bound
        xl = np.zeros(n_cities)
        # upper bound
        xu = (n_cities-1) * np.ones(n_cities)
        
        self.n_cities = n_cities
        self.distances = []
        for i in range(n_obj):
            # random symmetric matrix
            d = np.random.rand(n_cities, n_cities)
            d = np.tril(d) + np.tril(d, -1).T
            d[np.diag_indices(n_cities)] = 0
            self.distances.append(d)
        
        super().__init__(n_var=n_cities, n_obj=n_obj, n_constr=1,
                        xl=xl, xu=xu, elementwise_evaluation=True)
        
    def total_distance(self, x, d):
        t = 0
        for i in range(len(x)):
            t += self.distances[d][x[i-1], x[i]]
        return t
    
    def _evaluate(self, x, out, *args, **kwargs):
        # fitness based on each distance matrix
        fits = np.zeros(len(self.distances))
        for i in range(len(self.distances)):
            fits[i] = self.total_distance(x, i)
        
        # constraints return negative if met
        c = -np.sum(np.arange(self.n_cities) != np.sort(x))
        
        # return by modifying out
        out["F"] = np.column_stack(fits)
        out["G"] = np.array([c])


