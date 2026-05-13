from flask import Flask,jasonify



courses = [ { "id":1, "title":DevOps Engineering}, "instructor": "Memoona Amjad" }, { "id":2, "title":"Software Design", "instructor": "Dr. Adnan Shah" } ] 

@app.route("/api/health", Method = "POST")
def health():
    return(health)

@app.route("/api/courses", Method = "POST")
def courses():
    return(courses)

@app.route("/api/courses/<int:tid>", Method = "POST")
def id(tid):
    tid = next((for s in courses, if s['id'] == tid), None)
    tid = courses[tid]
    return tid

if app = (__main__):

