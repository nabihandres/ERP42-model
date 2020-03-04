#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64


def wheels_effort_controllers_JointEffortController(torque): 
    #Define publishers for each joint effort controller commands.
    
    #keti mobile robot
    #pub1 = rospy.Publisher('/simple_model/right_front_wheel_controller/command', Float64, queue_size=10)
    #pub2 = rospy.Publisher('/simple_model/right_middle_wheel_controller/command', Float64, queue_size=10)
    #pub3 = rospy.Publisher('/simple_model/right_back_wheel_controller/command', Float64, queue_size=10)
    #pub4 = rospy.Publisher('/simple_model/left_front_wheel_controller/command', Float64, queue_size=10)
    #pub5 = rospy.Publisher('/simple_model/left_middle_wheel_controller/command', Float64, queue_size=10)
    #pub6 = rospy.Publisher('/simple_model/left_back_wheel_controller/command', Float64, queue_size=10)
    
    #erp42_control
    pub1 = rospy.Publisher('/erp42_control/right_front_wheel_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/erp42_control/right_back_wheel_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/erp42_control/left_front_wheel_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/erp42_control/left_back_wheel_controller/command', Float64, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        rospy.loginfo(torque)
        
        pub1.publish(torque)
        pub2.publish(torque)
        pub3.publish(torque)
        pub4.publish(torque)
        #pub5.publish(torque)
        #pub6.publish(torque)
        rate.sleep()  #sleep for rest of rospy.Rate(10)

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
    
    #Initiate node for controlling torques in the wheeel
    rospy.init_node('keit_wheels', anonymous=True)
    try:
        wheels_effort_controllers_JointEffortController(12) #Nm INPUT the TORQUE
        
    except rospy.ROSInterruptException:
        pass
