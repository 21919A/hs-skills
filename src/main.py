#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # General event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    # Reset robot position and inertial heading to the starting autonomous position and heading
    robot_position.reset(Position(-1650, 0))
    inertial.set_heading(90)

    reset_robot_position_and_heading_to_gps()

    intake.spin_forward()

    wait(1000, MSEC)

    intake.stop()

    trigger_mover.move(Position(-1230, 0))
    slow_trigger_mover.move(Position(-1230, 600), REVERSE)

    wait_and_clamp()

    trigger_turner.turn(90, FRAME_ABSOLUTE)
    reset_robot_position_and_heading_to_gps()

    intake.spin_forward()
    trigger_mover.move(Position(-720, 600))

    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-610, 1200))

    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1230, 1500))

    trigger_mover.move(Position(-610, 1200), REVERSE)
    reset_robot_position_and_heading_to_gps()

    trigger_mover.move(Position(-1410, 1200))

    trigger_mover.move(Position(-1500, 1350), REVERSE)
    unclamp()

    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1250, 600))
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1200, 0), REVERSE)
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    slow_trigger_driver.drive(-650)
    wait_and_clamp()

    reset_robot_position_and_heading_to_gps()

    intake.spin_forward()
    trigger_mover.move(Position(-600, -600))
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-600, -1200))
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1200, -1500))
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-600, -1200), REVERSE)
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1400, -1200))
    trigger_mover.move(Position(-1500, -1450), REVERSE)
    unclamp()
    trigger_mover.move(Position(-1400, -1200))
    intake.stop()

    # use this for extra ring
    trigger_mover.move(Position(0, -1450))
    intake.spin_forward()
    wait(800, MSEC)
    intake.stop()

    # trigger_mover.move(Position(0, -1200)) # dont use for extra ring
    trigger_turner.turn(90, FRAME_ABSOLUTE)

    wait(600, MSEC)
    reset_robot_position_and_heading_to_gps(ENABLE_GPS)
    inertial.set_heading(90)


    trigger_mover.move(Position(600, -1200))
    intake.spin_forward()
    wait(300, MSEC)
    intake.stop()

    trigger_mover.move(Position(1200, -350), REVERSE)
    trigger_turner.turn(180, FRAME_ABSOLUTE)
    slow_trigger_mover.move(Position(1200, 0), REVERSE)

    wait_and_clamp()

    intake.spin_forward()
    trigger_mover.move(Position(600, -600))

    # use this for blue goal shove
    trigger_mover.move(Position(1400, -1400), REVERSE)
    unclamp()
    # trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(48, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(2800)

    wait(1000, MSEC)
    reset_robot_position_and_heading_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
