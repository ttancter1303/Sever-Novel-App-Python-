import mysql


class user():
    id = -1
    name = ''
    email = ''
    birth = ''
    phone_number = ''
    introduce = ''

    def __init__(self, _id=-1, name='', email='',birth='',phone_number='',introduce =''):
        self.id = _id
        self.name = name
        self.email = email
        self.birth = birth
        self.phone_number = phone_number
        self.introduce = introduce

    def save(self):
        # Create the connection object
        myconn = mysql.connector.connect(host="localhost", user="root",
                                         passwd="", database="app_novel_database")
        cursor = myconn.cursor()
        query = ("insert into user(name, email, birth, phone_number, introduce) "
                 + "values (%s, %s)")
        val = (self.name,self.email,self.birth,self.phone_number,self.introduce)
        try:
            # inserting the values into the table
            cursor.execute(query, val)
            # commit the transaction
            myconn.commit()
        except Exception as e:
            myconn.rollback()
            cursor.close()
            myconn.close()
            return str(e)
        cursor.close()
        myconn.close()
        return 'success'

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birth': self.birth,
            'phone_number': self.phone_number,
            'introduce': self.introduce
        }
