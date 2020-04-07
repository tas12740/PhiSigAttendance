# Phi Sigma Pi - Alpha Kappa Website

The original purpose of this website is to provide a centralized hub for Phi Sig at UNC, serving any function the fraternity sees fit, whether tracking attendance, handling voting, or serving as a PR boost.  

As you can see, this site utilizes Git as source control. This allows multiple people to collaborate on the website's code, including IT chairs across generations.  

## Project Overview - WTF Is This Wizardry

This site uses [Django](https://www.djangoproject.com/), a Python library which handles a lot of the complex Web things like routing (when you get "phisigunc.com/contact", Django helps you tell the server to give the user back something which corresponds to that "contact" path), connecting to a database, and user privileges for us. I highly recommend that you at least skim through their [documentation](https://docs.djangoproject.com/en/3.0/), which has a fantastic tutorial as an introduction (Google and Stack Overflow are also great help if you can't find something in the docs!). Don't worry if you don't have any Python experience; given your previous programming experience, it should be no trouble to pick it up.  

The Django site is then deployed on the [Google cloud](https://console.cloud.google.com/) (you'll have to log in with the PSP IT account - phisiginfotech@gmail.com to see the site project). I'll go over how this works in a later section, but my hope is that I have set up everything so that for the most part you won't have to dig into the weeds here.

## Getting Started

### Step 1: Clone the Repo

Open up your favorite command prompt (on Windows, type `cmd` in your search bar (or use the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)); on Mac, use your built-in command prompt; on Linux, I'm sure you know what to do) and clone the repository by typing the following:

`git clone git@github.com:tas12740/PhiSigAttendance.git`

You can do this over HTTPS instead, but I highly recommend using this method, which uses an SSH key for authentication (see [here](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) for instructions!).  

You'll see the basic structure of the project now. Django is organized into so-called "apps," each with their own models (which turn into database tables), URLs (the routes), and views (what the server uses to respond to a route, usually the rendering of an HTML page, but in the case of the API, also can be JSON responses or others). At the time of writing, these apps are `api` (to which POST requests are routed, like checking in or voting), `checkin` (where the ability to create Siblings, Events, and Check-Ins for these events lives - please note that I never really completed these, so feel free to tune them up!), `ipanel` (where I-Panel voting lives), `recruitment` (where PNM check-ins and pages about the recruitment process and schedule live), `root` (where a lot of the basic pages live), and `siblings` (where information for siblings lives - this could be due for a large expasion in the future!).

### Step 2: Getting Setup With Python

You'll also see a file called `manage.py` here. This is a file that can help you do a lot of the Django functions (see [here](https://docs.djangoproject.com/en/3.0/ref/django-admin/) for documentation), whether it's starting a new app, creating migration files for the database tables, or spinning up a development server so you can see your changes without having to push them live. To use these, you'll want to either have the Python modules installed globally (`python -m pip install -r requirements.txt` on Windows or `python3 -m pip install -r requirements.txt` on Mac or Linux) or set-up a [virtual environment](https://docs.python.org/3/tutorial/venv.html) (`python -m venv env-name` or `python3 -m venv env-name`, activate it for your platform, then install the requirements in the same way; here you'll have to reactivate your environment everytime you do some development). Once you have this set up, you'll be able to use Django commands. Try this one:  

`python manage.py runserver` or `python3 manage.py runserver`

Hmm, you probably got an error. WTF is going on? Why did you tell us to do this, Taylor? The error here deals with connecting to the database. Obviously we have to limit who can just get into our stuff, and we do this by limiting the IP addresses that can connect (sounds scary, but in reality you don't really have to understand what's going on). To fix this, go to a site like [here](https://www.whatismyip.com/), copy that value, and go to the Google Cloud console [page](https://console.cloud.google.com/). Once you're logged in, click on the hamburger icon in the upper left, scroll down to click SQL, and then click Connections. You'll see a long list of IP addresses under "Authorized networks," just click the "+ Add Network" button and paste yours in and save it. Now you should be able to type the command and run the development server! Type in `localhost:8000` in your browser and you should see the home page pop up! Append any slashes after this and you should see those pages too.  

### Step 3: Understanding Django

I'm sure that you are familiar that the Web runs a lot on Hyper-Text Markup Language (HTML), Cascading Style Sheets (CSS), and JavaScript. Django integrates all these technologies a little bit differently, which makes things easier on you as a developer.  

#### Templates

Instead of making every HTML page just pure HTML, Django uses something fancy called ["templates,"](https://docs.djangoproject.com/en/3.0/topics/templates/) which allows it to generate HTML content dynamically. This enables us to make use of some advanced features, like creating pages which are extensions of other pages (sort of like Object-Oriented Programming) - which allows us to avoid repeating a lot of code (for example, in this project, the top navigation bar), loading static resources (CSS, JS, etc.) without hardcoding the location, and more.  

The Django Template Language (side note: Django can also be configured to work with other template engines like the popular Jinja2 if you want to get that fancy) works through template tags (which look like this `{% content %}`). One example is the `extends` tag, which you put at the top of the file - this forces you to use the `block` (and `endblock`) tags to fill in pieces in the document you're extending from. Other tags you might have to load (using the `load` tag), for example `{% load static %}`). See the documentation for more!  

You can also pass variables into templates (giving it a context in the view) and use things like if statements or for loop to generate HTML content based on that.  

We store the templates for each app in `app-name/templates/app-name`, which you can then render in a view by just referring to it as `app-name/template-name.html`.  

#### Static Files

Static files for each app are stored in `app-name/static/app-name` (which we then usually separate into separate folders like `js` or `css`). Instead of hard-coding the locations of these files in an HTML file, Django instead allows us to refer to them in a relative way with the use of the `static` tag. This tag allows us to substitute the location of a file like as follows: `{% static 'app-name/sub-folder/file' %}` (for example, on the Contact page, my image, though it will be deleted soon, is referred to as `root/img/exec/taylor.png`).  

To make sure that these work, run that development server and go to the page to see!  

One final thing here is before you deploy or push some changes up to Github, you'll have to collect the files into one place. I like to delete the `static` folder before I do this (the root level one, not the one that's in the individual apps!). Then run the `collectstatic` command with `manage.py` (do you remember how to do this?).  

#### Sidenote: JavaScript

This project makes use of [jQuery](https://jquery.com/), a JavaScript library which makes manipulating the DOM and sending requests much easier. For examples, take a look at the existing files, Stack Overflow, or the documentation (or take 426!). Or, maybe in the future you want to transition to native JavaScript. Do whatever you feel!  

#### Sidenote: Vendor Files

There is a static folder called `root/static/root/vendor` which stores external libraries. At the time of writing, these are jQuery and [Bootstrap](https://getbootstrap.com/), which is an easy way to style things (although the project uses custom CSS as well).  

#### URLs

Each app comes with a file called `urls.py`. It is here that you define routes that users which visit the site will see in their address bar (for example, `phisigunc.com/foo/bar`). Django allows you to redirect these routes to views, which we'll discuss in the next section. You can also make app-level URLs follow some prefix by utilizing the root-level URLs in the `phisigattendance` file, for example including the check-in URLs allows you to define check-in URLs called `checkin` and `bruh` and then have these be routed to by `phisigunc.com/checkin/checkin/` and `phisigunc.com/checkin/bruh/`.

#### Views

Each app also comes with a `views.py` file. This file defines Python functions which respond to the URLs, whether it's rendering an HTML template (with or without variables as context) or giving back an API response. See some of the existing files or the documentation for examples!  

#### Models

Each app can define [models](https://docs.djangoproject.com/en/3.0/topics/db/models/), which turn into database tables. Django uses models to make it so you don't have to write fancy SQL queries. Instead, you get to interact with tables through a well-defined model API.  

Each object in the `models.py` file defines a table, with each of its properties as a column in the table. There are lots of different options you can choose from to customize your models and add constraints. See the docs for lots of great information, including on making foreign keys in your tables and much, much more!  

When you make a change to the models, you want those changes to affect the database. To do this, use the `manage.py` command `makemigrations` to make migration files (Django uses these in the case that you have multiple database locations to make sure they're all on the same page) then migrate the DB with the command `migrate`.  

##### Making a new entry

In Python code, you create a new row in the table by instantiating an instance of the model with parameters which represent the different fields. Then call the `save` method on the object (which can potentially fail, whether for lack of connection or failing some constraint!).  

##### Getting objects from the table

See this [page](https://docs.djangoproject.com/en/3.0/topics/db/queries/) for a great introduction on making queries of different types!  

#### Admin

Django has a built-in admin page which allows you to look at the tables and rows without having to write complex code. This page lives at `/admin` (so `localhost:8000/admin` for local or `phisigunc.com/admin`), but to see models in here you have to register them. This is the purpose of the `admin.py` file in each `app`, where you register each model. You'll have to login, for which you can make different users, but I setup one so-called superuser called `admin` (password `admin`) so you can get started.  

#### Settings

The `settings.py` file (`phisigattendance/settings.py`) has a lot of settings in it. You don't have to understand a lot of what goes on in here (though you may have to add to it or change to it if you run into errors), but the most important piece is the `DEBUG` flag. The version you'll get through `git` has `DEBUG=False` since this is the version which gets deployed, but I recommend setting it to `True` in your local version (this is the only way you'll be able to get the development server working).  

The `settings.py` file also is where we tell Django about our apps in the `INSTALLED_APPS` variable. So, if you define a new app, (using - what else? - the `startapp app-name` `manage.py` command), you'll tell Django about it in this variable.  

### Step 4: Understanding the Cloud

You can install some command prompt commands to run by going [here](https://cloud.google.com/sdk/install) and then using various commands (like `gcloud app deploy` will deploy what you have locally). However, I've also set it up so whenever you make a push to the `git` `master` branch, the website will be deployed automatically to the App Engine on the Google cloud.

The deployment of the website uses something called the [App Engine](https://cloud.google.com/appengine), which allows us to have something on the Cloud without worrying about fancy server stuff. The files which govern how this works are `app.yaml` and `main.py`. The `main.py` file gets the application instance for the Engine to create, and the `app.yaml` file gives the various configuration parameters for the startup.  

The automated deployment is handled in the `cloudbuild.yaml` file. This file is used by Git to deploy the site automatically on a push.  

There are a lot more things you can explore on the App Engine page in the Google Cloud Console, for instance the Dashboard shows you a nice graph of how often the site is being accessed and the Versions page shows you if your new version got deployed (and, if not, what went wrong).  

## That Was a Lot of Content

I tried to put everything I could think of into this document on how the site works from a technical level without trying to get bogged down into too much detail. This, I hope, is or will be a helpful guide to get started on working with the site, but it does not include any details on procedural things like I-Panel voting. For these, I hope they'll be in your Drive.  

If you need any help, please don't hesitate to reach out to me:

* Email: tas12740@gmail.com
* Text: (919)-622-5071

And, finally, don't be afraid to make changes. You are prepared and capable of effecting change on this website, in Phi Sig, and in the broader world. Whoever you are, I am proud of you for taking up this mantle. Now go out and make this website an even bigger part of Phi Sig!  
