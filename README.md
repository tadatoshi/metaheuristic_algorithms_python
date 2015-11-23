# MetaheuristicAlgorithmsPython

Various metaheuristic algorithms implemented in Python.

This is equivalent to MetaheuristicAlgorithms written in Ruby (https://github.com/tadatoshi/metaheuristic_algorithms). The reason why I wrote it in Python is that I would like to potentially utilize Python's Scientific Computing libraries. 

As a programming lanugage, I prefer Ruby, because it's fully Object-Oriented programming language (also Dynamic language) and because it has a community with the culture of writing unit tests. Both of these characteristics lead to cleaner, well structured, easy-to-maintain codes. Also it's easier to understand other people's codes written in such a way. 

But scientists use Python for their activities such as Scientific Computing, Optimization, Data Science, Data Mining, Machine Learning etc. In other words, Python has a community of scientists.  

## Installation

Use ``pip3``:

```
pip3 install metaheuristic_algorithms_python
```

## Supported Platforms

* Python 3.5. 

It's not tested on Python 2.6 or 2.7 yet. 

## Available Algorithms

* Harmony Search

* Simplified Particle Swarm Optimization

* Simulated Annealing

* Firefly Algorithm

Algorithms under construction:

* Genetic Algorithm

## Provided Objective Functions

Function Wrappers (See "Usage" section below) for the following Objective Functions are available in metaheuristic_algorithms.function_wrappers package

(You can write your own Fuction Wrapper for your Objective Function. See "Usage" section below.)

* Nonsmooth Multipeak Function

* Easom Function

* Rosenbrook Function

* Michaelwicz Function

## Usage

### Programming

Step 1. Create a Function Wrapper for your objective function by extending MetaheuristicAlgorithms::FunctionWrappers::AbstractWrapper

   Example: Rosenbrook's Function: f(x,y) = (1 - x)^2 + 100(y - x^2)^2

```python
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
```

Step 2. Instantiate the created Function Wrapper and pass it as the first argument of the Algorithm instantiation. 
        Also specify the number of variables and objective ("maximization" or "minimization")
        Then call the search method passing the algorithm specific parameters. 

   Example: Harmony Search for the glocal minimum value for Rosenbrook's Function

```python
    from metaheuristic_algorithms.harmony_search import HarmonySearch
    from metaheuristic_algorithms.function_wrappers.rosenbrook_function_wrapper import RosenbrookFunctionWrapper

    rosenbrook_function_wrapper = RosenbrookFunctionWrapper()

    number_of_variables = 2
    objective = "minimization"

    harmony_search = HarmonySearch(rosenbrook_function_wrapper, number_of_variables, objective)

    maximum_attempt = 25000
    pitch_adjusting_range = 100
    harmony_search_size = 20
    harmony_memory_acceping_rate = 0.95
    pitch_adjusting_rate = 0.7

    result = harmony_search.search(maximum_attempt = maximum_attempt, 
                                   pitch_adjusting_range = pitch_adjusting_range, 
                                   harmony_search_size = harmony_search_size, 
                                   harmony_memory_acceping_rate = harmony_memory_acceping_rate, 
                                   pitch_adjusting_rate = pitch_adjusting_rate)

    print(result["best_decision_variable_values"][0]) # x value: Example: 1.0112
    print(result["best_decision_variable_values"][1]) # y value: Example: 0.9988
    print(result["best_objective_function_value"])    # f(x,y) value: Example: 0.0563    
```

### Command line execution

Examples: 

* Firefly Algorithm:
```
    $ metaheuristic_algorithms_python --objective_function 'nonsmooth_multipeak_function' --number_of_variables 2 --objective 'maximization' firefly_algorithm --number_of_fireflies 10 --maximun_generation 10 --randomization_parameter_alpha 0.2 --absorption_coefficient_gamma 1.0
```    

* Harmony Search:
```
    $ metaheuristic_algorithms_python --objective_function 'rosenbrook_function' --number_of_variables 2 --objective 'minimization' harmony_search --maximum_attempt 25000 --pitch_adjusting_range 100 --harmony_search_size 20 --harmony_memory_acceping_rate 0.95 --pitch_adjusting_rate 0.7
```    

* Simplified Particle Swarm Optimization:
```
    $ metaheuristic_algorithms_python --objective_function 'michaelwicz_function' --number_of_variables 2 --objective 'minimization' simplified_particle_swarm_optimization --number_of_particiles 20 --number_of_iterations 15 --social_coefficient 0.5 --random_variable_coefficient 0.2
```    

* Simulated Annealing:
```
    $ metaheuristic_algorithms_python --objective_function 'rosenbrook_function' --number_of_variables 2 --objective 'minimization' simulated_annealing --temperature 1.0 --minimal_temperature 1e-10 --maximum_number_of_rejections 2500 --maximum_number_of_runs 500 --maximum_number_of_acceptances 15 --bolzmann_constant 1 --cooling_factor 0.95 --energy_norm 1e-8 --standard_diviation_for_estimation 1 --ratio_of_energy_delta_over_evaluation_delta 1
```

## Development



## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/tadatoshi/metaheuristic_algorithms_python. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](contributor-covenant.org) code of conduct.


## License

The project is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## References

X.-S. Yang, Engineering Optimization : An Introduction with Metaheuristic Applications. Hoboken, New Jersey, United States: John Wiley & Sons, 2010.

