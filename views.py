from flask import render_template
from route_helper import simple_route
import random

NUMBER_OF_PAGES=4 #constant

@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.
    :param world: The current world
    :return: The HTML to show the player
    """
    world['pages']=[{"template": "breakfast.html", "name": "breakfast"},
                       {"template": "songs.html", "name": "song selection"},
                       {"template": "dresses.html", "name": "dresses"},
                       {"template": "passtime.html", "name": "passing time"}]
    return render_template("header.html")+"""It’s your first day on the job and Beyoncé is getting ready for a red carpet! <br>
    <img src="/static/beyoncegif.gif" alt="beyonce sassy gif"><br><br>
    <a href="/next/"><button name="startButton">Start your day!</button><br>
    """

@simple_route('/next/')
def decide(world: dict) -> str:
    """
    Update the player location and encounter a decision, prompting the player
    to choose a picture.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    if len(world['pages'])==0:
        return render_template("won.html")
    else:
        next_world = random.choice(world['pages']) #randomly select the page they go to
        #progress bar at bottom of game
        progress=100-(100/NUMBER_OF_PAGES*len(world['pages']))
        value_now=str(int(progress))
        style="width: "+value_now+"%"

        world['pages'].remove(next_world)

        return render_template(next_world["template"], helping_with=next_world["name"])+render_template("progress_bar.html", now_value=value_now, style_value=style)


@simple_route('/chose/<what>/')
def chose(world: dict, what: str) -> str:
    """
     Determine whether the user chose right or wrong

     :param world: The current world
     :param where: The new location to move to
     :return: The HTML to show the player
     """
    world['user decision'] = what
    if world['user decision']=="wrong":
        return render_template("incorrect.html")
    if world['user decision']=="right":
        return render_template("correct.html")
