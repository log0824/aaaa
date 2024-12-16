import random

#thuật toán ga


target_password = "hoilamgi"
password_length = len(target_password)
population_size = 100
mutation_rate = 0.01
generations = 1000

def random_individual():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    return ''.join(random.choice(chars) for _ in range(password_length))

def fitness(individual):
    return sum(1 for a, b in zip(individual, target_password) if a == b)

def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probs = [f/total_fitness for f in fitnesses]
    return random.choices(population, probs, k = 2)

def crossover(parent1, parent2):
    split = random.randint(0, password_length - 1)
    return parent1[:split] + parent2[split:]

def mutate(individual):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    individual = list(individual)
    for i in range(password_length):
        if random.random() < mutation_rate:
            individual[i] = random.choice(chars)
    return ''.join(individual)

def genetic_algorithm():
    population = [random_individual() for _ in range(population_size)]

    for gen in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        if max(fitnesses) == password_length:
            best = population[fitnesses.index(max(fitnesses))]
            print(gen )
            print(best)
            return best
        new_population = []
        for _ in range(population_size//2):
            par1, par2 = selection(population, fitnesses)
            child1, child2 = crossover(par1, par2), crossover(par2, par1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        
        population = new_population
        
    return None 

genetic_algorithm()


#thuật toán pso


# Tạo hạt ngẫu nhiên
def random_particle():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    return ''.join(random.choice(chars) for _ in range(password_length))

# Tính độ phù hợp
def fitness(particle):
    return sum(1 for a, b in zip(particle, target_password) if a == b)

# Cập nhật vận tốc
def update_velocity(velocity, particle, pbest, gbest, w=0.5, c1=1.5, c2=1.5):
    new_velocity = []
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    for i in range(password_length):
        if random.random() < w:  # Quán tính
            new_velocity.append(velocity[i])
        elif random.random() < c1:  # Hướng tới pbest
            new_velocity.append(pbest[i])
        elif random.random() < c2:  # Hướng tới gbest
            new_velocity.append(gbest[i])
        else:  # Ngẫu nhiên
            new_velocity.append(random.choice(chars))
    return ''.join(new_velocity)

# PSO
def pso():
    particles = [random_particle() for _ in range(population_size)]
    velocities = [' ' * password_length for _ in range(population_size)]
    pbests = particles[:] #sao chép
    pbest_scores = [fitness(p) for p in particles]
    gbest = pbests[pbest_scores.index(max(pbest_scores))]

    for generation in range(generations):
        for i in range(population_size):
            velocities[i] = update_velocity(velocities[i], particles[i], pbests[i], gbest)
            particles[i] = ''.join(velocities[i])
            score = fitness(particles[i])
            if score > pbest_scores[i]:
                pbests[i] = particles[i]
                pbest_scores[i] = score
            if score > fitness(gbest):
                gbest = particles[i]

        if fitness(gbest) == password_length:
            print(f"Found password '{gbest}' at generation {generation}")
            return gbest

    print("Password not found.")
    return None

# Chạy PSO
pso()
