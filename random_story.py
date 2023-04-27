# Import modules
import tkinter as tk
from tkinter import messagebox
import random

# Defining list of phrases which will help to build a story
sentence_starter = ['About 100 years ago, ', 'In the 20 BC, ', 'Once upon a time, ', 'In a far-off land, ', 'Long long ago, ', 
                    'In a kingdom far away, ', 'In a magical land, ', 'In a distant galaxy, ', 'Many years ago, ', 
                    'In the depths of the forest, ']
character = ['there lived a king. ', 'there was a man named Jack. ', 'there lived a farmer. ', 'there was a queen. ',
             'there was a princess. ', 'there was a wicked sorcerer. ', 'there was a brave knight. ', 'there was a merchant. ',
             'there was a wise old sage. ', 'there was a mischievous imp. ']
time = ['One day, ', 'One full-moon night, ', 'On a sunny morning, ', 'On a dark and stormy night, ', 'In the dead of winter, ', 
        'In the middle of summer, ', 'On a balmy evening, ', 'At the stroke of midnight, ', 'In the early hours of dawn, ',
        'On a peaceful afternoon, ']
story_plot = ['they were passing by ', 'they were going for a picnic to ', 'they were on their way to ', 'they were exploring ', 
              'they were on a mission to find ', 'they were searching for ', 'they were lost in ', 'they were visiting ', 
              'they stumbled upon ', 'they were wandering through ']
place = ['the mountains. ', 'the forest. ', 'the city. ', 'the desert. ', 'the sea. ', 'the countryside. ', 'a haunted house. ', 
         'a mysterious island. ', 'a faraway planet. ', 'an enchanted castle. ']
second_character = ['They saw a man ', 'They saw a young lady ', 'They met a talking animal ', 'They met a friendly alien ',
                    'They encountered a ghost ', 'They met a giant ', 'They saw a unicorn ', 'They came across a mermaid ', 
                    'They met a dragon ', 'They found a magical genie ']
age = ['who seemed to be in late 20s ', 'who seemed very old and feeble ', 'who was in his prime ', 'who looked very young ', 
       'who was about the same age as them ', 'who was ancient and wise ', 'who was full of energy and life ', 
       'who was a little child ', 'who was in his mid-thirties ', 'who was a teenager ']
work = ['searching something. ', 'digging a well on roadside. ', 'fishing in a pond. ', 'hunting for treasure. ', 
        'picking flowers in a meadow. ', 'climbing a tree. ', 'sitting by a stream. ', 'rowing a boat. ', 'painting a picture. ', 
        'reading a book. ']

# Generate the story
story = random.choice(sentence_starter) + random.choice(character) + random.choice(time) + random.choice(story_plot) + random.choice(place) + random.choice(second_character) + random.choice(age) + random.choice(work)

# Show the story in a message box
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Random Story Generator", story)
