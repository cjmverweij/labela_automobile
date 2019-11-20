# Label-A autoparts API

## Running the app

I've containerized the application with [docker](https://www.docker.com/products/docker-desktop). If you have docker installed, you can easily start the application by running:

- `docker compose-up`

Running this the first time it wil build and then run the application and a postgres database service. When the containers are running you will need to run the following commands in a new terminal window to initialize and populate the database:

- `docker exec labela_app init_mob_db development.ini`
- `docker exec labela_app mock_mob_db development.ini`

Running the second command will populate the database with two users and an inventory of car parts that is parsed from the `mock_inventory.json` file, which has mock data found [here](https://datasn.io/p/370) 

## API

**Postman Collection**

*You can find the API documentation [here](https://documenter.getpostman.com/view/4313438/SW7aXTL2).* 

the documentation has been generated using [Postman](https://www.getpostman.com).
if you have postman installed on your computer clicking `run in postman` on the documentation page will import the collection into the postman app. This will allow you to easly play around with the API!
