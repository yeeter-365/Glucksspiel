import time

def intovertext():

    intro_text = "Welcome to the Investment Banking Game!\nIn this competitive world of financial prowess, you and your friends will engage in a high-stakes investment challenge.\nEach of you will start with an initial sum of money and the goal is to be the first to reach a bank balance of 1,000,000.\nBut watch out! The market is unpredictable and you'll need to use your wits and strategic skills to outsmart your opponents.\nYou can use special abilities to gain an advantage, adapt your strategy to market changes, and rise to the top as the ultimate investor!\nGet ready to test your financial acumen and embark on this thrilling investment journey!"

    for char in intro_text:
        print(char, end='', flush=True)  # Use end='' to avoid newline after each character
        time.sleep(0.05)  # Adjust the time (in seconds) as needed for the delay
    
    input("\n( NEXX[>] )\n")



def menusatext():

    player_info = {}                                                            # Just avg player_info of the form {'Player1': ['John', 1, 1000, 'None', 'Normal']}
    Abilities = ["Double Down", "Shield", "Swap", "Jackpot", "Steal"]           # Just abilities

    while True:
        N_Players = input("How many players are cooking? ")         # No error input to enter the number of players
        if N_Players.isdigit():
            N_Players=int(N_Players); print(); break
        else:
            print("Please enter an integer number.")

    for iterate_players_in_player_info in range(N_Players):                                                         # Just entering the user names and abilities
        player_info["Player"+str(iterate_players_in_player_info+1)] = ['Name', 1, 1000, 'None', 'Normal',(1/N_Players)*100]
        Name = input("Player"+str(iterate_players_in_player_info+1)+" enter thy name. "); player_info["Player"+str(iterate_players_in_player_info+1)][0] = Name

    abilities_text = "Abilities are as follows:\n1. Double Down: Double your bet.\n2. Shield: Protect from loss.\n3. Swap: Exchange bets.\n4. Jackpot: Increase winnings.\n5. Steal: Take opponent's bet.\n\nRules: Thy have to obey them rules:\n1. Double Down: Use every 3 rounds. Wins double the bet.\n2. Shield: Activate before results to protect bet.\n3. Swap: Exchange bets with another player's agreement.\n4. Jackpot: Increases win by 50%, risk up by 25%.\n5. Steal: Use once every 5 rounds. Steals 25% of opponent's bet.\n\nChoose 1 2 3 4 5 respectively wisely!"

    for char in abilities_text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the time delay as needed

    for iterate_abilities_in_player_info in range(N_Players):
        while True:
            Ability = input("Player"+str(iterate_abilities_in_player_info+1)+" enter Ability. ")
            if Ability in "12345" and len(Ability) == 1:
                Ability=int(Ability); player_info["Player"+str(iterate_abilities_in_player_info+1)][3] = Abilities[Ability-1]; break
    
    list_lose_Probablity = [list(player_info.keys())]

    for iterate_probablity_in_player_info in range(N_Players):
        player_info["Player"+str(iterate_probablity_in_player_info+1)][5] = list_lose_Probablity.count("Player"+str(iterate_probablity_in_player_info+1))
