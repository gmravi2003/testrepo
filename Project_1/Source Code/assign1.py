#!/usr/bin/python
import component
import commands


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
                    
    
def LearnTransitionsOut(self):
    


class Assign1:
    
    list_of_frames=[]
    ProcessFile=ProcessFileOut
    LearnTransitions=LearnTransitionsOut
    

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


