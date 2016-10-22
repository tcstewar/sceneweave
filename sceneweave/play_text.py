import sys

from . import world
from . import scene


def run():
    TextGame(sys.argv[1]).run()

class TextGame(object):
    def __init__(self, filename):
        self.world = world.World()
        self.world.choose = self.choose
        self.world.scenes.extend(scene.load_scenes(filename))

    def run(self):
        while True:
            scene, actors = self.world.select()
            print 'doing scene', scene.name
            scene.play(actors)

    def choose(self, choices):
        for text in self.world.texts:
            print(text)
        del self.world.texts[:]

        while True:
            for i, option in enumerate(choices.options):
                print('%d: %s' % (i+1, option[1]))

            value = raw_input('>>>')
            try:
                value = int(value)
            except:
                print('invalid number')
                continue

            if value < 0 or value > len(choices.options):
                print('invalid choice')
                continue

            return choices.options[value - 1][0]
