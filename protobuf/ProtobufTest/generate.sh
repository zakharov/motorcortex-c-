#!/bin/bash

protoc --csharp_out=. msg/motorcortex.proto
python3 msg/hash_generator/protobuf_hashgen.py msg/motorcortex.proto --csharp -o ./MotorcortexHash

