from itertools import compress
import random

### returns random entity of given length
def random_gene_gen(llen):
    random_genes = [random.randint(0, 1) for _ in range(llen)]
    return random_genes



### calculates the fitness of an entity
def fit_cal(entt, values_list):
    possible_values = values_list[:len(entt)]
    selected_vals = list(compress(possible_values, entt))
    fitness = sum(selected_vals)
    return fitness


### calculates the sum of constraints of an entity
def cstrnt_cal(entt, cstrnt_list):
    possible_cstrnts = cstrnt_list[:len(entt)]
    selected_cstrnts = list(compress(possible_cstrnts, entt))
    cstrnt = sum(selected_cstrnts)
    return cstrnt


### selects and strikes out entities from a given list of entities
### function to discard entities that exceed the constraint limit
### do I want to remove ALL entities that do not FIT, or do I want to let a small portion of them stay ?
### -> think about this later
def selector(entts, MAX_CSTRNT, cstrnt_list):
    selected_entts = []
    for entt in entts:
        # if cstrnt_cal(entt) < MAX_CSTRNT:
        if cstrnt_cal(entt, cstrnt_list) <= MAX_CSTRNT:
            selected_entts.append(entt)
        else:
            pass
        
    return selected_entts




### mutates all entities
### function for mutation
def mutate(entt, mut_rate):
    result_entt = []
    for i in range(len(entt)):
        
        mutation = random.choices(population=[True, False], weights=[mut_rate, 1-mut_rate], k=1)[0]
        # print(i, mutation)
        if mutation is True:
            result_entt.append((1 - entt[i]))
            # result_entt.append(9)
        else:
            result_entt.append(entt[i])
            # result_entt.append(9)
        
    return result_entt