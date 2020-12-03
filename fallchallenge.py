import sys
import math


class Player:
    def __init__(self):
        self.tab_players = [my_inv_0, my_inv_1, my_inv_2, my_inv_3]
        self.inventaire = my_inv_0 + my_inv_1 + my_inv_2 + my_inv_3
        # self TODO


class Action(Player):
    def __init__(self):
        self.tab_actions = actions
        self.tab_potions = []
        self.tab_cast_learn = []
        self.tab_cast = []
        self.meilleur_potion = 0
        # Création de mon tableau de Potion
        for i in range(5):
            self.tab_potions.append(
                (
                    self.tab_actions[i][0],
                    self.tab_actions[i][1],
                    self.tab_actions[i][2],
                    self.tab_actions[i][3],
                    self.tab_actions[i][4],
                    self.tab_actions[i][5],
                    self.tab_actions[i][6],
                )
            )
        # Création de mon tableau de Recette
        for i in range(5, 11):
            self.tab_cast_learn.append(
                (
                    self.tab_actions[i][1],
                    self.tab_actions[i][2],
                    self.tab_actions[i][3],
                    self.tab_actions[i][4],
                    self.tab_actions[i][5],
                    self.tab_actions[i][6],
                    self.tab_actions[i][9],
                    self.tab_actions[i][10],
                )
            )
        # Création de mon tableau de Sort
        for i in range(11, 15):
            self.tab_cast.append(
                (
                    self.tab_actions[i][1],
                    self.tab_actions[i][2],
                    self.tab_actions[i][3],
                    self.tab_actions[i][4],
                    self.tab_actions[i][5],
                    self.tab_actions[i][6],
                    self.tab_actions[i][9],
                    self.tab_actions[i][10],
                )
            )
        # self TODO

    def best_potion(self):
        self.tab_potions.sort(reverse=True)
        self.id_meilleur_potion = self.tab_potions[0][1]
        self.nb_ingredient = abs(
            self.tab_potions[0][2]
            + self.tab_potions[0][3]
            + self.tab_potions[0][4]
            + self.tab_potions[0][5]
        )

    def potion(self, var):
        super().__init__()
        if self.tab_players[0] < self.nb_ingredient and var == 1:
            if self.tab_cast[0][6] == True:
                print("CAST " + str(self.tab_cast[0][0]))
                if (
                    self.tab_players[0] == self.nb_ingredient
                    or self.tab_players[0] > self.nb_ingredient
                ):
                    var = 0
            else:
                print("REST")
        # Si pas autant de jaune que la potion faire les jaunes
        elif self.tab_players[3] != abs(self.tab_potions[0][5]) and self.tab_players[
            3
        ] < abs(self.tab_potions[0][5]):
            if self.tab_cast[0][6] == True:
                print("CAST " + str(self.tab_cast[0][0]))
            elif self.tab_cast[1][6] == True:
                print("CAST " + str(self.tab_cast[1][0]))
            elif self.tab_cast[2][6] == True:
                print("CAST " + str(self.tab_cast[2][0]))
            elif self.tab_cast[3][6] == True:
                print("CAST " + str(self.tab_cast[3][0]))
            else:
                print("REST")
        # Si pas autant de orange que la potion faire les oranges
        elif self.tab_players[2] != abs(self.tab_potions[0][4]) and self.tab_players[
            2
        ] < abs(self.tab_potions[0][4]):
            # if (self.tab_cast[0][6] == True):
            #     print("CAST " + str(self.tab_cast[0][0]))
            if self.tab_cast[1][6] == True:
                print("CAST " + str(self.tab_cast[1][0]))
            elif self.tab_cast[2][6] == True:
                print("CAST " + str(self.tab_cast[2][0]))
            else:
                print("REST")
        # Si pas autant de vert que la potion faire les vert
        elif self.tab_players[1] != abs(self.tab_potions[0][3]) and self.tab_players[
            1
        ] < abs(self.tab_potions[0][3]):
            # if (self.tab_cast[0][6] == True):
            #     print("CAST " + str(self.tab_cast[0][0]))
            if self.tab_cast[1][6] == True:
                print("CAST " + str(self.tab_cast[1][0]))
            else:
                print("REST")
        # elif (self.tab_players[0] != abs(self.tab_potions[0][2]) and self.tab_players[0] < abs(self.tab_potions[0][2])):
        #     if (self.tab_cast[0][6] == True):
        #         print("CAST " + str(self.tab_cast[0][0]))
        #     else:
        #         print("REST")
        else:
            var = 1
            print("BREW " + str(self.id_meilleur_potion))


actions = []
players = []
var = 1
# game loop
while True:
    players = []
    actions = []
    action_count = int(input())  # the number of spells and recipes in play
    for i in range(action_count):
        (
            action_id,
            action_type,
            delta_0,
            delta_1,
            delta_2,
            delta_3,
            price,
            tome_index,
            tax_count,
            castable,
            repeatable,
        ) = input().split()
        action_id = int(action_id)
        delta_0 = int(delta_0)
        delta_1 = int(delta_1)
        delta_2 = int(delta_2)
        delta_3 = int(delta_3)
        price = int(price)
        tome_index = int(tome_index)
        tax_count = int(tax_count)
        castable = castable != "0"
        repeatable = repeatable != "0"
        actions.append(
            (
                price,
                action_id,
                delta_0,
                delta_1,
                delta_2,
                delta_3,
                action_type,
                tome_index,
                tax_count,
                castable,
                repeatable,
            )
        )
    for i in range(2):
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]
        if i == 0:
            my_inv_0 = inv_0
            my_inv_1 = inv_1
            my_inv_2 = inv_2
            my_inv_3 = inv_3
    player = Player()
    action = Action()
    action.best_potion()
    action.potion(var)
    # action.action_potion()
    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    print(str(action.tab_players[0]), file=sys.stderr, flush=True)
    print(str(action.nb_ingredient), file=sys.stderr, flush=True)
    print(str(action.tab_potions[0]), file=sys.stderr, flush=True)
    print(str(action.tab_players), file=sys.stderr, flush=True)
    print(str(action.meilleur_potion), file=sys.stderr, flush=True)
