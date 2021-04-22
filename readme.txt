Crud Application using Flask and SQLAlchemy

created by- Rohan Singh

CRUD:

C for CREATE -- INSERT
R for READ   -- SELECT
U for Update -- UPDATE
D for Delete -- DELETE


Database Name - 'crud'

Login Details for postgres
loginname-'rohan'
password-'1234'

"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rohan:1234@localhost:5432/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""

