import inspect

class Scene(object):
    def __init__(self, name, valid, scene):
        self.name = name
        args, _, _, defaults = inspect.getargspec(valid)
        args2, _, _, defaults2 = inspect.getargspec(scene)
        assert args == args2
        assert defaults == defaults2
        assert defaults is None
        self.roles = args
        self.valid_function = valid
        self.scene_function = scene

    def valid(self, world):
        for actors in world.iterator(self.roles):
            if self.valid_function(*actors):
                yield self, actors

    def play(self, actors):
        return self.scene_function(*actors)


