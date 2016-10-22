from setuptools import setup

setup(
    name='OpenTire',
    version='0.1',
    description='An open-source mathematical tire model library for tire and vehicle research and development.',
    url='https://github.com/OpenTire/OpenTire',
    author='OpenTire',
    license='MIT',
    packages=['opentire'],
    zip_safe=False,
    install_requires=['numpy'],
    classifiers=[
       'Programming Language :: Python :: 2'
    ],
)
