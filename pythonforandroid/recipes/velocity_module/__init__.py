from pythonforandroid.recipe import CythonRecipe
from os import environ

class VelocityRecipe(CythonRecipe):
    name = 'velocity_module'

    depends = [('python2', 'python3crystax')]

    def download_if_necessary(self):
        key = 'P4A_{}_DIR'.format(self.name.lower())
        environ[key] = environ.get(key, '/Users/ivc/kivy/velocity_module')
        return

recipe = VelocityRecipe()
