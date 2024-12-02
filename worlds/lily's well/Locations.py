from BaseClasses import LocationProgressTypek
from typing import Dict, TypedDict, List, Location

class LLwLocation(Location):
    game: str = "Lily's Well"

    locsphere0_table = {
        "Bed": 231370,
        "Bedroom_Drawer": 231371,
        "bathroom":231372,
        "Dad's drawer":231373,
        "Driveway":231374,
        "Woods":231375,
        "Well_Entrance":231376,
        "Dad's_Coat":231377,
        "Couch_Right":231378,
        "Bookshelf":231379,
        "Kitchen_Pantry":231380,
        "Shed_Outside":231381
        }

    locsphere1_table = {
        "Dad's_Safe":231382,
        "Kitchen_Wall":231383,
        "Outside_Left":231384,
        "Shed_Right":231385,
        "Shed_Left":231386,
        "Cave_Note":231387,
        "Bridge":231388,
        "Red_Tree":231389,
        "Blue_Tree":231390,
        "Yellow_Tree":231391,
        "Lab_Cage":231392
    }

    locsphere2_table = {
        "Lab_Guilt":231393,
        "Couch_Left":231394,
        "Altar":231395
    }

    locspere3_table = {
        "Cave_Net":231396,
        "Cave_Wall":231397
}
    locprogress_table = {
        "Yarn":55,
        "Stool":56
}