import unittest
from metaheuristic_algorithms.simulated_annealing import SimulatedAnnealing
from metaheuristic_algorithms.function_wrappers.rosenbrook_function_wrapper import RosenbrookFunctionWrapper

class TestSimulatedAnnealing(unittest.TestCase):

    @unittest.skip("Execution takes too long")
    def test_find_glocal_minimum_for_rosenbrook_function(self):

        rosenbrook_function_wrapper = RosenbrookFunctionWrapper()

        number_of_variables = 2
        objective = "minimization"

        simulated_annealing = SimulatedAnnealing(rosenbrook_function_wrapper, number_of_variables, objective)

        temperature = 1.0
        minimal_temperature = 1e-10 # Final stopping temperature
        # minimal_temperature = 1e-1 # Final stopping temperature
        maximum_number_of_rejections = 2500
        # maximum_number_of_rejections = 1000
        maximum_number_of_runs = 500
        # maximum_number_of_runs = 100
        maximum_number_of_acceptances = 15
        bolzmann_constant = 1
        cooling_factor = 0.95
        energy_norm = 1e-8
        # energy_norm = 1e-1
        standard_diviation_for_estimation = 1
        ratio_of_energy_delta_over_evaluation_delta = 1

        result = simulated_annealing.search(temperature, minimal_temperature, 
                                            bolzmann_constant, energy_norm, 
                                            maximum_number_of_rejections = maximum_number_of_rejections, 
                                            maximum_number_of_runs = maximum_number_of_runs, 
                                            maximum_number_of_acceptances = maximum_number_of_acceptances, 
                                            cooling_factor = cooling_factor, 
                                            standard_diviation_for_estimation = standard_diviation_for_estimation, 
                                            ratio_of_energy_delta_over_evaluation_delta = ratio_of_energy_delta_over_evaluation_delta)

        self.assertAlmostEqual(result["best_decision_variable_values"][0], 1.0112, delta = 1)
        self.assertAlmostEqual(result["best_decision_variable_values"][1], 0.9988, delta = 1)
        self.assertAlmostEqual(result["best_objective_function_value"], 0.0563, delta = 1)

if __name__ == '__main__':
    unittest.main()        