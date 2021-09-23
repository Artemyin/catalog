from flask import url_for, redirect, render_template, request, abort

from app import app, db

#Import Flask-Admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import helpers as admin_helpers

#Import Flask-Security
from flask_security import Security, SQLAlchemyUserDatastore, current_user




from app.models import  Lamp, Street, Building, Entrance, Address, User, Role


#Setup Flask-Admin
#admin = Admin(app, template_mode='bootstrap3')

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create customized model view class
class SuperuserModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
        )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class EditorModelView(SuperuserModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('editor')
        )


class UserModelView(SuperuserModelView):
    def is_accessible(self):
        """
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('user')
        )
        """
         # set accessibility...
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        
        # roles with ascending permissions...
        if current_user.has_role('superuser'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return True
            
        if current_user.has_role('editor'):
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return True
        
        if current_user.has_role('user'):
            self.can_create = False
            self.can_edit = False
            self.can_delete = False
            return True
        return False
        
        

# Flask views
@app.route('/')
def index():
    config = app.config.get("NAME")
    return render_template('index.html', config=config)


# Create admin
admin = Admin(
    app,
    'Catalog',
    base_template='my_master.html',
    template_mode='bootstrap4',
)

# Add model views
admin.add_view(SuperuserModelView(Role, db.session))
admin.add_view(SuperuserModelView(User, db.session))

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


admin.add_view(UserModelView(Address, db.session))
admin.add_view(EditorModelView(Street, db.session))
admin.add_view(EditorModelView(Building, db.session))
admin.add_view(EditorModelView(Entrance, db.session))
admin.add_view(EditorModelView(Lamp, db.session))