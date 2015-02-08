try:
    from setuptools import setup
except:
    from distutils.core import setup


config = {
    'description': 'Dymouse: Raspberry Pi + Dymo USB Scale',
    'author': 'Charles Reid',
    'url': 'https://github.com/charlesreid1/dymouse',
    'download_url': 'https://github.com/charlesreid1/dymouse',
    'author_email': 'charles@charlesreid1.com',
    'version': '1.0',
    'install_requires': ['pyusb','flask','numpy'],
    'packages': ['dymouse','dymouse.driver','dymouse.webapp'],
    'include_package_data' : True,
    'scripts': [],
    'name': 'dymouse',
    'zip_safe' : False
}

setup(**config)
