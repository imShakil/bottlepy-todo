% rebase('base.tpl', title='Todo List')
<div class="task_title">
    <h2>{{id}}: {{title}} </h2>
</div>
<div class="task_date">
    <strong>Posted: {{date}} </strong>
</div>
<div class="task_desc">
    <p> {{desc}}</p>
</div>
<br>
<button onclick="history.back()">Back</button><button type="button" onclick="location.href='/edit/{{id}}'">Edit</button>