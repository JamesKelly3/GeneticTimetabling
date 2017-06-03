import random
from Representation.Random_Generator import generate_random_uni
from Representation.University import University
from Genetic_Algorithm.Selection import select
from Genetic_Algorithm.Recombination import crossover
from Genetic_Algorithm.Mutation import mutate
from Genetic_Algorithm.Fitness import eval_fitness
from Genetic_Algorithm.Selection import elitism


def ga(university: University):
    max_gens = 100
    pop_size = 50
    num_elite = 5
    mutation_prob = 0.3
    crossover_prob = 0.8
    gen_count = 0
    population = generate_initial_population(university, pop_size)
    fitness = [eval_fitness(indiv, university) for indiv in population]
    while gen_count < max_gens and not stopping_criteria(fitness):
        elites = elitism(num_elite, fitness, population)
        parents = select(pop_size - len(elites), fitness, population)
        print(parents)
        offspring = crossover(parents, crossover_prob)
        offspring = mutate(offspring, mutation_prob)
        population = elites + offspring
        fitness = [eval_fitness(indiv, university) for indiv in population]
        gen_count += 1


def generate_initial_population(university: University, pop_size: int):
    population = []
    for i in range(pop_size):
        indiv = []
        for mod in university.courses:
            room_no = random.randint(0, len(university.rooms)-1)
            time_slot = random.randint(0, university.num_time_slots)
            indiv.append((mod, room_no, time_slot))
        population.append(indiv)
    return population


def stopping_criteria(fitness):
    return False

if __name__ == '__main__':
    medium_uni = generate_random_uni(150, 10, 800, 10)
    ga(medium_uni)
