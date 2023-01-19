def gradient_descent(derivative_function, initial_guess, multiplier=0.02, precision=0.001) :
    new_x = initial_guess
    x_list = []
    slope_list = []

    for n in range(500) :
        previous_x = new_x
        gradient = derivative_function(previous_x)
        new_x = previous_x - multiplier * gradient

        step_size = abs(new_x - previous_x)

        x_list.append(new_x)
        slope_list.append(derivative_function(new_x))

        if step_size < precision :
            break

    return new_x, x_list, slope_list
