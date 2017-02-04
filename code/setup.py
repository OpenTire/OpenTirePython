from setuptools import setup, find_packages

setup(
    name='OpenTire',
    version='0.1',
    description='An open-source mathematical tire model library for tire and vehicle research and development.',
    url='https://github.com/OpenTire/OpenTire',
    author='OpenTire',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['numpy'],
    classifiers=[
       'Programming Language :: Python :: 2'
    ],
)
