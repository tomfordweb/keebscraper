FROM python
WORKDIR /app
RUN pip install scrapy click
COPY . .
ENTRYPOINT ["python", "-u", "spiders.py"]
