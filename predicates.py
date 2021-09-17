from typing import Dict
def has_more_than(item, amount):
        def predicate(state:Dict):
            state.setdefault(item, 0)
            return state[item] > amount
        return predicate

def has_less_than(item, amount):
    def predicate(state):
        return state[item] < amount
    return predicate

def has_not_got(item):
    return has_less_than(item, 1)

def all(predicates):
    def result(state):
        for predicate in predicates:
            if (not predicate(state)):
                return False
        return True
    return result

def inverse(predicate):
    return lambda state : not (predicate(state))


def always_valid(_):
    return True