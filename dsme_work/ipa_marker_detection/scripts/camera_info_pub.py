#!/usr/bin/env python


import rospy
import numpy as np
import roslib
from sensor_msgs.msg import CameraInfo


def main () :

    mtx = np.load("/root/Aruco_Tracker/mtx.npy")
    dist = np.load("/root/Aruco_Tracker/dist.npy")

    info=CameraInfo()
    print(mtx)
    print(dist)
    seq=0
    while not rospy.is_shutdown():
            print(info)
            info.header.seq=seq
            info.header.stamp.secs = rospy.Time.now().secs
            info.header.stamp.nsecs = rospy.Time.now().nsecs
            info.width=1280
            info.height=720
            info.distortion_model='plumb-bob'
            info.D=[0,0,0,0,0,0]

            info.K=np.reshape(mtx,(1,9)).tolist()
            info.R[:]={0}
            info.P[:]={0}
            camera_info.publish((info))
            seq+=1
if __name__ == '__main__':

    try:
        rospy.init_node("dsme_camera")

        camera_info=rospy.Publisher("dsme_camera_info", CameraInfo,queue_size=10)

        main()

        rospy.spin()

    except rospy.ROSInterruptException:
        pass


