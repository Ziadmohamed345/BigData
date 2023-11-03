# Specify the base image as Ubuntu
FROM ubuntu

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container at /home/doc-bd-a1/
RUN mkdir /home/doc-bd-a1

# Copy the dataset file to the container
COPY train_titanic.csv /home/doc-bd-a1/
