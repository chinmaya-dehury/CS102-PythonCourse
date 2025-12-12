curl -X POST http://SERVER_IP:8000/report \
-H "Content-Type: application/json" \
-d "{
  \"username\": \"$(whoami)\",
  \"ip_addresses\": \"$(hostname -I)\"
}"
