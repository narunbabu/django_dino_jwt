curl --request POST \
  --url http://localhost:8000/auth-jwt/ \
  --header 'content-type: application/json' \
  --data '{"username": "ab", "password": "arun@123"}'

  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFiIiwiZXhwI
joxNTA0NzgwMzI4LCJlbWFpbCI6IiJ9.DAs8UplpPbKYuNQ4dSDDPS-8Q21tlYFFdas5La97urw
curl -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJvcm4yY29kZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNTAxNDE4OTYzfQ.VOLCx7uVNa5CXFLos2grecJV2CzrK4FyVj4ontjKUrw" -X GET  http://localhost:8000/api/products/

curl --request POST   --url http://localhost:8000/auth-jwt/   --header 'content-type: application/json'   --data '{"username": "ab", "password": "arun@123"}' 


curl -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFiIiwiZXhwIjoxNTA1MDI1ODAwLCJlbWFpbCI6IiJ9.wn4QAoRu488o6IQ8HTGtVzPY_didVzNfbVGrNqlTRa4" -X GET  http://localhost:8000/dinosaurs/


 http POST 127.0.0.1:8000/api-auth/ username=admin password=admin

 curl -X POST -i -H "Content-type: application/json" -c cookies.txt -X POST http://localhost:58416/api-register/ -d '
    {
  "password": "admin3",
  "username": "admin3",
  "firstName": "Arun3",
  "lastName": "Nalamara3"
}
    '

curl -X POST -d  http://localhost:8000/api-auth/ '{ "password": "admin",  "username": "admin"}'
curl -X POST -i -H  "Content-type: application/json" -c cookies.txt -X POST http://localhost:8000/api-register/ '{ "password": "admin",  "username": "admin"}'

api-register/