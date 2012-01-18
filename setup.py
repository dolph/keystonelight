from setuptools import setup, find_packages

setup(name='keystone',
      version='2012.1',
      description="Authentication service for OpenStack",
      author='OpenStack, LLC.',
      author_email='openstack@lists.launchpad.net',
      url='http://www.openstack.org',
      packages=find_packages(exclude=['test', 'bin']),
      scripts=['bin/keystone', 'bin/keystone-manage'],
      zip_safe=False,
      install_requires=['setuptools'],
      )
