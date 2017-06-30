mystring = """# Assignment 1




Calls demo.py on a series of test images.
+
+IN: dir containing series of test images.
+OUT: output of demo.py.
+
+Run instruction:
+python runtest.py <dir>
+
+NOTE: dir must be absolute.
+"""
+
+import sys
+import os
+import subprocess
+
+if len(sys.argv) < 2:
+	print "Run instruction: python runtest.py <dir>\nABORTING"
+	sys.exit()
+
+run_command = "python demo.py --input_image"
+
+# Directory of images
+dir_in = sys.argv[1]
+
+# Loop over each image file in given directory
+frame_number = 1
+for file in sorted(os.listdir(dir_in)):
+	image_file = dir_in + '/' + str(file)
+	print image_file
+	subprocess.call(run_command + " " + image_file + " " + frame_number)
+	frame_number = frame_number + 1 


np.savez('simple_data.npz',
        imgs=all_imgs,
        spds=spds,
        accel=accel,
        steer=steer,
        gas=gas,
        brake=brake,
idx = np.array(fstarts))


all_data = np.load('simple_data.npz')
imgs_color = all_data['imgs']


import h5py
f = h5py.File('file.h5')
for i in range(len(list_arrays)):
  f.create_dataset('arr_{}'.format(i), data=list_arrays[i])


fetching arrays:

f = h5py.File('file.h5')
f.keys()
f['arr_0'].value
f['arr_0'][:]




