class WrongNumberOfPlayersError(Exception):
    '''Класс исключения при количестве игроков больше двух'''
    pass


class NoSuchStrategyError(Exception):
    '''Класс исключения при неправильном ходе игрока'''
    pass


def verify_number(args):
    """validation of players number"""
    if len(args) > 2:
        raise WrongNumberOfPlayersError


def verify_players_steps(args):
    """validation of players steps"""

    for el in args:
        if el[1] not in ['R', 'P', 'S']:
            raise NoSuchStrategyError


def rps_game_winner(*args):
    """RPS-game algorithm"""
    try:
        verify_number(args)
        verify_players_steps(args)
    except WrongNumberOfPlayersError as er:
        return er
    except NoSuchStrategyError as er:
        return er

    if args[0][1] == args[1][1]:
        return " ".join(map(str, (args[0][0], args[0][1])))  # case of equal player steps

    elif args[0][1] == 'R':
        if args[1][1] == 'S':  # Rock against Scissors
            return " ".join(map(str, (args[0][0], args[0][1])))
        else:
            return " ".join(map(str, (args[1][0], args[1][1])))  # Rock against Paper

    elif args[0][1] == 'S':
        if args[1][1] == 'P':
            return " ".join(map(str, (args[0][0], args[0][1])))  # Scissors against Paper
        else:
            return " ".join(map(str, (args[1][0], args[1][1])))  # Scissors against Rock

    elif args[0][1] == 'P':
        if args[1][1] == 'R':
            return " ".join(map(str, (args[0][0], args[0][1])))  # Paper against Rock
        else:
            return " ".join(map(str, (args[1][0], args[1][1])))  # Paper against Scissors

# TEST
#
# rps_game_winner(['player1', 'P'], ['player2', 'S'], ['player3', 'S'])
# rps_game_winner(['player1', 'P'], ['player2', 'A'])
# rps_game_winner(['player1', 'P'], ['player2', 'S'])
# rps_game_winner(['player1', 'P'], ['player2', 'P'])
