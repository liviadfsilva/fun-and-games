import os

print(r'''
                            .-----.
                          .'       `.
                         :      ^v^  :
                         :           :
                         '           '
          |~        www   `.       .'
         /.\       /#^^\_   `-/\--'
        /#  \     /#%    \   /# \
       /#%   \   /#%______\ /#%__\
      /#%     \   |= I I ||  |- |
      ~~|~~~|~~   |_=_-__|'  |[]|
        |[] |_______\__|/_ _ |= |`.
 ^V^    |-  /= __   __    /-\|= | :;
        |= /- /\/  /\/   /=- \.-' :;
        | /_.=========._/_.-._\  .:'
        |= |-.'.- .'.- |  /|\ |.:'
        \  |=|:|= |:| =| |~|~||'|
         |~|-|:| -|:|  |-|~|~||=|      ^V^
         |=|=|:|- |:|- | |~|~|| |
         | |-_~__=_~__=|_^^^^^|/___
         |-(=-=-=-=-=-(|=====/=_-=/\
         | |=_-= _=- _=| -_=/=_-_/__\
         | |- _ =_-  _-|=_- |]#| I II
         |=|_/ \_-_= - |- = |]#| I II
         | /  _/ \. -_=| =__|]!!!I_II!!
        _|/-'/  ` \_/ \|/' _ ^^^^`.==_^.
      _/  _/`-./`-; `-.\_ / \_'\`. `. ===`.
     / .-'  __/_   `.   _/.' .-' `-. ; ====;\
    /. .__./    \ `. \ / -  /  .-'.' ====='  >
   /  \  _/  .-' `--.  / .' /  `-.' ======.' /
''')

print("It's Halloween night and you decide to go to a haunted house.\n"
      "There's only one exit, and you must make the right choices in order to reach it.\n"
      "Find the way out before someone — or something — finds you first.")

choice1 = input('You\'re standing in a dark, dim-lit foyer, covered in cobwebs and dust. '
      'Scanning the room, you find a door on the left with a sign that says "kitchen" on it. '
      'On the other hand, right in front of you there\'s a grand staircase. '
      'You can either go up the staircase or walk into the kitchen. '
      'Which way do you want to go?\n'
      'Type "staircase" or "kitchen"\n').lower().strip()

if choice1 == "staircase":
    os.system('cls' if os.name == 'nt' else 'clear')
    choice2 = input('You reached the top of the staircase. '
          'There\'s a corridor on the left and another one on the right. '
          'Which way do you want to go? '
          'Type "left" or "right"\n').lower().strip()
    if choice2 == "left":
        os.system('cls' if os.name == 'nt' else 'clear')
        choice4 = input('There\'s 3 doors at the end of the corridor. '
                        'The one on the left says "BEWARE! '
                        'The one in the middle says "DANGER! '
                        'And the one on the right says "EXIT" '
                        'Which door will you choose? '
                        'Type "beware", "danger" or "exit"\n').lower().strip()
        if choice4 == "beware":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You walked into a den of vipers. Game over!")
        elif choice4 == "danger":
            choice6 = input('You walk into a room full of dolls, with a red light on. '
                            'In the left corner, you spot a human-size doll seated in a rocking chair. '
                            'As the chair begins to rock, the doll begins to speak with a childish, yet eerie voice. '
                            '"There are two ways out of this trap. '
                            'Bright will lead to pain, and dark will lead to death.'
                            'You might want to follow my warning, '
                            'if you wish to keep your breath." '
                            'Scanning the room, you find two windows. '
                            'One whose color is bright, and the other dark. '
                            'You\'re one choice away from finding your way out,'
                            'but can you really trust the doll? '
                            'You\'re unsure, but you must choose a window. '
                            'Type "bright" or "dark"').lower().strip()
            if choice6 == "bright":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Never trust eerie dolls. By walking on the line, you triggered a gas bomb. "
                      "Game over!")
            elif choice6 == "dark":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You found the exit! "
                      "You trusted your instincts and they led you to a window with a fire escape. "
                      "You win!")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(r''' 
    ⠀⢀⣴⣿⣿⣿⣦⠀
⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧
⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿
⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀

You chose an option that doesn't exist. Game over!''')
        elif choice4 == "exit":
            choice5 = input('In the middle of the room, you find a stand with a red button on it. '
                            'Taking a closer look, you see the word "exit" written on it. '
                            'You start to wonder if this could really be the way out, or a trap.'
                            'You\'re indecisive, but you must make a choice. '
                            'Press the button or go back. What do you choose to do?'
                            'Type "button" or "back"\n').lower().strip()
            if choice5 == "button":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("It was a trap! The floor gave out and you fell into a spiderweb. Game over!")
            elif choice5 == "back":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You ran into the murderer. "
                      "He's wearing a rotten pumpkin as a mask while holding an axe in his hand. "
                      "Game over!")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(r''' 
    ⠀⢀⣴⣿⣿⣿⣦⠀
⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧
⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿
⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀

You chose an option that doesn't exist. Game over!''')
    elif choice2 == "right":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("The boards were rotten and you fell through them, "
              "right into a room full of corpses. Game over!")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r''' 
    ⠀⢀⣴⣿⣿⣿⣦⠀
⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧
⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿
⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀

You chose an option that doesn't exist. Game over!''')
elif choice1 == "kitchen":
    choice3 = input('You entered the kitchen. '
                    'There\'s a slaughtered pig lying on the counter with a knife stabbed at its belly.'
                    'Across the room there\'s an open window with the word "exit" written on it.'
                    'With a closer look at it, you realize the message was written with blood.'
                    'You can either run back to the foyer or climb out the window.'
                    'What do you do?'
                    'Type "exit" or "run"\n').lower().strip()
    if choice3 == "exit":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You climbed out the window and fell into a grave. Game over.")
    elif choice3 == "run":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You ran into the murderer. "
              "He's wearing a rotten pumpkin as a mask while holding an axe in his hand."
              "Game over.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r''' 
    ⠀⢀⣴⣿⣿⣿⣦⠀
⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧
⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿
⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀

You chose an option that doesn't exist. Game over!''')
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r''' 
    ⠀⢀⣴⣿⣿⣿⣦⠀
⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧
⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿
⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀

You chose an option that doesn't exist. Game over!''')
