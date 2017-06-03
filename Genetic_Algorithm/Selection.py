import random


def select(num_to_select: int, fitnesses: list, population: list):
    selected = []
    for i in range(num_to_select):
        x = random.randint(0, len(population) - 1)
        y = random.randint(0, len(population) - 1)
        if fitnesses[x] > fitnesses[y]:
            selected.append(population[x])
        else:
            selected.append(population[y])
    return selected


def elitism(num_to_take: int, fitnesses: list, population: list):
    both = zip(fitnesses, population)
    both = sorted(both, key=lambda x: x[0])
    fit, pop = zip(*both)
    print(fit)
    return pop[:num_to_take]
