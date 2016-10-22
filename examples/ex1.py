import sceneweave as sw

class Player(sw.Player):
    def __init__(self):
        super(Player, self).__init__()
        self.health = 0
        self.items = []
    def gains(self, item):
        self.items.append(item)
    def take_damage(self, amount):
        self.health -= amount
    def has(self, item):
        return item in self.items


def condition_init(world):
    return not hasattr(world, 'initialized')

def scene_init(world):
    player = Player()
    world.add_actor(player)
    c = world.rng.choice([0,1])
    if c == 0:
        player.text('You are Gringr the barbarian')
        player.gains('sword')
        player.health = 10
    elif c == 1:
        player.text('You are Finmr the elf.')
        player.gains('sword')
        player.gains('bow')
        player.health = 5
    player.location = 'forest'
    world.initialized = True



def condition_ex1(player):
    return player.location == 'forest'
def scene_ex1(player):
    player.text('''
You sneak along a small forest trail, moving cautiously, avoiding making any
sound. The tall trees arch overhead, casting shadows while the wind whispers
through them.  Gradually, you start to make out voices ahead of you.  Deep,
gutteral voices, spitting their sounds through sharpened teeth.  Do you:''')

    choices = sw.Choices()
    if player.has('sword'):
        choices.add(charge='Charge in and attack')
    choices.add(sneak='Sneak wide around them')
    if player.has('bow'):
        choices.add(bow='Pick them off from a distance')
    c = player.choose(choices)

    if c == 'charge':
        player.text('''
With a sudden yell, you charge out of the clearing.  Three grotesque
monsters are suddenly visible, turning and snapping.  You slice one neck
cleanly off its body, and then quickly kill the next.  The third nicks you
slightly with its sword, before you crush its skull.''')
        player.take_damage(1)
    elif c == 'bow':
        player.text('''
Moving silently, you creep closer to the sounds.  Eventually, you see
three grotesque monsters...  You target them carefully, and when you are
sure of your shot, you kill one, and then the other two without incident.''')
    elif c == 'sneak':
        player.trigger(scene_sneak)

def condition_sneak(player):
    return False
def scene_sneak(player):
    player.text('''
You sneak through the forest for a while in the other direction.''')

def condition_die(player):
    return player.health < 0
def scene_die(player):
    player.text('''You fall to the ground, dead.''')
    player.game_over()



