import unittest
from metaheuristic_algorithms.firefly_algorithm import FireflyAlgorithm
from metaheuristic_algorithms.function_wrappers.nonsmooth_multipeak_function_wrapper import NonsmoothMultipeakFunctionWrapper

class TestFireflyAlgorithm(unittest.TestCase):

    def test_find_glocal_maximum_for_nonsmooth_multipeak_function(self):

        nonsmooth_multipeak_function_wrapper = NonsmoothMultipeakFunctionWrapper()

        number_of_variables = 2
        objective = "maximization"

        firefly_algorithm = FireflyAlgorithm(nonsmooth_multipeak_function_wrapper, number_of_variables, objective)

        number_of_fireflies = 10
        maximun_generation = 10
        randomization_parameter_alpha = 0.2
        absorption_coefficient_gamma = 1.0

        result = firefly_algorithm.search(number_of_fireflies = number_of_fireflies, maximun_generation = maximun_generation, 
                                          randomization_parameter_alpha = randomization_parameter_alpha, absorption_coefficient_gamma = absorption_coefficient_gamma)

        # TODO: Improve accuracy:
        self.assertAlmostEqual(result["best_decision_variable_values"][0], 2.8327, delta = 5)
        self.assertAlmostEqual(result["best_decision_variable_values"][1], -0.0038, delta = 5)
        self.assertAlmostEqual(result["best_objective_function_value"], 3.4310, delta = 5)

if __name__ == '__main__':
    unittest.main()        