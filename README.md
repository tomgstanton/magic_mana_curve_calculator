# MANA CURVE CALCULATOR

## Driving Question

Assume the following:
The starting deck consists of land cards and nonland cards.
In order to play nonland cards you need to pay a specified amount of mana. (Referred to as the mana value.)
Land cards produce one mana each per turn. (They can be used again on future turns.)
You may play only one land card from your hand each turn.
Each turn you draw only one card.
Before the game begins you have 7 cards in hand already.

Question:
If you know the size of your starting deck and the number of land cards it contains, what should the distribution of mana values be across your nonland cards?

## Approach

I start by calculating the probabilities of having drawn 1 land card by the end of turn 1, having drawn 2 land cards by the end of turn 2, and so on.

Hypergeometic distribution is preferred here over binomial distribution as the total population changes on each draw, rather than remaining fixed.

-Probability Mass Function-

P(k) = (C(K,k) x C(N-K,n-k)) / C(N,n)

k = number of observed successes = number of desired land cards drawn
K = number of successes in the population = number of land cards in starting deck
N = number of the population = number of all cards in starting deck
n = number of draws from the population = number of cards drawn
C(a,b) = a Choose b = the number of combinations of choosing a b number of elements from a group of size a

For each turn, I input the turn number itself (n) as the number of desired land cards drawn, and the number of total cards drawn will be the turn number (n) plus the number of cards in the starting hand before the game began (n+7).

On turn 1 though, it doesn't matter that we have drawn exactly 1 land card, we want to have drawn at least 1 land card. So for turn 1, I check the probabilities of having drawn 1, 2, 3, 4, 5, 6, 7, and 8 land cards and sum those probabilities together. And then the same consideration is brought to calculating turn 2, and then turn 3, and so on.

This front-loads the distribution, with having 1 land card played by the end of turn 1 more likely than having 2 land cards played by the end of turn 2, and so on. This is as expected. If nonland cards were equally effective when played irrespective of their mana value, then you would opt for nonland cards that had a mana value of 1 over nonlands cards that had a mana value of 2.

However, there is (generally) a relationship between a nonland card's effectiveness and its mana value. Nonland cards with higher mana values tend to "do more" than cards with lower mana values. The exact nature of this relationship is far from clear, and I have made a choice as to an approximation of that relationship.

-Effectiveness Weighting-

x' = x^(log(n)+1)

x = hypergeometric probability
n = turn number

For turn 1 the power that the value is raised to is the power of 1 (remaining the same). For turn 2 the power the value is raised to is 1.301... (growing somewhat). For turn 3 the power the value is raised to is 1.477... (growing somewhat faster).

The resulting values are taken to demonstrate the distribution of mana values across the nonland cards. Everything is scaled so that the sum total of all the figures will equal the number of nonland cards in the starting deck.

## Observations

By keeping the total number of cards in the starting deck fixed, and playing around with the number of land cards the below results can be seen.

- A lower proportion of land cards results in a distribution that favours nonland cards of a lower mana value.
- A higher proportion of land cards results in a distribution that favours nonland cards of a higher mana value.

## Notes

Deck sizes in the game tend to be in the 40-100 range, although there is technically no restriction on how large a deck can be. The desire to be able to play as efficiently as possible is what encourages players not to be greedy in their deck-building.

run.py only shows results where the value rounded to 1 decimal place does not equal 0.0. The values for all the turns will have been calculated, even if they are absent from display.

