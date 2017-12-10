def acceleration(final_vel, initial_vel, time):
    accelerate=(final_vel-initial_vel)/time
    print("The acceleration when final velocity is {}m/s, initial velocity is {}m/s and time is {}s is: ".format(final_vel,initial_vel,time),accelerate)

acceleration(25, 0, 10)

