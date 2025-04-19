### compute various type of summed utility values
### average of top N %
### HEAD(TOP ENTITY)
### TAIL(BOTTOM ENTITY)
def compute_avg_summed_util(entts_dict, current_pop, percentage=1):
    
    if percentage == 'head':
        result = list(entts_dict.keys())[0]
    elif percentage == 'tail':
        result = list(entts_dict.keys())[-1]

    elif (percentage >= 0) and (percentage <= 1):
        until_which = int(-(-current_pop//(1/percentage)))
        
        total_sum = 0
        prev_ccount = 0
        ccount = 0

        for kkey in entts_dict:
            prev_ccount = ccount
            ccount += len(entts_dict[kkey])
            if ccount <= until_which:
                total_sum += int(kkey*len(entts_dict[kkey]))
            else:
                # print(prev_ccount)
                total_sum += int(kkey*(until_which - prev_ccount))
                break

        result = total_sum/until_which

    return result



### compute plateau by averaging the moving averages
## compute plateau by averaging moving averages 

def compute_plateau(metric_list, nn=50):
    avg_list = []

    for i in range(len(metric_list)-nn+1):
        avg_list.append(sum(metric_list[i:i+nn])/nn)
    
    return sum(avg_list)/len(avg_list)
    
# print(compute_plateau(weibull_all_result_list_top_10p[j][0]))