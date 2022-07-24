# syntax=docker/dockerfile:1

FROM python:3.10.5-slim-buster

WORKDIR /flask_restx_demo

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -e .

# EXPOSE 8000
# ENTRYPOINT ["waitress-serve"]
# CMD ["--port=8000", "--call", "src.flask_restx_demo:create_app"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000" ]