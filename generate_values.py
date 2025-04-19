import random

### function to generate random items
def generate_items(num_items):
    num_items = int(num_items)
    # return(num_items)
    return [f'item_{x+1}' for x in range(num_items)]



### function to generate utility values for the items
### select distribution with arg

def generate_util_vals(num_items, dist='normal'):
    # num_items = int(num_items)
    if dist == 'normal':
        result = [random.normalvariate(mu=0.0, sigma=1.0)+100 for _ in range(num_items)]
        
    elif dist == 'log_normal' or dist == 'lognormal':
        mu, sigma = 3., 1.
        result = [random.lognormvariate(mu, sigma) for _ in range(num_items)]
    elif dist == 'uniform':
        
        result = [random.uniform(0, 1) for _ in range(num_items)]
        
    elif dist == 'expovariate':
        llambda = 1.5
        result = [random.expovariate(llambda) for _ in range(num_items)]
        
    elif dist == 'gauss':
        result = [random.gauss(mu=0.0, sigma=1.0) for _ in range(num_items)]
        
    elif dist == 'vonmise':
        mu, kappa = 0, 4.
        result = [random.vonmisesvariate(mu, kappa) for _ in range(num_items)]
        
    elif dist == 'pareto':
        alpha = 3
        result = [random.paretovariate(alpha) for _ in range(num_items)]
        
    elif dist == 'weibull':
        alpha, beta = 1, 1.5
        result = [random.weibullvariate(alpha, beta) for _ in range(num_items)]
        
    elif dist == 'left_skewed' or dist == 'leftskewed':
        # alpha, beta = -1, 1.5
        # result = [random.weibullvariate(alpha, beta)+100 for _ in range(num_items)]
        alpha, beta = 50, 100
        result = [random.weibullvariate(alpha, beta) for _ in range(num_items)]
        
    else:
        result = [random.normalvariate(mu=0.0, sigma=1.0)+100 for _ in range(num_items)]
    

    return result




### function to generate utility values for the items
### select distribution with arg

def generate_cstrnt_vals(num_items, dist='normal'):
    # num_items = int(num_items)
    if dist == 'normal':
        result = [random.normalvariate(mu=0.0, sigma=1.0)+100 for _ in range(num_items)]
        
    elif dist == 'log_normal' or dist == 'lognormal':
        mu, sigma = 3., 1.
        result = [random.lognormvariate(mu, sigma) for _ in range(num_items)]

    elif dist == 'uniform':
        result = [random.uniform(0, 1) for _ in range(num_items)]
        
    elif dist == 'expovariate':
        llambda = 1.5
        result = [random.expovariate(llambda) for _ in range(num_items)]
        
    elif dist == 'gauss':
        result = [random.gauss(mu=0.0, sigma=1.0) for _ in range(num_items)]
        
    elif dist == 'vonmise':
        mu, kappa = 0, 4.
        result = [random.vonmisesvariate(mu, kappa) for _ in range(num_items)]
        
    elif dist == 'pareto':
        alpha = 3
        result = [random.paretovariate(alpha) for _ in range(num_items)]
        
    elif dist == 'weibull':
        alpha, beta = 1, 1.5
        result = [random.weibullvariate(alpha, beta) for _ in range(num_items)]
        
    elif dist == 'left_skewed' or dist == 'leftskewed':
        # alpha, beta = -1, 1.5
        # result = [random.weibullvariate(alpha, beta)+100 for _ in range(num_items)]
        alpha, beta = 50, 100
        result = [random.weibullvariate(alpha, beta) for _ in range(num_items)]
        
    else:
        result = [random.normalvariate(mu=0.0, sigma=1.0)+100 for _ in range(num_items)]
    

    return result




