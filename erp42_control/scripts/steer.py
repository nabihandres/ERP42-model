#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64


def steer_wheels_effort_controllers_JointEffortController():
    #Define publishers for each joint effort controller commands.
    pub1 = rospy.Publisher('/erp42_control/right_steer_wheel_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/erp42_control/left_steer_wheel_controller/command', Float64, queue_size=10)
    #Initiate node for controlling torques in the wheeel
    rospy.init_node('erp42_steer_wheels', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        angle = 0.4 #Nm INPUT radians -0.4<T<0.4
 
        rospy.loginfo(angle)
        
        pub1.publish(angle)
        pub2.publish(angle)
        rate.sleep()  #sleep for rest of rospy.Rate(10)

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
    try:
        steer_wheels_effort_controllers_JointEffortController() 
        


    except rospy.ROSInterruptException:
        pass
