"""Packages in Python....."""
# Cowsay is the package....
import cowsay

def greetings(name):
    cowsay.trex(f"Welcome {name} to the world of Python..")

def accept_name():
    name = input("What's your name? ")
    greetings(name)

accept_name()