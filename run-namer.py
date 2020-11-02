#!/usr/bin/python3
"""
Generates "suitable" run names for excercise records (such as RunKeeper or Strava).
"""

import numpy as np
import argparse

day_events_list = [
    ("breakfast", 700, 830),  # event name, start time, end time (2400 Hr time)
    ("brunch", 1030, 1130),
    ("elevenses", 1045, 1115),
    ("lunch", 1130, 1300),
    ("tea", 1545, 1630),
    ("supper", 1800, 1900),
    ("dinner", 1900, 2100),
    ("morning", 0, 1200),
    ("afternoon", 1200, 1800),
    ("evening", 1800, 2400),
    ("midnight", 2400, 2400)
]

activity_names = {
    "run": [
        "run", "trot", "whiz", "skedaddle", "bound", "canter", "leap",
        "lope", "skip", "spring", "barrel", "belt", "blast", "blaze", "blow",
        "bolt", "breeze", "bustle", "buzz", "cannonball", "careen", "course",
        "hasten", "hotfoot", "hurl", "hurry", "hurtle", "hustle", "jet", "leg",
        "pelt", "race", "ram", "rip", "rocket", "rush", "shoot", "speed", "whirl",
        "whisk", "zip", "zoom", "nip", "scoot", "scurry", "scuttle", "hightail",
        "gallop", "flit"
    ]
}


def get_random_time_desc(activity_time):
    name, start, end = day_events_list[np.random.randint(0, len(day_events_list) - 1)]
    mod = ""
    if activity_time < start:
        mod = "Pre-"
    elif activity_time > end:
        mod = "Post-"

    return mod + name.capitalize()


def get_random_activity_desc(activity_class):
    return np.random.choice(activity_names[activity_class]).capitalize()


def get_activity_name(activity_time, activity_class):
    return "%s %s" % (get_random_time_desc(activity_time), get_random_activity_desc(activity_class))



def print_activity(time_num, name):
    def twelve_hour(a):
        if a == 0:
            a = 12
        return a
    print("%2d:%02d %s" % (twelve_hour((time_num % 1200)//100), time_num % 100, "am" if time_num < 1200 else "pm"), name)


def demo(n_runs=1):
    # demo
    descs = []
    for i in range(n_runs):
        demo_time = np.random.randint(24 * 60)
        demo_time = 100 * (demo_time // 60) + demo_time % 60
        demo_type = "run"
        descs.append((demo_time, get_activity_name(demo_time, "run")))
    return descs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="run-namer")
    parser.add_argument("--time", "-t", help="The start time of an activity in 24-hour format ")
    args = parser.parse_args()

    descs = []
    if args.time is not None:
        time_num = int(args.time.replace(':', ''))
        descs.append((time_num, get_activity_name(time_num, "run")))
    else:
        descs = demo(10)

    for time_num, name in descs:
        print_activity(time_num, name)
