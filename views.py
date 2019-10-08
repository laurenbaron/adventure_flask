from route_helper import simple_route
import random

GAME_HEADER = """
<h1>Be Beyoncé's assistant for a day! Don't get fired...</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""

@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.
    :param world: The current world
    :return: The HTML to show the player
    """
    return GAME_HEADER+"""It’s your first day on the job and Beyoncé is getting ready for a red carpet! <br>
    <img src="/static/beyoncegif.gif" alt="beyonce sassy gif"><br><br>
    <a href="goto/song selection"><button name="startButton">Start your day!</button><br>
    """

@simple_route('/continue/')
def next(world: dict):
    """
    The welcome screen for the game.
    :param world: The current world
    :return: The HTML to show the player
    """
    possible_worlds=["breakfast", "song selection", "dresses", "passing time"]
    next_world=random.choice(possible_worlds)
    decide(world, next_world)

ENCOUNTER_DECISION = """
    <!-- Curly braces let us inject values into the string -->
    You are helping Beyoncé with {}. You must make a decision by clicking the picture you wish to bring to Beyoncé!<br><br>
    """

ENCOUNTER_WRONG = GAME_HEADER + """You have made the wrong decision for Beyoncé!!! She has her lawyers send you 
    termination letter :( <br><br>
            
    <iframe width="560" height="315" src="https://www.youtube.com/embed/JXmUYdOVJtc?controls=0" frameborder="0" 
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>

    <a href='/'>Return to the start</a>
    """

ENCOUNTER_RIGHT= GAME_HEADER+"""Congrats you chose correctly! You live to survive another day as Beyoncé's assistant...
    <br><br>
        
    <iframe width="560" height="315" src="https://www.youtube.com/embed/VBmMU_iwe6U?controls=0" frameborder="0"
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>

    <a href='/'>Return to the start</a> <br>
    <a href='/continue/'>Continue to the next task</a>
    """

BREAKFAST = """
    <a href='/chose/wrong/'><img src="/static/breakfast1.jpeg" alt="breakfast option 1">
    <a href='/chose/right/'><img src="/static/breakfast2.jpeg" alt="breakfast option 2"><br>
    """

SONGS='''
    <embed name="sandcastles" src="/static/08 Sandcastles.m4a"width="150" height="90" loop="false" autostart="false">
    <embed name="formation" src="/static/12 Formation.m4a"width="150" height="90" loop="false" autostart="false">
    
    <p>Based on the two downloads of Beyoncé's songs, click the corresponding button for what song to play for Beyoncé 
    while she gets ready :) </p><br>
    
    <a href='/chose/wrong/'><button name="Sandcastles">Sandcastles</button>
    <a href='/chose/right/'><button name="Formation">Formation</button><br>
    '''

DRESS='''
    <a href='/chose/wrong/'><img src="/static/dress1.jpeg" alt="dress option 1">
    <a href='/chose/right/'><img src="/static/dress2.jpeg" alt="dress option 2"><br>
    '''

PASS_TIME='''
    <a href='/chose/wrong/'><img src="/static/read.jpeg" alt="pass time option 1">
    <a href='/chose/right/'><img src="/static/swim.jpeg" alt="pass time option 2"><br>
    '''

@simple_route('/goto/<where>/')
def decide(world: dict, where: str) -> str:
    """
    Update the player location and encounter a decision, prompting the player
    to choose a picture.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where
    image=""
    if world['location'] == "breakfast":
        image=BREAKFAST
    elif world['location']=="song selection":
        image=SONGS
    elif world['location']=="dresses":
        image=DRESS
    elif world['location']=="passing time":
        image=PASS_TIME
    if world['location'] == "next_world":
        return "<p>fail</p>".format(where)

    return GAME_HEADER+ENCOUNTER_DECISION.format(where)+image


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
        return ENCOUNTER_WRONG
    if world['decision']=="right":
        return ENCOUNTER_RIGHT

