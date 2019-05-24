from distutils.core import setup

setup(
    name='robodkdriver',
    packages=['robodkdriver'],
    version='0.1',
    license='gpl-3.0',
    description='Boilerplate for RoboDK Robot Driver',
    author='Egehan Dulger',
    author_email='egehandulger94@gmail.com',
    url='https://github.com/egehandulger/robodkdriver',
    download_url='https://github.com/egehandulger/robodkdriver/archive/v0.1.tar.gz',
    keywords=['RoboDK', 'robotics', 'driver', 'online programming', 'simulation'],
    install_requires=[
        'pyserial',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
