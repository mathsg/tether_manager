# tether_manager

The tether_manager package contains a node counting the number of turns the robot has made since the beginning of its mission.

## Installation

### Installing ROS
First of all, intall ROS on your computer (using Ubuntu 16.04 or 18.04 is recommended). See [ROS Installation](http://wiki.ros.org/ROS/Installation) for more information.

You should also install the following dependencies:
`sudo apt install git build-essential python-pip`

### Preparing your workspace
Then, create a ROS workspace:
```bash
cd $HOME
mkdir -p Dev/ros_ws/src && cd Dev/ros_ws/src
catkin_init_workspace
```

Clone this repository:
```bash
git clone https://github.com/forssea-robotics/tether_manager.git
```

Install its dependencies:
```bash
rosdep install --from-paths ./ -i -r -y
```

And build your ROS workspace:
```bash
cd ..
catkin_make
```

## Instructions
See the pdf file included in this repository.
