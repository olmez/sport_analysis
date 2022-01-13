from access_token_from_strava import access_token_from_strava
from parse_running_activity_strava import parse_running_activity_strava
print("Analysis for the sports data is starting!!!")

if __name__ == "__main__":
    print("Analyzing...")
    access_token_from_strava_ = access_token_from_strava()
    access_token_from_strava_.run()
    parse_running_activity_strava_ = parse_running_activity_strava(access_token_from_strava_.activities_data[0])
    print(parse_running_activity_strava_.name)
    print(parse_running_activity_strava_.distance)
    print(parse_running_activity_strava_.moving_time)