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

        x_axis = list()
        y_axis_mean_error_forward_difference = list()
        y_axis_mean_error_backward_difference = list()
        y_axis_mean_error_centered_difference = list()
        y_axis_mean_error_second_derivative_centered_difference = list()

        y_axis_error_std_forward_difference = list()
        y_axis_error_std_backward_difference = list()
        y_axis_error_std_centered_difference = list()
        y_axis_error_std_second_derivative_centered_difference = list()

        running_time_forward_difference = list()
        running_time_backward_difference = list()
        running_time_centered_difference = list()
        running_time_second_derivative_centered_difference = list()

        analytic_der_values = list()
        analytic_second_der_values = list()
        # First and second derivative evaluation
        for x in x_values:
            analytic_der_values.append(float(analytic_der.subs(sym.Symbol('x'), x).evalf()))
            analytic_second_der_values.append(float(analytic_second_der.subs(sym.Symbol('x'), x).evalf()))

        h_values = list(np.linspace(0.001, 2, num = 10))
        for h in h_values:
            print(h)
            x_axis.append(h)

            # First derivative approximation: forward difference
            der_values = list()
            start = time.time()
            for x in x_values:
                der_values.append(forward_difference(f, x, h))
            end = time.time()
            elapsed = end - start

            # Evaluation
            der_error = abs_error(analytic_der_values, der_values)
            mean_der_error = np.mean(der_error)
            der_error_std = np.std(der_error)

            y_axis_mean_error_forward_difference.append(mean_der_error)
            y_axis_error_std_forward_difference.append(der_error_std)
            running_time_forward_difference.append(elapsed)

            # First derivative approximation: backward difference
            der_values = list()
            start = time.time()
            for x in x_values:
                der_values.append(backward_difference(f, x, h))
            end = time.time()
            elapsed = end - start

            # Evaluation
            der_error = abs_error(analytic_der_values, der_values)
            mean_der_error = np.mean(der_error)
            der_error_std = np.std(der_error)

            y_axis_mean_error_backward_difference.append(mean_der_error)
            y_axis_error_std_backward_difference.append(der_error_std)
            running_time_backward_difference.append(elapsed)

            # First derivative approximation: centered difference
            der_values = list()
            start = time.time()
            for x in x_values:
                der_values.append(centered_difference(f, x, h))
            end = time.time()
            elapsed = end - start

            # Evaluation
            der_error = abs_error(analytic_der_values, der_values)
            mean_der_error = np.mean(der_error)
            der_error_std = np.std(der_error)

            y_axis_mean_error_centered_difference.append(mean_der_error)
            y_axis_error_std_centered_difference.append(der_error_std)
            running_time_centered_difference.append(elapsed)

            second_der_values = list()

            # Second derivative approximation: centered difference
            start = time.time()
            for x in x_values:
                second_der_values.append(second_derivative_centered_difference(f, x, h))
            end = time.time()
            elapsed = end - start

            # Evaluation
            second_der_error = abs_error(analytic_second_der_values, second_der_values)
            mean_second_der_error = np.mean(second_der_error)
            second_der_error_std = np.std(second_der_error)

            y_axis_mean_error_second_derivative_centered_difference.append(mean_second_der_error)
            y_axis_error_std_second_derivative_centered_difference.append(second_der_error_std)
            running_time_second_derivative_centered_difference.append(elapsed)

        # Plotting
        fig1, ax1 = plt.subplots()
        ax1.plot(x_axis, y_axis_mean_error_forward_difference, label="Forward difference")
        ax1.plot(x_axis, y_axis_mean_error_backward_difference, label="Backward difference")
        ax1.plot(x_axis, y_axis_mean_error_centered_difference, label="Centered difference")
        ax1.legend()
        ax1.set_xlabel("h")
        ax1.set_ylabel("Mean error")

        fig2, ax2 = plt.subplots()
        ax2.plot(x_axis, y_axis_error_std_forward_difference, label="Forward difference")
        ax2.plot(x_axis, y_axis_error_std_backward_difference, label="Backward difference")
        ax2.plot(x_axis, y_axis_error_std_centered_difference, label="Centered difference")
        ax2.legend()
        ax2.set_xlabel("h")
        ax2.set_ylabel("Standard deviation")

        fig3, ax3 = plt.subplots()
        ax3.plot(x_axis, running_time_forward_difference, label="Forward difference")
        ax3.plot(x_axis, running_time_backward_difference, label="Backward difference")
        ax3.plot(x_axis, running_time_centered_difference, label="Centered difference")
        ax3.legend()
        ax3.set_xlabel("h")
        ax3.set_ylabel("Time (seconds)")

        fig4, ax4 = plt.subplots()
        ax4.plot(x_axis, y_axis_mean_error_second_derivative_centered_difference, label="Centered difference")
        ax4.legend()
        ax4.set_xlabel("h")
        ax4.set_ylabel("Mean error")

        fig5, ax5 = plt.subplots()
        ax5.plot(x_axis, y_axis_error_std_second_derivative_centered_difference, label="Centered difference")
        ax5.legend()
        ax5.set_xlabel("h")
        ax5.set_ylabel("Standard deviation")

        fig6, ax6 = plt.subplots()
        ax6.plot(x_axis, running_time_second_derivative_centered_difference, label="Centered difference")
        ax6.legend()
        ax6.set_xlabel("h")
        ax6.set_ylabel("Time (seconds)")

        plt.show()
    else:
        a = MIN
        b = MAX
        analytic_integral = sym.integrate(f, sym.Symbol('x'))
        definite_integral = sym.integrate(f, (sym.Symbol('x'), a, b)).evalf()
        print(f"f(x) = {f}")
        print(f"∫f(x) = {analytic_integral}")
        print(f"∫f(x)|(a = {a}, b = {b}) = {definite_integral}")

        x_axis = list()
        
        running_time_composite_rectangle_rule = list()
        running_time_composite_trapezoid_rule = list()
        running_time_composite_simpsons_rule = list()

        abs_error_composite_rectangle_rule = list()
        abs_error_composite_trapezoid_rule = list()
        abs_error_composite_simpsons_rule = list()

        n = 10
        while(n <= 200):
            print(n)
            x_axis.append(n)
            # Composite rectangle rule
            start = time.time()
            approximate_definite_integral = composite_rectangle_rule(f, a, b, n)
            end = time.time()
            elapsed = end - start
            error = abs(approximate_definite_integral - definite_integral)
            running_time_composite_rectangle_rule.append(elapsed)
            abs_error_composite_rectangle_rule.append(error)

            # Composite trapezoid rule
            start = time.time()
            approximate_definite_integral = composite_trapezoid_rule(f, a, b, n)
            end = time.time()
            elapsed = end - start
            error = abs(approximate_definite_integral - definite_integral)
            running_time_composite_trapezoid_rule.append(elapsed)
            abs_error_composite_trapezoid_rule.append(error)

            # Composite simpsons rule
            start = time.time()
            approximate_definite_integral = composite_simpsons_rule(f, a, b, n)
            end = time.time()
            elapsed = end - start
            error = abs(approximate_definite_integral - definite_integral)
            running_time_composite_simpsons_rule.append(elapsed)
            abs_error_composite_simpsons_rule.append(error)
            n += 10

        # Plotting
        fig1, ax1 = plt.subplots()
        ax1.plot(x_axis, abs_error_composite_rectangle_rule, label="Composite rectangle rule")
        ax1.plot(x_axis, abs_error_composite_trapezoid_rule, label="Composite trapezoid rule")
        ax1.plot(x_axis, abs_error_composite_simpsons_rule, label="Composite Simpsons rule")
        ax1.legend()
        ax1.set_xlabel("Number of panels")
        ax1.set_ylabel("Absolute error")

        fig2, ax2 = plt.subplots()
        ax2.plot(x_axis, running_time_composite_rectangle_rule, label="Composite rectangle rule")
        ax2.plot(x_axis, running_time_composite_trapezoid_rule, label="Composite trapezoid rule")
        ax2.plot(x_axis, running_time_composite_simpsons_rule, label="Composite Simpsons rule")
        ax2.legend()
        ax2.set_xlabel("Number of panels")
        ax2.set_ylabel("Time (seconds)")

        plt.show()

    return 0

if __name__ == '__main__':
    main()