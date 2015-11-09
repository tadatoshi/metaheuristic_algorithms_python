from metaheuristic_algorithms.base_algorithm import BaseAlgorithm
import random

class HarmonySearch(BaseAlgorithm):

    def __init__(self, function_wrapper, number_of_variables = 1, objective = "maximization"):
        super().__init__(function_wrapper, number_of_variables, objective)

    def search(self, maximum_attempt = 2500, pitch_adjusting_range = 100, 
               harmony_search_size = 20, harmony_memory_acceping_rate = 0.95, 
               pitch_adjusting_rate = 0.7):
        
        self.__initialize_harmony_memory(harmony_search_size)

        for count in range(maximum_attempt):

            decision_variable_values = [self.__get_decision_variable(variable_index, pitch_adjusting_range, harmony_search_size, harmony_memory_acceping_rate, pitch_adjusting_rate) for variable_index in range(self.number_of_variables)]

            best_function_value = self.function_wrapper.objective_function_value(decision_variable_values) 

            sampled_best_function_value = super(HarmonySearch, self).best_function_value_from_list(self.__best_function_value_harmony_memory)

            if self.__compare_best_function_value(best_function_value, sampled_best_function_value):

                # If harmony_memory_random_index is not set in the if statement above, it means a new search and use the index for the max best function value:
                # TODO: As written in __get_decision_variable method below, Find the way not to use member field for harmony_memory_random_index when using list comprehension using __get_decision_variable method.
                if self.__harmony_memory_random_index is None: 
                    self.__harmony_memory_random_index = self.__best_function_value_harmony_memory.index(sampled_best_function_value)

                self.__harmony_memory[self.__harmony_memory_random_index] = decision_variable_values
                self.__best_function_value_harmony_memory[self.__harmony_memory_random_index] = best_function_value

        objective_function_value = super(HarmonySearch, self).best_function_value_from_list(self.__best_function_value_harmony_memory)
        decision_variable_values = self.__harmony_memory[self.__best_function_value_harmony_memory.index(objective_function_value)]

        return { "best_decision_variable_values": decision_variable_values, "best_objective_function_value": objective_function_value }

    def __initialize_harmony_memory(self, harmony_search_size):

        self.__harmony_memory = []
        self.__best_function_value_harmony_memory = []

        for i in range(harmony_search_size):
            decision_variable_values = [super(HarmonySearch, self).get_decision_variable_value_by_randomization(variable_index) for variable_index in range(self.number_of_variables)]

            self.__harmony_memory.append(decision_variable_values)
            self.__best_function_value_harmony_memory.append(self.function_wrapper.objective_function_value(decision_variable_values))

        print("min(self.__best_function_value_harmony_memory)=", min(self.__best_function_value_harmony_memory))

    def __get_decision_variable(self, variable_index, pitch_adjusting_range, harmony_search_size, harmony_memory_acceping_rate, pitch_adjusting_rate):
                  
        if random.random() > harmony_memory_acceping_rate:
            decision_variable_value = super(HarmonySearch, self).get_decision_variable_value_by_randomization(variable_index)
        else:
            # Since the list index starts with 0 unlike MatLab, 1 is not added as in the code example in MatLab:
            # TODO: Find the way not to use member field for harmony_memory_random_index when using list comprehension using this method.
            self.__harmony_memory_random_index = int((harmony_search_size * random.random()))
            decision_variable_value = self.__harmony_memory[self.__harmony_memory_random_index][variable_index]
            
            if random.random() < pitch_adjusting_rate:
              pitch_adjusting = (self.function_wrapper.maximum_decision_variable_values()[variable_index] - self.function_wrapper.minimum_decision_variable_values()[variable_index]) / pitch_adjusting_range
              decision_variable_value = decision_variable_value + pitch_adjusting * (random.random() -0.5)

        return decision_variable_value

    # best_function_value > sampled_best_function_value or best_function_value < sampled_best_function_value
    def __compare_best_function_value(self, best_function_value, sampled_best_function_value):

        if self.objective == "maximization":
            comparison_result = best_function_value > sampled_best_function_value
        elif self.objective == "minimization":
            comparison_result = best_function_value < sampled_best_function_value

        # Note: getattr seems to work only on object attributes not method:
        # comparison_result = getattr(best_function_value, self.objective_comparison_operator)(sampled_best_function_value)            

        return comparison_result
