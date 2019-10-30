from flask import render_template, request, redirect
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
    world['pages']=[{'template': "breakfast.html", 'name': "breakfast"},
                       {'template': "songs.html", 'name': "song selection"},
                       {'template': "dresses.html", 'name': "dresses"},
                       {'template': "passtime.html", 'name': "passing time"}]
    world['fans']=['fake fan','supporter', 'LEADER OF THE BEYHIVE']
    world['user']={'first name':"",
                    'decision':"",
                    'fan_level':"",
                    'promotion':""}
    return render_template("welcome.html")

@simple_route('/user/')
def get_user(world: dict)->str:
    """
    The screen after the welcome that gets the user's name
    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template("user_info.html", fan_types=world['fans'])

@simple_route('/save/')
def save(world: dict, *args)->str:
    """
    Save the user's input into world dictionary
    :param world: The current world
    :return: The next page (start beyonce adventure)
    """
    if len(request.values.get('user_name'))>0:
        world['user']['name']=request.values.get('user_name')
    else:
        world['user']['name']="Anonymous User"
    world['user']['fan_level']=request.values.get('fan_level')
    index=world['fans'].index(world['user']['fan_level'])
    if index==2:
        world['user']['promotion'] = "truly awe-inspiring sorcerer in all things Beyoncé"
    else:
        world['user']['promotion'] = world['fans'][index+1]
    return redirect('/next/')

@simple_route('/next/')
def decide(world: dict) -> str:
    """
    Encounter a randomly selected decision for beyonce
    :param world: The current world
    :return: The HTML to show the player depending on what random page they've been selected to go to
    """
    if len(world['pages'])==0:
        return render_template("won.html", name=world['user']['name'], old=world['user']['fan_level'], new=world['user']['promotion'])
    else:
        next_world = random.choice(world['pages']) #randomly select the page they go to
        #progress bar at bottom of game
        progress=100-(100/NUMBER_OF_PAGES*len(world['pages']))
        value_now=str(int(progress))
        style="width: "+value_now+"%"

        world['pages'].remove(next_world)

        return render_template(next_world['template'], helping_with=next_world['name'])+render_template("progress_bar.html",
                now_value=value_now, style_value=style)


@simple_route('/chose/<what>/')
def chose(world: dict, what: str) -> str:
    """
    Determine whether the user chose right or wrong
    :param world: The current world
    :param what: What user chose (right or wrong)
    :return: The HTML to show the player
    """
    world['user']['decision'] = what
    if world['user']['decision']=="wrong":
        return render_template("incorrect.html")
    if world['user']['decision']=="right":
        return render_template("correct.html")
