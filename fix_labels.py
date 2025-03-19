import os
import glob

# Path to your label files
labels_path = 'data/dataset/helicopter/train/labels/*.txt'

# Process each label file
for label_file in glob.glob(labels_path):
    with open(label_file, 'r') as f:
        lines = f.readlines()
    
    # Convert class IDs to 0
    new_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 5:  # Make sure it's a valid label line
            parts[0] = '0'  # Set class ID to 0
            new_lines.append(' '.join(parts) + '\n')
    
    # Write back to file
    with open(label_file, 'w') as f:
        f.writelines(new_lines)

print("Finished converting all class IDs to 0") 