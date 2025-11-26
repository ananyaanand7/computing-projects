# Define initial cards for player and dealer
p_card_1 = 10  # Player's first card
p_card_2 = 5   # Player's second card
d_card_1 = 8   # Dealer's first card
d_card_2 = 7   # Dealer's second card

# Additional cards if player or dealer decides to hit
p_card_3 = 2   # Player's potential third card
d_card_3 = 3   # Dealer's potential third card

# Calculate starting scores
p_score = p_card_1 + p_card_2  # Initial player score
d_score = d_card_1 + d_card_2  # Initial dealer score

# Player decision: hit if score is below 16
if p_score < 16:
    p_score += p_card_3  # Add third card to player score

# Dealer decision: hit if score is below 17
if d_score < 17:
    d_score += d_card_3  # Add third card to dealer score

# Determine game outcome
if p_score > 21:
    # Player busts
    player_wins = False
elif d_score > 21 and p_score <= 21:
    # Dealer busts, player did not bust
    player_wins = True
elif d_score >= p_score:
    # Neither busts, dealer wins or ties
    player_wins = False
else:
    # Player has higher score, wins
    player_wins = True

# Output result for autograder
answer = player_wins
print(answer)
