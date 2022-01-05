% rebase('base.tpl', title="Todo List")

<form action="/edit/{{id}}" method="post">
    <label>Task</label><br>
    <input type="text" size="100" name="task" value="{{title}}"><br>
    <label>Description</label><br>
    <textarea rows="10" cols="30" name="desc"> {{desc}} </textarea><br>
    <input type="submit" name="save" value="save">
    <input type="button" value="cancel" onclick="parent.location='/'">
</form>