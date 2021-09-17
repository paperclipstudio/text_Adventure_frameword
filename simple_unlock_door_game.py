from typing import Dict
from Option import Option
from Page import Page
from Book import Book
import actions as act
import predicates as pred
import random


# This is an example preidicate takes in a state and returns true or false
def is_dark(state: Dict[str, int]) -> bool:
    return (state["time"] % 4 <= 1)

# These are options that you can choose to do
take_key = Option(
    "Take the key from the floor", # The text that is shown on the button
    act.gain("key", 1),             # What changes to the state
    pred.all([                          # this is the checks that all of the following are true
        pred.has_not_got("key"),            # Doesn't current have a key
        pred.inverse(is_dark)        # Isn't currently Dark
    ])
)

unlock_door = Option(
    "Unlock the door with the key",
    act.chain_actions([
        act.lose("key", 1), 
        act.goto_page(2)
    ]),
    pred.all([
        pred.has_more_than("key" , 0),
        is_dark
    ])
)

wait = Option(
    "Wait for something to happen",
    act.gain("time", 1),
    pred.always_valid
)

go_back = Option(
    "Go back out the foest",
    act.goto_page(0),
    pred.always_valid
)

follow_path = Option(
    "Follow down the path",
    act.goto_page(1),
    pred.always_valid
)


get_to_path:Page = Page()
get_to_path.set_text("You come to a forest with a dark path down the middle")
get_to_path.add_options([
    follow_path,
    wait
])

at_door:Page = Page()

# Example of creating text based on current state
# but in this case might be better to have two different Pages for night and day
# but also shows random text genration
# Would be nice if there was a system of auto replacment 
# e.g. "{Guard_name} does't think that £{money} is worth getting fired from his job"

def door_text(stats):
    text = ""
    if is_dark(stats):
        text += "Its dark You get to what looks like a crumbling tomb, There are some glowing patterns in the shape of a door on the rock."
    else:
        text += "You get to a old crumbling tomb, there is a large slab of sandstone blocking the entrance. You see there is a key on the ground"

    if (random.randint(1,3) == 1):
        text += "\nA rabbit scuttles into a bush"    
    else :
        text += "\nNot much else to see here"
    return text

at_door.set_text_gen(door_text)

at_door.add_options([
    wait,
    unlock_door,
    take_key,
    go_back
])

open_door:Page = Page()
open_door.set_text("Inside is the jewel of text adventure\nYOU WIN")


# Binding the book
this_book = Book()

this_book.set_pages([
    get_to_path,
    at_door,
    open_door
])

this_book.stats["key"] = 0
this_book.stats["time"] = 1

def get_book()-> Book:
    return this_book

