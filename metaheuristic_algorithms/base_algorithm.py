import random

class BaseAlgorithm(object):

    def __init__(self, function_wrapper, number_of_variables = 1, objective = "maximization"):
        self.function_wrapper = function_wrapper
        self.number_of_variables = number_of_variables

        self.objective = objective

        # if objective == "maximization":
        #     self.objective_method_name = "max"
        # elif objective == "minimization":
        #     self.objective_method_name = "min"

        # if objective == "maximization":
        #     self.objective_comparison_operator = ">"
        # elif objective == "minimization":
        #     self.objective_comparison_operator = "<" 

    def get_decision_variable_value_by_randomization(self, decision_variable_index):
        return self.function_wrapper.miminum_decision_variable_values()[decision_variable_index] + (self.function_wrapper.maximum_decision_variable_values()[decision_variable_index] - self.function_wrapper.miminum_decision_variable_values()[decision_variable_index]) * random.random()