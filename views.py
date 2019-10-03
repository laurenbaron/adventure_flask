from route_helper import simple_route

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
    
    <a href="goto/breakfast">Start your day.</a><br>
    """

ENCOUNTER_DECISION = """
<!-- Curly braces let us inject values into the string -->
You are helping Beyoncé with {}. You must make a decision!<br>

<a href='/displayImage/{}/'><br>

<a href='/chose/wrong/'><button name="button1">Click me for the left picture!</button> <br>
<a href='/chose/right/'><button name="button2">Click me for the right picture!</button>
"""

ENCOUNTER_WRONG = GAME_HEADER + """You have made the wrong decision for Beyoncé!!! She has her lawyers send you 
            termination letter :( <br><br>
            <a href='/'>Return to the start</a>
            """

ENCOUNTER_RIGHT= GAME_HEADER+"""Congrats you chose correctly! You live to survive another day as Beyoncé's assistant...
        <br><br>
        <a href='/'>Return to the start</a> <br>
        <a href='/'>Continue to the next task</a>
        """

BREAKFAST="""<img src = "breakfast1.jpeg" /><br>
        <img src = \"breakfast2.jpeg\" /><br>
        """

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
    return GAME_HEADER+ENCOUNTER_DECISION.format(where)

@simple_route('/displayImage/<where>/')
def display_image(world: dict, where: str) -> str:
    if where=="breakfast":
        return BREAKFAST


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

