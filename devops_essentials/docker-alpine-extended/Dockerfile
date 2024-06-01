# Use the Alpine base image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Copy the configuration file to /app/config.txt
COPY config.txt /app/config.txt

# Default command
CMD ["echo", "Hello, World!"]
