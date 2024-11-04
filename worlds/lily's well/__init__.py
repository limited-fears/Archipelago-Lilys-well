import functools
import logging
from typing import Any, Dict, List

from BaseClasses import Entrance, CollectionState, Item, Location, MultiWorld, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .items import Items, Locations, Maps, Regions, Rules
from .Options import Choice, Toggle, PerGameCommonOptions, StartInventoryPool

logger = logging.getLogger