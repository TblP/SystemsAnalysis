from scipy.optimize import linprog
import numpy as np

def Solution_scipy(ref: list):
    ref = list(map(lambda x: int(x), ref))

    obj = list(map(lambda x: -1 * x, ref[9:]))

    lhs_ineq = [
        ref[:2],
        ref[3:5],
        ref[6:8]
    ]

    rhs_ineq = [
        ref[2],
        ref[5],
        ref[8]
    ]

    bnd = [(0, None),
           (0, None)
    ]

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
                  method="revised simplex")

    temp = (int(opt.x[0]), int(opt.x[1]), int(opt.fun * -1))
    result = f"Позиций A - {temp[0]} \n" + \
             f"Позиций В - {temp[1]} \n" + \
             f"Максимальнаяя прибыль - {temp[2]}р."

    return "Ответ: \n" + result + "\n\nРешено с помощью Scipy"

def Solution_algo(ref: list):
    ref = list(map(lambda x: int(x), ref))
    ''' F = 7x1 + 9x2 формула 
    
    3х1 + 6х2 <= 102
    4x1 + 3x2 <= 91
    5x1 + 2x2 <= 105
    x1 x2 >= 0
    
    F(x1*x2) = 7x1 + 9x2 -> max
    
    
    '''


    result = f"Позиций A - {1} \n" + \
             f"Позиций В - {1} \n" + \
             f"Позиций C - {1} \n" + \
             f"Максимальнаяя прибыль - {1}р."

    return "Ответ: \n" + result + "\n\nРешено с помощью алгоритмов"

testo = [3,6,102,4,3,91,5,2,105,7,9]
print(Solution_scipy(testo))