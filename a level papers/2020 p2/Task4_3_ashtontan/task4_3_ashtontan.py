import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/')

def index():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute('SELECT FullName , ScreenName , IsAdult FROM People')
    rows = cursor.fetchall()
    conn.close()
    
    people = []
    for row in rows:
        full_name , screen_name , is_adult = row
        if screen_name[-5:] == 'Staff':
            identity = 'Staff'
            
        elif is_adult == 0:
            identity = 'Student'
            
        else:
            identity = 'Person'
            
        people.append({'full_name' : full_name , 'screen_name' : screen_name , 'identity' : identity})
        
    return flask.render_template('index.html' , people=people)      

if __name__ == '__main__':
       
    app.run(debug=True) 
