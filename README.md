# VoronoiParcellation
Python code snippet for generating random parcellations on the cortical surface.

The script assumes that you have the following: 
1. Anatomical surface in gifti format
2. A binary mask that excludes vertices in the medial wall of the cortical surface, also in gifti format

These are then used to generate a .shape.gii file containing whichever number of parcels you want. If you want to then use this parcellation for other analyses in Connectome Workbench e.g. `wb_command -cifti-parcellate` then you need to do the following:
1. Convert the .shape.gii output into a .label.gii file using `wb_command -metric-label-import. An example lable table has been provided
2. Create a .dscalar.nii cifti file using `wb_command -cifti-create-label`
