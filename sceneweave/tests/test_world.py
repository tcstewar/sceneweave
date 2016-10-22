import sceneweave as sw

def condition_test1(world):
    return True
def scene_test1(world):
    world.text('hello')

def test_select():
    world = sw.World()
    world.scenes.append(sw.Scene('test1', condition_test1, scene_test1))

    scene, actors = world.select()

    scene.play(actors)



