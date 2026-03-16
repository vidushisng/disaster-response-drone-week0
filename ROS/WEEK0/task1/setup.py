from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'drone_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vidushisng',
    maintainer_email='vidushi0401@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'simple_node = drone_sim.simple_node:main',
            'altitude_publisher = drone_sim.altitude_publisher:main',
            'altitude_subscriber = drone_sim.altitude_subscriber:main',
            'arm_service = drone_sim.arm_service:main',
	    'arm_client = drone_sim.arm_client:main',
        ],
    },
)
