def arithmetic_arranger(problems, solve=False):
    # Initialize variables
    line_1, line_2, line_3, line_4 = str(), str(), str(), str()

    # Split the problems into a list of lists
    problems_list = [problem.split() for problem in problems]

    # Check if the number of problems exceeds the maximum
    if len(problems_list) > 5:
        return "Error: Too many problems."

    for problem in problems_list:
        # Get the number of digits in the largest number
        num_max_len = max(len(str(problem[0])), len(str(problem[2])))

        # Check if the problem is valid  
        if len(problem) != 3:
            return "Error: Each problem needs three parts."
        elif not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."
        elif problem[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-' ."
        elif num_max_len > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Arrange problem outputs
        line_1 += problem[0].rjust(num_max_len+2)+"    "
        line_2 += problem[1] + problem[2].rjust(num_max_len+1)+"    "
        line_3 += "-" *(num_max_len+2)+"    "
        # If solve is True, solve the problem and add the solution to line_4
        if solve:
            solution = eval(' '.join(problem))
            line_4 += str(solution).rjust(num_max_len+2)+"    "

    arranged_problems = line_1+"\n"+line_2+"\n"+line_3

    if solve:
        arranged_problems += "\n"+ line_4

    return arranged_problems


test = arithmetic_arranger(["3801 - 2", "123 + 49"])
print(test)