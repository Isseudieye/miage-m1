FROM python:3.13-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /_notebooks

COPY ../../requirements.txt requirements.txt
RUN pip3 install jupyterlab && \
    pip3 install -r requirements.txt && rm requirements.txt

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]