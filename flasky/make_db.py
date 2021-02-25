# %%

from hello import db

# %%
db.create_all()


# %%
from hello import db
from hello import Role, User

adminRole = Role(name="Admin")
modRole = Role(name="Moderator")
userRole = Role(name="User")
userJohn = User(username="john", role=adminRole)
userSusan = User(username="susan", role=userRole)
userDavid = User(username="david", role=userRole)
db.session.add_all([adminRole, userRole, modRole, userJohn, userSusan, userDavid])
db.session.commit()

adminRole.name = "Administrator"
db.session.add(adminRole)
db.session.commit()

db.session.delete(modRole)
db.session.commit()

# %%
