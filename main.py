from webcam import sidecam
from dataprocessing import horizontal_vel
from dataprocessing import projected_dist
res=sidecam()
vel=horizontal_vel(res[0],res[1])
proj_dist=projected_dist(res[0])
print('velocity is',vel,'feet/sec, projected to go',proj_dist,'feet')
