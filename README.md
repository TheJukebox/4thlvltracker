# 4th Level Tracker
---
## *An initiative tracker built for 5th Edition Dungeons &amp; Dragons*
4th Level Tracker is an initiative tracker for D&D 5e, built using python3. It features a straight forward, no-frills
interface that lets you track important things, like the hit points of all the characters engaged in combat.

## Features
### Current:
- Initiative tracking (duh).
- An initiative roller.
- Health tracking.
- Concentration tracking.

### Planned:
- Armour Class tracking.
- Combat modifiers and damage resistance tracking.
- Spell tracking.
- Note input.
- Saveable initiative orders.
- XP tracking.
- CR tracking.
- Surprise round tracking.
- Death saving throw tracking.

## Usage
To access different options of 4th Level Tracker, you simply type commands into any prompt.

- `help` displays a similar set of instructions from within the program.
- `exit`, `e`, `quit`, or `q` will prompt an exit dialogue.
- Typing `done` during the initiative creation stage will instantly attempt to start running through the order.
If there are no items in the order, the program will prompt the user for more input.
- Typing `roll` when prompted for an initiative score will prompt the user to input a modifier, which is then used in conjunction with a D20 roll in order to generate an initiative score.
- Inputting any integer during a turn in the initiative order will add or subtract that integer from the character's current HP.
For instance, if a creature has 13 health, inputting `-3` will lower that creature's health to 10 from that point on. If a creature has the concentration condition, it will prompt the user to input whether the concentration check succeeded or failed after damage.
- `conc`, `con`, `concentrate`, or `concentration` will toggle the concentration condition for the current character.
