from setuptools import setup

setup(name='cursed',
      version='1.0.0',
      description='A tool to decompile Minecraft mods straight from CurseForge',
      url='https://github.com/Ewpratten/cursedecompiler',
      author='Evan Pratten',
      author_email='ewpratten@gmail.com',
      license='GPLv3',
      packages=['cursed'],
      zip_safe=False,
      include_package_data=True,
      instapp_requires=[
          "requests"
      ]
      )
