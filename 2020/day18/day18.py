#day 18

def precedence(op, part):
    # the operators have the same precedence
    if part == 1:
        if op == '+':
            return 1
        if op == '*':
            return 1
    
    # addition is evaluated before multiplication
    else:
        if op == '+':
            return 2
        if op == '*':
            return 1

 
def applyOperation(a, b, operation):
    if operation == '+': 
        return a + b

    if operation == '*': 
        return a * b
 

def evaluate(expresion, part):
    values = []
    operations = []
  
    i = 0
    while i < len(expresion):
        if expresion[i] == '(':
            operations.append(expresion[i])
         
        #  push number into number stack
        elif expresion[i].isdigit():
            values.append(int(expresion[i]))
         
        # solve entire expresion from brace
        elif expresion[i] == ')':
            while len(operations) > 0 and operations[-1] != '(':
                right = values.pop()
                left = values.pop()
                op = operations.pop()
                values.append(applyOperation(left, right, op))
             
            # pop opening brace.
            operations.pop()
         
        # operator
        else:
            # depending on operations precedence apply operator
            # if the top operations from stack has the same or greater precedence -> apply operator
            while (len(operations) > 0 and 
                   precedence(operations[-1], part) >= precedence(expresion[i], part)):
                left = values.pop()
                right = values.pop()
                op = operations.pop()
                values.append(applyOperation(left, right, op))
             
            # push operation into operaion stack
            operations.append(expresion[i])
         
        i += 1
     
    # apply remains operations
    while len(operations) > 0:
        left = values.pop()
        right = values.pop()
        op = operations.pop()
        values.append(applyOperation(left, right, op))
     
    return values[-1]


if __name__ == "__main__":
    with open("input", 'r') as input:
        lines = input.read().splitlines()
        # print(lines)
    
    part1 = []
    for line in lines:
        result = evaluate(line.replace('(', '( ').replace(')', ' )').split(' '), 1)
        part1.append(result)
    print("Part1: " + str(sum(part1)))

    part2 = []
    for line in lines:
        result = evaluate(line.replace('(', '( ').replace(')', ' )').split(' '), 2)
        part2.append(result)
    print("Part2: " + str(sum(part2)))	