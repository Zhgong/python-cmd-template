from distutils.core import setup

setup(name='Funniest',
      version='0.1',
      description='Dummy funniest',
      author='seangg',
      author_email='seangg@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=["funniest"],
      install_requires=[
          'fire',
      ],
      entry_points = {
        'console_scripts': ['funniest=funniest.command_line:main'],
    }
     )