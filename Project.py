#Q1:
from random import randint

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)


def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice

def pig_out(num_rolls,dice):
    score=0
    while num_rolls>0:
        a=dice()
        if a==1:
            score=a+score
        num_rolls-=1
    return score



def roll_dice(num_rolls, dice):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    score=0
    b=1
    score1=0
    while num_rolls>0:
        a=dice()
        score=a+score
        if a==1:
            score1=b
            b+=1
        num_rolls-=1
    if score1>0:
        score=score1
    return score



#Q2:

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    a,b=opponent_score%10,opponent_score//10
    maximum=max(a,b)
    current_players_score=maximum+1
    return current_players_score
def factor(opponent_score):
    n=1
    factors=1
    while n<opponent_score:
        if opponent_score%n==0:
          factors+=1
        n+=1
    return factors
def is_prime(opponent_score):
    if opponent_score==1:
        return False
    f=factor(opponent_score)
    if f==2:
        return True
    else:
        return False
def hogtimus_prime(opponent_score):
    if not is_prime(opponent_score):
        return opponent_score
    if is_prime(opponent_score):
        opponent_score+=1
    while not is_prime(opponent_score):
        opponent_score+=1
    return opponent_score
def when_pigs_fly(opponent_score,num_rolls):
    opponent_score=25-num_rolls
    return opponent_score

def take_turn(num_rolls, opponent_score, dice=make_test_dice(5,4,3,2,1)):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    if num_rolls==0:
        opponent_score=free_bacon(opponent_score)
    opponent_score= hogtimus_prime(opponent_score)
    opponent_score= when_pigs_fly(opponent_score,num_rolls)
    return opponent_score

#Q3:

def reroll(dice):
    """Return dice that return even outcomes and re-roll odd outcomes of DICE."""
    def rerolled():
        reroll=dice()
        if reroll%2==0:
            return reroll
        else:
            return dice()
    return rerolled

#Q4:




def select_dice(score, opponent_score, dice_swapped):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).

    DICE_SWAPPED is True if and only if four-sided dice are being used.
    """
    if dice_swapped==True:
        dice=four_sided
    else:
        dice=six_sided
    if (score + opponent_score) % 7 == 0:
        dice = reroll(dice)
    return dice

