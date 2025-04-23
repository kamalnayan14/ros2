from setuptools import find_packages, setup

package_name = 'turtlesim_contro_exp2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kamal',
    maintainer_email='kamal@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'circle_publisher=turtlesim_contro_exp2.circle_publisher:main',
            'pose_subscriber = turtlesim_contro_exp2.pose_subscriber:main',
            'wall_avoider = turtlesim_contro_exp2.wall_avoider:main'
        ]
    },
)
