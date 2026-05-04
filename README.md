# RPG Character Engine

## Overview
This project is an object-oriented Python RPG character engine. It loads character data from a CSV file, creates character objects, and runs a turn-based battle simulation.

## Features
- Base `Character` class with shared attributes and behavior
- `Warrior`, `Mage`, and `Rogue` subclasses
- Unique combat behavior through method overriding
- Save and load functionality using a `Serializable` mixin
- CSV file loading with `csv.DictReader`
- Turn-based battle simulation

## Concepts Practiced
- Classes and objects
- Inheritance
- Multiple inheritance
- Method overriding
- Special methods like `__str__`, `__lt__`, and `__gt__`
- File handling
- CSV data loading

## How to Run
```bash
python game.py

The program loads characters from characters.csv, prints them, and runs a battle between the first two characters.

Project Background

This project began as a Computer Science course project focused on classes, inheritance, and file handling. I completed the implementation myself and later refined it for portfolio use.

Future Improvements
Add player selection
Add more character types
Improve battle output
Add item or skill systems