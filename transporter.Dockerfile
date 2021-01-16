FROM ubuntu

ENV TRANSPORTER_VERSION 0.5.2

RUN apt-get update && apt-get install -y  curl
# RUN apk add curl tar gzip


RUN curl -L --verbose -SLO "https://github.com/compose/transporter/releases/download/v${TRANSPORTER_VERSION}/transporter-${TRANSPORTER_VERSION}-linux-amd64" 
COPY transporter-${TRANSPORTER_VERSION}}-linux-amd64 /usr/local/bin
    # && gzip -dc "transporter-${TRANSPORTER_VERSION}-linux-amd64" | tar xf "transporter-${TRANSPORTER_VERSION}-linux-amd64" -C /usr/local/bin --strip-components=1 \
    # && rm "transporter-${TRANSPORTER_VERSION}-linux-amd64"

ENTRYPOINT ["transporter"]