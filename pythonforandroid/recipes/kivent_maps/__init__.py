from pythonforandroid.recipe import CythonRecipe
from os.path import join


class KiventMapsRecipe(CythonRecipe):
    name = 'kivent_maps'

    depends = ['kivent_core', 'tmx']

    subbuilddir = False

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super(KiventMapsRecipe, self).get_recipe_env(
            arch, with_flags_in_cc=with_flags_in_cc)
        kivy = self.get_recipe('kivy', self.ctx).get_build_dir(arch.arch)
        kivent = self.get_recipe('kivent_core',
                                 self.ctx).get_build_dir(arch.arch, sub=True)
        env['CYTHONPATH'] = ':'.join((kivy, kivent))
        env['PYTHONPATH'] += ':' + self.ctx.get_python_install_dir()
        return env

    def prepare_build_dir(self, arch):
        '''No need to prepare, we'll use kivent_core'''
        return

    def get_build_dir(self, arch):
        builddir = self.get_recipe('kivent_core', self.ctx).get_build_dir(arch)
        return join(builddir, 'modules', 'maps')


recipe = KiventMapsRecipe()
