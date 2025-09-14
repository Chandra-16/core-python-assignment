def calculate_fare(distance):

    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

trips = list(map(int, input("Enter trip distances (km) space separated: ").split()))

total = 0
for i, dist in enumerate(trips, start=1):
    fare = calculate_fare(dist)
    total += fare
    print(f"Trip {i}: Rs {fare}")

print("Total Fare:", f"Rs {total}")