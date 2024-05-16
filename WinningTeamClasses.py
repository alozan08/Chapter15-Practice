'''
    Complete the Team class implementation. For the instance method get_win_percentage(), the formula is:
    wins / (wins + losses). Note: Use floating-point division
    For instance method print_standing(), output the win % of the team with 2 digits after the decimal point and
    whether the team has a winning/losing average. A team has a winning average if the win % is >= 0.5
    ex:
        input:
            Ravens
            13
            3
        output:
            Win percentage: 0.81
            Congratulations, Team Ravens has a winning average!
'''
class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        win_percentage = (float(self.wins) / float((self.wins + self.losses)))
        return win_percentage

    def print_standing(self):
        win_percent = self.get_win_percentage()
        print(f'Win percentage: {win_percent:.2f}')
        if win_percent >= 0.5:
            print(f'Congratulations, Team {self.name} has a winning average!')
        else:
            print(f'Team {self.name} has a losing average.')


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()