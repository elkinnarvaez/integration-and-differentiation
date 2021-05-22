from sys import stdin
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from differentiation import forward_difference, backward_difference, centered_difference, second_derivative_centered_difference
from integration import rectangle_rule, trapezoid_rule, simpsons_rule, composite_rectangle_rule, composite_trapezoid_rule, composite_simpsons_rule
from utils import abs_error
import time

MIN = -2
MAX = 5

def main():
    x = sym.Symbol('x')
    f1 = x*sym.sin(x**2) + 1
    f2 = sym.cos(x**2) - x**3 + sym.exp(x)
    f3 = sym.sin(sym.pi*x) + x**2 + 2
    f4 = sym.sinh(x)*0.3 + x**3 - sym.exp(x) + sym.pi
    f5 = sym.sin(x**2 + 10)/2**((x**3 -3 + sym.pi/2)/sym.pi)
    functions = [f1, f2, f3, f4, f5]
    # NOTE: If you define a new function, you also need to add it to the functions list above in order to use it later on
    #       The analytic derivate is calculated using sym.diff Python function, so you don't need to provide it to the program
    i = 1
    for func in functions:
        print(f"{i}. {func}")
        i += 1
    good = False
    option = None
    while(not good):
        option = int(input("Please choose the function you want to work with: ")); option -= 1
        if(option < 0 or option >= len(functions)):
            print("Invalid option. Please try again")
        else:
            good = True
    f = functions[option]
    print("1. Differentiation")
    print("2. Integration")
    good = False
    option = None
    while(not good):
        option = int(input("Please choose the operation: "))
        if(option < 1 or option > 2):
            print("Invalid option. Please try again")
        else:
            good = True
    if(option == 1):
        analytic_der = sym.diff(f, sym.Symbol('x'))
        analytic_second_der = sym.diff(analytic_der, sym.Symbol('x'))
        print(f"f(x) = {f}")
        print(f"df(x)/dx = {analytic_der}")
        print(f"d2f(x)/dx2 = {analytic_second_der}")
        x_values = list(np.linspace(MIN, MAX, num = 1000))
        f_values = list()
        analytic_der_values = list()
        analytic_second_der_values = list()
        der_values = list()
        second_der_values = list()
        h = 0.1
        # First and second derivative evaluation
        for x in x_values:
            f_values.append(float(f.subs(sym.Symbol('x'), x).evalf()))
            analytic_der_values.append(float(analytic_der.subs(sym.Symbol('x'), x).evalf()))
            analytic_second_der_values.append(float(analytic_second_der.subs(sym.Symbol('x'), x).evalf()))
        # First derivative approximation
        start1 = time.time()
        for x in x_values:
            der_values.append(backward_difference(f, x, h)) # We can change the differentiation method here
        end1 = time.time()
        elapsed1 = end1 - start1

        # Second derivative approximation
        start2 = time.time()
        for x in x_values:
            second_der_values.append(second_derivative_centered_difference(f, x, h))
        end2 = time.time()
        elapsed2 = end2 - start2

        # Evaluation
        der_error = abs_error(analytic_der_values, der_values)
        mean_der_error = np.mean(der_error)
        der_error_std = np.std(der_error)

        second_der_error = abs_error(analytic_second_der_values, second_der_values)
        mean_second_der_error = np.mean(second_der_error)
        second_der_error_std = np.std(second_der_error)

        # Plotting
        fig1, ax1 = plt.subplots()
        # ax1.plot(x_values, f_values, label="Function")
        ax1.plot(x_values, analytic_der_values, label="Analytic derivative")
        ax1.plot(x_values, der_values, label="Numerical derivative")
        ax1.legend()
        ax1.set_xlabel("x")
        ax1.set_ylabel("df(x)/dx")
        scalar_offset = 0 # 1.3
        x0_1, xmax_1 = plt.xlim()
        y0_1, ymax_1 = plt.ylim()
        text_x_pos_1 = 1.49
        text_y_pos_1 = y0_1 + (ymax_1 - y0_1) + scalar_offset
        ax1.text(text_x_pos_1, text_y_pos_1, "Mean error: {:e} \nStandard deviation: {:e} \nRunning time: {:e} sec".format(mean_der_error, der_error_std, elapsed1), bbox=dict(boxstyle="round",
                    ec=(1., 0.5, 0.5),
                    fc=(1., 0.9, 0.8),
                    ))
        # ax1.set_title(f'Analytic and numerical derivative')
        # ax1.grid(True)

        fig2, ax2 = plt.subplots()
        # ax2.plot(x_values, f_values, label="Function")
        ax2.plot(x_values, analytic_second_der_values, label="Analytic second derivative")
        ax2.plot(x_values, second_der_values, label="Numerical second derivative")
        ax2.legend()
        ax2.set_xlabel("x")
        ax2.set_ylabel("d2f(x)/dx2")
        scalar_offset = 0 # 1.7
        x0_2, xmax_2 = plt.xlim()
        y0_2, ymax_2 = plt.ylim()
        text_x_pos_2 = 1.45
        text_y_pos_2 = y0_2 + (ymax_2 - y0_2) + scalar_offset
        ax2.text(text_x_pos_2, text_y_pos_2, "Mean error: {:e} \nStandard deviation: {:e} \nRunning time: {:e} sec".format(mean_second_der_error, second_der_error_std, elapsed2), bbox=dict(boxstyle="round",
                    ec=(1., 0.5, 0.5),
                    fc=(1., 0.9, 0.8),
                    ))
        # ax2.set_title(f'Analytic and numerical second derivative')
        # ax2.grid(True)

        fig3, ax3 = plt.subplots()
        # ax2.plot(x_values, f_values, label="Function")
        ax3.plot(x_values, f_values)
        ax3.set_xlabel("x")
        ax3.set_ylabel("f(x)")
        # ax3.set_title(f'Function')
        # ax3.grid(True)

        plt.show()
    else:
        good = False
        n = None
        while(not good):
            n = int(input("Please select the number of panels: "))
            if(n <= 0):
                print("Invalid option. Please try again")
            else:
                good = True
        a = MIN
        b = MAX
        analytic_integral = sym.integrate(f, sym.Symbol('x'))
        definite_integral = sym.integrate(f, (sym.Symbol('x'), a, b)).evalf()
        start = time.time()
        approximate_definite_integral = composite_trapezoid_rule(f, a, b, n)
        end = time.time()
        elapsed = end - start
        print(f"f(x) = {f}")
        print(f"∫f(x) = {analytic_integral}")
        print(f"∫f(x)|(a = {a}, b = {b}) = {definite_integral}")
        print(f"Approximate ∫f(x)|(a = {a}, b = {b}) = {approximate_definite_integral}")
        print("Running time:", elapsed)
        print("Error:", abs(approximate_definite_integral - definite_integral))
    return 0

if __name__ == '__main__':
    main()