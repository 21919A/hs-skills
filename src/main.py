#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()

DEFAULT_THRUST_PID_CONFIG.proportional = 0.08


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")
    controller.buttonX.pressed(lambda: pid_driver.drive(1000))
    controller.buttonY.pressed(lambda: pid_driver.drive(-1000))
    controller.buttonLeft.pressed(lambda: pid_turner.turn(-90,FRAME_HEADING_RELATIVE))
    controller.buttonRight.pressed(lambda: pid_turner.turn(90, FRAME_HEADING_RELATIVE))

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")



def autonomous_function():
    """Function for the autonomous part of a competition match"""


    # Reset odometry to the starting autonomous position
    odometry.reset(PositionWithHeading(-1500, 600, 270))

    # # Then try resetting it to GPS if GPS sensor is installed and reports high quality
    reset_odometry_to_gps()

    log(("Competition", "competition"), "autonomous_begin")

    intake_1st_stage.set_velocity(450, RPM)
    intake_2nd_stage.set_velocity(450, RPM)



    wait(100, MSEC)

    # wait(500, MSEC)
    reset_odometry_to_gps()

    pid_mover.move(Position(-1200, 600), FRAME_ABSOLUTE, REVERSE, True)

    clamp.set(True)

    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)

  
    pid_turner.turn(90, FRAME_ABSOLUTE)

    pid_driver.drive(600)
    
    wait(250, MSEC)
    reset_odometry_to_gps()
    pid_turner.turn(0, FRAME_ABSOLUTE)

    pid_driver.drive(600)

    wait(250, MSEC)
    reset_odometry_to_gps()
    pid_turner.turn(270, FRAME_ABSOLUTE)

    pid_driver.drive(900)

    wait(250, MSEC)
    reset_odometry_to_gps()
    pid_turner.turn(120, FRAME_HEADING_RELATIVE)

    pid_driver.drive(300)
    pid_driver.drive(-50)

    wait(250, MSEC)
    reset_odometry_to_gps()
    pid_turner.turn(90, FRAME_HEADING_RELATIVE)

    pid_driver.drive(-175)

    clamp.set(False)
    intake_2nd_stage.spin(REVERSE)

    wait(100, MSEC)
    pid_driver.drive(350)
    pid_turner.turn(353, FRAME_ABSOLUTE)
    intake_2nd_stage.spin(FORWARD)
    pid_driver.drive(-1950, True)

    clamp.set(True)
    pid_turner.turn(90, FRAME_HEADING_RELATIVE)

    reset_odometry_to_gps()
    pid_driver.drive(600)
    pid_turner.turn(90, FRAME_HEADING_RELATIVE)

    pid_driver.drive(500)
    reset_odometry_to_gps()
    pid_turner.turn(90, FRAME_HEADING_RELATIVE)

    pid_driver.drive(800)
    pid_turner.turn(-120, FRAME_HEADING_RELATIVE)

    pid_driver.drive(300)
    pid_driver.drive(-50)
    wait(250, MSEC)
    reset_odometry_to_gps()
    pid_turner.turn(-90, FRAME_HEADING_RELATIVE)
    
    pid_driver.drive(-175)
    intake_2nd_stage.spin(REVERSE)
    clamp.set(False)
    pid_driver.drive(200)



    # pid_mover.move(Position(1200, -1200), FRAME_ABSOLUTE)

    # sleep(1000, TimeUnits.MSEC)

    # reset_odometry_to_gps()

    # pid_mover.move(Position(-1200, -1200), FRAME_ABSOLUTE)

    # sleep(1000, TimeUnits.MSEC)

    # reset_odometry_to_gps()

    # pid_mover.move(Position(-1200, 1200), FRAME_ABSOLUTE)

    # sleep(1000, TimeUnits.MSEC)

    # reset_odometry_to_gps()

    # pid_mover.move(Position(1200, 1200), FRAME_ABSOLUTE)

    # sleep(1000, TimeUnits.MSEC)

    # reset_odometry_to_gps()

    # pid_aimer.aim(Position(1200, -1200), FRAME_ABSOLUTE)

    # sleep(1000, TimeUnits.MSEC)

    # reset_odometry_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
