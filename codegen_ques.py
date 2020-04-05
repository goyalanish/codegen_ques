def assign_group(group,time_value):
    result=True
    for grp in group:
        if(time_value[0]>=grp[1] or (time_value[0]<=grp[1] and time_value[1]<=grp[0])):
            result=result and True
        else:
            result=result and False
    return result

def overlap_grouping(*time_bounds):
    group1=[time_bounds[0]]
    group2=[]
    for bound in range(0,(len(time_bounds)-1)):
        if(assign_group(group1,time_bounds[bound+1])):
            group1.append(time_bounds[bound+1])
        else:
            group2.append(time_bounds[bound+1])
    return group1,group2
    
def checkvalidity(time_group1,time_group2,n_activity,time_bounds):
    out_str=''
    if len(time_group1)+len(time_group2)<n_activity:
        out_str='IMPOSSIBLE'
    else:
        for bound in time_bounds:
            if(bound in time_group1):
                out_str=out_str+'C'
            else:
                out_str=out_str+'J'
    return(out_str)

cnt=int(input())
n_activity=[]
time_bounds=[]
for c in range(0,cnt):
    time_cnt=int(input())
    temp_arr=[]
    for time in range(0,time_cnt):
        temp_arr.append(list(map(int,input().split())))
    n_activity.append(time_cnt)
    time_bounds.append(temp_arr)
    
for bound in range(0,len(time_bounds)):
    time_group=overlap_grouping(*time_bounds[bound])
    time_group1=time_group[0]
    time_group2=time_group[1]
    if(len(time_group[1])==0):
        print('Case #'+str(bound+1)+':'+checkvalidity(time_group1,time_group2,n_activity[bound],time_bounds[bound]))
    else:
        time_group2=overlap_grouping(*overlap_grouping(*time_bounds[bound])[1])[0]
        print('Case #'+str(bound+1)+':'+checkvalidity(time_group1,time_group2,n_activity[bound],time_bounds[bound]))