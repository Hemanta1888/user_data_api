# python version that is used
FROM python:3.9 


# The directory name
WORKDIR /code

#Port number
EXPOSE 8000

# Copy the requirement.txt file to code folder
COPY ./requirements.txt /code/requirements.txt

#Installing packages by calling the requirements.txt file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy all the folder from the current directory to the 'code' directory
COPY ./API_Pro /code/API_Pro

# Command to run the 'API project'
CMD ["uvicorn", "API_Pro.views:app", "--host", "0.0.0.0", "--port", "8000"]
