# register user
echo 'REGISTER...'
curl --request POST --url http://127.0.0.1:5000/register --data '{"username": "fabio", "password": "123"}' --header "Content-Type: application/json"

# auth
echo 'AUTH...'
#curl --request POST --url http://127.0.0.1:5000/auth --data '{"username": "fabio", "password": "123"}' --header "Content-Type: application/json"
# token extraction || brew install jq
TOKEN=$(curl -s -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"username": "fabio", "password": "123"}' --url http://127.0.0.1:5000/auth | jq -r '.access_token')
echo $TOKEN

echo 'POST ADD ITEM...'
curl --request POST --url http://127.0.0.1:5000/item/salt --data '{"price": 3.99, "store_id": 1}' --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'POST ADD ITEM...'
curl --request POST --url http://127.0.0.1:5000/item/pasta --data '{"price": 8.89, "store_id": 1}' --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'GET ITEM LIST...'
#curl --request GET --header "Authorization: JWT $TOKEN" --url http://127.0.0.1:5000/items
#curl --request GET --url http://127.0.0.1:5000/items
curl --request GET --url http://127.0.0.1:5000/items \
--header "Authorization: JWT $TOKEN"

echo 'GET ITEM WITHOUT AUTH...'
curl --request GET --url http://127.0.0.1:5000/item/salt

echo 'GET ITEM WITH AUTH...'
#curl --request GET --header "Content-Type: application/json" --header "Authorization: JWT $TOKEN" --url http://127.0.0.1:5000/item/salt
curl --request GET --url http://127.0.0.1:5000/item/salt --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'GET ITEM THAT DOES NOT EXIST WITH AUTH...'
curl --request GET --url http://127.0.0.1:5000/item/xyz --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'DELETE ITEM WITH AUTH...'
curl --request DELETE --url http://127.0.0.1:5000/item/pasta --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'GET ITEM LIST...'
curl --request GET --url http://127.0.0.1:5000/items \
--header "Authorization: JWT $TOKEN"

echo 'PUT (ADD/UPDTATE) ITEM...'
curl --request PUT --url http://127.0.0.1:5000/item/salt --data '{"price": 2.99, "store_id": 1}' --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN" 

echo 'PUT (ADD/UPDTATE) ITEM...'
curl --request PUT --url http://127.0.0.1:5000/item/pasta --data '{"price": 7.89, "store_id": 1}' --header "Authorization: JWT $TOKEN" \
--header "Content-Type: application/json" 

echo 'GET ITEM LIST...'
curl --request GET --url http://127.0.0.1:5000/items \
--header "Authorization: JWT $TOKEN"

echo 'PUT ADD/UPDATE...'
curl --request PUT --url http://127.0.0.1:5000/item/pasta --data '{"pric": 5.55, "store_id": 1}' --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN" 

echo 'GET ITEM WITH AUTH...'
curl --request GET --url http://127.0.0.1:5000/item/pasta --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN" 

echo 'POST ADD STORE...'
curl --request POST --url http://127.0.0.1:5000/store/silver --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'POST ADD STORE...'
curl --request POST --url http://127.0.0.1:5000/store/banana --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'GET STORE LIST...'
curl --request GET --url http://127.0.0.1:5000/stores \
--header "Authorization: JWT $TOKEN"

echo 'DELETE STORE WITH AUTH...'
curl --request DELETE --url http://127.0.0.1:5000/store/banana --header "Content-Type: application/json" \
--header "Authorization: JWT $TOKEN"

echo 'GET STORE LIST...'
curl --request GET --url http://127.0.0.1:5000/stores \
--header "Authorization: JWT $TOKEN"


#curl --request GET --header 'Accept: application/json' -H "Authorization: JWT " --url http://127.0.0.1:5000/item/salt
#curl --request GET --url http://127.0.0.1:5000/item/pepper

#curl --request GET \
#	--url 'https://weatherbit-v1-mashape.p.rapidapi.com/current?lang=en&lon=-30.056815&lat=-51.180344' \
#	--header 'x-rapidapi-host: weatherbit-v1-mashape.p.rapidapi.com' \
#	--header 'x-rapidapi-key: 607b6a2047msh17362ad5723df14p1ba8e9jsn8e7357a4c283'

#curl --header "Content-Type: application/json" \
#  --request POST \
#  --data '{"username":"xyz","password":"xyz"}' \
#  http://localhost:3000/api/login

