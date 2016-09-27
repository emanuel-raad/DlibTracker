import dlib
import time

start_time = time.time()

options = dlib.simple_object_detector_training_options()
options.C = 50
options.num_threads = 4
options.be_verbose = True
options.epsilon = 0.01
dlib.train_simple_object_detector('apples_dataset.xml', 'detector.svm', options)

print("--- %s seconds ---" % (time.time() - start_time))