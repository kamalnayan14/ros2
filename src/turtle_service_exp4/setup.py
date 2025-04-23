from setuptools import find_packages, setup

package_name = 'turtle_service_exp4'

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
             'clear_client = turtle_service_exp4.clear_client:main',
             'color_control = turtle_service_exp4.color_control:main',
        ],
    },
)
