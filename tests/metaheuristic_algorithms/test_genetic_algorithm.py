import unittest
from metaheuristic_algorithms.genetic_algorithm import GeneticAlgorithm
from metaheuristic_algorithms.function_wrappers.easom_function_wrapper import EasomFunctionWrapper

class TestGeneticAlgorithm(unittest.TestCase):

    @unittest.skip("Need to find a way to convert float to binary and vice versa")
    def test_find_glocal_minimum_for_easom_function(self):

        easom_function_wrapper = EasomFunctionWrapper()

        number_of_variables = 1
        objective = "maximization"

        genetic_algorithm = GeneticAlgorithm(easom_function_wrapper, number_of_variables, objective)

        population_size = 20
        maximum_number_of_generations = 100
        number_of_mutation_sites = 2
        crossover_probability = 0.95
        mutation_probability = 0.05

        result = genetic_algorithm.search(population_size = population_size, maximum_number_of_generations = maximum_number_of_generations, 
                                          number_of_mutation_sites = number_of_mutation_sites, crossover_probability = crossover_probability, 
                                          mutation_probability = mutation_probability)

        self.assertAlmostEqual(result["best_decision_variable_values"][0], 3.1416, delta = 1)
        self.assertAlmostEqual(result["best_objective_function_value"], 1.000, delta = 1)

if __name__ == '__main__':
    unittest.main()