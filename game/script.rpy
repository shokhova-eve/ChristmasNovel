# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

        
define config.name = _('The Best Gift')

init python:
    # Create the 'characters' class for tracking character attributes
    class Characters(object): 
        _instances = set()

        def __init__(self, abbreviation, given, color, like=0):
            self.abbreviation = abbreviation
            self.given = given  
            self.color = color
            self.like = like
            Characters._instances.add(self)
    
    #Standart Characters
    Nissa = Characters("n", "Nissa", "#f82bff")
    Jane = Characters("e", "Jane", "#9122DD")
    Ania = Characters("a", "Ania", "#3fa800")
    Rima = Characters("r", "Rima", "#F68C01")
    Juls = Characters("j", "Juls", "#F9F8F8") 
    You = Characters("u", "You", "#706B66")

    import gc

    for x in gc.get_objects():
        if isinstance(x, Characters):
            globals()[x.abbreviation] = Character(
                x.given,
                who_color=x.color
            )
    # Create array for storing records of critical choices
    globals()['Choices'] = [] 

screen point_indicator(text):
    # The transient ensures the screen only appears temporarily.
    zorder 100  
    # Makes sure it appears on top of everything.
    frame: 
        xpos 100
        ypos 50
        text "[text]":
            color "#F9F8F8"
        at fade_out

# Add the fade-out transformation.
transform fade_out:
    alpha 1.0
    linear 1 alpha 0.0  # Fades out over 0.5 seconds.
    on hide:
        alpha 0.0

init python:
    def approval_check(character, x):
        character.like += x
        renpy.show_screen("point_indicator", text="{}'s approval + {}".format(character.given, x))
        renpy.pause(2)  # Allows player to see the message

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg start

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nissa worried
    # These display lines of dialogue.

    n "Oh, hi! My friends are coming... You're probably be better off..."

    hide nissa

    show ania unhappy at left

    a "Hi. Traffic was horrendous."

    show rima happy at right
    
    r "Hi there. It is nice to see a new face"

    show juls playful at right

    j "It is nice to see a face that is not prepared for what's coming!"

    show eve happy at left

    e "What is coming?"

    u "Hi everyone. I am so glad you came to pick me up! I've never been to Stuttgart before"
    
    a "Be grateful you are not on a car, or you wouldn't have such a pleasant visit"


    menu:
        "I am a driver myself, by the way.":
            u "I am a driver myself, by the way."
            $ approval_check(Ania, 1)

        "And Juls, what is coming actually?":
            u "And Juls, what is coming actually?"
            $ approval_check(Juls, 1)

        "It is nice to see new faces too, Rima.":
            u "It is nice to see new faces too, Rima."
            $ approval_check(Rima, 1)

        "What are you reading? I breezed through a novel on the train too!":
            u "What are you reading? I breezed through a novel on the train too!"
            $ approval_check(Jane, 1)

        "You have nice hair color, Nissa. I plan to color mine pink next time!":
            u "You have nice hair color, Nissa. I plan to color mine pink next time!"
            $ approval_check(Nissa, 1)


    u "Actually, Leuten, I need a favor."
    u "There is a person here in Stuttgart. They moved recently. We were in one college, and they switched the major."
    u "However, she doesn't know that I moved too. I've never been brave enough to be proper friends with her, but I hope that this Christmas we can connect."
    u "So I need a really good gift. Could you help me?"

    r "Oh, that is so sweet. The best you can do is to craft something from your heart."
     
    j "The best you can do is tell her right away, what's the worse that can happen?"

    a "Let's go to Christmas fair and pick her something there"

    e "We can go bake cookies together! And then you gift them to her"

    jump market_scene

    # This ends the game.

    return
