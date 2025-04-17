<h1>How to use?</h1>
<p>Write in console:</p>
<p>python main.py "command" "args"</p>

<h1>Commands list</h1>
<h2>add</h2>
<h3>Arguments</h3>
<p>description</p>
<h3>Example</h3>
<code>python main.py add "Buy groceries"</code>
<p># Output: Task added successfully (ID: 0)</p>
<h2>delete</h2>
<h3>Arguments</h3>
<p>id</p>
<h3>Example</h3>
<code>python main.py delete 0</code>
<p># Output: Task 0 has been deleted</p>
<h2>update</h2>
<h3>Arguments</h3>
<p>id</p>
<h3>Example</h3>
<code>python main.py update 0 "Buy 2 groceries"</code>
<p># Output: Task 0 has been updated</p>
<h2>mark-in-progress</h2>
<h3>Arguments</h3>
<p>id</p>
<h3>Example</h3>
<code>python main.py mark-in-progress 0</code>
<p># Output: Status of Task 0 updated</p>
<h2>mark-done</h2>
<h3>Arguments</h3>
<p>id</p>
<h3>Example</h3>
<code>python main.py mark-done 0</code>
<p># Output: Status of Task 0 updated</p>
<h2>list</h2>
<h3>Arguments</h3>
<p>status(optional: todo, done, in-progress)</p>
<h3>Examples</h3>
<code>python main.py list</code>
<p># Output: Task 0: {'id': 0, 'description': 'Buy 2 groceries', 'status': 'in-progress', 'createdAt': '2025-04-17 19:38:46.693704', 'updatedAt': '2025-04-17 19:38:46.693729'}
Task 1: {'id': 1, 'description': 'Buy bread', 'status': 'todo', 'createdAt': '2025-04-17 19:43:57.501677', 'updatedAt': '2025-04-17 19:43:57.501700'}</p>
<code>python main.py list todo</code>
<p># Output: Task 1: {'id': 1, 'description': 'Buy bread', 'status': 'todo', 'createdAt': '2025-04-17 19:43:57.501677', 'updatedAt': '2025-04-17 19:43:57.501700'}</p>
