# game status variables

player_score = 0

def update_player_score(points):
    global player_score
    player_score += points

def get_player_score():
    return player_score

def reset_player_score():
    global player_score
    player_score = 0

