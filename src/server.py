import socket
from datetime import datetime
import threading
import random
import os

SERVER_PORT: int = 40000
BUFFER_SIZE: int = 1024

connections = {}
rooms = []
lock = threading.Lock()

os.makedirs("logs", exist_ok=True)


class Room:
    is_pass: bool = False

    def __init__(self, room_id: str, name: str, password: str, members: dict):
        self.name = name
        self.password = password
        self.id = room_id
        self.members = members

    def is_pass_available(self):
        if self.password == "":
            self.is_pass = False
        else:
            self.is_pass = True

    def add_member(self, nickname: str, conn=None):
        with lock:
            self.members[nickname] = conn
        self.broadcast(f"{nickname} joined the room.", sender_conn=None)

    def remove_member(self, nickname: str, conn=None):
        with lock:
            if nickname in self.members:
                del self.members[nickname]
        self.broadcast(f"{nickname} left the room.", sender_conn=None)

    def broadcast(self, message: str, sender_conn=None):
        data = message.encode('utf-8')
        with lock:
            member_list = list(self.members.values())
        for conn in member_list:
            if conn != sender_conn:
                try:
                    conn.sendall(data)
                except Exception:
                    pass
        date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"logs/room_{self.id}.txt", "a", encoding="utf-8") as f:
            f.write(f"[{date_and_time}] {sender_conn}: {message}\n")


def create_room(room_id: str, room_name: str, room_pass: str, room_members: dict):
    if room_id == "":
        room_id = str(random.randint(100001, 999999))
    new_room = Room(f"{room_id}", f"{room_name}", f"{room_pass}", room_members)
    with lock:
        rooms.append(new_room)
    return new_room


def find_room(room_id: str, room_pass: str):
    with lock:
        for room in list(rooms):
            if room.id == room_id and room.password == room_pass:
                return room
    return None


def log_write(message: str):
    date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('NetworkChatLog.txt', "a", encoding='utf-8') as f:
        f.write(f"[{date_and_time}] {message}\n")


def communication(nickname: str, conn: socket.socket, room: Room):
    while True:
        try:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                log_write(f"Connection lost for user: {nickname}")
                with lock:
                    if nickname in connections:
                        del connections[nickname]
                room.remove_member(nickname, conn)
                log_write(f"{nickname} left the chat.")
                break

            print(data.decode('utf-8'))
            room.broadcast(data.decode('utf-8'), conn)

        except Exception as e:
            print(e)
            break


def client_handler(connection: socket.socket, addr):
    try:
        raw_name = connection.recv(16)
        client_nickname = raw_name.decode('utf-8', errors='ignore').strip()

        connection.sendall(b"OK")
        raw_room_id = connection.recv(16)
        room_id = raw_room_id.decode('utf-8', errors='ignore').strip()

        raw_room_pass = connection.recv(16)
        room_pass = raw_room_pass.decode('utf-8', errors='ignore').strip()

        room = find_room(room_id, room_pass)
        if room is None:
            connection.sendall(b"NO")
            data = connection.recv(BUFFER_SIZE)
            
            if data.decode('utf-8') == "CRT":
                room_name = f"{room_id}'s Room"
                room = create_room(room_id, room_name, room_pass, {})
            else:
                connection.close()
                return
        else:
            connection.sendall(b"OK")

        room.add_member(client_nickname, connection)
        with lock:
            connections[client_nickname] = connection

        thread = threading.Thread(target=communication, args=(client_nickname, connection, room))
        thread.daemon = True
        thread.start()

    except Exception as e:
        print(f"Error occurred: {e}")
        connection.close()


def main():
    create_room("MAIN", "", "", {})

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', SERVER_PORT))
    server_socket.listen()

    print("Server Started")
    print("Listening for incoming connections...")

    while True:
        connection, addr = server_socket.accept()
        handler_thread = threading.Thread(target=client_handler, args=(connection, addr))
        handler_thread.daemon = True
        handler_thread.start()


if __name__ == "__main__":
    main()
