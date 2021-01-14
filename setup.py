from setuptools import setup

with open('readme.md', 'r') as f :
    readme_content = f.read()

setup(
    name='petit_type_system',
    version='0.1.4',
    description='Backend to handle type conversion from python to another language',
    packages=['petit_type_system'],
    url='https://github.com/Plawn/petit_type_system',
    license='apache-2.0',
    author='Plawn',
    author_email='plawn.yay@gmail.com',
    long_description=readme_content,
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
    install_requires=['executing'],
)
