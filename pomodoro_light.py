from functions import *
import schedule
from user import bridge_url, hue_user
import time


# Define pause light
lights = get_connected_lights(bridge_url, hue_user)
light1, light2, light3 = lights


# Define functions for setting lights
def set_pause_light():
    set_color(light=light1, hue=23181, sat=215)
    set_color(light=light3, hue=23181, sat=215)


def set_work_light():
    set_color(light=light1, hue=8418, sat=140)
    set_color(light=light3, hue=8418, sat=140)


def set_lunch_break_light():
    set_color(light=light1, hue=42167, sat=141)
    set_color(light=light3, hue=41106, sat=141)


def set_work_day_over_light():
    set_color(light=light1, hue=48235, sat=175)
    set_color(light=light3, hue=58728, sat=217)


# Define times to change lights at
start_pause_times = ['09:25', '09:55', '10:25', '10:55', '11:25', '13:25', '13:55', '14:25', '14:55', '15:25']
start_work_times = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30',
                    '15:00', '15:30']
start_lunch_break_time = '12:00'
start_party_time = '16:00'


# Add functions to schedule
# Set break light
for t in start_pause_times:
    schedule.every().day.at(t).do(set_pause_light)

# Set work light
for t in start_work_times:
    schedule.every().day.at(t).do(set_work_light)

# Set lunch break light
schedule.every().day.at(start_lunch_break_time).do(set_lunch_break_light)

# Set work day over light
schedule.every().day.at(start_party_time).do(set_work_day_over_light)

print('Running pomodoro light schedule')
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    set_color_all(bridge_url, hue_user, hue=8418, sat=140)
    print('Program stopped')
