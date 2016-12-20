#codingame Thor feladat

light_x=31 
light_y=4
initial_tx=0
initial_ty=17

initial_tx=0
initial_ty=17

movement=''
step=0
space=' '
full_step = 0


stepx=1
stepy=1

while True:
    if (initial_ty>light_y and initial_tx<light_x):
        movement = movement + ('SE'+space)*stepx
        initial_tx = initial_tx+(stepx*(+1))
        initial_ty = initial_ty+(stepy*(-1))
        full_step = full_step + stepx
        print 'go1', 'X: ', initial_tx, ' : ', 'Y: ', initial_ty
    else: break
        
while True:
    if (initial_tx>light_x and initial_ty<light_y):
        movement = movement + ('NW'+space)*stepx
        initial_tx = initial_tx+(stepx*(-1))
        initial_ty = initial_ty+(stepy*(+1))
        full_step = full_step + stepx
        print 'go2', 'X: ', initial_tx, ' : ', 'Y: ', initial_ty
    else: break
    
while True:
    if (initial_ty<light_y and initial_tx<light_x):
        movement = movement + ('NE'+space)*stepx
        initial_tx = initial_tx+(stepx*(+1))
        initial_ty = initial_ty+(stepy*(+1))
        full_step = full_step + stepx
        print 'go3', 'X: ', initial_tx, ' : ', 'Y: ', initial_ty
    else: break

while True:
    if (initial_ty>light_y and initial_tx>light_x):
        movement = movement + ('SW'+space)*stepy
        initial_ty = initial_ty+(stepy*(-1))
        initial_tx = initial_tx+(stepx*(-1))
        full_step = full_step + stepx
        print 'go4', 'X: ', initial_tx, ' : ', 'Y: ', initial_ty
    else: break

stepx = abs(light_x-initial_tx)
stepy =abs(light_y-initial_ty)
    
if initial_tx<light_x:
    movement = movement + ('E'+space)*stepx
    initial_tx = initial_tx+(stepx*(+1))
    full_step = full_step + stepx
else:
    movement = movement + ('W'+space)*stepx
    initial_tx = initial_tx+(stepx*(-1))
    full_step = full_step + stepx
    
if initial_ty<light_y:
    movement = movement + ('N'+space)*stepy
    initial_ty = initial_ty+(stepy*(+1))
    full_step = full_step + stepx
else:
    movement = movement + ('S'+space)*stepy
    initial_ty = initial_ty+(stepy*(-1))
    full_step = full_step + stepx
    
    print movement
    print 'X: ', initial_tx, ' : ', 'Y: ', initial_ty
    print 'Full steps', full_step
    
    




