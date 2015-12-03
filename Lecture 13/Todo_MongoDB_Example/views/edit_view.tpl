<p>Edit the task with ID = {{id}}</p>
<form action="/edit/{{id}}" method="post">
<input type="text" name="task" value="{{task}}" size="100" maxlength="100">
<select name="status">
<option>open</option>
<option>closed</option>
</select>
<br/>
<input type="submit" name="save" value="save">
</form>