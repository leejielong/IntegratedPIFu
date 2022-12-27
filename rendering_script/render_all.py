from tqdm import tqdm
import numpy as np
import os

training_subject_list = np.loadtxt("train_set_list.txt", dtype=str)
training_subject_list = training_subject_list.tolist()
root_dir = "rendering_script/buffer_fixed_full_mesh"
angles = [0,45,90,135,180,225,270,315]

for subject in tqdm(training_subject_list):
    for angle in angles:
        os.system(f"blender rendering_script/blank.blend -b -P rendering_script/render_full_mesh.py -- {subject} {angle}")
