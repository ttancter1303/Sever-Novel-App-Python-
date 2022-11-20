import mysql


class chapter():
    id = -1
    title = ''
    content = ''
    date = ''

    def __init__(self, _id=-1, title='', content='', date=''):
        self.id = _id
        self.title = title
        self.content = content
        self.date = date

    def save(self):
        # Create the connection object
        myconn = mysql.connector.connect(host="localhost", user="root",
                                         passwd="", database="app_novel_database")
        cursor = myconn.cursor()
        query = ("insert into chapter(title, content, date) "
                 + "values (%s, %s)")
        val = (self.title, self.content, self.date)
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
            'content': self.content,
            'date': self.date
        }
