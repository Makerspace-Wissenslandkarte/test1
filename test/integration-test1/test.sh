set -e
ping -c 10 python && curl http://python:8000/ | grep 'c0bbdbcd-957f-4d56-ac3c-6c06ae06e27e' || (echo "ERROR: Failed to find integration test token in html header."; false)
