from setuptools import setup

setup(name='tk-notepad',
      version='0.1',
      description='tk-notepad is a notepad program developed with Tkinter, equipped with a simple interface.',
      url='https://github.com/ryanvij/tk-notepad',
      author='ryanvij',
      author_email='ryan.vijay2006@gmail.com',
      license='MIT',
      entry_points={
        'console_scripts': ['tk-notepad=tk_notepad.notepad:main']
      },
      packages=['tk_notepad'],
      zip_safe=False)