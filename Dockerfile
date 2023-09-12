####### 👇 OPTIMIZED SOLUTION (x86)👇 #######
## cada vez que cambio el dockerfile, tengo que correr la imagen

# tensorflow base-images are optimized: lighter than python-buster + pip install tensorflow
FROM tensorflow/tensorflow
#:2.10.0
#From python:3.8.12-buster
# OR for apple silicon, use this base image instead
# FROM armswdev/tensorflow-arm-neoverse:r22.09-tf-2.10.0-eigen

# WORKDIR /prod
WORKDIR /code/jotanavarrete/goalguru

# We strip the requirements from useless packages like `ipykernel`, `matplotlib` etc...
#requirements_prod.txt (se lo agregan, pero nose si sera necesario.)
# COPY requirements.txt requirements.txt
COPY requirements_prod.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY data data
COPY goalguru goalguru
COPY setup.py setup.py
RUN pip install .

#COPY Makefile Makefile
#RUN make reset_local_files

CMD uvicorn goalguru.api.fast:app --host 0.0.0.0 --port $PORT
# $DEL_END

## docker run -it -e PORT=8000 -p 8000:8000 goalguru
