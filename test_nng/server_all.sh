#!/bin/bash
script_full_path=$(dirname "$0")
${script_full_path}/server_reqrep.sh
${script_full_path}/server_pubsub.sh
