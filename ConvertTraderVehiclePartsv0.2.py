import json

def convert_config(input_file, output_file):
    vehicles = []
    current_vehicle = None

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith("<VehicleParts> "):
                if current_vehicle:
                    vehicles.append(current_vehicle)

                vehicle_name = line.replace("<VehicleParts> ", "")
                current_vehicle = {
                    "VehicleName": vehicle_name,
                    "Height": 0,
                    "VehicleParts": []
                }

            elif current_vehicle:
                part = line.strip()
                if part:  # Check if the line is not empty
                    current_vehicle["VehicleParts"].append(part)

    # Handle wheel parts for each vehicle
    for vehicle in vehicles:
        wheel_count = vehicle["VehicleParts"].count(vehicle["VehicleParts"][-1])
        if wheel_count > 0:
            vehicle["VehicleParts"] = vehicle["VehicleParts"][:-wheel_count] + [vehicle["VehicleParts"][-1]] * 7

    with open(output_file, 'w') as f:
        json.dump(vehicles, f, indent=4)

#File paths
input_file = "TraderVehicleParts.txt"
output_file = "TraderPlusVehiclesConfig.json"

convert_config(input_file, output_file)