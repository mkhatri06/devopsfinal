from flask import Flask,jasonify

app = Flask(__name__)


courses = [ { "id":1, "title":DevOps Engineering}, "instructor": "Memoona Amjad" }, { "id":2, "title":"Software Design", "instructor": "Dr. Adnan Shah" } ] 

@app.route("/api/health", Method = "GET")
def health():
    return jasonify(stutus)

@app.route("/api/courses", Method = "GET")
def courses():
    return jasonify(courses)

@app.route("/api/courses/<int:tid>", Method = "GET")
def id(tid):
    tid = next((for s in courses, if s['id'] == tid), None)
    tid = courses[tid]
    return jasonify (tid)

if name == __main__:
    Flask(debug=True, host='0.0.0.0', PORT = 5000)

