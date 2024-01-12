import socket
import struct

robot_ip = "localhost"
robot_port = 16389
listen_on_port = 5005


def test_udp():
    # create socket and start listing
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind(("", listen_on_port))
    counter = 0
    joystick = [1, 2]
    # packing command message
    while True:
        command_message = struct.pack("I2f", counter & 0xffffffff, joystick[0], joystick[1])
        sock.sendto(command_message, (robot_ip, robot_port))

        reply_message, addr = sock.recvfrom(1024)
        if len(reply_message) > 0:
            msg = struct.unpack("I3ff", reply_message)
            print(f"{msg}, {addr}")
            counter += 1


if __name__ == "__main__":
    test_udp()
