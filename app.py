from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_task = request.form.get('task_content')

        if new_task:
            tasks.append(new_task)

    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('home'))

if __name__ == "__main__":
        app.run(debug=True)
    