FROM python
WORKDIR /app
RUN pip install scrapy click elasticsearch
COPY ./scrapy.cfg /app
COPY ./scraper /app 
COPY ./spiders.py /app 

ENTRYPOINT ["python", "-u"]
