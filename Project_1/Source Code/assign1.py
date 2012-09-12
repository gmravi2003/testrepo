#!/usr/bin/python
import component
import commands
class Assign1:
    
    list_of_frames=[]
    def ProcessFile(self,filename):
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
                    #Check if the line is about relative positions
                    # or component description
                    if('LEFT' in line or 'ABOVE' in line or 'INSIDE'
                       in line or 'OUTSIDE' in line):
                        comp1=line[0]
                        comp2=line[2]
                        fr.relative_positions[line[1]].append((comp1,comp2))
                    else:
                        # This is simply a description of the component
                        name=line[0]
                        size=float(line[1])
                        orientation=int(line[2])
                        reflection=int(line[3])
                        # provide name,size,orientation,reflection.
                        comp=component.Component(name,size,orientation,\
                                                 reflection)
                        # Now add the component to the list of components
                        fr.list_of_comp.append(comp)
                


##################### MAIN FUNCTION ################

current_dir=commands.getoutput('pwd')
print current_dir
filename='1-3.txt'
full_filename=('/'.join(current_dir.split('/')[0:-1])+
                     '/Representations/'+filename)
print full_filename
ass1=Assign1()
ass1.ProcessFile(full_filename)

print "Number of frames is ",len(ass1.list_of_frames)
for val in ass1.list_of_frames[5].list_of_comp:
    print val.__str__()

