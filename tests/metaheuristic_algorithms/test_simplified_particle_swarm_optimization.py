import unittest
from metaheuristic_algorithms.simplified_particle_swarm_optimization import SimplifiedParticleSwarmOptimization
from metaheuristic_algorithms.function_wrappers.michaelwicz_function_wrapper import MichaelwiczFunctionWrapper

class TestSimplifiedParticleSwarmOptimization(unittest.TestCase):

    def test_find_glocal_minimum_for_michaelwicz_function(self):

        michaelwicz_function_wrapper = MichaelwiczFunctionWrapper()

        number_of_variables = 2
        objective = "minimization"

        simplified_particle_swarm_optimization = SimplifiedParticleSwarmOptimization(michaelwicz_function_wrapper, number_of_variables, objective)

        number_of_particiles = 20
        number_of_iterations = 15
        social_coefficient = 0.5
        random_variable_coefficient = 0.2

        result = simplified_particle_swarm_optimization.search(number_of_particiles = number_of_particiles, number_of_iterations = number_of_iterations, 
                                                               social_coefficient = social_coefficient, random_variable_coefficient = random_variable_coefficient)

        self.assertAlmostEqual(result["best_decision_variable_values"][0], 2.1701, delta = 1)
        self.assertAlmostEqual(result["best_decision_variable_values"][1], 1.5703, delta = 1)
        self.assertAlmostEqual(result["best_objective_function_value"], -1.7843, delta = 1)

if __name__ == '__main__':
    unittest.main()        