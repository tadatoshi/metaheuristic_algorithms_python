# import sys
# import getopt
import argparse

# def main(argv):
def main():

    '''
    Example:
    $ metaheuristic_algorithms_python --name 'harmony_search' --objective-function 'rosenbrook_function' --number-of-variables 2 --objective 'minimization' --parameters maximum_attempt=25000 pitch_adjusting_range=100 harmony_search_size=20 harmony_memory_acceping_rate=0.95 pitch_adjusting_rate=0.7
    '''

    parser = argparse.ArgumentParser(prog='Executes a specified metaheuristic algorithm')
    parser.add_argument('--name', nargs='?', required=True, choices=['firefly_algorithm', 'harmony_search', 'simplified_particle_swarm_optimization', 'simulated_annealing'])
    parser.add_argument('--objective-function', nargs='?', required=True, choices=['easom_function', 'michaelwicz_function', 'nonsmooth_multipeak_function', 'rosenbrook_function'])
    parser.add_argument('--number-of-variables', nargs='?', type=int, required=True)
    parser.add_argument('--objective', nargs='?', required=True, choices=['maximization', 'minimization'])
    parser.add_argument('--parameters', nargs='+', required=True)

    args = parser.parse_args()

    # print("args=", args)

    # try:
    #     opts, args = getopt.getopt(argv, "", [""])

    # except getopt.GetOptError:
    #     sys.exit(2)

if __name__ == "__main__":
    # main(sys.argv[1:])
    main() 