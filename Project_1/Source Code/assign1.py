#!/usr/bin/python
import component
import commands
import itertools
import copy

def ProcessFileOut(self,filename):
    fin=open(filename)
    # Just a flag to say if we have just
    # encountered the first frame
    flag_start=0
    for line in fin:
        if(not line[0:2]=='//'):
            # This means this line is not a comment
            if(line=='\n'):
                if flag_start==1:
                    self.list_of_frames.append(fr)
                    print "Number of components in the frame are ",len(fr.list_of_comp).__str__()
                    del fr
                else:
                    flag_start=1
                
                # Start a new frame
                fr=component.Frame()
            else:
                line=line.strip()
                line=line.split('\t')
                line=[val.lstrip() for val in line]
                line=[val.rstrip() for val in line]
                #Check if the line is about relative positions
                # or component description
                if(('LEFT' in line or 'ABOVE' in line or 'INSIDE'
                    in line or 'OUTSIDE' in line)):
                        comp1=line[0]
                        comp2=line[2]
                        fr.relative_positions[line[1]].append((comp1,comp2))
                else:
                    # This is simply a description of the component
                    print line
                    name=line[0]
                    size=float(line[1])
                    orientation=int(line[2])
                    reflection=int(line[3])
                    # provide name,size,orientation,reflection.
                    comp=component.Component(name,size,orientation,\
                                            reflection)
                    # Now add the component to the list of components
                    fr.list_of_comp.append(comp)



# This functions takes 2 dictionaries with the same keys and whose each
# value is a list of tuples, and checks to see if the dictionaries are
# identical (in the sense of a set)

def CompareDictionaries(dict1,dict2):
    print "Dictionaries to be compared are "
    print dict1
    print dict2
    for key in dict1.keys():
        set_1=set(dict1[key])
        set_2=set(dict2[key])
        # Check to see if set_1=set_2
        if(not set_1==set_2):
            return 0
    return 1
                 
def LearnMappingOut(self):
    print "Learning mappings"
    frame_a=self.list_of_frames[0]
    frame_b=self.list_of_frames[2]
    list_of_components_frame_b=frame_b.list_of_comp
    list_of_components_frame_a=frame_a.list_of_comp

    name_of_components_frame_a=[val.name for val in frame_a.list_of_comp]
    name_of_components_frame_b=[val.name for val in frame_b.list_of_comp]
    
    # See which permutation of naming in frame_b matches that in frame_a
    perm_list=itertools.permutations(name_of_components_frame_b)
    
    # Go through each permutation and change the relative positions 
    # hash to see if it matches A
    
    for perm in perm_list:
        # Create a reordering hash where
        # the key is given by perm
        print perm
        name_mapping={}
        for val in enumerate(perm):
            name_mapping[val[1]]=name_of_components_frame_a[val[0]]
            
        #### Finished the name_match hash
        # Fetch a copy 
        temp_copy=copy.deepcopy(frame_b.relative_positions)
        # Now make changes in temp_copy as dictated by the permutation
        for (key,list) in temp_copy.iteritems():
            for index in range(0,len(list)):
                # val is a 2-tuple
                new_tuple=((name_mapping[temp_copy[key][index][0]],
                           name_mapping[temp_copy[key][index][1]]))
                temp_copy[key][index]=new_tuple
                                        
                
        flag=CompareDictionaries(temp_copy,frame_a.relative_positions)
        if(flag==1):
            # Permutation found. Capture this map and return
            print "permutation found"
            print name_mapping
            return name_mapping
                
    else:
        print "Could not find a mapping"
    
class Assign1:
    
    list_of_frames=[]
    ProcessFile=ProcessFileOut
    LearnMapping=LearnMappingOut

##################### MAIN FUNCTION ################

current_dir=commands.getoutput('pwd')
print current_dir
filename='1-2.txt'
full_filename=('/'.join(current_dir.split('/')[0:-1])+
                     '/Representations/'+filename)
print full_filename
ass1=Assign1()
ass1.ProcessFile(full_filename)

print "Number of frames is ",len(ass1.list_of_frames)
print ass1.list_of_frames[2].relative_positions

# Our next step is to learn the mapping between the 0th and 2nd frames.
ass1.LearnMapping()

