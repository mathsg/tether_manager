#!/usr/bin/env python

from math import pi

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32
from std_srvs.srv import Trigger
from transforms3d.euler import quat2euler


def to_angle(vec):
    return (vec + pi) % (2 * pi) - pi


class TurnCounter(object):
    def __init__(self):
        rospy.init_node('turn_counter')
        rospy.Subscriber('imu_input', Imu, self.on_imu_received)
        self.pub = rospy.Publisher('count_output', Float32, queue_size=1)
        self.reset_server = rospy.Service("reset_counter", Trigger, self.reset)
        self.int = 0
        self.old_heading, self.init_heading = None, None

    def on_imu_received(self, msg):
        """
        Process incoming imu messages
        :param sensor_msgs.msg.Imu msg: incoming msg message
        """
        q = msg.orientation
        if self.init_heading is not None:
            _, _, new_heading = quat2euler([q.w, q.x, q.y, q.z])
            self.int += to_angle(new_heading - self.old_heading)
            self.pub.publish(Float32(self.int / (2 * pi)))
        else:
            _, _, self.init_heading = quat2euler([q.w, q.x, q.y, q.z])
        _, _, self.old_heading = quat2euler([q.w, q.x, q.y, q.z])

    def reset(self, req):
        self.init_heading, self.old_heading = None, None

    def work(self):
        rospy.spin()


if __name__ == "__main__":
    tc = TurnCounter()
    tc.work()
