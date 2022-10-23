#!/usr/bin/env python3
import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

from mmdet3d.apis import inference_detector, init_model
from mmdet3d.core.points import get_points_type


class Mmdetection3dRosNode:
    def __init__(self, args):
        rospy.init_node("mmdetection3d_ros_node")
        self._sub = rospy.Subscriber("/point_cloud2", PointCloud2, self.callback_pcd)
        self._model = init_model(args.config, args.checkpoint, device=args.device)
        self._points_class = get_points_type("LIDAR")
        rospy.loginfo("Start mmdetection3d_ros_node!")

    def callback_pcd(self, msg):
        points = np.array([[point[0], point[1], point[2]] for point in pc2.read_points(msg)])
        points = self._points_class(points, points_dim=points.shape[-1])
        result, data = inference_detector(self._model, points)
        rospy.loginfo(result)
        rospy.loginfo(data)

    def spin(self):
        rospy.spin()


def main(args):
    node = Mmdetection3dRosNode(args)
    node.spin()


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("config", help="Config file")
    parser.add_argument("checkpoint", help="Checkpoint file")
    parser.add_argument(
        "--device", default="cuda:0", help="Device used for inference")
    args = parser.parse_args()
    main(args)
