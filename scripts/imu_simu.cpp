#include "std_msgs/String.h"
#include "sensor_msgs/Imu.h"
#include "geometry_msgs/Twist.h"
#include "geometry_msgs/Pose.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  ros::init(argc, argv, "imu_simu");
  ros::NodeHandle n;

  ros::Publisher pub_01 = n.advertise<sensor_msgs::Imu>("imu_simu", 1);

  ros::Rate loop_rate(10);

  int count = 0;
  while (ros::ok())
  {
    /**
     * This is a message object. You stuff it with data, and then publish it.
     */
    sensor_msgs::Imu msg;


    ss << "hello world " << count;
    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());

    chatter_pub.publish(msg);

    // Complete the header
    msg.header.stamp = ros.Time.now();
    msg.header.seq++;

    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }


  return 0;
}
