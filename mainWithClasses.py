from itertools import takewhile, dropwhile
import sys

"""
Example input:

Enter max value: 300                       
Enter rules wanted (subset of {3, 5, 7, 11, 13, 17}):3 5 7 11 13 17            
Would you like a new rule? Enter 'No' to finish, or a rule of the form (Trigger, Word, Delete above, Before, Reverse): 19 Guzz False ? False     
Would you like a new rule? Enter 'No' to finish, or a rule of the form (Trigger, Word, Delete above, Before, Reverse): No   
"""

class Rule:
    def __init__(self, trigger, active, word, deleteAbove, before, reverse):
        self.trigger = trigger
        self.active = active
        self.word = word
        self.deleteAbove = deleteAbove
        self.before = before
        self.reverse = reverse

    def __str__(self):
        output = str(self.trigger) + " " + str(self.active) + " " + str(self.word) + " " + str(self.deleteAbove) + " " + str(self.before) + " " + str(self.reverse) + " "
        return output

# (Trigger, Active, Word, Delete above, Before, Reverse)
# Rules begin inactive until user specifies they want them
rules = [
    Rule(3, False, "Fizz", False, "?", False),
    Rule(5, False, "Buzz", False, "?", False),
    Rule(7, False, "Bang", False, "?", False),
    Rule(11, False, "Bong", True, "?", False),
    Rule(13, False, "Fezz", False, "B", False),
    Rule(17, False, "", False, "?", True)
]

def outputString(n):
    output = []
    # Rules applied in sequential order of list - fixing an order removes ambiguity
    for rule in filter(lambda x: x.active, rules):
        # Trigger
        if n % rule.trigger == 0:
            # Undo all previously applied rules
            if rule.deleteAbove:
                output = []

            # Place word in correct location
            if(rule.before != "?"):
                # Find the first occurence of the desired starting letter and place before
                output = (list(takewhile(lambda x: x[0] != rule.before, output))) + [rule.word] + (list(dropwhile(lambda x: x[0] != rule.before, output)))
            else:
                # Check a word needs to be added
                if rule.word != "":
                    output.append(rule.word)

            # Reverse current string
            if rule.reverse:
                output.reverse()

    # Add number if no rules applicable
    if output == []:
        output = str(n)
    else:
        output = "".join(output)

    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max = int(input("Enter max value: "))

    rulesWanted = input("Enter rules wanted (subset of {3, 5, 7, 11, 13, 17}): ")
    rulesWantedList = rulesWanted.split(" ")

    # Activate appropriate rules
    for j in range(0, len(rulesWantedList)):
        for rule in range(0, len(rules)):
            if int(rulesWantedList[j]) == rules[rule].trigger:
                rules[rule].active = True

    # Accept new rules from user
    finished = False
    while(not finished):
        newRule = input("Would you like a new rule? Enter 'No' to finish, or a rule of the form (Trigger, Word, Delete above, Before, Reverse): ")
        if(newRule == "No"):
            finished = True
        else:
            newRuleSplit = newRule.split(" ")
            # If syntactically correct input create new rule
            if(len(newRuleSplit) == 5):
                nextRule = Rule(int(newRuleSplit[0]), True, newRuleSplit[1], bool(newRuleSplit[2]), newRuleSplit[3], bool(newRuleSplit[4]))
                rules = rules + [nextRule]
            else:
                print("Invalid input, please try again")

    for i in range(0, max):
       print(outputString(i))