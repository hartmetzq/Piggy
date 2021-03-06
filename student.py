#!/usr/bin python3
from collections import OrderedDict
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 90
        self.RIGHT_DEFAULT = 92
        self.SAFE_DISTANCE = 250
        self.CLOSE_DISTANCE = 150
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        
        if not self.safe_to_dance():
            return False # Shut it down 
        for x in range(2):
            self.chacha_slide()
            self.backward_shuffle()
            self.twist_move()
            self.headwhip()
            self.forward_shuffle()

        
        
        # New Dance 
            #self.chacha_slide ()
            #self.backward_shuffle()
            #self.twist_move()
            #self.forward_shuffle()
            #self.headwhip()

    def chacha_slide(self):
        """This is a new move to try and replicate the chacha slide"""
        # Try to replicate the chacha slide in the loop which goes through once 
        for x in range(1):
            self.turn_to_deg(90)
            time.sleep(.1)
            self.back()
            time.sleep(.1)
            self.turn_by_deg(270)
            time.sleep(.1)
            self.turn_by_deg(270)
            time.sleep(.1)
            self.turn_to_deg(90)
            time.sleep(.1)
            self.back()
            time.sleep(.1)
            self.turn_by_deg(180)
            time.sleep(.1)
            self.turn_by_deg(180)
            time.sleep(.1)
            self.fwd()
            time.sleep(.1)
            self.stop()

    def backward_shuffle(self):
        """This is a dance that will make the robot move back aand shake at the same time"""
        #The shuffle is 12 because that way it shakes for a decent amount of time 
        for x in range(12):
            self.right(primary=-60, counter=0)
            time.sleep(.1)
            self.left(primary=-60, counter=0)
            time.sleep(.1)
        #Then it stops and proceeds to do the same thing forward
        for x in range(12):
            self.right(primary=60, counter=0)
            time.sleep(.1)
            self.left(primary=60, counter=0)
            time.sleep(.1)
        for x in range(12):
            self.right(primary=-60, counter=0)
            time.sleep(.1)
            self.left(primary=-60, counter=0)
            time.sleep(.1)
        for x in range(12):
            self.right(primary=60, counter=0)
            time.sleep(.1)
            self.left(primary=60, counter=0)
            time.sleep(.1)
        self.stop()
  
    def twist_move(self): 
        """Dance to demonstrate the use of twirling and turning head"""
        # Loop of the robot moving forward 
        for x in range(6): 
            self.fwd()
            time.sleep(.1)
            self.stop()
            time.sleep(.1)
        # Then proceeds to twist in different directions and turn its head 
        self.fwd()
        time.sleep(1) 
        self.servo(1800)
        time.sleep(.5)
        self.servo(1200)
        time.sleep(.1)
        self.turn_by_deg(180)
        time.sleep(.1)
        self.turn_by_deg(180)
        time.sleep(.1) 
        self.back()
        time.sleep(.5)
        self.servo(1200)
        time.sleep(.1)
        self.servo(1800)
        time.sleep(.1)
        self.turn_by_deg(180)
        time.sleep(.1)
        self.turn_to_deg(180)
        time.sleep(.1)
        self.stop()

    def headwhip(self): 
        """This move shows the robots ability to look around and do different moves at the same time"""
        #first loop has it move forward
        for x in range(1): 
            self. fwd()
            time.sleep(.1)
            #This loop is the head shaking no 
            for x in range(3):
                self.servo(1900)
                time.sleep(.2)
                self.servo(1050)
                time.sleep(.1)
            # Does a 360 turn 
            self.turn_by_deg(180)
            time.sleep(.01)
            self.turn_by_deg(180)
            time.sleep(.01)
            #Shakes his head again in the no motion 
            for x in range(3):
                self.servo(1900)
                time.sleep(.2)
                self.servo(1050)
                time.sleep(.1)
            # Moves back and shakes head which is in the loop 
            self.back()
            time.sleep(.5)
            for x in range(3):
                self.servo(1900)
                time.sleep(.2)
                self.servo(1050)
                time.sleep(.1)
            # Does another 360 while shaking head which is shown in loop 
            self.turn_by_deg(180)
            time.sleep(.01)
            self.turn_by_deg(180)
            time.sleep(.01)
            for x in range(3):
                self.servo(1900)
                time.sleep(.2)
                self.servo(1050)
                time.sleep(.1)
            self.stop()

#forward shuffle code taken from Hayden 
    def forward_shuffle(self): 
        """ This move is a snake backwards smoothy then stip and do it forward"""
        # First loop is the snake motion bakward 
        for x in range(6):
            self.right(primary=-90, counter=-30)
            time.sleep(.7)
            self.left(primary=-90, counter=-30)
            time.sleep(.7)
        # Stop and turn by 180 degrees 
        self.turn_by_deg(180)
        time.sleep(.01)
        # This loop shows the snake move going forward 
        for x in range(6):
            self.right(primary=90, counter=30)
            time.sleep(.7)
            self.left(primary=90, counter=30)
            time.sleep(.7)
        self.stop()
        # The end of the dance 








            
    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        # check for allfail/early termination conditions 
        for x in range(4):
            if self.read_distance() < 300: 
                print("NOT SAFE TO DANCE")
                return False 
            else: 
                self.turn_by_deg(90)

        #After all checks have been done, We deduce it's safe 
        print("SAFE TO DANCE")
        return True 
    
    def shake(self):
        self.deg_fwd(720)
        self.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-450, self.MIDPOINT+450, 30):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()
        # sort the scan data for easier analysis 
        self.scan_data = OrderedDict(sorted(self.scan_data.items()))

    def right_or_left(self): 
        """Should I turn left or right? Returns a 'r' or 'l' based on scan data"""
        self.scan()
        # average up the3 distances on the right side 
        right_sum = 0 
        right_avg = 0
        left_sum = 0
        left_avg = 0 
        for angle in self.scan_data: 
            # average up the distance on the right side 
            if angle < self.MIDPOINT: 
                right_sum += self.scan_data[angle]
                right_avg += 1 
            else: 
                left_sum += self.scan_data[angle]
                left_avg += 1 
        # calculate averages 
        left_avg = left_sum / left_avg
        right_avg = right_sum / right_avg

        if left_avg > right_avg: 
            return 'l'
        else: 
            return 'r'

    
    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        # do a scan of area in front of robot 
        count = 0 
        for x in range(4):
            self.scan()
        # FIGURE OUT HOW MANY OBSTACLES THERE WERE 
            see_an_object = False 
            
        # print the results 
            for angle in self.scan_data: 
                dist = self.scan_data[angle] 
                if dist < self.SAFE_DISTANCE and not see_an_object:
                    see_an_object = True 
                    count += 1 
                    print("~~~ I SEE SOMETHING ~~~")
                elif dist > self.SAFE_DISTANCE and see_an_object:
                    see_an_object = False 
                    print("I guess the object is gone")
           
                print("ANGLE: %d | DIST: %d" % (angle, dist))
            print("\nI saw %d objects" % count)
            self.turn_by_deg(45)
        print("\nI saw %d objects" % count)
        

    def quick_check(self):
        """ Moves the servo to three angles and performs a distance check"""
        # loop 3x and move the servo
        for ang in range(self.MIDPOINT - 100, self.MIDPOINT + 101, 100):
            self.servo(ang)
            time.sleep(.1)
            if self.read_distance() < self.SAFE_DISTANCE:
                return False 
        # if the 3 part check did not freak out 
        return True
   
    def turn_until_clear(self):
        """Rotate right until no obsatacle is seen"""
        print("----!!! TURNING UNTIL CLEAR !!! ------")
        # make sure we are looing straight 
        self.servo(self.MIDPOINT)
        # so long as we see something close keep turning left 
        while self.read_distance() < self.SAFE_DISTANCE + 100:
            self.left(primary=40, counter=-40)
            time.sleep(.05)
        # stop motion before we end the method 
        self.stop()

   
    def nav(self):
        """ Auto-Pilot Program """
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
    
        exit_ang = self.get_heading()
        # because I've written down the exit's angle, at anytime I can use:
        # self.turn_to_deg(exit_ang)
        turn_count = 0

        while True:
            if not self.quick_check(): 
                turn_count += 1
                self.stop()
                time.sleep(.01)
                self.back()
                time.sleep(.7)
                self.stop()
                # self.turn_until_clear()
                if turn_count > 3 and turn_count % 4 == 0:
                    self.turn_to_deg(exit_ang)

                elif 'l' in self.right_or_left():
                    self.turn_by_deg(-35)
                else: 
                    self.turn_by_deg(35)
            else:
                self.fwd()
                
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
