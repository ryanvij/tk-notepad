from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(name='tk-notepad',
      version='0.2',
      description='tk-notepad is a notepad program developed with Tkinter, equipped with a simple interface.',
      long_description_content_type='text/markdown',
      long_description = (here / 'README.md').read_text(encoding='utf-8'),
      url='https://github.com/ryanvij/tk-notepad',
      author='ryanvij',
      author_email='ryan.vijay2006@gmail.com',
      license='MIT',
      entry_points={
        'console_scripts': ['tk-notepad=tk_notepad.notepad:main']
      },
      packages=['tk_notepad'],
      zip_safe=False)

