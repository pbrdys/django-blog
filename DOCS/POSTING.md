pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7




# CSRF again!
This is another way Django helps to protect us from cross-site attacks. We discussed some of these earlier in the course when we set the CSRF_ALLOWED_HOSTS setting. If you remove the {% csrf_token %} tag then Django will return an error when you try to submit the form. We'll explain why in more detail below. Make sure to add your CSRF token back into your code before you continue.

Earlier in the course, we talked about cross-site scripting and how Django helps to protect us from that using the CSRF_ALLOWED_HOSTS setting. We see another of Django's protections against cross-site request forgery in our comments form, the {% csrf_token %} tag.

This little tag needs to be added every time we render a form. When this tag is present, Django generates a unique CSRF token, which it sends along with our POST request. Django then checks that token before processing the POST request. When you removed the token or if it doesn't match what Django was expecting, then we get an error, and Django won't process the request.

Exactly how it does this is quite complicated. The critical thing to remember, though, is that you won't be able to process any POSTed forms unless you've provided a {% csrf_token %}. If you have more than one form on a page, you will need this tag on each of them.

