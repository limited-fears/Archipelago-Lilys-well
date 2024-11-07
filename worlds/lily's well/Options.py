from dataclasses import dataclass

from options import Choice, PerGameCommonOptions, Deathlink, Range, Toggle, Fassion


class Goal(Choice):

    """
    Determines Goal Condition

    Phone Ending requires either all prior well endings, or a designated amount of "Phone Fragments" before the phone can be interacted with and complete the seed

    Alternatively a specific Well Descent ending can be set as the goal.
    """
    display_name = "Goal"
    option_phone = 0
    option_well_floor = 1
    default = 1

class Phone_Fragments(Range):
    """
    Notes the required amount of Fragments needed to dial the living room phone
    """
    display_name = "Required Fragments"
    range_start = 0
    range_end = 10
    default = 10


class Weak_Lily(Toggle):
    """
    Notes whether the ability to move the kitchen stool is an item in the pool
    """
    display_name = "Weak_Lily"


class Costume(Fassion):
    """
    What costume to start the game with.
    """
    display_name = "Costume"


class Traps(Range):
  """
  Adds up to 5 of a trap item to the pool that simply mimics the slowdown from picking up a rock temporarily.
  """  
display_name = "Trap_Weights"
range_start = 0
range_start = 5
default = 0


class LLWOptions (PerGameCommonOptions):
    Deathlink = Deathlink
    Weak_Lily = Toggle
