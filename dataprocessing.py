import math
def horizontal_vel(coor_lst,elapsed_time):
    start_coor=coor_lst[0][0]#find first coordinate
    end_coor=coor_lst[len(coor_lst)-1][0]#find end coordinate
    tot_dist=abs(end_coor-start_coor)#determine pixel length
    foot_dist=tot_dist*.01#600width
    res=foot_dist/elapsed_time
    return res#return velocity using time elapsed

'''def vert_vel(coor_lst, startTime, endTime):#same as horizontal code
    start_coor=coor_lst[0][1]
    end_coor=coor_lst[5][1]
    tot_dist=end_coor-start_coor
    foot_dist=tot_dist*0.0008680556
    elapsed_time=5*((endTime-startTime)/len(coor_lst))
    res=foot_dist/elapsed_time
    return res
'''
def projected_dist(coor_lst):
    for i in range(len(coor_lst)):#find the peak of the arc
        if i !=0:
            if coor_lst[i][1]>coor_lst[i-1][1]:
                top_coor=coor_lst[i]
    half_coor=top_coor#find the distance between the two
    first_coor=coor_lst[0][0]
    hlfproj_dist=half_coor[0]-first_coor
    res=hlfproj_dist*.01*2#convert to feet and full
    return res
'''
def accu(coor_lst,target):
    wall_hit=coor_lst[len(coor_lst)-1]#find where it hit the wall
    xdif=abs(wall_hit[0]-target[0])
    ydif=abs(wall_hit[1]-target[1]
    tot_dif=math.sqrt(xdif**2+ydif**2)#find distance between target and ball
    return tot_dif

def write_to(accu):#writes to text file and averages values
    if not os.path.exists('accu.txt'):
        file(filename, 'w').close()
    fa=open("accu.txt","a")
    fa.write(str(accu))
    fa.close()
    fr=open("accu.txt","r")
    lst=fr.readlines()
    res=0
    for i in range(len(lst)):
        res+=float(lst[i])
    res/=len(lst)
    return res'''
