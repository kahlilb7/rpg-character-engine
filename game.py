# Kahlil Batieste
# 03/29/2026
# Project 2: RPG Character Engine
# Builds a character system using classes, inheritance, and file loading

# ============================================================
# game.py — Project 2: RPG Character Engine
# DO NOT modify the run_battle() function below.
# Add all of your class definitions and functions beneath it.
# ============================================================

import random
import csv

def run_battle(fighter1, fighter2):
    """
    Runs a turn-based battle between two character objects.
    The higher level character attacks first each round.
    Returns the winning character.

    Parameters:
        fighter1: a character object with attack(), is_alive(), and comparison methods
        fighter2: a character object with attack(), is_alive(), and comparison methods

    Returns:
        The character object that is still alive at the end of the battle.
    """
    print(f"\n{'='*40}")
    print(f"  BATTLE START")
    print(f"  {fighter1} vs {fighter2}")
    print(f"{'='*40}")

    round_num = 1
    while fighter1.is_alive() and fighter2.is_alive():
        print(f"\n--- Round {round_num} ---")

        # Higher level character attacks first
        if fighter1 > fighter2:
            first, second = fighter1, fighter2
        else:
            first, second = fighter2, fighter1

        first.attack(second)
        print(f"  {first.name} attacks {second.name}")
        print(f"  {second}")

        if second.is_alive():
            second.attack(first)
            print(f"  {second.name} attacks {first.name}")
            print(f"  {first}")

        round_num += 1

    winner = fighter1 if fighter1.is_alive() else fighter2
    print(f"\n{'='*40}")
    print(f"  {winner.name} wins!")
    print(f"{'='*40}\n")
    return winner


# ============================================================
# Write your classes and functions below this line.
# ============================================================

# ============================================================
# Step 1: Character Class Structure (Attributes & Constructor)
# ============================================================

class Character:
    """
    Represents a basic game character with shared stats and behavior.

    Parameters:
        name (str): The character's name.
        level (int): The character's level.
        health (float): The character's current health.
        attack_power (float): The character's attack strength.
        defense (float): The character's defense stat.

    Returns:
        None
    """

    def __init__(self, name, level, health, attack_power, defense):
        """
        Initializes a Character object with basic attributes.

        Parameters:
            name (str): The character's name.
            level (int): The character's level.
            health (float): The character's current health.
            attack_power (float): The character's attack strength.
            defense (float): The character's defense stat.

        Returns:
            None
        """
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack_power
        self.defense = defense


    # ============================================================
    # Step 2: Character Methods (Combat & Status Behavior)
    # ============================================================

    def attack(self, target):
        """
        Attacks another character by dealing damage.
        """
        damage = self.attack_power
        target.defend(damage)


    def defend(self, damage):
        """
        Reduces health based on incoming damage and defense.

        Parameters:
            damage (float): The raw damage being dealt to this character.

        Returns:
            None
        """
        # base character takes damage but is reduced by defense
        damage_taken = damage - (self.defense / 2)

        # ensure damage taken is not negative (healing)
        if damage_taken < 0:
            damage_taken = 0

        # reduce health by the damage taken
        self.health -= damage_taken


    def is_alive(self):
        """
        Checks if the character is still alive.
        """
        return self.health > 0


    def __str__(self):
        """
        Returns a readable string of the character.
        """
        return f"{self.name} (Level {self.level}) - Health: {self.health}"


    # ============================================================
    # Step 3: Comparison Methods (Level-Based Ordering)
    # ============================================================

    def __lt__(self, other):
        """
        Compares if this character's level is less than another.

        Parameters:
            other (Character)

        Returns:
            bool
        """
        return self.level < other.level


    def __gt__(self, other):
        """
        Compares if this character's level is greater than another.

        Parameters:
            other (Character)

        Returns:
            bool
        """
        return self.level > other.level


# ============================================================
# Step 4: Serializable Mixin (File Save and Load System)
# ============================================================

class Serializable:
    """
    Mixin class that adds save and load functionality.
    """

    def save(self, filepath):
        """
        Saves the object's data to a file.

        Parameters:
            filepath (str)

        Returns:
            None
        """
        with open(filepath, "w") as file:
            file.write(f"{self.name},{self.level},{self.health},{self.attack_power},{self.defense}")


    def load(self, filepath):
        """
        Loads the object's data from a file.

        Parameters:
            filepath (str)

        Returns:
            None
        """
        with open(filepath, "r") as file:
            data = file.read().strip().split(",")

            self.name = data[0]
            self.level = int(data[1])
            self.health = float(data[2])
            self.attack_power = float(data[3])
            self.defense = float(data[4])


# ============================================================
# Step 5: Subclass Overrides (Unique Combat Behavior)
# ============================================================

class Warrior(Character, Serializable):
    """
    Represents a Warrior character.
    """

    def __init__(self, name, level, health, attack_power, defense):
        """
        Initializes a Warrior object.

        Parameters:
            name (str)
            level (int)
            health (float)
            attack_power (float)
            defense (float)

        Returns:
            None
        """
        super().__init__(name, level, health, attack_power, defense)

    def defend(self, damage):
        """
        Reduces incoming damage with stronger defense.

        Parameters:
            damage (float): damage being dealt to this character.

        Returns:
            None
        """
        # warriors block more damage than the base Character
        damage_taken = damage - (self.defense)

        if damage_taken < 0:
            damage_taken = 0

        self.health -= damage_taken


class Mage(Character, Serializable):
    """
    Represents a Mage character.
    """

    def __init__(self, name, level, health, attack_power, defense):
        """
        Initializes a Mage object.

        Parameters:
            name (str)
            level (int)
            health (float)
            attack_power (float)
            defense (float)

        Returns:
            None
        """
        super().__init__(name, level, health, attack_power, defense)

    def attack(self, target):
        """
        Attacks with stronger magic damage.

        Parameters:
            target (Character)

        Returns:
            None
        """
        # mages hit harder than the base Character
        damage = self.attack_power * 1.5
        target.defend(damage)


class Rogue(Character, Serializable):
    """
    Represents a Rogue character.
    """

    def __init__(self, name, level, health, attack_power, defense):
        """
        Initializes a Rogue object.

        Parameters:
            name (str)
            level (int)
            health (float)
            attack_power (float)
            defense (float)

        Returns:
            None
        """
        super().__init__(name, level, health, attack_power, defense)

    def attack(self, target):
        """
        Attacks with a quicker strike.

        Parameters:
            target (Character)

        Returns:
            None
        """
        # rogues get a smaller attack boost
        damage = self.attack_power * 1.2
        target.defend(damage)

# ============================================================
# Step 6: load_characters Function (CSV to Character Objects)
# ============================================================

def load_characters(filepath):
    """
    Loads character data from a CSV file and returns a list of objects.

    Parameters:
        filepath (str): The path to the CSV file.

    Returns:
        list: A list of character objects.
    """
    characters = []

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        # each row in the CSV corresponds to a character's attributes
        for row in reader:
            name = row["name"]
            character_type = row["character_type"]
            level = int(row["level"])
            health = float(row["health"])
            attack_power = float(row["attack_power"])
            defense = float(row["defense"])

            # create the right subclass from character_type
            if character_type == "Warrior":
                character = Warrior(name, level, health, attack_power, defense)
            elif character_type == "Mage":
                character = Mage(name, level, health, attack_power, defense)
            elif character_type == "Rogue":
                character = Rogue(name, level, health, attack_power, defense)

            characters.append(character)

    return characters


# ============================================================
# Step 7: main Function (Run and Display Game)
# ============================================================

def main():
    """
    Runs the program by loading characters, displaying them,
    and running a battle.

    Returns:
        None
    """
    # load characters from the CSV file
    characters = load_characters("characters.csv")

    # print all characters
    for character in characters:
        print(character)

    # run a battle between the first two characters
    if len(characters) >= 2:
        run_battle(characters[0], characters[1])


if __name__ == "__main__":
    main()