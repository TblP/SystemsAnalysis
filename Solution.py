from scipy.optimize import linprog
import math
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

    A = [
        ref[:2],
        ref[3:5],
        ref[6:8]
    ]

    b = [
        ref[2],
        ref[5],
        ref[8]
    ]

    c = ref[9:]

    def to_tableau(c, A, b):
        xb = [eq + [x] for eq, x in zip(A, b)]
        z = c + [0]
        return xb + [z]

    def can_be_improved(tableau):
        z = tableau[-1]
        return any(x > 0 for x in z[:-1])

    def get_pivot_position(tableau):
        z = tableau[-1]
        column = next(i for i, x in enumerate(z[:-1]) if x > 0)

        restrictions = []
        for eq in tableau[:-1]:
            el = eq[column]
            restrictions.append(math.inf if el <= 0 else eq[-1] / el)

        row = restrictions.index(min(restrictions))
        return row, column

    def pivot_step(tableau, pivot_position):
        new_tableau = [[] for eq in tableau]

        i, j = pivot_position
        pivot_value = tableau[i][j]
        new_tableau[i] = np.array(tableau[i]) / pivot_value

        for eq_i, eq in enumerate(tableau):
            if eq_i != i:
                multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
                new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier

        return new_tableau

    def is_basic(column):
        return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

    def get_solution(tableau):
        columns = np.array(tableau).T
        solutions = []
        for column in columns:
            solution = 0
            if is_basic(column):
                one_index = column.tolist().index(1)
                solution = columns[-1][one_index]
            solutions.append(solution)

        return solutions

    def simplex(c, A, b):
        tableau = to_tableau(c, A, b)

        while can_be_improved(tableau):
            pivot_position = get_pivot_position(tableau)
            tableau = pivot_step(tableau, pivot_position)

        return get_solution(tableau)

    solution = simplex(c, A, b)

    result = f"Позиций A - {solution[0]} \n" + \
             f"Позиций В - {solution[1]} \n" + \
             f"Максимальнаяя прибыль - {sum([int(ref[9 + i] * solution[i]) for i in range(2)])}р."

    return "Ответ: \n" + result + "\n\nРешено с помощью algoritma"

testo = [17,24,114,15,12,115,15,14,155,18,20]

print(Solution_algo(testo))
print(Solution_scipy(testo))