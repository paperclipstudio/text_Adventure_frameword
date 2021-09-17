from typing import Dict

def chain_actions(actions:list):
    def chained_actions(state):
        for action in actions:
            state = action(state)
        return state
    return chained_actions

def gain(item, amount=1):
    def func(game_state:Dict)-> Dict:
        game_state.setdefault(item, 0)
        game_state[item] = game_state[item] + amount
        return game_state
    return func

def lose(item, amount=1):
    return gain(item, -amount)

def goto_page(id):
    def change_page(game_state:Dict) -> Dict:
        game_state["page"] = id
        return game_state
    return change_page