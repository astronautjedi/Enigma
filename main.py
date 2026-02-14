

#plug board *2
#enter keys/message
#rotating gears 3 
#reflector
#bulb
#send the string 
#get answer in bulb 

#starting position of the rotors 
#position fo rthe plugs 2,3
#plug board pair switches 

'''
requirements:
-lookup table for rotors positions 
-pointers for 3 rotor positions
-dictionry/lookuptable for internal rotor mapping,reflector
- input letters converted to list
-output list/bulb 
-dictionary form input plugs
-dictionary for rotor notches

process:
-set rotor positions
-set plug positions

-put in values/ asci
-gets converted gets converted to a list 
-checks in plugs for switching
-then that pointer goes to each of the rotors 
-the values goes throught the reflector 
-coomes throught the dictionary/plug board
-output list 
-display output list

'''

'''
#defines
fleet_pos
fleet_pos_l
fleet_pos_plg1
rotor_list=[1 to 26]
digits=26

ptr_ctr_1=0
ptr_ctr_2=0
ptr_ctr_3=0

#fucntion
def convert_to_list(a,b):

def plugboard(b,a):
for i in b:
if i in dict_plugboard:
    a.append(i.value)

def rotor(num,fleet_pos,rotot_out)
    ptr=rotor_num_ptr.value
    dict_rotor=rotor_num_dict_ptr.value
    notch_rtr=rotor_num_notch.value or pointer

    rotate=[]

    if num==1:
        ptr=rotor_list[ptr+1]
        if ptr_ctr1>26:
            ptr_ctr1=0

    else:
        if ptr_ctr1 

    for i in fleet pos:
        if ((i+ptr)>digits):
            val=rotor_list[((i+ptr)-digits)+1]
            rotate.append(val)

        else:
            val=rotor_list[ptr+1]
            rotate.append(val)
                
    for i in rotate:
        rotor.append(dict_rotor.value(i))         

        
def reflector(fleet_pos,fleet_out):
    for i in fleet_pos:
        fleet_out.append(dict_reflector.value(i))        

#main:
ptr_rotor1=0
ptr_rotor2=0
ptr_rotor3=0

ptr_rotor1_notch=0
ptr_rotor2_notch=0
ptr_rotor3_notch=0

fleet_position=scan for value:
convert_to_list(fleet_pos,fleet_pos_l)
plugboard(fleet_pos_l,fleet_pos_plug)

rotor(1,fleet_pos_plug,fleet_pos_rot1)
rotor(2,fleet_pos_plug,fleet_pos_rot2)
rotor(3,fleet_pos_plug,fleet_pos_rot3)

reflector(fleet_pos_rot3,fleet_pos_ref)

rotor(3,fleet_pos_ref,fleet_pos_rot3_en)
rotor(2,fleet_pos_rot3_en,fleet_pos_rot2_en)
rotor(1,fleet_pos_rot1_en,fleet_pos_rot1_en)

plugboard(fleet_pos_rot1_en)

bulb(fleet_pos_rot1_en)


#main func call

'''
  