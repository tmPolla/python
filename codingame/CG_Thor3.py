#codingame Thor feladat

#Tower
light_x=36
light_y=17
#Thor
initial_tx=0
initial_ty=0


border_min_x=0
border_min_y=0

border_max_x=40
border_max_y=18

#initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x

while True:
    if ((light_x==initial_tx) and (light_y==initial_ty)): exit()
    
    if (initial_ty>light_y and initial_tx<light_x and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        initial_tx = initial_tx+1
        initial_ty = initial_ty+1
        print 'NE'
        #print "Border min: ",border_min_x, border_min_y
        #print "Border max: ",border_max_x, border_max_y
        #print "Tower: ",light_x,light_y
        #print "Thor: ",initial_tx, initial_ty
        continue          

    elif (initial_tx>light_x and initial_ty<light_y and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        initial_tx = initial_tx-1
        initial_ty = initial_ty+1
        print 'SW'
        # print "Border min: ",border_min_x, border_min_y
        # print "Border max: ",border_max_x, border_max_y
        # print "Tower: ",light_x,light_y
        # print "Thor: ",initial_tx, initial_ty
        continue

    elif (initial_ty<light_y and initial_tx<light_x and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        initial_tx = initial_tx+1
        initial_ty = initial_ty+1
        # print "Border min: ",border_min_x, border_min_y
        # print "Border max: ",border_max_x, border_max_y
        # print "Tower: ",light_x,light_y
        # print "Thor: ",initial_tx, initial_ty
        print 'SE'
        continue

    elif (initial_ty>light_y and initial_tx>light_x and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        initial_ty = initial_ty-1
        initial_tx = initial_tx-1
        print 'NW'
        #print "Border min: ",border_min_x, border_min_y
        #print "Border max: ",border_max_x, border_max_y
        #print "Tower: ",light_x,light_y
        #print "Thor: ",initial_tx, initial_ty
        continue

    elif (initial_tx<light_x and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        print 'E'
        #print "Border min: ",border_min_x, border_min_y
        #print "Border max: ",border_max_x, border_max_y
        #print "Tower: ",light_x,light_y
        #print "Thor: ",initial_tx, initial_ty
        initial_tx = initial_tx+1
        continue
        
    elif (initial_tx>light_x and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        print 'W'
        #print "Border min: ",border_min_x, border_min_y
        #print "Border max: ",border_max_x, border_max_y
        #print "Tower: ",light_x,light_y
        #print "Thor: ",initial_tx, initial_ty
        initial_tx = initial_tx-1
        continue
       
    elif (initial_ty<light_y and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        print 'S'
        #print "Border min: ",border_min_x, border_min_y
        #print "Border max: ",border_max_x, border_max_y
        #print "Tower: ",light_x,light_y
        #print "Thor: ",initial_tx, initial_ty
        initial_ty = initial_ty+1
        continue

    elif (initial_ty>light_y and initial_ty>=border_min_y and initial_tx>=border_min_x and initial_ty<=border_max_y and initial_tx<=border_max_x):
        print 'N'
        #print "Border min: ",border_min_x, border_min_y
        #print "Border max: ",border_max_x, border_max_y
        #print "Tower: ",light_x,light_y
        #print "Thor: ",initial_tx, initial_ty
        initial_ty = initial_ty-1
        continue
    




