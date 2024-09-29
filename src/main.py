#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function_absolute():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    # Reset odometry to the starting autonomous position
    odometry.reset(PositionWithHeading(1200, 1200, 0))

    # Then try resetting it to GPS if GPS sensor is installed and reports high quality
    reset_odometry_to_gps()

    pid_mover.move(Position(1200, -1200), FRAME_ABSOLUTE)

    reset_odometry_to_gps()

    pid_mover.move(Position(-1200, -1200), FRAME_ABSOLUTE)

    reset_odometry_to_gps()

    pid_mover.move(Position(-1200, 1200), FRAME_ABSOLUTE)

    reset_odometry_to_gps()

    pid_mover.move(Position(1200, 1200), FRAME_ABSOLUTE)

    reset_odometry_to_gps()

    log(("Competition", "competition"), "autonomous_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    # Reset odometry to the starting autonomous position
    odometry.reset(PositionWithHeading(1200, 1200, 180))

    # Then try resetting it to GPS if GPS sensor is installed and reports high quality
    reset_odometry_to_gps()

    pid_mover.move(Position(1200, -1200), FRAME_ABSOLUTE)

    sleep(1000, TimeUnits.MSEC)

    reset_odometry_to_gps()

    pid_mover.move(Position(-1200, -1200), FRAME_ABSOLUTE)

    sleep(1000, TimeUnits.MSEC)

    reset_odometry_to_gps()

    pid_mover.move(Position(-1200, 1200), FRAME_ABSOLUTE)

    sleep(1000, TimeUnits.MSEC)

    reset_odometry_to_gps()

    pid_mover.move(Position(1200, 1200), FRAME_ABSOLUTE)

    sleep(1000, TimeUnits.MSEC)

    reset_odometry_to_gps()

    pid_aimer.aim(Position(1200, -1200), FRAME_ABSOLUTE)

    sleep(1000, TimeUnits.MSEC)

    reset_odometry_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
