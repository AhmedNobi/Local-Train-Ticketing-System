import psycopg2
import datetime
import random

conn = psycopg2.connect(
    host="localhost",
    database="train_ticketing_system",
    user="your_user",
    password="your_password"
)

def generate_ticket_id():
    ticket_id = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + str(random.randint(1000, 9999))
    return ticket_id

def display_trains():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trains")
    rows = cursor.fetchall()
    print("Train No.\tFrom\tTo\tDeparture Time")
    for row in rows:
        print(f"{row[0]}\t\t{row[1]}\t{row[2]}\t{row[3]}")

def book_ticket():
    cursor = conn.cursor()
    print("Enter passenger details:")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender (M/F/O): ")
    from_station = input("From station: ")
    to_station = input("To station: ")
    departure_time = input("Departure time: ")
    ticket_id = generate_ticket_id()
    cursor.execute("INSERT INTO tickets (ticket_id, name, age, gender, from_station, to_station, departure_time) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ticket_id, name, age, gender, from_station, to_station, departure_time))
    conn.commit()
    print("Ticket booked successfully. Your ticket ID is:", ticket_id)

def main():
    while True:
        print("Welcome to the Local Train Ticketing System!")
        print("1. Display available trains")
        print("2. Book a ticket")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_trains()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
