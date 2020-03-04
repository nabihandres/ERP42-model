# ERP42-model
Simulation model of ERP42 working with ROS in Gazebo simulator

erp42 is the description of the robot, the xacro files are inside
erp42.launch is for run the simulation model 
controllers.yaml file into config folder it show the controllers
	joint_state_controller
	4 wheel controllers (effort controllers) (N*m)
	1 controller in each front wheel due to in urdf is not possible to create a kinematic chain 		loop, right and left steer wheel controller (position controller) minimun= -0.4 (radian) 		maximun= 0.4 (radian)
 
erp42_control 
have two important scripts 
main.py it permit to put input of torque in each wheel (torque controller)
steer.py it permit to change the steer of the vehicle  (position controller)

erp42_sdf_files
it have a ramp of 5 degree

gazebo_ros_pkgs
it permit access to the controllers of gazebo and ROS
