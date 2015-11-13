from metaheuristic_algorithms.base_algorithm import BaseAlgorithm
import copy
from math import sqrt, exp
import random

class FireflyAlgorithm(BaseAlgorithm):

    class Firefly(object):

        def __init__(self, function_wrapper, location_coordinates, light_intensity):
            self.function_wrapper = function_wrapper
            self.location_coordinates = location_coordinates
            self.light_intensity = light_intensity

        def update_light_intensity(self):
            self.light_intensity = self.function_wrapper.objective_function_value(self.location_coordinates)

        # copy.deepcopy deep-clones function_wrapper, which is fine. 
        # But only one function_wrapper instance is needed. 
        # Hence, function_wrapper is simply cloned and the rest of the arguments get deep-cloned. 
        def fuction_wrapper_preserving_clone(self):
            clone_object = copy.copy(self)
            clone_object.location_coordinates = copy.deepcopy(self.location_coordinates)
            clone_object.light_intensity = copy.deepcopy(self.light_intensity)
            return clone_object

    def __init__(self, function_wrapper, number_of_variables = 1, objective = "maximization"):
        super().__init__(function_wrapper, number_of_variables, objective)

    def search(self, number_of_fireflies = 10, maximun_generation = 10, randomization_parameter_alpha = 0.2, absorption_coefficient_gamma = 1.0):

        self.__initialize_fireflies(number_of_fireflies)

        for generation in range(maximun_generation):

            for firefly in self.__fireflies:
                firefly.update_light_intensity()

            self.__move_fireflies(randomization_parameter_alpha, absorption_coefficient_gamma)

        solution_firefly = self.__select_best_firefly_by_light_intensity(self.__fireflies)

        return { "best_decision_variable_values": solution_firefly.location_coordinates, "best_objective_function_value": solution_firefly.light_intensity }

    def __initialize_fireflies(self, number_of_fireflies):
        
        self.__fireflies = []

        for i in range(number_of_fireflies):
            decision_variable_values = [super(FireflyAlgorithm, self).get_decision_variable_value_by_randomization(variable_index) for variable_index in range(self.number_of_variables)]
            firefly = FireflyAlgorithm.Firefly(self.function_wrapper, decision_variable_values, 0)
            self.__fireflies.append(firefly)

    def __select_best_firefly_by_light_intensity(self, fireflies):

        if self.objective == "maximization":
            best_firefly = max(fireflies, key = lambda firefly : firefly.light_intensity)
        elif self.objective == "minimization":
            best_firefly = min(fireflies, key = lambda firefly : firefly.light_intensity)

        return best_firefly

    def __move_fireflies(self, randomization_parameter_alpha, absorption_coefficient_gamma):
        
        attractiveness_beta_at_distance_0 = 1

        fireflies_copy = [firefly.fuction_wrapper_preserving_clone() for firefly in self.__fireflies]

        fireflies = self.__fireflies

        for firefly_i in self.__fireflies:

            self.__remove_matching_element_from_fireflies_copy(fireflies_copy, firefly_i)

            for firefly_j in fireflies_copy:

                if firefly_i.light_intensity < firefly_j.light_intensity:

                    distance_of_two_fireflies = self.__distance_of_two_fireflies(firefly_i, firefly_j)

                    attractiveness_beta = attractiveness_beta_at_distance_0 * exp(-absorption_coefficient_gamma * distance_of_two_fireflies**2)

                    for variable_index in range(self.number_of_variables):
                        new_location_coordinate = firefly_i.location_coordinates[variable_index] * (1 - attractiveness_beta) \
                                                  + firefly_j.location_coordinates[variable_index] * attractiveness_beta \
                                                  + randomization_parameter_alpha * (random.random() - 0.5)                
                        new_location_coordinate = self.__constrain_within_range(new_location_coordinate, variable_index)

                        firefly_i.location_coordinates[variable_index] = new_location_coordinate

    def __remove_matching_element_from_fireflies_copy(self, fireflies_copy, firefly):
        matching_fireflies_copy_element = next((fireflies_copy_element for fireflies_copy_element in fireflies_copy if fireflies_copy_element.light_intensity == firefly.light_intensity), None)
        fireflies_copy.remove(matching_fireflies_copy_element)                    

    def __constrain_within_range(self, location_coordinate, variable_index):
        if location_coordinate < self.function_wrapper.minimum_decision_variable_values()[variable_index]:
            return self.function_wrapper.minimum_decision_variable_values()[variable_index]
        elif location_coordinate > self.function_wrapper.maximum_decision_variable_values()[variable_index]:
            return self.function_wrapper.maximum_decision_variable_values()[variable_index]
        else:
            return location_coordinate

    def __distance_of_two_fireflies(self, firefly_1, firefly_2):

        sum_of_squares_of_distance = 0

        for variable_index in range(self.number_of_variables):
            square_of_distance = (firefly_1.location_coordinates[variable_index] - firefly_2.location_coordinates[variable_index])**2
            sum_of_squares_of_distance += square_of_distance

        return sqrt(sum_of_squares_of_distance)



