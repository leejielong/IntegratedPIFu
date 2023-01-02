from tqdm import tqdm
import numpy as np
import os

training_subject_list = np.loadtxt("train_set_list.txt", dtype=str)
training_subject_list = training_subject_list.tolist()

test_subject_list = np.loadtxt("test_set_list.txt", dtype=str)
test_subject_list = test_subject_list.tolist()
training_subject_list.extend(test_subject_list)

angles = [0,45,90,135,180,225,270,315]

for subject in tqdm(training_subject_list):
    for angle in angles:
        # os.system(f"blender rendering_script/blank.blend -b -P rendering_script/render_full_mesh.py -- {subject} {angle}")
        os.system(f"blender rendering_script/blank.blend -b -P rendering_script/render_normal_map_of_full_mesh.py -- {subject} {angle}")
        os.system(f"blender rendering_script/blank.blend -b -P rendering_script/render_depth_map_of_full_mesh.py -- {subject} {angle}")
