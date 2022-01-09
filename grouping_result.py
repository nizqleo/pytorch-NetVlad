import os

group_dir = "/app/mid_data/group"

group_result = dict()

group_names = os.listdir(group_dir)
for group_name in group_names:
    for image_name in os.listdir(os.path.join(group_dir, group_name)):
        group_result[image_name] = group_name

