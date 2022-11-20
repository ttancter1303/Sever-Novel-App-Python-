import mysql


class author():
    id = -1
    name = ''
    introduce = ''

    def __init__(self, _id=-1, name='',introduce =''):
        self.id = _id
        self.name = name
        self.introduce = introduce

    def save(self):
        # Create the connection object
        myconn = mysql.connector.connect(host="localhost", user="root",
                                         passwd="", database="app_novel_database")
        cursor = myconn.cursor()
        query = ("insert into author(name, introduce) "
                 + "values (%s, %s)")
        val = (self.name,self.introduce)
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
            'introduce': self.introduce
        }
