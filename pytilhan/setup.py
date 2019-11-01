from setuptools import setup, find_packages, _install_setup_requires

setup_requires = [
    ]

install_requires = [
    ]

dependency_links = [
    ]

setup(
    name='jimmy_util',
    version='0.1.6',
    last_date='2019.09.10',
    url='https://github.com/seungjinhan/python_packages/tree/master/python_packages/src/jimmy_util',
    description='python utils',
    author='jimmy han',
    author_email='hanblues@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    zip_safe=False,
    dependency_links=dependency_links,
    entry_points={
        'console_scripts': [
            ],
        "egg_info.writers": [
                "foo_bar.txt = setuptools.command.egg_info:write_arg",
            ],
        },    
)