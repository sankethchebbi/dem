import random
from deap import base, creator, tools, algorithms

# Define the problem type (minimization or maximization)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def evaluate_truss(individual):
    """
    Evaluates the truss design based on its weight and a simplistic performance metric.
    Lower values are better.
    """
    length, cross_section = individual
    weight = length * cross_section * 0.1  # Assume density and gravitational constant result in this formula
    performance_metric = (length * cross_section) / 100.0  # Simplified performance metric
    if length * cross_section > 100:  # Arbitrary threshold for structural integrity
        return 9999,  # Return a high cost if the design exceeds the threshold
    return weight + performance_metric,

def generate_individual():
    """
    Generates a random individual representing a truss design.
    Each individual is a list of two parameters: [length, cross_sectional_aea].
    """
    length = random.uniform(1.0, 10.0)  # Length between 1 and 10 meters
    cross_section = random.uniform(0.1, 1.0)  # Cross-sectional area between 0.1 and 1 square meters
    return [length, cross_section]

MAX_DIAMETER = 1.0  # Define maximum diameter
MAX_LENGTH = 10.0  # Define maximum length

def mutate(individual):
    # Randomly mutate one of the parameters (diameter or length)
    mutation_type = random.choice(["diameter", "length"])
    if mutation_type == "diameter":
        individual[1] = random.uniform(0.1, MAX_DIAMETER)  # Corrected index for diameter
    else:
        individual[0] = random.uniform(1.0, MAX_LENGTH)  # Corrected index for length
    return (individual,)  # Ensure the mutated individual is returned

# Create a toolbox
toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, generate_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate_truss)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutate)
toolbox.register("select", tools.selTournament, tournsize=3)

def optimize_truss(population_size=50, generations=20):
    population = toolbox.population(n=population_size)

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    for generation in range(generations):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.7, mutpb=0.2)
        
        # Evaluate offspring
        fitnesses = list(map(toolbox.evaluate, offspring))
        for ind, fit in zip(offspring, fitnesses):
            ind.fitness.values = fit

        population = toolbox.select(population + offspring, k=population_size)

    # Get the best individual
    best_ind = tools.selBest(population, k=1)[0]
    
    return best_ind, best_ind.fitness.values[0]

if __name__ == "__main__":
    best_solution, best_fitness = optimize_truss()
    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
