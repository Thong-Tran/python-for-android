from pythonforandroid.recipe import CythonRecipe
from os.path import join


class KiventProjectilesRecipe(CythonRecipe):
    name = 'kivent_projectiles'

    depends = ['kivent_core']

    patches = ['fix-include-dirs.patch']

    subbuilddir = False

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super(KiventProjectilesRecipe, self).get_recipe_env(
            arch, with_flags_in_cc=with_flags_in_cc)
        kivy = self.get_recipe('kivy', self.ctx).get_build_dir(arch.arch)
        kivent = self.get_recipe('kivent_core',
                                 self.ctx).get_build_dir(arch.arch, sub=True)
        cymunk = join(self.get_recipe('cymunk', self.ctx).get_build_dir(arch.arch), 'cymunk')
        env['CYTHONPATH'] = ':'.join((kivy, kivent, cymunk))
        env['PYTHONPATH'] += ':' + self.ctx.get_python_install_dir()
        return env

    def prepare_build_dir(self, arch):
        '''No need to prepare, we'll use kivent_core'''
        return

    def get_build_dir(self, arch):
        builddir = self.get_recipe('kivent_core', self.ctx).get_build_dir(arch)
        return join(builddir, 'modules', 'projectiles')


recipe = KiventProjectilesRecipe()
