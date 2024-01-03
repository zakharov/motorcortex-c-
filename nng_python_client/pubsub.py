"""
Request/Reply is used for synchronous communications where each question is responded with a single answer,
for example remote procedure calls (RPCs).
Like Pipeline, it also can perform load-balancing.
This is the only reliable messaging pattern in the suite, as it automatically will retry if a request is not matched with a response.

"""
import datetime
import pynng

DATA = "Answer to the Ultimate Question of Life, the Universe, and Everything."

address = "tcp://ec2-3-149-25-0.us-east-2.compute.amazonaws.com:9001"


def subscribe():
    with pynng.Sub0() as sock:
        sock.dial(address)
        sock.subscribe("")
        while True:
            msg = sock.recv_msg()
            print(f"NODE1: RECEIVED DATA: {msg.bytes.decode()}")


if __name__ == "__main__":
    subscribe()
