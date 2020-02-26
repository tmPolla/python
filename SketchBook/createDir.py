# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:14:22 2020

@author: Polla.Tamas-Marosi

task: create a directory in the current place, move into that and create a new file. Finally list
the files from the directory

"""



import os

""" original task
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.exists(directory) == False:
    os.mkdir(directory)
  # Create the new file inside of the new directory
  os.open(filename,"r")
  # Return the list of files in the new directory
  return os.listdir(directory)
print(new_directory("PythonPrograms", "script.py"))
"""


def new_directory(directory, filename):
  print(os.getcwd())
  
  # Before creating a new directory, check to see if it already exists
  if os.path.exists(directory) == False:
    os.mkdir(directory)
  
    # Create the new file inside of the new directory
  os.chdir(directory)
  print(os.getcwd()) 
  open(filename, 'a').close()
  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))