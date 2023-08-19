from sklearn.neighbors import RadiusNeighborsClassifier
import numpy as np

def sort_location(service_location,radius,user_location):

    # Example dataset of 5 coordinates
    example_coordinates = np.array(service_location)

    user_coordinate = np.array([user_location])


    # Set the radius to 2 kilometers
    radius_km = radius

    # Convert radius from kilometers to latitude and longitude using the provided formula
    earth_radius_km = 6371.0
    radius_lat_lon = np.degrees(radius_km / earth_radius_km)

    # Create dummy labels for training (not used for the actual task)
    dummy_labels = np.zeros(example_coordinates.shape[0])

    # Create and train the RadiusNeighborsClassifier with dummy labels
    radius_classifier = RadiusNeighborsClassifier(radius=radius_lat_lon)
    radius_classifier.fit(example_coordinates, dummy_labels)
    print(user_coordinate)
    # Find coordinates within the specified circle
    indices = radius_classifier.radius_neighbors(user_coordinate, return_distance=False)[0]

    print(indices)
    coordinates_in_circle = example_coordinates[indices]

    # Print the coordinates within the circle
    print("Coordinates within the specified circle:")
    sorted_location=list()
    print(coordinates_in_circle)
    for coordinate in coordinates_in_circle:
        sorted_location.append(coordinate)
        print(coordinate)
radius=4.0
service_location=[]
user_location=[10.826791727279064, 77.06045867362013]
service_details=[{'name':'p1','age':10,'service':'plumber','coordinates':(10.83056425650903, 77.0673895019098)},
 {'name':'p2','age':21,'service':'garderner','coordinates':(10.880113699590112, 76.88839388766401)},
 {'name':'p3','age':21,'service':'garderner','coordinates':(10.733748736388042, 76.92634790681397)},
 {'name':'p4','age':21,'service':'garderner','coordinates':(11.057429829574625, 75.87659990960414)},
 {'name':'p5','age':21,'service':'garderner','coordinates':(10.473138149687488, 77.47857289617184)},]
for service_detail in service_details:
    service_location.append(list(service_detail['coordinates']))
print(sort_location(service_location,radius,user_location))