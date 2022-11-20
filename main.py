# This is a sample Python script.
import pathlib
import time
import random
import mysql.connector

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, request, jsonify

from music import music

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

ALLOWED_EXTENSIONS = {'jpg', 'png', 'pdf','jpeg','PNG'}

ALLOWED_EXTENSIONS_doc = {'txt', 'docx'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return jsonify({
        'upload_music': {
            'url': 'http://113.22.176.40:8888/api/upload',
            'method': ['POST'],
            'param': [],
            'body': [{
                'name': 'title',
                'type': 'text'
            }, {
                'name': 'file',
                'type': 'file with extension in one of ' + str(ALLOWED_EXTENSIONS)
            }]
        },
        'get_all_music': {
            'url': 'http://113.22.176.40:8888/api/musics',
            'method': ['GET', 'POST'],
            'param': [],
            'body': []
        },
        'delete_music': {
            'url': 'http://113.22.176.40:8888/api/delete/<_id>',
            'method': ['GET', 'POST'],
            'param': [],
            'body': []
        },
    })


@app.route('/api/delete/<int:_id>', methods=['GET', 'POST'])
def delete(_id):
    try:
        music_item = get_by_id(_id)
        if music_item:
            pathlib.Path(music_item.data).unlink()
        else:
            return jsonify({
                'success': False,
                'message': 'Not found song with id = ' + str(_id),
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e),
        })
    # Create the connection object
    myconn = mysql.connector.connect(host="localhost", user="root",
                                     passwd="", database="music_database")
    cursor = myconn.cursor()
    try:
        query = "DELETE FROM music WHERE id=%s"
        val = str(_id)
        cursor.execute(query, (val,))
        myconn.commit()
    except Exception as e:
        myconn.rollback()
        cursor.close()
        myconn.close()
        return jsonify({
            'success': False,
            'message': str(e),
        })
    cursor.close()
    myconn.close()

    return jsonify({
        'success': True,
        'message': 'Delete success song with id = ' + str(_id)
    })


@app.route('/api/upload', methods=['POST'])
def upload_img():
    # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({
            'success': False,
            'message': 'No file part'
        })
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify({
            'success': False,
            'message': 'No selected file'
        })
    if file:
        if allowed_file(file.filename):
            title = request.form['name']
            file_path = 'static/img/' + str(time.time()) + str(random.randint(0, 100000)) + file.filename.lower()
            new_img = music(title=title, data=file_path)
            result = new_img.save()
            if result != 'success':
                return jsonify({
                    'success': False,
                    'message': result
                })
            try:
                file.save(file_path)
            except Exception as e:
                return jsonify({
                    'success': False,
                    'message': str(e)
                })
            return jsonify({
                'success': True,
                'message': 'Upload new image successfully with title is ' + title
            })
        else:
            return jsonify({
                'success': False,
                'message': 'File extension mush be one of ' + str(ALLOWED_EXTENSIONS)
            })
    else:
        return jsonify({
            'success': False,
            'message': 'File undefined'
        })


def upload_text():
    # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({
            'success': False,
            'message': 'No file part'
        })
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify({
            'success': False,
            'message': 'No selected file'
        })
    if file:
        if allowed_file(file.filename):
            title = request.form['title']
            file_path = 'static/musics/' + str(time.time()) + str(random.randint(0, 100000)) + file.filename.lower()
            new_music = music(title=title, data=file_path)
            result = new_music.save()
            if result != 'success':
                return jsonify({
                    'success': False,
                    'message': result
                })
            try:
                file.save(file_path)
            except Exception as e:
                return jsonify({
                    'success': False,
                    'message': str(e)
                })
            return jsonify({
                'success': True,
                'message': 'Upload new music successfully with title is ' + title
            })
        else:
            return jsonify({
                'success': False,
                'message': 'File extension mush be one of ' + str(ALLOWED_EXTENSIONS)
            })
    else:
        return jsonify({
            'success': False,
            'message': 'File undefined'
        })


@app.route('/api/musics', methods=['GET', 'POST'])
def get():
    # Create the connection object
    myconn = mysql.connector.connect(host="localhost", user="root",
                                     passwd="", database="music_database")
    cursor = myconn.cursor()
    all_music = []
    try:
        cursor.execute("SELECT * FROM music")
        result = cursor.fetchall()
        for item in result:
            music_item = music(item[0], item[1], item[2])
            all_music.append(music_item.toJSON())
    except Exception as e:
        myconn.rollback()
        cursor.close()
        myconn.close()
        return jsonify({
            'success': False,
            'message': str(e),
            'music': []
        })
    cursor.close()
    myconn.close()
    return jsonify({
        'success': True,
        'message': 'Query success ' + str(len(all_music)) + ' song',
        'music': all_music
    })


def get_by_id(_id):
    # Create the connection object
    myconn = mysql.connector.connect(host="localhost", user="root",
                                     passwd="", database="music_database")
    cursor = myconn.cursor()
    music_item = None
    try:
        where = "id=%s"
        val = _id
        cursor.execute("SELECT * FROM music WHERE " + where, (val,))
        result = cursor.fetchone()
        music_item = music(result[0], result[1], result[2])
    except Exception as e:
        myconn.rollback()
        cursor.close()
        myconn.close()
    cursor.close()
    myconn.close()
    return music_item


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from waitress import serve

    serve(app, host="0.0.0.0", port=8888)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
