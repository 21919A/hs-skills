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

    clamp.set(True)

    trigger_turner.turn(90, FRAME_ABSOLUTE)
    reset_robot_position_and_heading_to_gps()

    intake.spin_forward()
    trigger_mover.move(Position(-610, 600))

    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-610, 1200))

    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1244, 1496))

    trigger_mover.move(Position(-610, 1200), REVERSE)
    reset_robot_position_and_heading_to_gps()

    trigger_mover.move(Position(-1410, 1200))

    trigger_mover.move(Position(-1500, 1400), REVERSE)
    clamp.set(False)

    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1230, 700))
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(-1180, 0), REVERSE)
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    slow_trigger_driver.drive(-650)
    clamp.set(True)

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
    trigger_mover.move(Position(-1500, -1200))
    trigger_mover.move(Position(-1550, -1350), REVERSE)
    clamp.set(False)
    intake.stop()

    trigger_mover.move(Position(600, -1200))
    intake.spin_forward()
    intake.stop()

    trigger_mover.move(Position(1200, 0))
    clamp.set(True)

    intake.spin_forward()
    trigger_mover.move(Position(600, -600))


    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(600)

    # trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(600)
    # reset_robot_position_and_heading_to_gps()

    # trigger_turner.turn(65, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(700)
    # trigger_driver.drive(-700)

    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(25, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(800)

    # trigger_turner.turn(115, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(-300)
    # clamp.set(False)

    # trigger_driver.drive(300)
    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(65, FRAME_HEADING_RELATIVE)

    # intake.stop()
    # trigger_driver.drive(2000)

    # intake.spin_reverse()
    # wait(100, MSEC)
    # intake.stop()

    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(115, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(-1200)
    # clamp.set(True)

    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(20, FRAME_HEADING_RELATIVE)

    # intake.spin_forward()
    # trigger_driver.drive(700)

    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(900)
    # trigger_turner.turn(92, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(900)

    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(-48, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(600)

    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(-110, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(-800)
    # clamp.set(False)

    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(-73, FRAME_HEADING_RELATIVE)
    # trigger_driver.drive(3000)

    wait(1000, MSEC)
    reset_robot_position_and_heading_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
