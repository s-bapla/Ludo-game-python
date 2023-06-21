# Author: Simran Bapla
# GitHub username: baplas
# Date: August 11, 2022
# Description: Represents a version of the ludo game that can be played with 2-4 players. The Player class represents
#              a player playing the game, and the LudoGame class represents the game as played.
#              The class contains information about the players playing. And the players themselves contain information
#              about the board, its position, and its tokens

class Player:
    """
    Represents a player playing the Ludo game. Each player has a position; a start and end space; current position of
    the player’s two tokens: in the home yard, ready to go, somewhere on the board, or has finished; the total step
    count of both p and q tokens; the current state of the player: whether the player has won and finished the game,
    or is still playing; and a boolean value of whether the tokens are stacked
    """

    def __init__(self, position):
        self._position = position

        if position == 'A':
            self._start_space = '1'
            self._end_space = '50'
        elif position == 'B':
            self._start_space = '15'
            self._end_space = '8'
        elif position == 'C':
            self._start_space = '29'
            self._end_space = '22'
        else:
            self._start_space = '43'
            self._end_space = '36'

        self._current_space_p = 'H'
        self._current_space_q = 'H'

        self._total_steps_p = -1
        self._total_steps_q = -1

        self._has_player_won = False

        self._is_stacked = False

    def get_position(self):
        """returns the position of the Player"""
        return self._position

    def get_completed(self):
        """returns True or False if the player has finished or not finished the game"""
        return self._has_player_won

    def get_token_p_step_count(self):
        """returns the total steps that token p has taken on the board. Steps = -1 for home yard position and steps = 0
         for ready to go position"""
        return self._total_steps_p

    def get_token_q_step_count(self):
        """returns the total steps that token q has taken on the board. Steps = -1 for home yard position and steps = 0
         for ready to go position. Every time a player’s token q moves the step count gets increased or decreased."""
        return self._total_steps_q

    def get_space_name(self, total_steps):
        """takes the parameter of the total steps of the token and returns the name of the space the token has landed on
         on the board as a string. “H” will be returned for home and “R” will be returned as ready to go as well as
          “X1”,”X2”,...,”E”. If the total_steps_p(q) attribute is between 1-50 then a string with the tile number will
           be returned"""

        if self._position == 'A':
            if total_steps == -1:
                return 'H'
            elif total_steps == 0:
                return 'R'
            elif total_steps >= 1 and total_steps <= 50:
                return str(total_steps)
            elif total_steps <= 56:
                return 'A' + str(total_steps - 50)
            else:
                return 'E'

        if self._position == 'B':
            if total_steps == -1:
                return 'H'
            elif total_steps == 0:
                return 'R'
            elif total_steps >= 1 and total_steps <= 42:
                return str(total_steps + int(self._start_space) - 1)
            elif total_steps > 42 and total_steps <= 50:
                return str(total_steps % 42)
            elif total_steps <= 56:
                return 'B' + str(total_steps - 50)
            else:
                return 'E'

        if self._position == 'C':
            if total_steps == -1:
                return 'H'
            elif total_steps == 0:
                return 'R'
            elif total_steps >= 1 and total_steps <= 28:
                return str(total_steps + int(self._start_space) - 1)
            elif total_steps > 28 and total_steps <= 50:
                return str(total_steps % 28)
            elif total_steps <= 56:
                return 'C' + str(total_steps - 50)
            else:
                return 'E'

        if self._position == 'D':
            if total_steps == -1:
                return 'H'
            elif total_steps == 0:
                return 'R'
            elif total_steps >= 1 and total_steps <= 14:
                return str(total_steps + int(self._start_space) - 1)
            elif total_steps > 14 and total_steps <= 27:
                return str(total_steps % 14)
            elif total_steps > 27 and total_steps <= 41:
                return str(total_steps % 14 + 14)
            elif total_steps > 41 and total_steps <= 50:
                return str(total_steps % 14 + 28)
            elif total_steps <= 56:
                return 'D' + str(total_steps - 50)
            else:
                return 'E'

    def token_stack_trigger(self):
        """will set the stack attribute to True for the Player"""

        self._is_stacked = True

        return

    def update_steps(self, turn):
        """The turn parameter is a tuple that represents a turn for the player. For example, (‘p’, 4) represents a turn
         where the player rolls a 4 on the dice and intends to move the p token. The method then updates the the
          player’s p token’s total_steps_p attribute by moving it 4 steps forward. The method also moves tokens as a
          stack if stack attribute is True. It also sets the _current_space_p/q and _has_player_won attributes."""

        if self._is_stacked:
            self._total_steps_p += turn[1]
            # if in home squares and rolls higher than 57
            if self._total_steps_p > 57:
                temp_var = self._total_steps_p - 57
                self._total_steps_p = 57 - temp_var
            self._current_space_p = self.get_space_name(self._total_steps_p)
            self._total_steps_q += turn[1]
            # if in home squares and rolls higher than 57
            if self._total_steps_q > 57:
                temp_var = self._total_steps_q - 57
                self._total_steps_q = 57 - temp_var
            self._current_space_q = self.get_space_name(self._total_steps_q)
            return

        if turn[0] == 'p':
            self._total_steps_p += turn[1]
            # if in home squares and rolls higher than 57
            if self._total_steps_p > 57:
                temp_var = self._total_steps_p - 57
                self._total_steps_p = 57 - temp_var
            self._current_space_p = self.get_space_name(self._total_steps_p)
        else:
            self._total_steps_q += turn[1]
            # if in home squares and rolls higher than 57
            if self._total_steps_q > 57:
                temp_var = self._total_steps_q - 57
                self._total_steps_q = 57 - temp_var
            self._current_space_q = self.get_space_name(self._total_steps_q)
        # if player has won the game set attribute to True
        if self._total_steps_q == 57 and self._total_steps_p == 57:
            self._has_player_won = True

        return

    def reset_token(self, token):
        """resets given token 'p' or 'q' to homeyard space"""
        if token == 'p':
            self._total_steps_p = -1
            self._current_space_p = 'H'
            self._is_stacked = False
        if token == 'q':
            self._total_steps_q = -1
            self._current_space_q = 'H'
            self._is_stacked = False


class LudoGame:

    """The LudoGame object represents the game as played. The class contains information about the players playing. And
     the players themselves contain information about the board, its position, and its tokens"""

    def __init__(self):
        self._players = {}

    def get_player_by_position(self, player_position):
        """takes a parameter representing the player’s position as a string and returns the player object. Invalid
         string will be returned if player is not found. "Player not found!"  """

        for position in self._players:
            if player_position == position:
                return self._players[position]

        return "Player not found!"

    def move_token(self, player, token_name, steps):

        """takes three parameters, the player object, the token name (‘p’ or ‘q’) and the steps the player token will
         move on the board.  It will update the token’s total steps, and it will take care of removing other opponent
          tokens as needed. It will also be in charge of checking for stacking."""

        if token_name == 'p':
            player.update_steps(('p', steps))
            player_and_token_to_reset = self.check_players(player, token_name)
            if len(player_and_token_to_reset) != 0: # if there is a player and its token to reset
                self.reset_player(player_and_token_to_reset[0], player_and_token_to_reset[1])
                if len(player_and_token_to_reset) == 4:  # if stacked reset other token as well
                    self.reset_player(player_and_token_to_reset[2], player_and_token_to_reset[3])
            # if player's tokens are stacked trigger stack attribute to True
            if player.get_token_p_step_count() == player.get_token_q_step_count() and player.get_token_p_step_count() != 0 and player.get_token_p_step_count() != -1:
                player.token_stack_trigger()
        else:
            player.update_steps(('q', steps))
            player_and_token_to_reset = self.check_players(player, token_name)
            if len(player_and_token_to_reset) != 0: # if there is a player and its token to reset
                self.reset_player(player_and_token_to_reset[0], player_and_token_to_reset[1])
                if len(player_and_token_to_reset) == 4:  # if stacked reset other token as well
                    self.reset_player(player_and_token_to_reset[2], player_and_token_to_reset[3])
            # if player's tokens are stacked trigger stack attribute to True
            if player.get_token_p_step_count() == player.get_token_q_step_count() and player.get_token_q_step_count() != 0 and player.get_token_q_step_count() != -1:
                player.token_stack_trigger()


    def play_game(self, players, turns):
        """Takes two parameters, a list of positions players choose, like [‘A’, ‘C’] means two players will play the
         game at position A and C, and a turns list. The turns list is a list of tuples with each tuple representing a
          roll for one player. For example, [('A', 6), ('A', 4), ('C', 5)] means player A rolls 6, then rolls 4, and
           player C rolls 5. This method will add player objects to the player dictionary attribute of this class
            corresponding to the players list parameter. It will then move the tokens using a for loop iterating
             through the turns list following the priority rules and update the tokens position and the players game
             states. the method will return a list of strings representing the current spaces of all of the tokens for
              each player in the list after moving the tokens"""
        result = []
        # add to all players to players attribute
        for position in players:
            self._players[position] = Player(position)

        for turn in turns:
            # if player has already won skip turn
            if self._players[turn[0]].get_token_p_step_count() == 57 and self._players[turn[0]].get_token_q_step_count() == 57:
                continue
            # if both tokens are in homeyard
            if self._players[turn[0]].get_token_p_step_count() == -1 and self._players[turn[0]].get_token_q_step_count() == -1:
                # if rolled a 6, move token p to ready position
                if turn[1] == 6:
                    self.move_token(self._players[turn[0]], 'p', 1)
                continue
            # if token p has finished and token q is not in homeyard, move token q
            if self._players[turn[0]].get_token_p_step_count() == 57 and self._players[turn[0]].get_token_q_step_count() >= 0:
                self.move_token(self._players[turn[0]], 'q', turn[1])
                continue
            # if token q has finished and token p is not in homeyard, move token p
            if self._players[turn[0]].get_token_q_step_count() == 57 and self._players[turn[0]].get_token_p_step_count() >= 0:
                self.move_token(self._players[turn[0]], 'p', turn[1])
                continue
            # if token q is in homeyard and token p is not in homeyard move token p
            if self._players[turn[0]].get_token_q_step_count() == -1 and self._players[turn[0]].get_token_p_step_count() >= 0:
                if turn[1] == 6:
                    self.move_token(self._players[turn[0]], 'q', 1)
                else:
                    self.move_token(self._players[turn[0]], 'p', turn[1])
                continue
            # if token p is in homeyard and token q is not in homeyard move token p
            if self._players[turn[0]].get_token_p_step_count() == -1 and self._players[turn[0]].get_token_q_step_count() >= 0:
                if turn[1] == 6:
                    self.move_token(self._players[turn[0]], 'p', 1)
                else:
                    self.move_token(self._players[turn[0]], 'q', turn[1])
                continue
            # if token p can enter 'E' after moving, move token p
            if self._players[turn[0]].get_token_p_step_count() + turn[1] == 57:
                self.move_token(self._players[turn[0]], 'p', turn[1])
                continue
            # if token q can enter 'E' after moving, move token p
            if self._players[turn[0]].get_token_q_step_count() + turn[1] == 57:
                self.move_token(self._players[turn[0]], 'q', turn[1])
                continue
            # if token p can kick out another player's token after moving, move token p
            if self.can_kick_out(self._players[turn[0]], turn[1]) == 'p':
                self.move_token(self._players[turn[0]], 'p', turn[1])
                continue
            # if token q can kick out another player's token after moving, move token q
            if self.can_kick_out(self._players[turn[0]], turn[1]) == 'q':
                self.move_token(self._players[turn[0]], 'q', turn[1])
                continue
            # if token q is ahead of token p move token p; if they are stacked it will move both of them
            if self._players[turn[0]].get_token_q_step_count() >= self._players[turn[0]].get_token_p_step_count():
                self.move_token(self._players[turn[0]], 'p', turn[1])
                continue
            # if token q is ahead of token p move token q; if they are stacked it will move both of them
            if self._players[turn[0]].get_token_q_step_count() <= self._players[turn[0]].get_token_p_step_count():
                self.move_token(self._players[turn[0]], 'q', turn[1])
                continue
        # make list of all token's spaces/positions
        for position in self._players:
            result.append(self._players[position].get_space_name(self._players[position].get_token_p_step_count()))
            result.append(self._players[position].get_space_name(self._players[position].get_token_q_step_count()))

        return result

    def can_kick_out(self, player, steps):
        """determines whether the player object passed as a parameter can kick out another players token back to its homeyard after moving
         "steps" parameter forward. If it can, it will return the player parameters token name that can kick another
          players token out. If it cant kick out any tokens it will return zero."""
        result = 0
        for position in self._players:
            if position != player.get_position():
                if self._players[position].get_space_name(self._players[position].get_token_p_step_count()) == player.get_space_name(player.get_token_p_step_count() + steps):
                    result = 'p'
                elif self._players[position].get_space_name(self._players[position].get_token_q_step_count()) == player.get_space_name(player.get_token_p_step_count() + steps):
                    result = 'p'
                elif self._players[position].get_space_name(self._players[position].get_token_p_step_count()) == player.get_space_name(player.get_token_q_step_count() + steps):
                    result = 'q'
                elif self._players[position].get_space_name(self._players[position].get_token_q_step_count()) == player.get_space_name(player.get_token_q_step_count() + steps):
                    result = 'q'
                else:
                    continue
        return result


    def check_players(self, player, token_name):
        """determines whether the player parameter and it's token: token_name has landed on top of another player's token.
           If it has landed on another players token it will return a list with the first element being the player it has landed on
           and the second element being the token name 'p' or 'q' it has landed on. if it lands on a stacked token, it will return
           a list of 4 elements, [player, 'p', player, 'q']. if the player has not landed on any other player's tokens
           it will return an empty list"""

        result = []
        if token_name == 'p':
            if player.get_token_p_step_count() == -1 or player.get_token_p_step_count() == 0:
                return result
            for position in self._players:
                if position != player.get_position():
                    if self._players[position].get_space_name(self._players[position].get_token_p_step_count()) == player.get_space_name(player.get_token_p_step_count()):
                        result.append(self._players[position])
                        result.append('p')
                    if self._players[position].get_space_name(self._players[position].get_token_q_step_count()) == player.get_space_name(player.get_token_p_step_count()):
                        result.append(self._players[position])
                        result.append('q')
        if token_name == 'q':
            if player.get_token_q_step_count() == -1 or player.get_token_q_step_count() == 0:
                return result
            for position in self._players:
                if position != player.get_position():
                    if self._players[position].get_space_name(self._players[position].get_token_p_step_count()) == player.get_space_name(player.get_token_q_step_count()):
                        result.append(self._players[position])
                        result.append('p')
                    if self._players[position].get_space_name(self._players[position].get_token_q_step_count()) == player.get_space_name(player.get_token_q_step_count()):
                        result.append(self._players[position])
                        result.append('q')

        return result

    def reset_player(self, player, token):
        """resets the player parameter's token: token to the homeyard"""
        player.reset_token(token)
        return




