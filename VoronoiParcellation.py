#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 08:32:19 2023

@author: lw19
"""


import numpy as np
import nibabel as nb 
from sklearn.cluster import KMeans


n_clusters = 180

### Load anatomical surface
left_midthickness = nb.load('/data/Data/dHCP_1/dhcp_3rd_release_atlas/dhcpSym_3rd_release/dhcpSym_template/week-40_hemi-left_space-dhcpSym_dens-32k_midthickness.surf.gii')

### Load mask excluding the medial wall
left_roi = nb.load('/data/Data/dHCP_1/dhcp_3rd_release_atlas/week-40_hemi-left_space-dhcpSym_dens-32k_desc-medialwall_mask.shape.gii')

### Get indices of vertices in medial wall mask 
left_roi_vertices = np.where(left_roi.darrays[0].data == 1)[0]

### Only calculate k-means on vertices outside the medial wall 
left_midthickness_vertices = left_midthickness.darrays[0].data[left_roi_vertices,:]

### Set k-means params
kmeans = KMeans(n_clusters=n_clusters, max_iter=1000, n_init=5)

### Run k-means on surface vertices 
label = kmeans.fit_predict(left_midthickness_vertices)

### Replace medial wall mask values with new label values
left_roi.darrays[0].data[left_roi_vertices] = label +1

### Save new label as shape.gii
nb.save(left_roi,'/home/lw19/Desktop/dHCP.L.parcellation180.shape.gii')

### NOTE:
# If using wb_command -cifti-parcellate, this will need to be converted to a .dlabel.nii either by 
# 1. converting the .shape.gii metric file into a .label.gii file using wb_command -metric-label-import, and then wb_command -cifti-create-label, or
# 2. converting the .shape.gii metric into a dscalar.nii using wb_command -cifti-create-dense-scalar, and then wb_command -cifti-label-import 

