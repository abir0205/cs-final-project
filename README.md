# Evolution Game - CS 110 Final Project
### Spring Semester, 2018

### Link to repo
[https://github.com/<repo>](#)

### Link to Demo Presentation
https://docs.google.com/presentation/d/1f_1jkdI6SXypE06b-BwiF_Soeu8kvxhrR5K6EqWX48E/edit?usp=sharing(#)

# Team: Dan's Bagg o'Beer

# Members:
## Danny Adamczuk
## Jeffrey Bagg
## Abir Hossain

# Project Description/Idea

The “Evolution Game” is a bare-bones simulation where the player takes control of a Finch on one of the Galapagos islands. The player starts off with a originating finch in an environment where it has to search around its environment for food to survive and thus evolve. As the finch chooses options, it gains “Population Health”, indicative of its population evolving (because individuals don’t evolve, in case you live under a rock).  There are random variables put into these options that can result in the finch losing health, such as a predator invading its environment.

The finch gains character traits (beak type or body/wing color) depending on what options it chooses, which can be seen by pulling up a “Finch Evolution” screen. Upon gaining certain character traits, certain food options become unavailable to the finch as a result of its evolution. Once the Population Health reaches a certain point, the game is completed, indicating that the particular finch population has grown to the point of dominating the island as a new species.


# User Interface Design

1. Main Menu/Start Screen

This screen is the first thing a user sees. It prompts the user with a prompt explaining the game and instructions to enter the game by pressing the spacebar. It was accessed straight through the Controller class.


2. Environment Screen

This is the main playing screen and was accessed through the Controller class. In the top left corner is the “Population Health” bar, starting with 25 health. Under the bar are instructions on how to move around the environment as well as how to access the Finch Evolution screen. Within the environment screen, the user controls a bird icon (this is a sprite object) that can move around the screen via key commands. The bird then moves around the environment to find food in four types of environments which are also sprites (the sprites are intentionally hidden in the envi). Once the bird collides with the sprite, the user can then choose food options via buttons which update the health bar. The user can either eat food, which will increase health, or are attacked by a predator and lose health.

3. Options Pop-Ups
Upon moving the finch and colliding with an unknown environment (shrub sprite, tree sprite, river sprite, ground sprite), three options pop up onto the screen. The options are based on the sprite that is collided with and prompt a decision such as eating berries versus food. You can then move the cursor to select an option. When the cursor hovers over the option it lights up and changes color. If an option is clicked with the mouse, a result screen pops up.

4. Result Screen
The result screen occurs when an option is selected. Depending on the option selected, the result screen reads the consequence of the option selected. This includes population health changes and evolution changes. “R” can then be pressed to return to the environment screen.

4. The Bird Menu

The bird menu was a screen that was accessed via a key where the user could see their progress in the game. Every decision made after colliding with a sprite would update the bird image found on the menu, such as changes in color or the addition of a beak. The user can toggle between the Bird Menu and the Environment Class. 

5. Instructions Menu
The instructions menu class that explained to the user how to play the game. Listed here were commands to control the bird. The user can toggle between the Instructions screen and the Environment class via key commands

6. Game Over Screen
After the user either maxes out on their health bar or their health is zero, they are then forwarded to a screen that states that the game has ended. Here the final population health is displayed and whether the won or lose the game. The user can then press a key to see the final evolution of their finch. The user can also choose to restart the game if they so choose. 

7/8. Initial and Final GUI Interfaces

Go to this link to view our initial and final GUI interfaces: https://drive.google.com/open?id=1z-67-9esWa507Wa9ajBoaVoNHZMxSohK

# Program Design

No special libraries were used.

Go to this link to view our flowchart: https://drive.google.com/open?id=1z-67-9esWa507Wa9ajBoaVoNHZMxSohK

# Tasks and Responsibilities

## Software Lead - Jeff

Worked side by side with both front and back end writing code to help integrate the two. Structured and organized the classes, json files, image files, and controller/loop files to all run smoothly. Designed the environment class to run the whole game by implementing sprite, options, gameover, button, and further necessary classes. Also designed the different game outcomes and results implementing the json and image files for the finch and options. Had a part in writing nearly every class and document implemented in the code.

## Front End Specialist - Dan

The Front End Specialist worked diligently to learn and implement background screens and images, pop up options, result screens, and game over screens. The Front End Specialist discovered how to make click based buttons that change color when the cursor is hovered above the area of the button. He collaborated with the Back End Specialist and Project Lead to implement what the actual options and results were and have them properly displayed. It was also crucial to make a bird menu screen that displays the current evolution of the bird with its specific features.

## Back End Specialist - Abir

The back end specialist created created the framework of all the major classes by implementing the basic logic of the classes. The back end wrote the classes that would set the environments and the icon for the bird. The back end also created the controller class that would be used to access all of the classes. The back end worked with the front end specialist to create the the functions that would allow the user to move the character around the screen and make the options. They created a combination of button and key commands to allow the user to play the game. The software lead guided the back end and aided in the implementation of all the code.

# Testing

Menu Testing

We initially run the controller to see the main screen comes up. The screen then has instructions as to how to continue to the game. We then press the spacebar to start the game. 


Game Testing

After we enter the game screen, we move our bird all throughout the screen see that it is properly moving. We press I to see if the instructions menu is working we press E to make sure we can see the evolution screen. We then move the bird around to the river environment to ensure that once the bird collides with the sprite, button options appear on the screen that allow the user to make options. We make sure the different options either raise or lower the health bar. We ensure this works for every environment sprite within the environment. We make sure that once the sprite collides with an environment and makes decisions, the bird can no longer make certain decisions in other environments. Furthermore, we ensure that every decision the bird makes changes the image of the bird within the Bird Menu. We make as many decisions as possible to max out the health bar and therefore see if we get the game over screen. Once we get the game over screen, we check to see we can toggle back and forth between the bird menu and the end screen to check the final evolution of our bird. We do the same with killing the health bar to zero. We then check to see if the user can start the game over with a key press.

A link to our Acceptance Test Procedure can be seen here:
https://docs.google.com/document/d/1cLgB4PPsdzq8zqvGaHATF0d55NX1o9nJXzPwZCotSn4/edit?usp=sharing

