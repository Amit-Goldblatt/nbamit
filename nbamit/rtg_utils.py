from decimal import Decimal
import mpmath as math
# all the equations in this file are from the paper: http://www.glicko.net/glicko/glicko2.pdf 


def fx(a ,x, delta, phi, v, tao):
    return math.exp(x) * ((delta ** 2) - (phi ** 2) - v - (math.exp(x))) / (2 * (((phi ** 2) + v + (math.e ** x)) ** 2)) - (x - a) / ((tao) ** 2)
# mu = rating in glicko2 scale 
def calc_mu(rating):
    return (rating - 1500) / 173.7178
# phi = rating deviation in glicko2 scale 
def calc_phi(rd):
    return rd / 173.7178
# helper function 
def calc_g_phi(phi):
    return 1 / math.sqrt(1 + 3 * (phi ** 2) / (math.pi ** 2))
# helper function
def calc_E_mu(mu, mu_j, g_phi):
    return 1 / (1 + (math.exp(-g_phi * (mu - mu_j))))
# v = variance of rating 
def calc_v(g_phi, E_mu):
 
    return 1 / (g_phi ** 2 * E_mu * (1 - E_mu))
   
# delta = estimated improvement in rating
def calc_delta(v, g_phi, E_mu, s):
    return v * (g_phi * (s - E_mu))
# phi_tag = new rating deviation
def calc_new_volatility(vol,phi,v,delta,tao, sigma = 0.000001):
    a = math.log(vol ** 2)
    A=a
    if delta**2 > phi**2 + v:
        B = math.log(delta**2 - phi**2 - v)
    else:
        k = 1
        while fx(a, a - k * tao,  delta, phi, v, tao) < 0:
            k += 1
        B = a - k * tao
    f_A = fx(a, A, delta, phi, v, tao)
    f_B = fx(a, B, delta, phi, v, tao)
    while abs(B - A) > sigma:
        C=A+(A-B)*f_A/(f_B-f_A)
        f_C=fx(a, C, delta, phi, v, tao)
        if f_C*f_B<=0:
            A=B
            f_A=f_B
        else:
            f_A=f_A/2
        B=C
        f_B=f_C
    return math.e ** (A/2)
# update the rating deviation of a team
def calc_phi_tag(phi, vol, v):
    phi_star = math.sqrt(phi ** 2 + vol**2)
    return  1 / math.sqrt(1 / (phi_star ** 2) + 1 / v)

# update the rating of a team
def calc_mu_tag(mu, phi_tag,s, g_phi, E_mu):
    return mu + phi_tag ** 2 * g_phi * (s - E_mu)

# convert the rating to the glicko1 scale
def convert_to_original_scale(mu):
    return mu * 173.7178 + 1500
# convert the rating deviation to the glicko1 scale
def convert_to_original_scale_phi(phi):
    return phi * 173.7178
# this function is used to calculate the new rating , rating deviation and volatility of a team
def calc_new_rating(team1, team2,s, tao = 0.5):
    # check winner
    if s == team1:
        s = 1
    elif s == team2:
        s = 0
  
    mu = calc_mu(team1.rating)
    mu_j = calc_mu(team2.rating)
    phi = calc_phi(team1.rd)
    phi_j = calc_phi(team2.rd)
    g_phi_j = calc_g_phi(phi_j)
    E_mu_j = calc_E_mu(mu, mu_j, g_phi_j)
    v = calc_v(g_phi_j, E_mu_j)
    delta = calc_delta(v, g_phi_j, E_mu_j, s)
    new_vol = calc_new_volatility(team1.vol,phi,v,delta,tao)
    phi_tag = calc_phi_tag(phi, new_vol, v)
    mu_tag = calc_mu_tag(mu, phi_tag, s, g_phi_j, E_mu_j)
    return convert_to_original_scale(mu_tag), convert_to_original_scale_phi(phi_tag), new_vol

# helper function for predict_winner
def g(RD):
    return 1 / math.sqrt(1 + 3 * RD ** 2 / math.pi ** 2)

def predict_winner(team1, team2):
    diffRD = math.sqrt(team1.rd ** 2 + team2.rd ** 2)
    return 1 / (1 + math.exp(-1 * g(diffRD) *  (team1.rating - team2.rating)))



# test i wrote to check if the functions are working correctly
# theese tests are not complete and are not used in the program

# def test_fx():
#     a=-5.62682
#     x=a
#     delta=-0.4834
#     phi = 1.1513
#     v = 1.7785
#     tao = 0.5
#     f_a_test  = fx(a ,x, delta, phi, v, tao)
#     print(f_a_test)
#     assert f_a_test == -0.000535672453887165
#     x=-6.12682
#     f_b_test  = fx(a ,x, delta, phi, v, tao)
#     assert f_b_test == 1.99967496212253
# def test_calc_new_volatility():
#     vol = 0.06
#     phi = 1.1513
#     v = 1.7785
#     delta = -0.4834
#     tao = 0.5
#     new_vol = calc_new_volatility(vol,phi,v,delta,tao)
#     # assert new_vol == 0.0599959830198937
# def test_calc_phi_tag():
#     phi = 1.1513
#     vol = 0.05999
#     v = 1.7785
#     phi_tag = calc_phi_tag(phi, vol, v)
#     # assert phi_tag == 0.872152275371291

# def test_calc_mu_tag():
#     mu = 0.0
#     phi_tag = 0.87215
#     s = 1
#     g_phi = 0.9955
#     E_mu = 0.639
#     mu_tag = calc_mu_tag(mu, phi_tag, s, g_phi, E_mu)
#     print(mu_tag)
#     # assert mu_tag == 0.435


