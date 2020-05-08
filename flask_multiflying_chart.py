from flask import Flask, render_template

app = Flask(__name__)

n = []
for i in range(1, 10):
    for j in range(1, 10):
        n.append(("{} * {} = {}".format(i, j, i*j)))

@app.route('/')
def default_function():
    return render_template('for_loop.html', len=len(n), temp_list=n)

if __name__ == '__main__':
    app.run()