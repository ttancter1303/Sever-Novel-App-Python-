import mysql


class music():
    id = -1
    title = ''
    data = ''

    def __init__(self, _id=-1, title='', data=''):
        self.id = _id
        self.title = title
        self.data = data

    def save(self):
        # Create the connection object
        myconn = mysql.connector.connect(host="localhost", user="root",
                                         passwd="", database="music_database")
        cursor = myconn.cursor()
        query = ("insert into music(title, data) "
                 + "values (%s, %s)")
        val = (self.title, self.data)
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
            'data': self.data
        }
