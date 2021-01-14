FROM python
WORKDIR /app
RUN pip install scrapy click pymongo
COPY ./scrapy.cfg /app
COPY ./scraper /app 
COPY ./spiders.py /app 

ENTRYPOINT ["python", "-u"]
