#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # General event handling is initialized outside of this function by init_event_handling()

    controller.buttonX.pressed(lambda: trigger_driver.drive(1000))
    controller.buttonY.pressed(lambda: trigger_driver.drive(-1000))
    controller.buttonLeft.pressed(
        lambda: trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    )
    controller.buttonRight.pressed(
        lambda: trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    )

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    # Reset robot position and inertial heading to the starting autonomous position and heading
    robot_position.reset(Position(-1650, 0))
    inertial.set_heading(90)

    reset_robot_position_and_heading_to_gps()
    intake_1st_stage.set_velocity(600, RPM)
    intake_2nd_stage.set_velocity(600, RPM)
    drive_motor_group.set_velocity(600, RPM)

    intake_1st_stage.spin(FORWARD)
    intake_2nd_stage.spin(REVERSE)


    trigger_driver.drive(100)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(-600)
    clamp.set(True)

    trigger_turner.turn(90, FRAME_ABSOLUTE)
    reset_robot_position_and_heading_to_gps()
    trigger_driver.drive(600)

    trigger_turner.turn(0, FRAME_ABSOLUTE)
    reset_robot_position_and_heading_to_gps()
    trigger_driver.drive(600)

    trigger_turner.turn(-65, FRAME_HEADING_RELATIVE)
    reset_robot_position_and_heading_to_gps()
    trigger_driver.drive(700)

    trigger_driver.drive(-700)
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(-90, FRAME_ABSOLUTE)
    trigger_driver.drive(800)

    trigger_turner.turn(-115, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(-300)
    clamp.set(False)

    trigger_driver.drive(780)
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(-155, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(-1370)
    clamp.set(True)

    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(600)

    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(600)
    reset_robot_position_and_heading_to_gps()

    trigger_turner.turn(65, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(700)
    trigger_driver.drive(-700)

    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(25, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(800)

    trigger_turner.turn(115, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(-300)
    clamp.set(False) 

    trigger_driver.drive(300)
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(90, FRAME_ABSOLUTE)

    intake_1st_stage.stop()
    intake_2nd_stage.stop()
    trigger_driver.drive(2000)

    intake_1st_stage.spin(REVERSE)
    wait(100, MSEC)
    intake_1st_stage.stop()

    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(115, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(-1200)
    clamp.set(True)

    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)

    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(20, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(700)

    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(900)
    trigger_turner.turn(92, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(900)
    
    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_driver.drive(600)

    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(-110, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(-800)
    clamp.set(False)

    reset_robot_position_and_heading_to_gps()
    trigger_turner.turn(-73, FRAME_HEADING_RELATIVE)
    trigger_driver.drive(3000)

    # # Then try resetting to GPS if GPS sensor is installed and reports high quality
    # reset_robot_position_and_heading_to_gps()

    # intake_1st_stage.set_velocity(450, RPM)
    # intake_2nd_stage.set_velocity(450, RPM)

    # wait(100, MSEC)

    # # wait(500, MSEC)
    # reset_robot_position_and_heading_to_gps()

    # trigger_driver.drive(-300)

    # clamp.set(True)

    # intake_1st_stage.spin(REVERSE)
    # intake_2nd_stage.spin(FORWARD)

    # trigger_turner.turn(90, FRAME_ABSOLUTE)

    # trigger_driver.drive(600)

    # wait(250, MSEC)
    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(0, FRAME_ABSOLUTE)

    # trigger_driver.drive(600)

    # wait(250, MSEC)
    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(270, FRAME_ABSOLUTE)

    # trigger_driver.drive(900)

    # wait(250, MSEC)
    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(120, FRAME_HEADING_RELATIVE)

    # trigger_driver.drive(300)
    # trigger_driver.drive(-50)

    # wait(250, MSEC)
    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(90, FRAME_HEADING_RELATIVE)

    # trigger_driver.drive(-175)

    # clamp.set(False)
    # intake_2nd_stage.spin(REVERSE)

    # wait(100, MSEC)
    # trigger_driver.drive(370)
    # reset_robot_position_and_heading_to_gps()
    # wait(250, MSEC)
    # trigger_turner.turn(357, FRAME_ABSOLUTE)
    # intake_2nd_stage.spin(FORWARD)
    # trigger_driver.drive(-2000)

    # clamp.set(True)
    # trigger_turner.turn(83, FRAME_HEADING_RELATIVE)

    # reset_robot_position_and_heading_to_gps()
    # trigger_driver.drive(630)
    # trigger_turner.turn(97, FRAME_HEADING_RELATIVE)

    # trigger_driver.drive(475)
    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(270, FRAME_ABSOLUTE)

    # trigger_driver.drive(800)
    # trigger_turner.turn(-120, FRAME_HEADING_RELATIVE)

    # trigger_driver.drive(305)
    # trigger_driver.drive(-50)
    # wait(250, MSEC)
    # reset_robot_position_and_heading_to_gps()
    # trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)

    # trigger_driver.drive(-260)
    # intake_2nd_stage.spin(REVERSE)
    # clamp.set(False)
    # trigger_driver.drive(200)

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
