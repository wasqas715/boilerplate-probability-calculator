import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):   #Loops over list elements v times
        self.contents = []          #Empty list for list of balls
        for k, v in colors.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, amount):
        removed = []                # Empty list for balls removed from group
        if amount > len(self.contents): # Picking n+x from n gives all of n
             removed = self.contents
        for i in range(amount):
            # range over int here, range takes one arg
            # Pick ball at random from contents, add to removed, and pops it 
            # from contents - repeats for len(amount) times
                random_ball = random.randrange(len(self.contents))
                removed.append(self.contents[random_ball])
                self.contents.pop(random_ball)
        return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = 0
    # odds of picking n from n == 100%
    if num_balls_drawn >= len(hat.contents):
        return 1.0

    for j in range(1, num_experiments): #Loop num_exp times to get estimated ratio
        counter = 0
        ex_hat = copy.deepcopy(hat)     # makes a new list from hat elements
        test_case = ex_hat.draw(num_balls_drawn)    #Draws num_balls from ex_hat
        for i in set(test_case):        # Looping over colors that were removed
            if expected_balls.get(i) is not None:   
                # This is needed as it would break if ball isnt in expected
                if test_case.count(i) >= expected_balls.get(i): 
                    # if there are at least the expected amount of color, add to counter
                    counter += 1
        if counter == len(expected_balls): # If test_case has all the expected balls
            expected = expected + 1
    return (float(expected) / float(num_experiments))