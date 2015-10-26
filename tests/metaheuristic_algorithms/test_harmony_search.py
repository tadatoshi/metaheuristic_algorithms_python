import unittest
from metaheuristic_algorithms.harmony_search import HarmonySearch
from metaheuristic_algorithms.function_wrappers.rosenbrook_function_wrapper import RosenbrookFunctionWrapper

class TestHarmonySearch(unittest.TestCase):

    def test_find_glocal_minimum_for_rosenbrook_function(self):

        rosenbrook_function_wrapper = RosenbrookFunctionWrapper()

        number_of_variables = 2
        objective = "minimization"

        harmony_search = HarmonySearch(rosenbrook_function_wrapper, number_of_variables, objective)

        maximum_attempt = 25000
        pitch_adjusting_range = 100
        harmony_search_size = 20
        harmony_memory_acceping_rate = 0.95
        pitch_adjusting_rate = 0.7

        result = harmony_search.search(maximum_attempt, pitch_adjusting_range, 
                                       harmony_search_size, harmony_memory_acceping_rate, 
                                       pitch_adjusting_rate)

        self.assertAlmostEqual(result["best_decision_variable_values"][0], 1.0112, 0)
        self.assertAlmostEqual(result["best_decision_variable_values"][1], 0.9988, 0)
        self.assertAlmostEqual(result["best_objective_function_value"], 0.0563, 0)

if __name__ == '__main__':
    unittest.main()        