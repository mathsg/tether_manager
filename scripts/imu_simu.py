#!/usr/bin/env python
# license removed for brevity
from math import pi

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose

from transforms3d.euler import euler2quat


class ImuSimu(object):
    def __init__(self):
        self.pub = rospy.Publisher('imu_input', Imu, queue_size=1)
        rospy.init_node('imu_simu', anonymous=True)
        self.timestamp = 10.0
        self.rate = rospy.Rate(self.timestamp) # 10hz
        self.count = 0
        self.imu_msg = Imu()

    def simulate_imu(self):

        q = euler2quat(0, 0, 0.05 * self.count)
        self.imu_msg.orientation.w = q[0]
        self.imu_msg.orientation.x = q[1]
        self.imu_msg.orientation.y = q[2]
        self.imu_msg.orientation.z = q[3]

        self.imu_msg.angular_velocity.x = 0
        self.imu_msg.angular_velocity.y = 0
        self.imu_msg.angular_velocity.z = 0.05 / self.timestamp

        self.imu_msg.header.stamp = rospy.Time.now()
        self.imu_msg.header.seq += 1

        self.count += 1;

    def work(self):
        while not rospy.is_shutdown():
            # Complete header
            self.simulate_imu()
            self.pub.publish(self.imu_msg)
            self.rate.sleep()

if __name__ == '__main__':
    imu_sim = ImuSimu()
    try:
        imu_sim.work()
    except rospy.ROSInterruptException:
        pass
