from setuptools import setup, find_packages


setup(
    name='percentile-rank',
    version='0.0.1',
    description='Percentile rank calculator written in Python',
    author='Michael Tintiuc',
    author_email='contact@michaeltintiuc.com',
    maintainer='@michaeltintiuc',
    license='MIT',
    url='https://github.com/michaeltintiuc/python-percentile-rank',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
        'console_script': [
            'percentile-rank=percentile_rank.__main__:main'
        ]
    }
)
