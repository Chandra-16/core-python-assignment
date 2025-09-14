def book_seat(booked, seat, total):
    if seat in booked:
        print(f"Seat {seat} is already booked.")
    elif seat < 1 or seat > total:
        print(f"Seat {seat} is invalid.")
    else:
        booked.append(seat)
        print(f"Seat {seat} booked.")

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
        print(f"Seat {seat} cancelled.")
    else:
        print(f"Seat {seat} is not booked.")

def available(total, booked):
    return [seat for seat in range(1, total + 1) if seat not in booked]

total_seats = int(input("Enter total number of seats: "))
booked_seats = list(map(int, input("Enter booked seats (space separated): ").split()))

seat = int(input("Enter seat number to book: "))
book_seat(booked_seats, seat, total_seats)

cancel_seat_num = int(input("Enter seat number to cancel: "))
cancel_seat(booked_seats, cancel_seat_num)

print("Available seats:", available(total_seats, booked_seats))