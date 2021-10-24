# Surveillance-system

In the world day, researchers and developers have come up with a wide range of surveillance systems that are deployed at homes, in industries and remote areas at the same time control the tasks through affordable, intelligent, and easy-to-implement hardware and software systems. The system will be able to detect motion (intruder), activate the embedded camera to take pictures after motion is sensed and send the image through email to the home owner.

![IMG_20211024_191439__01](https://user-images.githubusercontent.com/88834520/138605576-5cd95895-a8dc-48ac-9531-7e8f4868548a.jpg)

# Components & Quantity:
Raspberry Pi 1,
Motion Sensor 1 &
Web Cam 1

# Working System process:
The IoT device built on Raspberry Pi 4 in this project has a simple and straightforward operation. The
device detects motion by the motion sensor and as it detects motion, it starts capturing images. The images
are stored on the MicroSD card and sent to the registered email of the user. All of this is managed by a
python script running over the Raspbian Operating System. Before running the python script, it is essential
to install an operating system on the Pi 3 and install the required libraries i.e., OpenCV on the operating
system. While installing the operating system, installing the libraries and the python script, the Raspberry Pi
should be connected to a display monitor using Joy pi kit.

On script execution, it enters into an infinite loop where the motion sensor continuously monitors and once
the change in the input is detected, the camera switches on and captures photo. The image that is captured is
saved with date time as name of the image using the datetime module and the image is sent through mail
with subject and body
