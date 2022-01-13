from access_token_from_strava import access_token_from_strava
print("Analysis for the sports data is starting!!!")

if __name__ == "__main__":
    print("Analyzing...")
    access_token_from_strava_ = access_token_from_strava()
    access_token_from_strava_.run()
    print(access_token_from_strava_.activities_data)
    print(access_token_from_strava_.activities_data[0]["name"])
    print(access_token_from_strava_.activities_data[0]["map"]["summary_polyline"])