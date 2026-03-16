from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='drone_sim',
            executable='altitude_publisher',
            name='altitude_publisher'
        ),

        Node(
            package='drone_sim',
            executable='altitude_subscriber',
            name='altitude_subscriber'
        ),

    ])
