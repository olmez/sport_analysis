from ctypes import sizeof
from access_token_from_strava import access_token_from_strava
from parse_running_activity_strava import parse_running_activity_strava
import matplotlib.pyplot as plt

print("Analysis for the sports data is starting!!!")

if __name__ == "__main__":
    print("Analyzing...")
    access_token_from_strava_ = access_token_from_strava()
    access_token_from_strava_.run()
    name = []
    distance = []
    moving_time = []
    start_date = []
    average_speed = []
    average_heartrate = []
    for i in range(30):
        print(i)
        if access_token_from_strava_.activities_data[i]["type"] == "Run":
            parse_running_activity_strava_ = parse_running_activity_strava(access_token_from_strava_.activities_data[i])
            name.append(parse_running_activity_strava_.name) 
            distance.append(parse_running_activity_strava_.distance) 
            moving_time.append(parse_running_activity_strava_.moving_time) 
            start_date.append(parse_running_activity_strava_.start_date) 
            average_speed.append(parse_running_activity_strava_.average_speed) 
            average_heartrate.append(parse_running_activity_strava_.average_heartrate) 
    
    fig, axs = plt.subplots(3)
    fig.suptitle('Running Analysis')
    axs[0].plot(range(len(name)), distance)
    axs[1].plot(range(len(name)), average_speed)
    axs[2].plot(range(len(name)), average_heartrate)
    plt.show()
    
