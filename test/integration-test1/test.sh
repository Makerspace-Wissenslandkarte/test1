set -e
ping -c 10 python
echo "CHECK integration test token in html header"
curl http://python:8000/ | grep 'c0bbdbcd-957f-4d56-ac3c-6c06ae06e27e' || (echo "ERROR"; false) && (echo "SUCCESS")
echo "CHECK integration test token in html header with localhost address"
curl http://python:8000/ -H "Host: localhost" | grep 'c0bbdbcd-957f-4d56-ac3c-6c06ae06e27e' || (echo "ERROR"; false) && (echo "SUCCESS")
echo "CHECK integration test token in html header with IPv4 loopback address"
curl http://python:8000/ -H "Host: 127.0.0.1" | grep 'c0bbdbcd-957f-4d56-ac3c-6c06ae06e27e' || (echo "ERROR"; false) && (echo "SUCCESS")
echo "CHECK integration test token in html header with IPv6 loopback address"
curl http://python:8000/ -H "Host: [::1]" | grep 'c0bbdbcd-957f-4d56-ac3c-6c06ae06e27e' || (echo "ERROR"; false) && (echo "SUCCESS")
