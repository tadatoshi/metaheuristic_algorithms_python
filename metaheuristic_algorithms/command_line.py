import argparse

def main():

    '''
    Based on https://docs.python.org/3.5/library/argparse.html#sub-commands

    Example:
    $ metaheuristic_algorithms_python --objective_function 'rosenbrook_function' --number_of_variables 2 --objective 'minimization' harmony_search --maximum_attempt 25000 --pitch_adjusting_range 100 --harmony_search_size 20 --harmony_memory_acceping_rate 0.95 --pitch_adjusting_rate 0.7
    '''

    parser = argparse.ArgumentParser(prog='Executes a specified metaheuristic algorithm')

    parser.add_argument('--objective_function', nargs='?', required=True, choices=['easom_function', 'michaelwicz_function', 'nonsmooth_multipeak_function', 'rosenbrook_function'])
    parser.add_argument('--number_of_variables', nargs='?', type=int, required=True)
    parser.add_argument('--objective', nargs='?', required=True, choices=['maximization', 'minimization'])    

    subparsers = parser.add_subparsers(title='algorithm_name')

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

    # Debug:
    print("args=", args)

def execute_firefly_algorithm(args):
    # Debug:
    print("args=", args)

def execute_harmony_search(args):
    # Debug:
    print("args=", args)

def execute_simplified_particle_swarm_optimization(args):
    # Debug:
    print("args=", args)

def execute_simulated_annealing(args):
    # Debug:
    print("args=", args)        

if __name__ == "__main__":
    main() 