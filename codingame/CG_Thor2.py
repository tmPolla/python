#codingame Thor feladat
# good test phase 2
light_x=31 
light_y=4

initial_tx=31
initial_ty=16

movement=''
movement_step=''
step=0
space=' '
full_step = 0


stepx=1
stepy=1

while True:
    if ((light_x==initial_tx) and (light_y==initial_ty)): exit()
    if (initial_ty>light_y and initial_tx<light_x):
        initial_tx = initial_tx+1
        initial_ty = initial_ty+1
        full_step = full_step + stepx
        print 'NE'
        continue          

    if (initial_tx>light_x and initial_ty<light_y):
        initial_tx = initial_tx-1
        initial_ty = initial_ty-1
        full_step = full_step + stepx
        print 'SW'
        continue

    if (initial_ty<light_y and initial_tx<light_x):
        initial_tx = initial_tx+1
        initial_ty = initial_ty-1
        full_step = full_step + stepx
        print 'SE'
        continue

    if (initial_ty>light_y and initial_tx>light_x):
        initial_ty = initial_ty+1
        initial_tx = initial_tx-1
        full_step = full_step + stepx
        print 'NW'
        continue

    if initial_tx<light_x:
        print 'E'
        initial_tx = initial_tx+1
        full_step = full_step + stepx
        continue
        
    if initial_tx>light_x:
        print 'W'
        initial_tx = initial_tx-1
        full_step = full_step + stepx
        continue
       
    if initial_ty<light_y:
        print 'S'
        initial_ty = initial_ty-1
        full_step = full_step + stepx
        continue

    if initial_ty>light_y:
        print 'N'
        initial_ty = initial_ty+1
        full_step = full_step + stepx
        continue
    
    




