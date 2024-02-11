import math

class Assumptions():
    def __init__(self,):
        self.hand_size = 7

class Values():
    def __init__(self,):
        self.number_of_land_cards = 0
        self.number_of_all_cards = 0
        self.number_of_nonland_cards = 0
        self.results = []

starting = Assumptions()
logged = Values()

def ManaCurveCalculator(number_of_land_cards,number_of_all_cards):
    logged.number_of_land_cards = number_of_land_cards
    logged.number_of_all_cards = number_of_all_cards
    logged.number_of_nonland_cards = logged.number_of_all_cards -logged.number_of_land_cards
    CheckInputs()
    RunHypergeometricCalculations()
    RaiseToPowerOfLogarithmicScale()
    AdjustToNumberOfNonLandCards()

def CheckInputs():
    if isinstance(logged.number_of_land_cards, int) == False or isinstance(logged.number_of_all_cards, int) == False:
        raise Exception('You need to ensure that your inputs are integers')
    if logged.number_of_all_cards < starting.hand_size:
        raise Exception('You need more total cards in your starting deck than the number of cards in your starting hand.')
    if logged.number_of_all_cards < logged.number_of_land_cards:
        raise Exception('Your starting deck cannot have a number of land cards in it greater than the number of cards in your starting deck.')

def RunHypergeometricCalculations():
    index_of_turn_being_considered = 0
    while index_of_turn_being_considered != logged.number_of_all_cards -starting.hand_size:
        logged.results.append(AssessSeenCards(index_of_turn_being_considered))
        index_of_turn_being_considered += 1

def AssessSeenCards(index_of_turn_being_considered):
    result = 0
    number_of_seen_cards = starting.hand_size +index_of_turn_being_considered +1
    for index in range(index_of_turn_being_considered,number_of_seen_cards):
        result += CalculateHypergeometricSuccesses(number_of_seen_cards,index)
    return result

def CalculateHypergeometricSuccesses(number_of_seen_cards,number_of_desired_land_cards):
    number_of_excess_seen_cards = number_of_seen_cards -number_of_desired_land_cards
    return (math.comb(logged.number_of_land_cards,number_of_desired_land_cards +1)*math.comb(logged.number_of_nonland_cards,number_of_excess_seen_cards))/math.comb(logged.number_of_all_cards,number_of_seen_cards)

def RaiseToPowerOfLogarithmicScale():
    for index in range(starting.hand_size):
        logged.results[index] = logged.results[index] **(math.log(index+1)+1)

def AdjustToNumberOfNonLandCards():
    denominator = sum(logged.results)
    for index in range(len(logged.results)):
        logged.results[index] = round(logged.results[index] *logged.number_of_nonland_cards /denominator,7)
