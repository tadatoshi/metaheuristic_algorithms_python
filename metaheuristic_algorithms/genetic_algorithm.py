from metaheuristic_algorithms.base_algorithm import BaseAlgorithm
import copy
import random
from math import floor

class GeneticAlgorithm(BaseAlgorithm):

    def __init__(self, function_wrapper, number_of_variables = 1, objective = "maximization"):
        super().__init__(function_wrapper, number_of_variables, objective)

    def search(self, population_size = 20, maximum_number_of_generations = 100, number_of_mutation_sites = 2, crossover_probability = 0.95, mutation_probability = 0.05):

        self.__initialize_population(population_size)

        for maximum_number_of_generations in range(maximum_number_of_generations):

            self.__population_copy = copy.deepcopy(self.__population)

            for individual_index in range(population_size):

                if random.random() < crossover_probability:

                    # Crossover pair:
                    crossover_pair_1_index = self.__generate_random_index(population_size)
                    crossover_pair_2_index = self.__generate_random_index(population_size)     

                    self.__crossover(crossover_pair_1_index, crossover_pair_2_index)

                if random.random() < mutation_probability:

                    mutation_individual_index = self.__generate_random_index(population_size)

                    self.__mutate(mutation_individual_index, number_of_mutation_sites)

        objective_function_value = super(GeneticAlgorithm, self).best_function_value_from_list(self.__population_fitness)
        decision_variable_values = self.__population[self.__population_fitness.index(objective_function_value)]

        return { "best_decision_variable_values": decision_variable_values, "best_objective_function_value": objective_function_value }

    def __initialize_population(self, population_size):
        self.__population = []
        self.__population_fitness = []

        for individual_index in range(population_size):
            decision_variable_values = [super(GeneticAlgorithm, self).get_decision_variable_value_by_randomization(variable_index) for variable_index in range(self.number_of_variables)]

            self.__population.append(decision_variable_values)
            self.__population_fitness.append(self.function_wrapper.objective_function_value(decision_variable_values))

    def __generate_random_index(self, population_size):
        return floor(population_size * random.random())

    def __crossover(self, crossover_pair_1_index, crossover_pair_2_index):

        crossover_pair_1_decimal_values = []
        crossover_pair_2_decimal_values = []

        for variable_index in range(self.number_of_variables):

            crossover_pair_1_decimal_value = self.__population_copy[crossover_pair_1_index][variable_index]
            crossover_pair_2_decimal_value = self.__population_copy[crossover_pair_2_index][variable_index]

            crossover_pair_1_binary_32_string = self.__decimal_to_binary_32_string(crossover_pair_1_decimal_value)
            crossover_pair_2_binary_32_string = self.__decimal_to_binary_32_string(crossover_pair_2_decimal_value)

            crossover_point = self.__pick_random_point_in_32_bit_string

            crossover_pair_1_binary_32_string_after_crossover = crossover_pair_1_binary_32_string[0 : crossover_point] + \
                                                                crossover_pair_2_binary_32_string[crossover_point+1 : 32]
            crossover_pair_2_binary_32_string_after_crossover = crossover_pair_2_binary_32_string[0 : crossover_point] + \
                                                                crossover_pair_1_binary_32_string[crossover_point+1 : 32] 

            crossover_pair_1_decimal_value_after_crossover = self.__binary_32_string_to_decimal(crossover_pair_1_binary_32_string_after_crossover)
            crossover_pair_2_decimal_value_after_crossover = self.__binary_32_string_to_decimal(crossover_pair_2_binary_32_string_after_crossover)

            if self.__in_the_range(crossover_pair_1_decimal_value_after_crossover, variable_index) and \
               self.__in_the_range(crossover_pair_2_decimal_value_after_crossover, variable_index):
              crossover_pair_1_decimal_values.append(crossover_pair_1_decimal_value_after_crossover)
              crossover_pair_2_decimal_values.append(crossover_pair_2_decimal_value_after_crossover)
            else:
              crossover_pair_1_decimal_values.append(crossover_pair_1_decimal_value)
              crossover_pair_2_decimal_values.append(crossover_pair_2_decimal_value)

        new_crossover_pair_1_fitness = self.function_wrapper.objective_function_value(crossover_pair_1_decimal_values)
        new_crossover_pair_2_fitness = self.function_wrapper.objective_function_value(crossover_pair_2_decimal_values)

        if new_crossover_pair_1_fitness > self.__population_fitness[crossover_pair_1_index] and \
           new_crossover_pair_2_fitness > self.__population_fitness[crossover_pair_2_index]:

            self.__population[crossover_pair_1_index] = self.__population_copy[crossover_pair_1_index] = crossover_pair_1_decimal_values 
            self.__population[crossover_pair_2_index] = self.__population_copy[crossover_pair_2_index] = crossover_pair_2_decimal_values 

            self.__population_fitness[crossover_pair_1_index] = new_crossover_pair_1_fitness
            self.__population_fitness[crossover_pair_2_index] = new_crossover_pair_2_fitness

    def __decimal_to_binary_32_string(self, decimal_number):
        # TODO: Must be able to convert float to binary:
        '{0:032b}'.format(int(decimal_number))

    def __binary_32_string_to_decimal(self, binary_32_string):
        # TODO: Must be able to convert binary to float:
        int(binary_32_string,2)

    def __mutate(self, individual_index, number_of_mutation_sites):

        decimal_values = []

        for variable_index in range(number_of_variables):

            decimal_value = self.__population_copy[individual_index][variable_index]
            binary_32_string = self.__decimal_to_binary_32_string(decimal_value)

            mutated_binary_32_string = copy.copy(binary_32_string)

            for i in range(number_of_mutation_sites):
                mutation_site_index = self.__pick_random_point_in_32_bit_string()
                # Flips 1 to 0 or 0 to 1:
                mutated_binary_32_string[mutation_site_index] = str((int(binary_32_string[mutation_site_index], 2) + 1) % 2)

            decimal_value_after_mutation = self.__binary_32_string_to_decimal(mutated_binary_32_string)

            if self.__in_the_range(decimal_value_after_mutation, variable_index):
                decimal_value_after_mutation
            else:
                decimal_value

        new_individual_fitness = self.function_wrapper.objective_function_value(decimal_values)

        if new_individual_fitness > self.__population_fitness[individual_index]:          
           self.__population[individual_index] = self.__population_copy[individual_index] = decimal_values
           self.__population_fitness[individual_index] = new_individual_fitness   

    # 32 bits string with the first bit as sign bit. Hence, the length is 32 - 1:
    def __pick_random_point_in_32_bit_string(self):
        return floor(31 * random.random())

    def __in_the_range(self, decimal_value, variable_index):
        decimal_value >= self.function_wrapper.minimum_decision_variable_values()[variable_index] and decimal_value <= self.function_wrapper.maximum_decision_variable_values()[variable_index]       
