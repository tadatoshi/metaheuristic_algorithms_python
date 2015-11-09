from metaheuristic_algorithms.function_wrappers.abstract_wrapper import AbstractWrapper

class RosenbrookFunctionWrapper(AbstractWrapper):

    def maximum_decision_variable_values(self):
        return [5, 5]

    def minimum_decision_variable_values(self):
        return [-5, -5]

    def objective_function_value(self, decision_variable_values):
        return (1 - decision_variable_values[0])**2 + 100 * (decision_variable_values[1] - decision_variable_values[0]**2)**2

    def initial_decision_variable_value_estimates(self):
        return [2, 2]