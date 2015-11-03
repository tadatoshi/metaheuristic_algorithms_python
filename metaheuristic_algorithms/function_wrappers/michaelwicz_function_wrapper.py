from metaheuristic_algorithms.function_wrappers.abstract_wrapper import AbstractWrapper
from math import sin, pi

class MichaelwiczFunctionWrapper(AbstractWrapper):

    def maximum_decision_variable_values(self):
        return [4, 4]

    def miminum_decision_variable_values(self):
        return [0, 0]

    def objective_function_value(self, decision_variable_values):
        return sin(decision_variable_values[0]) * (sin(decision_variable_values[0]**2 / pi))**20 - \
               sin(decision_variable_values[1]) * (sin(decision_variable_values[1]**2 / pi))**20

    def initial_decision_variable_value_estimates(self):
        pass