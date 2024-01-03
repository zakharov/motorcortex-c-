"""
Request/Reply is used for synchronous communications where each question is responded with a single answer,
for example remote procedure calls (RPCs).
Like Pipeline, it also can perform load-balancing.
This is the only reliable messaging pattern in the suite, as it automatically will retry if a request is not matched with a response.

"""
import datetime
import pynng

DATA = "Answer to the Ultimate Question of Life, the Universe, and Everything."

address = "tcp://ec2-3-149-25-0.us-east-2.compute.amazonaws.com:9000"


def request():
    with pynng.Req0() as sock:
        sock.dial(address)
        print(f"NODE1: SENT DATA: {DATA}")
        sock.send(DATA.encode())
        msg = sock.recv_msg()
        print(f"NODE1: RECEIVED DATA: {msg.bytes.decode()}")


if __name__ == "__main__":
    request()
