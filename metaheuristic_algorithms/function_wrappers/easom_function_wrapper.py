from metaheuristic_algorithms.function_wrappers.abstract_wrapper import AbstractWrapper
from math import cos, exp, pi

class EasomFunctionWrapper(AbstractWrapper):

    def maximum_decision_variable_values(self):
        return [10]

    def minimum_decision_variable_values(self):
        return [-10]

    def objective_function_value(self, decision_variable_values):
        return -cos(decision_variable_values[0]) * exp(-(decision_variable_values[0] - pi)**2)

    def initial_decision_variable_value_estimates(self):
        pass