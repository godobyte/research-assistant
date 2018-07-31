'''
Simulation - Python

@author: Bian

@description: This is the simulation computation in Python.

    python compute.py p1_za p1_zb p2_za p2_zb
'''

# temp setting for testing

# proportion of strategic customers in the markets
beta_za = 0
beta_zb = 0
# inconvenience cost associated with a connecting flight
delta_za = 0
delta_zb = 0
# 1's cost for ZA, 2's cost for ZB
c1 = 0
c2 = 0
# cost for AB and BA segments
alpha1 = 0
alpha2 = 0
# market size
lambda_za = 0.5
lambda_zb = 0.5

#################################################
# Profit Evaluation for Airline 1 and Airline 2 #
#################################################

def profit_eva_1(p1_za, p1_zb, p2_za, p2_zb):
    pi1_za = 0
    if p1_za <= p2_za + delta_za:
        pi1_za += (1 - beta_za) * (p1_za - c1)
    if (p1_za <= p2_za + delta_za) and (p1_za <= p1_zb):
        pi1_za += beta_za * (p1_za - c1)
    if (p1_zb <= p2_za + delta_za) and (p1_zb < p1_za):
        pi1_za += beta_za * (p1_zb - c1 - alpha1)

    pi1_zb = 0
    if p1_zb < p2_zb - delta_zb:
        pi1_zb += (1 - beta_zb) * (p1_zb - c1 - alpha1)
    if p1_zb < min(p2_zb - delta_zb, p2_za - delta_zb):
        pi1_zb += beta_zb * (p1_zb - c1 - alpha1)

    return lambda_za * pi1_za + lambda_zb * pi1_zb

def profit_eva_2(p1_za, p1_zb, p2_za, p2_zb):
    pi2_zb = 0
    if p2_zb <= p1_zb + delta_zb:
        pi2_zb += (1 - beta_zb) * (p2_zb - c2)
    if (p2_zb <= p1_zb + delta_zb) and (p2_zb <= p2_za):
        pi2_zb += beta_zb * (p2_zb - c2)
    if (p2_za <= p1_zb + delta_zb) and (p2_za < p2_zb):
        pi2_zb += beta_zb * (p2_za - c2 - alpha2)

    pi2_za = 0
    if p2_za < p1_za - delta_za:
        pi2_za += (1 - beta_za) * (p2_za - c2 - alpha2)
    if p2_za < min(p1_za - delta_za, p1_zb - delta_za):
        pi2_za += beta_za * (p2_za - c2 - alpha2)

    return lambda_za * pi2_za + lambda_zb * pi2_zb

###########################
# Airlines' Best Response #
###########################
class Response:
    def __init__(self, name, pi):
        self.name = name
        self.pi = pi

    def update(self, new_name, new_pi):
        self.name = new_name
        self.pi = new_pi

# Set up parameters
interval = 0.01
epsilon = 0.01

# Fix pi_za and p1_zb to find p2_za and p2_zb to maximize pi2
def best_response_2(p1_za, p1_zb):
    p2_za = 0
    p2_zb = 0

    #Candidate 1
    if (p1_zb + delta_zb >= p1_za - delta_za) or (p1_za - delta_za <= c2 + alpha2):
        p2_za = min(p1_zb + delta_zb, 1)
        p2_zb = p2_za
        res = Response("candidate 1", profit_eva_2(p1_za, p1_zb, p2_za, p2_zb))

    #Candidate 2
    if p1_za - delta_za > c2 + alpha2:
        p2_zb = min(p1_zb + delta_zb, 1)
        p2_za = p1_za - delta_za - epsilon
        pi_2 = profit_eva_2(p1_za, p1_zb, p2_za, p2_zb)
        if pi_2 > res.pi:
            res.update("candidate 2", pi_2)

    #Candidate 3
    if (p1_za > p1_zb) and (p1_zb - delta_za > c2 + alpha2):
        p2_zb = min(p1_zb + delta_zb, 1)
        p2_za = p1_zb - delta_za - epsilon
        pi_2 = profit_eva_2(p1_za, p1_zb, p2_za, p2_zb)
        if pi_2 > res.pi:
            res.update("candidate 3", pi_2)

    print("When p1_za = %s, p1_zb = %s, p2_za = %s, p2_zb = %s, the best response is %s with pi2 = %s"
    % (p1_za, p1_zb, p2_za, p2_zb, res.name, res.pi))

if __name__ == "__main__":
    import sys
    print(__doc__)
    # try:
    print("Executing profit evalutation for Airline 1: %s" %
    profit_eva_1(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
    print("Executing profit evalutation for Airline 2: %s" %
    profit_eva_2(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
    print("Executing best Candidate for Airline 2 pricing")
    best_response_2(int(sys.argv[1]), int(sys.argv[2]))
    print("Execution done")
    # except (IndexError, TypeError):
        # pass
