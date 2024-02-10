import socket
import struct
import requests
import time

robot_ip = "ec2-3-149-25-0.us-east-2.compute.amazonaws.com"
robot_port = 16389
listen_on_port = 5005


def test_http(url):
    status = requests.post(f"{url}/setParameter",
                           json={'Path': 'root/Control/temperatureSensor/switchOn',
                                 'Value': True})
    print(status.status_code)
    status = requests.post(f"{url}/setParameter",
                           json={'Path': 'root/Control/temperatureSensor/inputTemp',
                                 'Value': 0})
    print(status.status_code)

    linear = 0.1
    rotational = 0.1
    while True:
        temperature = requests.post(f"{url}/getParameter",
                                    json={'Path': 'root/Control/temperatureSensor/measuredTemp'})
        print(f"temperature: {temperature.text}")

        requests.post(f"{url}/setParameter",
                      json={'Path': 'root/Control/interpreterInVelocity', 'Value': [linear, rotational]})

        coordinates = requests.post(f"{url}/getParameter",
                                    json={'Path': 'root/Control/referenceCoordinates'})
        print(f"coordinates: {coordinates.text}")

        time.sleep(0.1)


def test_udp():
    # create socket and start listing
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind(("", listen_on_port))
    counter = 0
    joystick_velocity_command = [0, 1]
    # packing command message
    while True:
        command_message = struct.pack("I2f", counter & 0xffffffff, joystick_velocity_command[0],
                                      joystick_velocity_command[1])
        sock.sendto(command_message, (robot_ip, robot_port))

        reply_message, addr = sock.recvfrom(1024)
        if len(reply_message) > 0:
            msg = struct.unpack("I3ff", reply_message)
            print(f"{msg}, {addr}")
            counter += 1


if __name__ == "__main__":
    # test_udp()
    test_http("http://localhost:8888")
