import random

from . import exceptions

class Actor(object):
    def __init__(self, roles):
        self.roles = roles

class World(Actor):
    def __init__(self, seed=None):
        super(World, self).__init__(roles=['world'])
        self.scenes = []
        self.actors = {}
        self.add_actor(self)
        self.seed = seed
        self.rng = random.Random(seed)
        self.texts = []

    def text(self, text):
        self.texts.append(text)

    def add_actor(self, actor):
        for r in actor.roles:
            if r not in self.actors:
                self.actors[r] = set()
            self.actors[r].add(actor)

    def select(self):
        valid = []
        for s in self.scenes:
            valid.extend(s.valid(self))
        if len(valid) == 0:
            raise exceptions.NoValidSceneException()
        return self.rng.choice(valid)

    def iterator(self, roles):
        if len(roles) == 0:
            yield ()
        else:
            role = roles[0]
            if role not in self.actors:
                return
            for a in self.actors[role]:
                for x in self.iterator(roles[1:]):
                    yield (a,) + x

