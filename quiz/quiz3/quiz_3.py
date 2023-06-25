# Written by *** for COMP9021
#
# At stage 0, start with a toothpick centered at (0, 0).
# There is a free tip at the top, at coordinates (0, 2),
# and a free tip at the bottom, at coordinates (0, -2):
# 
#         *
#         *
#         *
#         *
#         *
#         
# At stage 1, perpendically place toothpicks on those tips.
# So there are now 3 toothpicks and 4 free tips,
# a top left one at coordinates (-2, 2),
# a top right one at coordinates (2, 2),
# a bottom left one at coordinates (-2, -2), and
# a bottom right one at coordinates (2, -2):
# 
#     * * * * *
#         *
#         *
#         *
#     * * * * *
#     
# At stage 2, perpendically place toothpicks on those tips.
# So there are now 7 toothpicks and 4 free tips,
# a top left one at coordinates (-2, 4),
# a top right one at coordinates (2, 4),
# a bottom left one at coordinates (-2, -4), and
# a bottom right one at coordinates (2, -4):
# 
# 
#     *       * 
#     *       *
#     * * * * *
#     *   *   *
#     *   *   *
#     *   *   *
#     * * * * *
#     *       *
#     *       *
# 
# Implements a function
# tooth_picks(stage, top_left_corner, bottom_right_corner)
# that displays, using black and white squares,
# that part of the plane that fits in a rectangle
# whose top left and bottom right corners are provided by the
# second and third arguments, respectively, at the stage of the
# construction provided by the first argument.
# You can assume that stage is any integer between 0 and 1000;
# top_left_corner and bottom_right_corner are arbitrary pairs
# of integers, but practically such that the output can fit
# on the screen.
# 
# For a discussion about the construction, see
# https://www.youtube.com/watch?v=_UtCli1SgjI&t=66s
# The video also points to a website that you might find useful:
# https://oeis.org/A139250/a139250.anim.html

def  tooth_picks(stage,top_left_corner,bottom_right_corner):

    min_x,max_y = top_left_corner
    max_x,min_y = bottom_right_corner
   
    black_points = [] # all black points
    last_ends = [(0,0)]
    from collections import Counter
    
    for i in range(stage+1):
        current_starts = last_ends[::] #end of last time is the beginning of this time
        current_ends = []
        current_black_points = []

        for cur_x, cur_y in current_starts:
            three_inc = [-1,0,1] #increment -1 +0 or +1
            if i%2==0: #vertical output when i is an even
                if min_y <= cur_y-2 <= max_y and (cur_x,cur_y-2) not in black_points:
                    current_ends.append((cur_x,cur_y-2))
                # judge the first and second end points
                if min_y <= cur_y+2 <= max_y and (cur_x,cur_y+2) not in black_points:
                    current_ends.append((cur_x,cur_y+2))
                # add three points in the middle
                current_black_points.extend([(cur_x,cur_y+inc_y) for inc_y in three_inc
                                            if min_y <=cur_y+inc_y <= max_y])

            else: # landscape orientation when is is an odd
                if min_x <=cur_x-2 <= max_x and (cur_x-2,cur_y) not in black_points:
                    current_ends.append((cur_x-2,cur_y))
                
                if min_x <=cur_x+2 <= max_x and (cur_x+2,cur_y) not in black_points:
                    current_ends.append((cur_x+2,cur_y))
                
                current_black_points.extend([(cur_x+inc_x,cur_y) for inc_x in three_inc
                                            if min_x <=cur_x+inc_x <= max_x])

        frequence = Counter(current_ends) # count end points
        last_ends = []
        for key,value in frequence.items():
            if value == 1: #edge points can only be used once
                last_ends.append(key)
    #the location of all the black squares(edge points+intermediate points)
        black_points.extend(current_black_points+current_ends)

    # print all white and black squares according to the rules
    cur_y = max_y
    while cur_y >= min_y:
        cur_x=min_x
        while cur_x<=max_x:
            if(cur_x,cur_y) in black_points:
                print("⬛",end="")
            else:
                print("⬜",end="")
    
            cur_x+=1
        print()
        cur_y-=1
