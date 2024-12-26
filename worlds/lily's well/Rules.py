from BaseClasses import CollectionState

#tools
def shears(state: CollectionState, player: int) -> bool:
    return state.has("shears",player)

def bolt_cutters(state: CollectionState, player: int) -> bool:
    return state.has("bolt_cutters",player)

def Knitting_Needles(state: CollectionState, player: int) -> bool:
    return state.has("Knitting_Needles",player)

def Knife(state: CollectionState, player: int) -> bool:
    return state.has("Knife",player)

def Shed_Key(state: CollectionState, player: int) -> bool:
    return state.has("Shed_Key",player)

def Garden_Shears(state: CollectionState, player: int) -> bool:
    return state.has("Garden_Shears",player)

def Red_Key(state: CollectionState, player: int) -> bool:
    return state.has("Red_Key",player)

def ID_Card(state: CollectionState, player: int) -> bool:
    return state.has("ID_Card",player)

def Jerkey(state: CollectionState, player: int) -> bool:
    return state.has("Jerkey",player)


#good rope material
def good(state: CollectionState, player: int) -> bool:
    return state.has("Whip","Knitted_Yarn", "Power_Chord", "Oily_Hair", "Net", "Blue_Flower_Vine", "Chain", "Bedsheets", "Belts", "Rope", player)

#bad rope materials

def bad(state: CollectionState, player: int) -> bool:
    return state.has("Toilet_Paper", "Red_Flower_Vine", "Yellow_Flower_Vine", "Charger_Wire", player)

