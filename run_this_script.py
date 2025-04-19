import os
import random
import copy
import itertools
import json


from itertools import compress
from itertools import product

from time import time
from time import sleep
from time import strftime
from time import localtime
from tqdm import tqdm

from datetime import date, timedelta, datetime



### Import custom functions
from basic_fxs import random_gene_gen, fit_cal, cstrnt_cal, selector, mutate
from procreate_fxs import lonely_procreate, monopoly_elite_procreate, monopoly_all_procreate, oligopoly_procreate, fav_high_procreate
from procreate_fxs import proportional_procreate, less_favour_high_procreate, opposites_procreate, birds_of_feather_procreate, random_selection_procreate
from generate_values import generate_items, generate_util_vals, generate_cstrnt_vals
from compute_fxs import compute_avg_summed_util, compute_plateau

#### END OF ALL IMPORTS #############

### Create List of Procreate Fxs
proc_fxs = [
    lonely_procreate, monopoly_elite_procreate, monopoly_all_procreate, oligopoly_procreate,
    fav_high_procreate, proportional_procreate, less_favour_high_procreate, opposites_procreate,
    birds_of_feather_procreate, random_selection_procreate
]


### Distribution Products & Combinations
# distri_list = ['normal', 'log_normal', 'uniform', 'expovariate', 'vonmise', 'pareto', 'weibull', 'left_skewed']
distri_list = ['normal', 'lognormal', 'uniform', 'expovariate', 'vonmise', 'pareto', 'weibull', 'leftskewed']

distri_products = list(product(distri_list, repeat=2))

# print(distri_products)

# distri_permutations = []

# for i in range(len(distri_products)):
#     if i % int(len(distri_list)) == 0:
#         pass
#     else:
#         distri_permutations.append(distri_products[i])
#         # print(distri_products[i])
# # print(len(distri_permutations))

### Set distri_part
# distri_part = distri_products[0:1]
# distri_part = distri_products[0:16]
# distri_part = distri_products[16:32]
# distri_part = distri_products[32:48]
distri_part = distri_products[48:64]
# print(distri_part)

### MAX_CSTRNT_PERC_list
MAX_CSTRNT_PERC_list = [x/100 for x in list(range(5, 105, 5))]
# MAX_CSTRNT_PERC_list

# print(len(MAX_CSTRNT_PERC_list))
### 0.05 0.1 0.15 0.20 .....

MAX_CSTRNT_PERC_list = MAX_CSTRNT_PERC_list[:]
# print(MAX_CSTRNT_PERC_list)


### Number of Items
num_items_0 = 10
num_items_1 = 40
num_items_2 = 100

### DEVICE ?
device = 'aws_ec2'

### Set path for jsons to be saved
json_fp_prefix = 'data/general_gen_algo/aws'


# final_result = {1:'123', 2:'ddd'}
# final_result_fp = f'{json_fp_prefix}/adf.json'

### save json
# with open(final_result_fp, 'w') as final_result_json:
#     json.dump(final_result, final_result_json)

### Set hyperparameters

num_items = num_items_1
# print(num_items)

# MAX_CSTRNT_PERC = 0.7
# MAX_CSTRNT = total_cstrnt * MAX_CSTRNT_PERC   ###
# print(f'MAX_CSTRNT: {MAX_CSTRNT}')

# POP_SIZE = 10
# POP_SIZE = 25
# POP_SIZE = 50
# POP_SIZE = 100
# POP_SIZE = 200
# POP_SIZE = 400
# POP_SIZE = 500
POP_SIZE = 1000
# POP_SIZE = 2000

### number of items to choose
NUM_ITEMS = num_items   ### == GENOME_LEN
GENOME_LEN = NUM_ITEMS  ### == NUM_ITEMS

# MUTATION_RATE = 0.01
MUTATION_RATE = 0.03
# MUTATION_RATE = 0.3

CROSSOVER_RATE = 0.7  ### currently not in use


# GENERATIONS = 10
# GENERATIONS = 250
GENERATIONS = 500
# GENERATIONS = 3000

### End of Hyperparameters


### Create VOID Genes

void_gene = [0 for _ in range(NUM_ITEMS)]

# print(len(void_gene))
# print(void_gene)


### Create GENESIS_0
genesis_0 = [copy.deepcopy(void_gene) for _ in range(POP_SIZE)]   ### fixed version
# print(len(genesis_0))

### Copy GENESIS_0 to GENESIS
genesis = copy.deepcopy(genesis_0)
# print(len(genesis))

### Commence Evolution
for d in tqdm(range(len(distri_part))):
# for d in range(len(distri_part[:])):
    # print(distri_part[d][0])
    # print(distri_part[d][1])

    ### generate item names (not crucial)
    items_list_0 = generate_items(num_items)

    ### set distribution for utility values
    util_distri = distri_part[d][0]

    ### set distribution for constraint values
    cstrnt_distri = distri_part[d][1]

    # print(f'util_distri: {util_distri}', end='\n')
    # print(f'cstrnt_distri: {cstrnt_distri}', end='\n')

    ### generate values for util & cstrnt
    values_list_0 = generate_util_vals(NUM_ITEMS, util_distri)
    cstrnt_list_0 = generate_cstrnt_vals(NUM_ITEMS, cstrnt_distri)

    ### total sum of util vals
    total_util = sum(values_list_0)

    ### total sum of cstrnt vals
    total_cstrnt = sum(cstrnt_list_0)

    ### adjust items, util vals, cstrnt vals
    items_list = items_list_0.copy()[:NUM_ITEMS]
    values_list = values_list_0.copy()[:NUM_ITEMS]
    cstrnt_list = cstrnt_list_0.copy()[:NUM_ITEMS]

    all_result_list_head = []
    all_result_list_top_10p = []
    all_result_list_tail = []


    # for i in tqdm(range(len(MAX_CSTRNT_PERC_list))):
    for i in range(len(MAX_CSTRNT_PERC_list)):

        ### MAX_CSTRNT set here instead in Set HyperParameters CELL
        MAX_CSTRNT = MAX_CSTRNT_PERC_list[i] * total_cstrnt

        # print(f'i : {i}', end='\r')
        # print(f'MAX_CSTRNT_PERC: {MAX_CSTRNT_PERC_list[i]}', end='\n')
        # print(f'MAX_CSTRNT: {MAX_CSTRNT}', end='\n')

        ### create result_lists
        result_list_head = []
        result_list_top_10p = []
        result_list_tail = []


        ### Evolve for 5 iterations
        for j in range(5):
            world = []
            world.extend(genesis)

            ### create one_runs
            one_run_head = []
            one_run_tail = []
            one_run_top_10p = []

            for k in range(GENERATIONS):

                ### Rank entities in order of summed utility values
                entts_dict = {}
                for entt in world:
                    summed_util = fit_cal(entt, values_list)
                    if summed_util in entts_dict:
                        entts_dict[summed_util].append(entt)
                    else:
                        entts_dict[summed_util] = [entt]

                ### sort entts_dict by summed utility values
                entts_dict = dict(sorted(entts_dict.items(), reverse=True))

                ### recreate world after ordering
                # world = list(entts_dict.values())
                world = [entt for li_of_entts in list(entts_dict.values()) for entt in li_of_entts]

                ### get current population
                current_pop = len(world)
                # print(f'current_pop: {current_pop}')

                ### append to one_runs
                # if i % 50 == 0:
                # one_run.append(sum(list(entts_dict.keys())[:30]) / 30)
                one_run_head.append(compute_avg_summed_util(entts_dict, current_pop, 'head'))
                one_run_tail.append(compute_avg_summed_util(entts_dict, current_pop, 'tail'))
                one_run_top_10p.append(compute_avg_summed_util(entts_dict, current_pop, 0.1))


                ### how many new entities to create ?
                # num_create = POP_SIZE - current_pop
                num_create = POP_SIZE - current_pop
                # print(f'how many to create ? : {num_create}')


                if num_create <= 0:
                    # num_create = 10
                    num_create = int(POP_SIZE * 0.03)
                else:
                    pass

                ### select procreate function
                procreate = proc_fxs[4]

                new_borns = []
                for _ in range(num_create):
                    children = procreate(world, POP_SIZE)

                    for new_entt in children:
                        new_borns.insert(0, new_entt)

                ### randomly select new entts
                ## percentage of new borns selected
                new_entt_perc = 0.5
                selected_new_entts = list(random.choices(population=new_borns, k=int(len(new_borns) * new_entt_perc)))

                ### introduce new born entts to world
                world = selected_new_entts + world

                for ix in range(len(world)):
                    world[ix] = mutate(world[ix], MUTATION_RATE)

                ### select entts & resize population
                world = selector(world, MAX_CSTRNT, cstrnt_list)
                world = world[:int(1.0 * POP_SIZE)]



            # print(entts_dict)
            ### final selection
            # world = selector(world)
            # print(len(world))

            ### append to result_lists
            # result_list.append(one_run)
            result_list_head.append(one_run_head)
            result_list_tail.append(one_run_tail)
            result_list_top_10p.append(one_run_top_10p)


            # print(f' *** Iteration #{j} COMPLETE *** ', end='\n')


        all_result_list_head.append(result_list_head)
        all_result_list_top_10p.append(result_list_top_10p)
        all_result_list_tail.append(result_list_tail)


    ###### ASSESSMENT PART
    ### Calcultae max_ever
    max_list_head = []
    for i in range(len(all_result_list_head)):
        for j in range(len(all_result_list_head[-1])):
            max_list_head.append(max(all_result_list_head[i][j]))
            # print(i,j)
    # print(max(max_list_head))
    max_ever = max(max_list_head)


    ### Create Peak List
    avg_peak_list = []
    for i in range(len(all_result_list_top_10p)):
        max_list_top_10p = []

        for j in range(len(all_result_list_top_10p[i])):
            max_list_top_10p.append(max(all_result_list_top_10p[i][j]))
        avg_peak = sum(max_list_top_10p)/len(max_list_top_10p)
        avg_peak_list.append(avg_peak)

    ### Create Plateau List
    avg_plateau_list = []
    for i in range(len(all_result_list_top_10p)):

        plateau_list_top_10p = []

        for j in range(len(all_result_list_top_10p[j])):
            # plateau_list_top_10p.append(sum(all_result_list_top_10p[j][i][-100:])/100)
            plateau_list_top_10p.append(compute_plateau(all_result_list_top_10p[i][j]))
        avg_plateau = sum(plateau_list_top_10p)/len(plateau_list_top_10p)
        avg_plateau_list.append(avg_plateau)


    ### Process values that are 0
    for i in range(len(MAX_CSTRNT_PERC_list)):
        if avg_peak_list[i] == 0:
            avg_peak_list[i] = 0.000000001
        else:
            pass

        if avg_plateau_list[i] == 0:
            avg_plateau_list[i] = 0.000000001
        else:
            pass


    ### Create avg dip list
    ### Create avg dip perc list
    avg_dip_list = []
    avg_dip_perc_list = []

    for i in range(len(avg_peak_list)):
        avg_dip = avg_peak_list[i] - avg_plateau_list[i]
        avg_dip_perc = avg_dip/avg_peak_list[i]
        avg_dip_list.append(avg_dip)
        avg_dip_perc_list.append(avg_dip_perc)





    ### Prepare JSON
    final_result = {}

    final_result['all_result_list_head'] = all_result_list_head
    final_result['all_result_list_top_10p'] = all_result_list_top_10p
    final_result['all_result_list_tail'] = all_result_list_tail
    final_result['util_distri'] = util_distri
    final_result['cstrnt_distri'] = cstrnt_distri
    final_result['POP_SIZE'] = POP_SIZE
    final_result['NUM_ITEMS'] = NUM_ITEMS
    final_result['GENOME_LEN'] = GENOME_LEN
    final_result['CROSSOVER_RATE'] = CROSSOVER_RATE
    final_result['GENERATIONS'] = GENERATIONS
    final_result['max_ever'] = max_ever
    final_result['avg_peak_list'] = avg_peak_list
    final_result['avg_plateau_list'] = avg_plateau_list
    final_result['MAX_CSTRNT_PERC_list'] = MAX_CSTRNT_PERC_list
    final_result['avg_dip_list'] = avg_dip_list
    final_result['avg_dip_perc_list'] = avg_dip_perc_list
    final_result['total_util'] = total_util
    final_result['total_cstrnt'] = total_cstrnt
    final_result['values_list'] = values_list
    final_result['cstrnt_list'] = cstrnt_list
    final_result['device'] = device

    ### Get time_of_save
    time_of_save = datetime.now()
    time_of_save = time_of_save.strftime('%Y%m%d_%H%M%S')

    final_result['time_of_save'] = str(time_of_save)

    final_result_fp = f'{json_fp_prefix}/final_result_{util_distri}_{cstrnt_distri}_{num_items}items_{time_of_save}.json'

    ## save json
    with open(final_result_fp, 'w') as final_result_json:
        json.dump(final_result, final_result_json)


### 15 mins per distri_product // POP_SIZE=1000, GENERATIONS=500