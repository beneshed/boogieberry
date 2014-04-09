BoogieBerry
========

A voting platform that votes on the song on the raspberry pi using the rdio api.Our team from Mason SRCT created this webapp in 36 hours (Well technically more around 30) at the Bitcamp Hackathon, at the University of Maryland College Park.

Installation
---
To install you must run the following commands below

    git clone https://github.com/the-ben-waters/boogieberry.git 
    virtualenv myenv
    source myenv/bin/activate
    cd ~/boogieberry  
    pip install -r requirements.txt
    python manage.py syncdb  
    python manage.py loaddata boogieberry/voting/fixtures/fix.json  
    python manage.py runserver

API Keys
---
You must configure your Rdio api key according to their documentation.  
You also must configure your twilio key in the voting/views.py files


