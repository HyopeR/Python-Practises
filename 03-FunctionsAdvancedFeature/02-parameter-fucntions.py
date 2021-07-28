def main_function(process_name):
    def addition(*args):
        total = 0

        for i in args:
            total += i

        return total

    def multiplication(*args):
        total = 1

        for i in args:
            total *= i

        return total

    function_case = {
        'addition': addition,
        'multiplication': multiplication,
    }
    target_function = function_case[process_name]
    return target_function


addition = main_function('addition')
print(addition(1, 2, 3, 4))

multiplication = main_function('multiplication')
print(multiplication(1, 2, 3, 4))


def f_addition(a, b):
    return a + b


def f_extraction(a, b):
    return a - b


def f_multiplication(a, b):
    return a * b


def f_division(a, b):
    return a / b


def f_main_function(func1, func2, func3, func4, process_name, a, b):
    try:
        function_case = {
            'addition': func1,
            'extraction': func2,
            'multiplication': func3,
            'division': func4,
        }

        target_function = function_case[process_name]
        return target_function(a, b)
    except:
        return 'This process is not valid!!!'


def f_calculator(process_name, a, b):
    return f_main_function(f_addition, f_extraction, f_multiplication, f_division, process_name, a, b)


print(f_calculator('addition', 3, 5))
print(f_calculator('extraction', 3, 5))
print(f_calculator('multiplication', 3, 5))
print(f_calculator('division', 3, 5))
print(f_calculator('xd', 3, 5))
