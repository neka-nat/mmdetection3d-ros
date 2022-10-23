## Installation

```sh
cd mmdetection3d
docker-compose up -d --build
docker exec -it mmdetection3d-ros bash
```

## Demo

```sh
python demo/pcd_demo.py demo/data/kitti/kitti_000008.bin configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py /models/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class_20220301_150306-37dc2420.pth --show
```

```sh
python /nodes/mmdetection3d_ros_node.py configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py /models/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class_20220301_150306-37dc2420.pth
```