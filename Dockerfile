FROM python:3
# set source dir, where the app is stored
COPY . /usr/src/app 
#set working directory same as the application directory
WORKDIR /usr/src/app
#install all the requirements
RUN pip install -r requirements.txt
# command that should run when starting the container.
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]   