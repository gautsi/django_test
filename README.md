# django_test
My first django project


## Setup
### docker
I'm using this development docker setup https://github.com/gautsi/dockers/tree/master/dev_env

### initialize project
```
django-admin startproject django_project
```

### make sure server works
```
python3 manage.py runserver 0.0.0:8000
```
Then open in browser http://127.0.0.1:8000/


### make it a repo on github
- create an empty repo django_test on github
- may need to define git global user.email, user.name before first commit works
```
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/gautsi/django_test.git
git push -u origin master
```

## To do
- [ ] follow https://docs.djangoproject.com/en/3.0/intro/tutorial01/ to make first app
