import mysql


class comic():
    id = -1
    title = ''
    email = ''
    author = ''
    status = ''

    def __init__(self, _id=-1, title='', email='', author='', status=''):
        self.id = _id
        self.title = title
        self.email = email
        self.author = author
        self.status = status

    def save(self):
        # Create the connection object
        myconn = mysql.connector.connect(host="localhost", user="root",
                                         passwd="", database="app_novel_database")
        cursor = myconn.cursor()
        query = ("insert into comic(title, email, author, status) "
                 + "values (%s, %s)")
        val = (self.title, self.email, self.author, self.status)
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
            'title': self.title,
            'email': self.email,
            'author': self.author,
            'status': self.status,
        }
