from flask import render_template
from route_helper import simple_route
import random

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

ENCOUNTER_DECISION = """
    <!-- Curly braces let us inject values into the string -->
    You are helping Beyoncé with {}. You must make a decision by clicking the picture you wish to bring to Beyoncé!<br><br>
    """

ENCOUNTER_WRONG = """You have made the wrong decision for Beyoncé!!! She has her lawyers send you 
    termination letter :( <br><br>
            
    <embed name="run the world" src="/static/Beyoncé - Broken-Hearted Girl (Video).mp4"width="600" height="400" 
    loop="false" autostart="false"><br><br>

    <a href='/reset/'>Return to the start</a>
    """

ENCOUNTER_RIGHT = """Congrats you chose correctly! You live to survive another day as Beyoncé's assistant...
    <br><br>
        
    <embed name="run the world" src="/static/Beyoncé - Run the World (Girls) (Video - Main Version).mp4"width="600" 
    height="400" loop="false" autostart="false"><br><br>

    <a href='/next/'>Continue to the next task</a>
    """

WON="""
    <div class="alert alert-light" role="alert">CONGRATULATIONS!!!
    You have succeeded in helping Beyoncé get ready for her red carpet appearance
    without getting fired! Show off your accomplishment with this certificate!
    </div>
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
    if len(world['pages'])==0:
        return render_template("header.html")+WON+"""<br>Your Progress: <br><div class="progress-bar bg-danger"><div class="progress-bar" role="progressbar" 
        style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div></div>"""
    next_world = random.choice(world['pages']) #randomly select the page they go to
    output=render_template("header.html") + ENCOUNTER_DECISION.format(next_world["name"]) + render_template(next_world["template"])
    world['pages'].remove(next_world)
    #progress bar at bottom of game. WHY DOES "YOUR PROGRESS" ACT AS A LINK??????
    if len(world['pages'])==1:
        output+="""<br>Your Progress: <br><div class="progress"><div class="progress-bar bg-danger" role="progressbar" style="width: 75%" aria-valuenow="75"
         aria-valuemin="0" aria-valuemax="100"></div></div>"""
    if len(world['pages'])==2:
        output+="""<br>Your Progress: <br><div class="progress"><div class="progress-bar bg-danger" role="progressbar" style="width: 50%" aria-valuenow="50" 
        aria-valuemin="0" aria-valuemax="100"></div></div>"""
    if len(world['pages'])==3:
        output+="""<br>Your Progress: <br><div class="progress"><div class="progress-bar bg-danger" role="progressbar" style="width: 25%" aria-valuenow="25" 
        aria-valuemin="0" aria-valuemax="100"></div></div>"""
    if len(world['pages'])==4:
        output+="""<br>Your Progress: <br><div class="progress"><div class="progress-bar bg-danger" role="progressbar" style="width: 0%" aria-valuenow="0" 
        aria-valuemin="0" aria-valuemax="100"></div></div>"""
    return output


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
        return render_template("header.html")+ENCOUNTER_WRONG
    if world['user decision']=="right":
        return render_template("header.html")+ENCOUNTER_RIGHT
