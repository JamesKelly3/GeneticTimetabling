import random
from Representation.University import University
from Genetic_Algorithm.Selection import select
from Genetic_Algorithm.Recombination import crossover
from Genetic_Algorithm.Mutation import mutate
from Genetic_Algorithm.Fitness import eval_fitness
from Genetic_Algorithm.Selection import elitism


def ga(university: University):
    max_gens = 100
    pop_size = 50
    mutation_prob = 0.3
    crossover_prob = 0.8
    gen_count = 0
    population = generate_initial_population(university, pop_size)
    fitness = [eval_fitness(indiv) for indiv in population]
    while gen_count < max_gens and not stopping_criteria(fitness):
        elites = elitism(fitness, population)
        parents = select(pop_size - len(elites), fitness, population)
        offspring = crossover(parents, crossover_prob)
        offspring = mutate(offspring, mutation_prob)
        population = elites + offspring
        fitness = [eval_fitness(indiv) for indiv in population]
        gen_count += 1


def generate_initial_population(university: University, pop_size: int):
    population = []
    for i in range(pop_size):
        for mod in university.courses:
            room_no = random.randint(0, len(university.rooms))
            time_slot = random.randint(0, university.num_time_slots)
            population.append((mod, room_no, time_slot))
    return population


def stopping_criteria(fitness):
    return False
