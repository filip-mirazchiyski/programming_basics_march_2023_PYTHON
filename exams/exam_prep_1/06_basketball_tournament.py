number_of_wins = 0
number_of_loses = 0
number_of_matches = 0

while True:

    name_of_tournament = input()

    if name_of_tournament == "End of tournaments":
        print(f"{(number_of_wins / number_of_matches) * 100:.2f}% matches win")
        print(f"{(number_of_loses / number_of_matches) * 100:.2f}% matches lost")

    number_of_games = int(input())

    for game_number in range (1, number_of_games + 1):
        desi_team_points = int(input())
        other_team_points = int(input())
        number_of_matches += 1
        diff_between_points = abs(desi_team_points - other_team_points)

        if desi_team_points > other_team_points:
            number_of_wins += 1
            print(f"Game {game_number} of tournament {name_of_tournament}: win with {diff_between_points}")
        else:
            number_of_loses += 1
            print(f"Game {game_number} of tournament {name_of_tournament}: lost with {diff_between_points}")
