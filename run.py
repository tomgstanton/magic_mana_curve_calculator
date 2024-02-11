import calculator

number_of_all_cards = int(input('How many cards are in your starting deck? '))
number_of_land_cards = int(input('How many land cards are in your starting deck? '))
calculator.ManaCurveCalculator(number_of_land_cards,number_of_all_cards)
print('--calculations completed--')
for index in range(len(calculator.logged.results)):
    if round(calculator.logged.results[index],1) != 0.0:
        print('mana value',index+1,':',calculator.logged.results[index],':',round(calculator.logged.results[index]),'cards (approx)')