# Itzel Munoz Monroy PSID: 1888446

team_roster = {}

for x in range(1, 6):
    number = input("Enter player {}'s jersey number:\n".format(x))
    rating = input("Enter player {}'s rating:\n".format(x))
    team_roster[number] = rating
    print("")

list_players = []
for key in team_roster.keys():
    list_players.append(int(key))
list_players.sort()

print("ROSTER")
for player in list_players:
    print("Jersey number: {}, Rating: {}".format(player, team_roster[str(player)]))

def edit_roster(roster):
    print("")
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("")
    commands = ["a", "d", "u", "r", "o"]
    command = ""
    while command != "q":
        command = input("Choose an option:")
        print("")
        if command == "a":
            n_number = input("Enter a new player jersey number:\n")
            n_rating = input("Enter player's rating:\n")
            roster[n_number] = n_rating
            print("")
            list_players = []
            for num in team_roster.keys():
                list_players.append(int(num))
            list_players.sort()

        elif command == "d":
            num_del = input("Enter a jersey number:\n")
            del roster[num_del]

        elif command == "u":
            num_up = input("Enter a jersey number:\n")
            rate_up = input("Enter a new rating for player:\n")
            roster[num_up] = rate_up

        elif command == "r":
            s_rate = input("Enter a rating:\n")
            print("")
            print("ABOVE", s_rate)
            list_players = []
            for num in team_roster.keys():
                list_players.append(int(num))
            list_players.sort()
            for person in list_players:
                if team_roster[str(person)] > s_rate:
                    print("Jersey number: {}, Rating: {}".format(person, team_roster[str(person)]))

        elif command == "o":
            print("ROSTER")
            list_players = []
            for num in team_roster.keys():
                list_players.append(int(num))
            list_players.sort()
            for person in list_players:
                print("Jersey number: {}, Rating: {}".format(person, team_roster[str(person)]))

        if command in commands:
            print("")
            print("MENU")
            print("a - Add player")
            print("d - Remove player")
            print("u - Update player rating")
            print("r - Output players above a rating")
            print("o - Output roster")
            print("q - Quit")
            print("")

edit_roster(team_roster)
