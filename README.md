# fastapi-example
trying implementation of APIs using FastAPI framework


Just run `uvicorn main:app --reload` after installing packages using pip `pip install -r requirements.txt`

## Lets go ahead and dockerize this FastAPI server application
Build docker imagee: `docker build -t myfastapiapp .`
run the docker container and point the localhost port 4000 to the docker container port 80: `docker run -p 4000:80 myfastapiapp`

localhost:4000/docs also displays the OpenAPI - swagger page
