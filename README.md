# Catalog

I make a web site which is a catalog of somewhat linked to address
in my case it is catalog of a lamps wich is instaled in the buldings.
And you have an oportunity to watch lamps by address where they installed.

User can access to admin panel by the link.
There is three roles: user, admin, superuser.
- user have access to watching(reading), searching, sorting address. 
- admin have access to adding, edditing  address and lamps.
- superuser have access to adding, edditing of all data, including users



## Used libraries:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/)
- [Flask-Security](https://flask-security-too.readthedocs.io/en/stable/)


## Problems in the project

### The most dificult was:

after integration Flask-Alchemy and Flask Admin.
I got posibility to watch and edit my models thru the admin panels.
But for models wich consist mostly from fields related to another tables it was a problem with friendly user experience.
In my case it was Address table. And i should to create first a street in Street table, building number in the Building table, number of entrance in the Entrance table ...
After this only i will be able to create Address, thru choosing elements for my address from drop down list.
My approach was to do pocibility to edit table and add new records to related fields by edit and add text right in the line of the editable table.

### what i try to do:
- I try to edit models, specifically Address table. 
Added constructor by passing elements of the address as the arguments to the model class for easy creation of the model.

### what i want to try:
- column_editable_list
- [inline_models](https://flask-admin.readthedocs.io/en/v1.4.0/api/mod_contrib_sqla/#flask_admin.contrib.sqla.ModelView.inline_models)
- Inline form editor
- [anoter one description how to add this posibility](https://wordpressify.ru/2018/09/flask-admin-hacks-for-many-to-many-relationships/)
- [anoter one description how to add this posibility](https://chase-seibert.github.io/blog/2015/09/25/flask-admin-list-edit-one-to-many.html)
- [try to understand what is scaffolding](https://flask-admin.readthedocs.io/en/v1.4.0/advanced/#overriding-the-form-scaffolding)
- edit_view
- https://gist.github.com/DrecDroid/398a05e4945805bc09d1


## list of references:
- [origin post on habr form creator of flask-admin](https://habr.com/ru/post/148765/)
- [post about authorization](https://ploshadka.net/flask-delaem-avtorizaciju-na-sajjte/)
- [anoter blog about integration admin and flask](https://russianblogs.com/article/37171301805/)
- [deploying on heroku](https://realpython.com/flask-by-example-part-1-project-setup/)
- [git branch](http://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [git merge](http://git-scm.com/docs/git-merge)

