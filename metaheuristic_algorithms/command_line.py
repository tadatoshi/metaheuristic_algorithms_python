import argparse

def main():

    '''
    Based on https://docs.python.org/3.5/library/argparse.html#sub-commands

    Examples
    -----------

    Firefly Algorithm:
    $ metaheuristic_algorithms_python --objective_function 'nonsmooth_multipeak_function' --number_of_variables 2 --objective 'maximization' firefly_algorithm --number_of_fireflies 10 --maximun_generation 10 --randomization_parameter_alpha 0.2 --absorption_coefficient_gamma 1.0

    Harmony Search:
    $ metaheuristic_algorithms_python --objective_function 'rosenbrook_function' --number_of_variables 2 --objective 'minimization' harmony_search --maximum_attempt 25000 --pitch_adjusting_range 100 --harmony_search_size 20 --harmony_memory_acceping_rate 0.95 --pitch_adjusting_rate 0.7

    Simplified Particle Swarm Optimization:
    $ metaheuristic_algorithms_python --objective_function 'michaelwicz_function' --number_of_variables 2 --objective 'minimization' simplified_particle_swarm_optimization --number_of_particiles 20 --number_of_iterations 15 --social_coefficient 0.5 --random_variable_coefficient 0.2

    Simulated Annealing:
    $ metaheuristic_algorithms_python --objective_function 'rosenbrook_function' --number_of_variables 2 --objective 'minimization' simulated_annealing --temperature 1.0 --minimal_temperature 1e-10 --maximum_number_of_rejections 2500 --maximum_number_of_runs 500 --maximum_number_of_acceptances 15 --bolzmann_constant 1 --cooling_factor 0.95 --energy_norm 1e-8 --standard_diviation_for_estimation 1 --ratio_of_energy_delta_over_evaluation_delta 1
    '''

    parser = argparse.ArgumentParser(prog='Executes a specified metaheuristic algorithm')

    parser.add_argument('--objective_function', nargs='?', required=True, choices=['easom_function', 'michaelwicz_function', 'nonsmooth_multipeak_function', 'rosenbrook_function'])
    parser.add_argument('--number_of_variables', nargs='?', type=int, required=True)
    parser.add_argument('--objective', nargs='?', required=True, choices=['maximization', 'minimization'])    

    # "dest": the name of the variable that holds the name of subparser.
    subparsers = parser.add_subparsers(title='algorithm_name', dest='algorithm_name')

    parser_firefly_algorithm = subparsers.add_parser('firefly_algorithm')
    parser_firefly_algorithm.add_argument('--number_of_fireflies', nargs='?', type=int, required=True)
    parser_firefly_algorithm.add_argument('--maximun_generation', nargs='?', type=int, required=True)
    parser_firefly_algorithm.add_argument('--randomization_parameter_alpha', nargs='?', type=float, required=True)
    parser_firefly_algorithm.add_argument('--absorption_coefficient_gamma', nargs='?', type=float, required=True)
    # Note: Calls execute_firefly_algorithm function with the arguments:
    parser_firefly_algorithm.set_defaults(func=execute_firefly_algorithm)

    parser_harmony_search = subparsers.add_parser('harmony_search')
    parser_harmony_search.add_argument('--maximum_attempt', nargs='?', type=int, required=True)
    parser_harmony_search.add_argument('--pitch_adjusting_range', nargs='?', type=int, required=True)
    parser_harmony_search.add_argument('--harmony_search_size', nargs='?', type=int, required=True)
    parser_harmony_search.add_argument('--harmony_memory_acceping_rate', nargs='?', type=float, required=True)
    parser_harmony_search.add_argument('--pitch_adjusting_rate', nargs='?', type=float, required=True)
    parser_harmony_search.set_defaults(func=execute_harmony_search)

    parser_simplified_particle_swarm_optimization = subparsers.add_parser('simplified_particle_swarm_optimization')
    parser_simplified_particle_swarm_optimization.add_argument('--number_of_particiles', nargs='?', type=int, required=True)
    parser_simplified_particle_swarm_optimization.add_argument('--number_of_iterations', nargs='?', type=int, required=True)
    parser_simplified_particle_swarm_optimization.add_argument('--social_coefficient', nargs='?', type=float, required=True)
    parser_simplified_particle_swarm_optimization.add_argument('--random_variable_coefficient', nargs='?', type=float, required=True)
    parser_simplified_particle_swarm_optimization.set_defaults(func=execute_simplified_particle_swarm_optimization)

    parser_simulated_annealing = subparsers.add_parser('simulated_annealing')
    parser_simulated_annealing.add_argument('--temperature', nargs='?', type=float, required=True)
    parser_simulated_annealing.add_argument('--minimal_temperature', nargs='?', type=float, required=True)
    parser_simulated_annealing.add_argument('--maximum_number_of_rejections', nargs='?', type=int, required=True)
    parser_simulated_annealing.add_argument('--maximum_number_of_runs', nargs='?', type=int, required=True)
    parser_simulated_annealing.add_argument('--maximum_number_of_acceptances', nargs='?', type=int, required=True)
    parser_simulated_annealing.add_argument('--bolzmann_constant', nargs='?', type=float, required=True)
    parser_simulated_annealing.add_argument('--cooling_factor', nargs='?', type=float, required=True)
    parser_simulated_annealing.add_argument('--energy_norm', nargs='?', type=float, required=True)
    parser_simulated_annealing.add_argument('--standard_diviation_for_estimation', nargs='?', type=float, required=True)
    parser_simulated_annealing.add_argument('--ratio_of_energy_delta_over_evaluation_delta', nargs='?', type=float, required=True)
    parser_simulated_annealing.set_defaults(func=execute_simulated_annealing)

    args = parser.parse_args()
    # Calls the function specified in "set_defaults" method:
    args.func(args)

def execute_firefly_algorithm(args):
    objective_function = instantiate_objective_function(args.objective_function)

    from metaheuristic_algorithms.firefly_algorithm import FireflyAlgorithm
    firefly_algorithm = FireflyAlgorithm(objective_function, args.number_of_variables, args.objective)

    result = firefly_algorithm.search(number_of_fireflies = args.number_of_fireflies, maximun_generation = args.maximun_generation, 
                                      randomization_parameter_alpha = args.randomization_parameter_alpha, absorption_coefficient_gamma = args.absorption_coefficient_gamma)

    print('best_decision_variable_values=', result["best_decision_variable_values"])
    print('best_objective_function_value=', result["best_objective_function_value"])

def execute_harmony_search(args):
    objective_function = instantiate_objective_function(args.objective_function)

    from metaheuristic_algorithms.harmony_search import HarmonySearch
    harmony_search = HarmonySearch(objective_function, args.number_of_variables, args.objective)

    result = harmony_search.search(maximum_attempt = args.maximum_attempt, pitch_adjusting_range = args.pitch_adjusting_range, 
                                   harmony_search_size = args.harmony_search_size, harmony_memory_acceping_rate = args.harmony_memory_acceping_rate, 
                                   pitch_adjusting_rate = args.pitch_adjusting_rate)

    print('best_decision_variable_values=', result["best_decision_variable_values"])
    print('best_objective_function_value=', result["best_objective_function_value"])

def execute_simplified_particle_swarm_optimization(args):
    objective_function = instantiate_objective_function(args.objective_function)

    from metaheuristic_algorithms.simplified_particle_swarm_optimization import SimplifiedParticleSwarmOptimization
    simplified_particle_swarm_optimization = SimplifiedParticleSwarmOptimization(objective_function, args.number_of_variables, args.objective)

    result = simplified_particle_swarm_optimization.search(number_of_particiles = args.number_of_particiles, number_of_iterations = args.number_of_iterations, 
                                                           social_coefficient = args.social_coefficient, random_variable_coefficient = args.random_variable_coefficient)

    print('best_decision_variable_values=', result["best_decision_variable_values"])
    print('best_objective_function_value=', result["best_objective_function_value"])

def execute_simulated_annealing(args):
    objective_function = instantiate_objective_function(args.objective_function)

    from metaheuristic_algorithms.simulated_annealing import SimulatedAnnealing
    simulated_annealing = SimulatedAnnealing(objective_function, args.number_of_variables, args.objective)

    result = simulated_annealing.search(args.temperature, args.minimal_temperature, 
                                        args.bolzmann_constant, args.energy_norm, 
                                        maximum_number_of_rejections = args.maximum_number_of_rejections, 
                                        maximum_number_of_runs = args.maximum_number_of_runs, 
                                        maximum_number_of_acceptances = args.maximum_number_of_acceptances, 
                                        cooling_factor = args.cooling_factor, 
                                        standard_diviation_for_estimation = args.standard_diviation_for_estimation, 
                                        ratio_of_energy_delta_over_evaluation_delta = args.ratio_of_energy_delta_over_evaluation_delta)

    print('best_decision_variable_values=', result["best_decision_variable_values"])
    print('best_objective_function_value=', result["best_objective_function_value"])

def instantiate_objective_function(objective_function_name):
    if objective_function_name == 'easom_function':
        from metaheuristic_algorithms.function_wrappers.easom_function_wrapper import EasomFunctionWrapper
        return EasomFunctionWrapper()
    elif objective_function_name == 'michaelwicz_function':
        from metaheuristic_algorithms.function_wrappers.michaelwicz_function_wrapper import MichaelwiczFunctionWrapper
        return MichaelwiczFunctionWrapper()
    elif objective_function_name == 'nonsmooth_multipeak_function':
        from metaheuristic_algorithms.function_wrappers.nonsmooth_multipeak_function_wrapper import NonsmoothMultipeakFunctionWrapper
        return NonsmoothMultipeakFunctionWrapper()
    elif objective_function_name == 'rosenbrook_function':
        from metaheuristic_algorithms.function_wrappers.rosenbrook_function_wrapper import RosenbrookFunctionWrapper
        return RosenbrookFunctionWrapper()
    else:
        return None

if __name__ == "__main__":
    main() 