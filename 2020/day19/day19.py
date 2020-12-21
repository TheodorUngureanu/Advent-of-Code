#day 19
# run with python3
import regex
from itertools import count


def parseRules(rules):
    rules = rules.splitlines()
    rulesDictionary = {}
    for rule in rules:
        number, values = rule.split(': ')
        rulesDictionary[number] = values
        
    return rulesDictionary


def build_regex(ruleKey, part):
    rule = rules[ruleKey]
    # get characters at the beginning of string that match the regular expression pattern
    match = regex.match(r'"(\w)"', rule)
    counter = count() # generate unique names
    
    if match:
        # get the string matched
        return match.group(1)

    # rule for 8: adding + to the 42 regex
    if part == 2 and ruleKey == "8":
        return f"({build_regex('42', 2)}+)"
    
    # rule for 11:
    if part == 2 and ruleKey == "11":
        a = build_regex("42", 2)
        b = build_regex("31", 2)
        name = f"r{next(counter)}"
        return f"(?P<{name}>{a}(?P>{name})?{b})"  # like the rule say: letter-rule11-letter

    pattern = "|".join("".join(build_regex(m, part) for m in sub_rule.split()) for sub_rule in rule.split(" | "))
    return f"({pattern})"


def computePart1(rules, messages):
    return len(regex.findall(f"^{build_regex('0', 1)}$", messages, flags=regex.MULTILINE))


def computePart2(rules, messages):
    return len(regex.findall(f"^{build_regex('0', 2)}$", messages, flags=regex.MULTILINE))


if __name__ == "__main__":
    with open("input", 'r') as input:
        rules, messages = input.read().split('\n\n')
        rules = parseRules(rules)

        print("Part1: " + str(computePart1(rules, messages)))
        print("Part2: " + str(computePart2(rules, messages)))