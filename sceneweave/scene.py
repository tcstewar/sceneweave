import inspect

class Scene(object):
    def __init__(self, name, valid, scene):
        self.name = name

        args, _, _, defaults = inspect.getargspec(scene)
        assert defaults is None
        if valid is not None:
            args2, _, _, defaults2 = inspect.getargspec(valid)
            assert args == args2
            assert defaults == defaults2
        self.roles = args
        self.valid_function = valid
        self.scene_function = scene

    def valid(self, world):
        for actors in world.iterator(self.roles):
            if self.valid_function is None or self.valid_function(*actors):
                yield self, actors

    def play(self, actors):
        return self.scene_function(*actors)

def load_scenes(filename):
    with open(filename) as f:
        compiled = compile(f.read(), '__sw_main__', 'exec')
    objs = {}
    scenes = []
    exec(compiled, objs)
    for k in objs.keys():
        if k.startswith('scene_'):
            sf = objs[k]
            name = k[6:]
            cf = objs.get('condition_' + name, None)
            scenes.append(Scene(name, cf, sf))
    return scenes



