#! /usr/bin/env python3

import os
import rospkg

rospack = rospkg.RosPack()
p = rospack.get_path('relaxed_ik')
os.chdir(p + "/src/RelaxedIK_Rust")
os.system('cargo run --bin relaxed_ik_node')

