import math
from typing import Dict, List

from BaseClasses import Item, Location, Region, Tutorial, MultiWorld
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule, forbid_item

from .Items import Bad_Rope_Material, Good_Rope_Material, Yarn, Tools, Rocks, Notes
from .Locations import locsphere0_table, locsphere2_table, locsphere3_table, locprogress_table
from .Options import LLWOptions

class LLWLocation(Location):
    game: str = "Lily's Well"


class LLWWebWorld(WebWorld):
    theme = "grass"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="How to play Lily's Well",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["LeonMillan"]
    )

    tutorials = [setup_en]


class LLWWorld(World):
    """Lil's Well"""