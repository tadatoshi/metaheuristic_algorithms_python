from metaheuristic_algorithms.base_algorithm import BaseAlgorithm
import numpy
from math import exp

class SimulatedAnnealing(BaseAlgorithm):

    # Real Boltzmann Constant. In general, for Simulated Annealing, it is set to 1 in order to simplify the calculation. 
    real_boltzmann_constant = 1.38065e-23

    def __init__(self, function_wrapper, number_of_variables = 1, objective = "maximization"):
        super().__init__(function_wrapper, number_of_variables, objective)

    def search(self, temperature, minimal_temperature, bolzmann_constant, energy_norm, 
               maximum_number_of_rejections = 2500, maximum_number_of_runs = 500, maximum_number_of_acceptances = 15, 
               cooling_factor = 0.95, standard_diviation_for_estimation = 6, ratio_of_energy_delta_over_evaluation_delta = 10):

        if bolzmann_constant == None:
            bolzmann_constant = self.real_boltzmann_constant

        number_of_runs = 0
        number_of_rejections = 0
        number_of_acceptances = 0
        total_evaluations = 0

        initial_estimates = self.function_wrapper.initial_decision_variable_value_estimates()

        best_evaluation = self.function_wrapper.objective_function_value(initial_estimates)

        best_solution = initial_estimates      

        # # TODO: Add the code to check with minimal_function_value if looking for the minimal value: 
        while temperature > minimal_temperature and number_of_rejections <= maximum_number_of_rejections:

            number_of_runs = number_of_runs + 1

            if number_of_runs >= maximum_number_of_runs or number_of_acceptances > maximum_number_of_acceptances:
                temperature = cooling_factor * temperature
                total_evaluations = total_evaluations + 1
                number_of_runs = 1
                number_of_acceptances = 1

            new_estimates = self.__estimate_solution(initial_estimates, standard_diviation_for_estimation)
            new_evaluation = self.function_wrapper.objective_function_value(new_estimates)

            evaluation_delta = ratio_of_energy_delta_over_evaluation_delta * (new_evaluation - best_evaluation)

            # Accept if improved:
            # When objective = :maximization, "if evaluation_delta > 0 && evaluation_delta > energy_norm"
            # When objective = :minimization, "if evaluation_delta < 0 && -evaluation_delta > energy_norm"
            if self.__compare_evaluation_delta(evaluation_delta, 0) or abs(evaluation_delta) > energy_norm:
                best_solution = new_estimates
                best_evaluation = new_evaluation
                number_of_acceptances = number_of_acceptances + 1
                number_of_rejections = 0
            # Accept with a small probability if not improved
            elif self.__acceptance_probability(evaluation_delta, temperature, bolzmann_constant) > random.random():
                best_solution = new_estimates
                best_evaluation = new_evaluation
                number_of_acceptances = number_of_acceptances + 1            
            else:
                number_of_rejections = number_of_rejections + 1

        return { "best_decision_variable_values": best_solution, "best_objective_function_value": best_evaluation }

    def __estimate_solution(self, previous_estimates, standard_diviation_for_estimation):
        return [self.__estimate_solution_for_given_variable_index(variable_index, previous_estimates, standard_diviation_for_estimation) for variable_index in range(self.number_of_variables)]

    def __estimate_solution_for_given_variable_index(self, variable_index, previous_estimates, standard_diviation_for_estimation):    

        # The value out-of-range in order to enter while loop
        new_estimate = self.function_wrapper.minimum_decision_variable_values()[variable_index] - 1

        while new_estimate < self.function_wrapper.minimum_decision_variable_values()[variable_index] or new_estimate > self.function_wrapper.maximum_decision_variable_values()[variable_index]:
            # MatLab example code uses newGuess = initialGuess + rand(1,2) * randn;
            # But in our case, the value range is different. 
            new_estimate = numpy.random.normal(previous_estimates[variable_index], standard_diviation_for_estimation)

        return new_estimate

    def __acceptance_probability(self, evaluation_delta, temperature, bolzmann_constant):
        exp(-evaluation_delta / (bolzmann_constant * temperature))     

    # evaluation_delta > comparison_value or evaluation_delta < comparison_value
    def __compare_evaluation_delta(self, evaluation_delta, comparison_value):

        if self.objective == "maximization":
            comparison_result = evaluation_delta > comparison_value
        elif self.objective == "minimization":
            comparison_result = evaluation_delta < comparison_value

        return comparison_result

