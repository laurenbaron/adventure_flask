from flask import render_template
from route_helper import simple_route
import random

GAME_HEADER = """
<h1>Be Beyoncé's assistant for a day! Don't get fired...</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""

unused_worlds=[{"template": "breakfast.html", "name": "breakfast"},
                       {"template": "songs.html", "name": "song selection"},
                       {"template": "dresses.html", "name": "dresses"},
                       {"template": "passtime.html", "name": "passing time"}]

re_add=[]

@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.
    :param world: The current world
    :return: The HTML to show the player
    """
    return GAME_HEADER+"""It’s your first day on the job and Beyoncé is getting ready for a red carpet! <br>
    <img src="/static/beyoncegif.gif" alt="beyonce sassy gif"><br><br>
    <a href="/next/"><button name="startButton">Start your day!</button><br>
    """

ENCOUNTER_DECISION = """
    <!-- Curly braces let us inject values into the string -->
    You are helping Beyoncé with {}. You must make a decision by clicking the picture you wish to bring to Beyoncé!<br><br>
    """

ENCOUNTER_WRONG = GAME_HEADER + """You have made the wrong decision for Beyoncé!!! She has her lawyers send you 
    termination letter :( <br><br>
            
    <embed name="run the world" src="/static/Beyoncé - Broken-Hearted Girl (Video).mp4"width="600" height="400" 
    loop="false" autostart="false"><br><br>

    <a href='/reset/'>Return to the start</a>
    """

ENCOUNTER_RIGHT= GAME_HEADER+"""Congrats you chose correctly! You live to survive another day as Beyoncé's assistant...
    <br><br>
        
    <embed name="run the world" src="/static/Beyoncé - Run the World (Girls) (Video - Main Version).mp4"width="600" 
    height="400" loop="false" autostart="false"><br><br>

    <a href='/next/'>Continue to the next task</a>
    """

WON=GAME_HEADER+"""CONGRATULATIONS!!!
    You have succeeded in helping Beyoncé get ready for her red carpet appearance
    without getting fired! <a href='/'>You can play again </a> or show off your accomplishment with this certificate!
    <img src="/static/certificate-page-001.jpg" alt="congrats" width="1300" height="900">
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
    if len(unused_worlds)==0:
        for world in re_add:
            unused_worlds.append(world)
        return WON
    next_world = random.choice(unused_worlds)
    output=GAME_HEADER + ENCOUNTER_DECISION.format(next_world["name"])+render_template(next_world["template"])
    unused_worlds.remove(next_world)
    re_add.append(next_world)
    return output


@simple_route('/chose/<what>/')
def chose(world: dict, what: str) -> str:
    """
     Determine whether the user chose right or wrong

     :param world: The current world
     :param where: The new location to move to
     :return: The HTML to show the player
     """
    world['decision'] = what
    if world['decision']=="wrong":
        for world in re_add:
            unused_worlds.append(world)
        return ENCOUNTER_WRONG
    if world['decision']=="right":
        return ENCOUNTER_RIGHT
