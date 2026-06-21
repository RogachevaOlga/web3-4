import random


class Battle:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    @staticmethod
    def _alive(team):
        return [c for c in team if c.is_alive]

    def _team_turn(self, attackers, defenders):
        for attacker in attackers:
            if not attacker.is_alive:
                continue
            alive_defenders = self._alive(defenders)
            if not alive_defenders:
                return
            attacker.attack(random.choice(alive_defenders))

    def run(self):
        round_num = 1
        while self._alive(self.team_a) and self._alive(self.team_b):
            print(f"\n--- Раунд {round_num} ---")
            self._team_turn(self.team_a, self.team_b)
            self._team_turn(self.team_b, self.team_a)
            round_num += 1

        if self._alive(self.team_a):
            print("\nПобедила команда A!")
        else:
            print("\nПобедила команда B!")
