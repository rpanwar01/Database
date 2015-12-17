%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<hr/>
Hello  {{uname}} ...!!
<hr/>
<p>The items are as follows:</p>
<table border="1">
%for row in rows:
	<tr>
	<!--td>#{{row[0]}}</td-->
	<td><a href="/edit/{{row[0]}}">{{row[1]}}</a></td>
	<td><a href="/edit/{{row[0]}}">{{row[2]}}</a></td>
	<td><a href="/delete/{{row[0]}}"><img src="/static/trash.png" style="width:16px;height:16px;border:0;"/></a></td>
	</tr>
%end
</table>
<hr/>
<p>Enter a new item...</p><br/>
<form action="/new" method="post">
	To be done: <input name="task" type="text" />
	<input value="Save new item..." type="submit" />
</form>

<hr>
<p>Please click <a href='/deleteall'>here</a> to Delete all items.</p>
<hr/>

<hr>
<p>Please click <a href='/archived'>here</a> to retrieve archived items.</p>
<hr/>

<html>
  <head>
    <script type="text/javascript"
          src="https://www.google.com/jsapi?autoload={
            'modules':[{
              'name':'visualization',
              'version':'1',
              'packages':['corechart']
            }]
          }"></script>

    <script type="text/javascript">
      str1 = {{str1}}
      %if not str1:
      str1 = 0
      %end
      str2 = {{str2}}
      google.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Tasks', 'Values'],
          ['Completed Task', str1 ],
          ['Not Completed Task', str2 ]
        ]);

        var options = {
          title: 'Task Status Chart',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    %if str1 or str2:
      <div id="curve_chart" style="width: 500px; height: 300px"></div>
    %end
  </body>
</html>

<hr>
<p>Please click <a href='http://localhost:8080/'>here</a> to Signout.</p>