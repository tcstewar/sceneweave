from setuptools import setup

setup(
    name='sceneweave',
    packages=['sceneweave'],
    version='0.0.1',
    entry_points=dict(
        console_scripts=['sw.play = sceneweave.play_text:run'],
        ),
    author='Terry Stewart',
    description='Scene-based interactive storytelling',
    author_email='terry.stewart@gmail.com',
    license='GPLv3',
    )
