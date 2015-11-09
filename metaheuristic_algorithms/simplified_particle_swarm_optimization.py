from metaheuristic_algorithms.base_algorithm import BaseAlgorithm
import random

class SimplifiedParticleSwarmOptimization(BaseAlgorithm):

    def __init__(self, function_wrapper, number_of_variables = 1, objective = "maximization"):
        super().__init__(function_wrapper, number_of_variables, objective)

    def search(self, number_of_particiles = 20, number_of_iterations = 15, social_coefficient = 0.5, random_variable_coefficient = 0.2):

        self.__initialize_particles(number_of_particiles)        

        global_best_position = None
        best_function_value = None

        for iteration in range(number_of_iterations):

            function_values = [self.function_wrapper.objective_function_value(self.__particle_locations[particle_location_index]) for particle_location_index in range(len(self.__particle_locations))]

            best_function_value = super(SimplifiedParticleSwarmOptimization, self).best_function_value_from_list(function_values)
            global_best_position = self.__particle_locations[function_values.index(best_function_value)]

            self.__move_particles(global_best_position, social_coefficient, random_variable_coefficient)

        return { "best_decision_variable_values": global_best_position, "best_objective_function_value": best_function_value } 

    def __initialize_particles(self, number_of_particiles):

        self.__particle_locations = []

        for individual_index in range(number_of_particiles):
            decision_variable_values = [super(SimplifiedParticleSwarmOptimization, self).get_decision_variable_value_by_randomization(variable_index) for variable_index in range(self.number_of_variables)]

            self.__particle_locations.append(decision_variable_values)

    def __move_particles(self, global_best_position, social_coefficient, random_variable_coefficient):

        particle_locations_after_move = []
       
        for particle_location in self.__particle_locations:        

            decision_variable_values = []

            for variable_index in range(self.number_of_variables):

                # The value out-of-range in order to enter while loop
                new_particle_location_coordinate = self.function_wrapper.minimum_decision_variable_values()[variable_index] - 1

                while new_particle_location_coordinate < self.function_wrapper.minimum_decision_variable_values()[variable_index] or new_particle_location_coordinate > self.function_wrapper.maximum_decision_variable_values()[variable_index]:
                    new_particle_location_coordinate = (1 - social_coefficient) * particle_location[variable_index] + social_coefficient * global_best_position[variable_index] + random_variable_coefficient * (random.random() - 0.5)
                
                decision_variable_values.append(new_particle_location_coordinate)

            particle_locations_after_move.append(decision_variable_values)

        self.__particle_locations = particle_locations_after_move