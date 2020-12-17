#day 16

def parseInput(lines):
    frecuencyArray = []
    notValid = []
    myTicket = []
    goodTickets = []
    rules = []
    
    # 1: ranges, 2: my ticket, 3: nearby tickets
    ok = 1
    for line in lines:
        if line == '':
            ok += 1
        
        elif ok == 1:	# read ranges
            aux = line.split(': ')[1]
            aux = aux.split(' or ')

            # get the rule
            firstInterval = aux[0].split('-')
            secondInterval = aux[1].split('-')
            # name, min_pair1, max_pair1, min_pair2, max_pair2
            rules.append([line.split(': ')[0], 
                          int(firstInterval[0]), int(firstInterval[1]), 
                          int(secondInterval[0]), int(secondInterval[1])])

            for pair in aux:
                rangePair = pair.split('-')

                for i in range(int(rangePair[0]), int(rangePair[1]) + 1):
                    frecuencyArray.append(i)


        elif ok == 2:	# read my ticket
            if line != 'your ticket:':
                aux = line.split(',')
                for number in aux:
                    myTicket.append(int(number))


        elif ok == 3:	# read nearby tickets
            if line != 'nearby tickets:':
                aux = line.split(',')
                
                isGoodTicket = True
                for number in aux:
                    if int(number) not in frecuencyArray:
                        notValid.append(int(number))
                        isGoodTicket = False
                if isGoodTicket:
                    goodTickets.append(list(map(int, aux)))

    return sum(notValid), myTicket, goodTickets, rules


def getMatchingRules(number, rules):
    respectedRules = []
    for i in range(len(rules)):
        if rules[i][1] <= number <= rules[i][2] or rules[i][3] <= number <= rules[i][4]:
            respectedRules.append(i)
    return set(respectedRules)


def computePart2(goodTickets, rules, myTicket):
    # this list contains the rules that are respected for each column/number from all tickets
    # at the beginning all I assume all rules are respected
    rulePosibility = [] 
    for _ in goodTickets[0]:
        rulePosibility.append(set(range(len(rules))))

    for ticket in goodTickets:
        # for every number from ticket I want to see which rules does the number respect
        ticketMathingRules = []
        for number in ticket:
            ticketMathingRules.append(getMatchingRules(number, rules))

        # update the general rule posibility (eliminate rules that are not respected for this thicket)
        for i in range(len(rulePosibility)):
            rulePosibility[i] &= ticketMathingRules[i]
    
    # get from rulePosibility the ones that match exactly one rule
    exactlyOneRuleMatch = []
    for match in rulePosibility:
        if len(match) == 1:
            exactlyOneRuleMatch.append(match)

    while len(exactlyOneRuleMatch):
        # pop the first exactly one rule match
        rulePosition = exactlyOneRuleMatch.pop()

        for i in range(len(rulePosibility)):
            rulesMatching = rulePosibility[i]

            # if there is no exactly one match
            if rulePosition != rulesMatching:
                # delete the rule that is already one matched for another column
                lengthBefore = len(rulesMatching)
                rulePosibility[i] -= rulePosition
                lengthAfter = len(rulePosibility[i])
                
                # if by deleting the one match rule we obtain another one match rule -> 
                # add the one match rule to the stack
                if lengthAfter == 1 and (lengthBefore - lengthAfter) == 1:
                    exactlyOneRuleMatch.append(rulePosibility[i])
    
    part2 = 1
    # for every exactly one match rule check if the rule starts with "departure"
    # if so multiply the coresponding number from myTicket
    for i in range(len(rulePosibility)):
        rulePosition = list(rulePosibility[i])[0]
        if rules[rulePosition][0].startswith("departure"):
            part2 *= myTicket[i]
            
    return part2


if __name__ == "__main__":
    with open("input", 'r') as input:
        lines = input.read().splitlines()
        # print(lines)
    
    part1, myTicket, goodTickets, rules = parseInput(lines)
    print("Part1: " + str(part1))	
    print("Part2: " + str(computePart2(goodTickets, rules, myTicket)))	