'''
Simulation - Python

@author: bian

@description: This is the simulation computation in Python.

    python compute.py p1_za p1_zb p2_za p2_zb
'''

# temp setting for testing
beta_za = 0
beta_zb = 0
delta_za = 0
delta_zb = 0
c1 = 0
c2 = 0
alpha1 = 0
alpha2 = 0

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

    return pi1_za + pi1_zb

if __name__ == "__main__":
    import sys
    print(__doc__)
    try:
        print("Executing profit evalutation for Airline 1: %s" %
        profit_eva_1(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
        print("Execution done")
    except (IndexError, TypeError):
        pass

