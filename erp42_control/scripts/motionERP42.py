#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

class motionerp42:

    def __init__(self):
        rospy.init_node('robot_control_node', anonymous=True)
    #Nm INPUT the TORQUE
    def wheels_effort_controllers_JointEffortController(self, torque): 
        #Define publishers for each joint effort controller commands.

        #erp42_control
        self.pub1 = rospy.Publisher('/erp42_control/right_front_wheel_controller/command', Float64, queue_size=10)
        self.pub2 = rospy.Publisher('/erp42_control/right_back_wheel_controller/command', Float64, queue_size=10)
        self.pub3 = rospy.Publisher('/erp42_control/left_front_wheel_controller/command', Float64, queue_size=10)
        self.pub4 = rospy.Publisher('/erp42_control/left_back_wheel_controller/command', Float64, queue_size=10)

        self.rate = rospy.Rate(10) # 10hz (10 per second send the command) limit the speed00
            
        while not rospy.is_shutdown():

            rospy.loginfo(torque)
                
            self.pub1.publish(torque)
            self.pub2.publish(torque)
            self.pub3.publish(torque)
            self.pub4.publish(torque)
            self.rate.sleep()  #sleep for rest of rospy.Rate(10)

    #INPUT angle radians -0.4<T<0.4
    def steer_wheels_effort_controllers_JointEffortController(self, angle): 
        #Define publishers for each joint position controller commands.
        self.pub1 = rospy.Publisher('/erp42_control/right_steer_wheel_controller/command', Float64, queue_size=10)
        self.pub2 = rospy.Publisher('/erp42_control/left_steer_wheel_controller/command', Float64, queue_size=10)
           
        self.rate = rospy.Rate(10) # 10hz
        
        while not rospy.is_shutdown():
            
            rospy.loginfo(angle)
                
            self.pub1.publish(angle)
            self.pub2.publish(angle)
            self.rate.sleep()  #sleep for rest of rospy.Rate(10)
    

 

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':

    a = motionerp42()
    try:
        a.steer_wheels_effort_controllers_JointEffortController(0)
        a.wheels_effort_controllers_JointEffortController(0)
        a.steer_wheels_effort_controllers_JointEffortController(0.4) 
        
    
    except rospy.ROSInterruptException:
        pass
