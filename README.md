# GitHub authentication
 - Web application that authenticates users through third-party applicaiton (GitHub).
 - The app is deployed on: https://githubauthentication.pythonanywhere.com
 - The app generates every 5 minutes a random number and displays it to the authenticated users.
 # Libraries/frameworks installed:
  1. Django (https://www.djangoproject.com/).
  2. Sass  (https://pypi.org/project/django-sass/).
  3. Social auth app (https://pypi.org/project/social-auth-app-django/), (https://python-social-auth.readthedocs.io/en/latest/configuration/django.html).
 # Languages:
 1. Python3
 2. JavaScript
 3. HTML/CSS/CSS3
# Requirements:
  - asgiref==3.5.2
  - backports.zoneinfo==0.2.1
  - certifi==2022.6.15.1
  - cffi==1.15.1
  - charset-normalizer==2.1.1
  - cryptography==38.0.1
  - defusedxml==0.7.1
  - Django==4.1.1
  - django-sass==1.1.0
  - idna==3.3
  - libsass==0.21.0
  - oauthlib==3.2.1
  - pycparser==2.21
  - PyJWT==2.4.0
  - python3-openid==3.2.0
  - requests==2.28.1
  - requests-oauthlib==1.3.1
  - six==1.16.0
  - social-auth-app-django==5.0.0
  - social-auth-core==4.3.0
  - sqlparse==0.4.2
  - urllib3==1.26.12
 # How to run the application:
 - Clone this repository to your local machine. 
 - Install virtual environment by the following command: 
   - linux: virtualenv my_env
   - Windows: py -m venv my_env
 - Activate the virtual environment by the following command:
    - Linux: source my_env/bin/activate
    - windows: https://docs.djangoproject.com/en/4.1/howto/windows/#setting-up-a-virtual-environment
 - Install the requirements by one of the following commands:
    - pip install -r requirements.txt
    - pip install django django-sass social-auth-app-django
  - Run the server by the following command:
    - Linux: python3 manage.py runserver
    - Windows: python manage.py runserver
  - Look at which port the server is running (e.g. http://127.0.0.1:8000/) and open it in the browswer.
  - Go to your GitHub and create an OAuth app by the following steps:
    - Settings -> Developer settings -> OAuth Apps -> New OAuth Apps:
    - Fill in the fields with the following:
      - Application name: test
      - Homepage URL: http://127.0.0.1:8000/
      - Authorization callback URL: http://127.0.0.1:8000/
    - Then copy Client Id and paste in the file settings.py in SOCIAL_AUTH_GITHUB_KEY.
    - The copy Client secret and paste it in th file settings.py in SOCIAL_AUTH_GITHUB_SECRET
  - Finally try it and enjoy! 

