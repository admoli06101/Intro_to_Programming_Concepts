class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition


class myTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

playerList = []
playerList.append(player1)
playerList.append(player2)
playerList.append(player3)
playerList.append(player4)

team = myTeam("The Thunderbolts", playerList)

print("Team Name:", team.teamName)

for player in team.players:
    print(player.playerName, "-", player.playerPosition)