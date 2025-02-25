from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=192.169.0.113,1433;'
    r'DATABASE=master;'
    r'UID=sa;'requirements.txt
    r'PWD=Caracas01-;'
)
conn = pyodbc.connect(conn_str)

@app.route('/data', methods=['GET'])
def get_data():
    cursor = conn.cursor()
    cursor.execute('SELECT TOP 5 * FROM sys.tables')
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(dict(zip([column[0] for column in cursor.description], row)))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
