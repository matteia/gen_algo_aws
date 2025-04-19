import random


### self-replicate top entity
def lonely_procreate(world, POP_SIZE):
    ### world is ordered before being input into function
    ### select top entity for return
    top_entt = world[0]
    
    
    ### return top entt (plain & simple)
    return [top_entt]


### winner takes all - only the top entity gets to choose a mate from the tope 10 %
def monopoly_elite_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    ### world is ordered before being input into function
    ### select top entity
    top_entt = world[0]
    
    ### choose the other parent
    ### from the top 10 %
    other_parent_id = random.choice([x for x in range(1, int(current_pop*0.1))])
    other_parent = world[other_parent_id]
    
    ### get length of entitiy
    llen = len(top_entt)
    
    ### select a point to slice
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = top_entt[:random_point]
    tail_1 = top_entt[random_point:]
    ## from entt_2
    head_2 = other_parent[:random_point]
    tail_2 = other_parent[random_point:]
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    
    return child_1, child_2


### winner takes all - only the top entity gets to choose a mate from the entire population
def monopoly_all_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    ### world is ordered before being input into function
    ### select top entity
    top_entt = world[0]
    
    ### choose the other parent
    ### from the top 10 %
    other_parent_id = random.choice([x for x in range(1, int(current_pop))])
    other_parent = world[other_parent_id]
    
    ### get length of entitiy
    llen = len(top_entt)
    
    ### select a point to slice
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = top_entt[:random_point]
    tail_1 = top_entt[random_point:]
    ## from entt_2
    head_2 = other_parent[:random_point]
    tail_2 = other_parent[random_point:]
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    
    return child_1, child_2



### the top few mix amongst themselves
def oligopoly_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    ### get number of elites
    elites_count = int(current_pop*0.1)
    
    parents_idx = random.choices(population=[x for x in range(elites_count)], weights=[POP_SIZE/(1*x+1) for x in range(elites_count)], k=2)
    parent_1_idx = parents_idx[0]
    parent_2_idx = parents_idx[1]
    
    parent_1 = world[parent_1_idx]
    parent_2 = world[parent_2_idx]
    
    ## get lenght(s) of given entities
    llen = len(parent_1)
    ## get a random point
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = parent_1[:random_point]
    tail_1 = parent_1[random_point:]
    ## from entt_2
    head_2 = parent_2[:random_point]
    tail_2 = parent_2[random_point:]
    
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    return child_1, child_2



### Favouring Entities with high summed utility values
### POP_SIZE divided by ...
### 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ...
def fav_high_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    ### get parent ids
    parents_idx = random.choices(population=[x for x in range(current_pop)], weights=[POP_SIZE/(2*x+1) for x in range(current_pop)], k=2)
    parent_1_idx = parents_idx[0]
    parent_2_idx = parents_idx[1]
    
    ### get parents
    parent_1 = world[parent_1_idx]
    parent_2 = world[parent_2_idx]
    
    ## get lenght(s) of given entities
    llen = len(parent_1)
    ## get a random point
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = parent_1[:random_point]
    tail_1 = parent_1[random_point:]
    ## from entt_2
    head_2 = parent_2[:random_point]
    tail_2 = parent_2[random_point:]
    
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    return child_1, child_2
    
    
    
### Proportional
def proportional_procreate(world, POP_SIZE, entts_dict=None):
    ### get current_pop
    current_pop = len(world)
    
    ### create list of summed utils allowing repetition
    all_summed_utils = []
    for kkey in entts_dict.keys():
        for _ in range(len(entts_dict[kkey])):
            all_summed_utils.append(kkey)
    
    ### get parent ids
    if sum(all_summed_utils) == 0:
        all_summed_utils=None
    
    parents_idx = random.choices(population=[x for x in range(current_pop)], weights=all_summed_utils, k=2)
    parent_1_idx = parents_idx[0]
    parent_2_idx = parents_idx[1]
    
    ### get parents
    parent_1 = world[parent_1_idx]
    parent_2 = world[parent_2_idx]
    
    ## get lenght(s) of given entities
    llen = len(parent_1)
    ## get a random point
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = parent_1[:random_point]
    tail_1 = parent_1[random_point:]
    ## from entt_2
    head_2 = parent_2[:random_point]
    tail_2 = parent_2[random_point:]
    
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    return child_1, child_2



### Less Favouring Top
### Favouring Entities with high summed utility values, but a bit less
### POP_SIZE divided by ...
### 1, 2, 3, 4, 5, 6, 7, ....
def less_favour_high_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    ### get parent ids
    parents_idx = random.choices(population=[x for x in range(current_pop)], weights=[POP_SIZE/(1*x+1) for x in range(current_pop)], k=2)
    parent_1_idx = parents_idx[0]
    parent_2_idx = parents_idx[1]
    
    ### get parents
    parent_1 = world[parent_1_idx]
    parent_2 = world[parent_2_idx]
    
    ## get lenght(s) of given entities
    llen = len(parent_1)
    ## get a random point
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = parent_1[:random_point]
    tail_1 = parent_1[random_point:]
    ## from entt_2
    head_2 = parent_2[:random_point]
    tail_2 = parent_2[random_point:]
    
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    return child_1, child_2




### Opposites Attract
def opposites_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    world_input = world.copy()
    
    ### choose entity for dissimilarity calculation
    parent_1_id = random.choice([x for x in range(1, int(current_pop))])
    ### get parent_1
    parent_1 = world_input[parent_1_id]
    world_input.remove(parent_1)
    
    comparison_dict = {}
    
    for entt in world_input:
        
        difference = sum([abs(x-y) for x, y in zip(parent_1, entt)])
        
        # entts_dict[fit_cal(entt)] = entt
        if difference in comparison_dict:
            comparison_dict[difference].append(entt)
        else:
            comparison_dict[difference] = [entt]
    
    ### get max diff
    max_diff = max(list(comparison_dict.keys()))
    
    ### get entity with max difference
    parent_2 = comparison_dict[max_diff][0]
    
    ## get lenght(s) of given entities
    llen = len(parent_1)
    ## get a random point
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = parent_1[:random_point]
    tail_1 = parent_1[random_point:]
    ## from entt_2
    head_2 = parent_2[:random_point]
    tail_2 = parent_2[random_point:]
    
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    return child_1, child_2




### Birds of Feather

def birds_of_feather_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    world_input = world.copy()
    
    ### choose entity for dissimilarity calculation
    parent_1_id = random.choice([x for x in range(1, int(current_pop))])
    ### get parent_1
    parent_1 = world_input[parent_1_id]
    world_input.remove(parent_1)
    
    comparison_dict = {}
    
    for entt in world_input:
        
        difference = sum([abs(x-y) for x, y in zip(parent_1, entt)])
        
                
        # entts_dict[fit_cal(entt)] = entt
        if difference in comparison_dict:
            comparison_dict[difference].append(entt)
        else:
            comparison_dict[difference] = [entt]
    
    ### difference of 0 is to be avoided (still)
    # if 0 in list(comparison_dict.keys()):
    #     del comparison_dict[0]
    
    comparison_dict_keys = list(comparison_dict.keys())
    comparison_dict_keys = sorted(comparison_dict_keys)
    
    ### get min diff that is not 0
    if len(comparison_dict_keys) == 1:
        min_diff = comparison_dict_keys[0]
    elif len(comparison_dict_keys) >=2:
        min_diff = comparison_dict_keys[1]
    else:
        pass
    
    ### get min diff that is not 0
    # min_diff = min(list(comparison_dict.keys()))
    
    ### get entity with min difference
    # random.choice([x for x in range(1, int(current_pop))])
    # parent_2 = comparison_dict[min_diff][0]
    parent_2 = comparison_dict[min_diff][random.choice([x for x in range(0, len(comparison_dict[min_diff]))])]
    
    ## get lenght(s) of given entities
    llen = len(parent_1)
    ## get a random point
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = parent_1[:random_point]
    tail_1 = parent_1[random_point:]
    ## from entt_2
    head_2 = parent_2[:random_point]
    tail_2 = parent_2[random_point:]
    
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    return child_1, child_2




### Pure Chance - Random Selection

def random_selection_procreate(world, POP_SIZE):
    ### get current_pop
    current_pop = len(world)
    
    ### get parent ids
    parents_idx = random.choices(population=[x for x in range(current_pop)], k=2)
    parent_1_idx = parents_idx[0]
    parent_2_idx = parents_idx[1]
    
    ### get parents
    parent_1 = world[parent_1_idx]
    parent_2 = world[parent_2_idx]
    
    ## get lenght(s) of given entities
    llen = len(parent_1)
    ## get a random point
    random_point = random.randint(1, llen-1)
    
    ## divide entities into two pairs of head & tail
    ## from entt_1
    head_1 = parent_1[:random_point]
    tail_1 = parent_1[random_point:]
    ## from entt_2
    head_2 = parent_2[:random_point]
    tail_2 = parent_2[random_point:]
    
    
    ## Make children
    child_1 = head_1
    child_2 = head_2
    child_1.extend(tail_2)
    child_2.extend(tail_1)
    
    return child_1, child_2