<p>The archived/deleted items are as follows:</p>
<table border="1">
%for row in rows:
	<tr>
	<!--td>#{{row[0]}}</td-->
	<td><a href="/archive/{{row[0]}}">{{row[1]}}</a></td>
	</tr>
%end
</table>
