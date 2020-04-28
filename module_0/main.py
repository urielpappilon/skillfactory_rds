#!/usr/bin/env python3
import core
from score import score_game


def main():
    score_game(core.game_core_v1, iterations=1000, seed=1)
    score_game(core.game_core_v2, iterations=1000, seed=1)
    score_game(core.game_core_v3, iterations=1000, seed=1)


if __name__ == '__main__':
    main()
