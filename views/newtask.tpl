% rebase('base.tpl', title='Todo List')
<h3>Add a new task to the Todo List</h3> <br>
<form action="/new" method="post">
    <label>Task</label><br>
    <input type="text" size="100" name="task"><br>
    <label>Description</label><br>
    <textarea rows="10" cols="30" name="desc"></textarea><br>
    <input type="submit" name="save" value="save">
    <input type="button" value="cancel" onclick="parent.location='/'">
</form>