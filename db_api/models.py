from db_api.database import db


class UserData(db.Model):
    first_name = db.Column(db.String(80), nullable=False, primary_key=True)
    family_name = db.Column(db.String(80), nullable=False, primary_key=True)
    age = db.Column(db.Integer)
    job = db.Column(db.String(80))
    address = db.Column(db.String(80))
    biography = db.Column(db.String(160))

    def __init__(self, json_data):
        self.first_name = json_data.get('first_name')
        self.family_name = json_data.get('family_name')
        self.age = json_data.get('age')
        self.job = json_data.get('job')
        self.address = json_data.get('address')
        self.biography = json_data.get('biography')

    def update(self, json_data):
        self.first_name = json_data.get('first_name', self.first_name)
        self.family_name = json_data.get('family_name', self.family_name)
        self.age = json_data.get('age', self.age)
        self.job = json_data.get('job', self.job)
        self.address = json_data.get('address', self.address)
        self.biography = json_data.get('biography', self.biography)
        
    def json(self):
        return {
            'first_name': self.first_name,
            'family_name': self.family_name,
            'age': self.age,
            'job': self.job,
            'address': self.address,
            'biography': self.biography
        }

