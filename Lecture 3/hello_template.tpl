%if name == 'World':
    <h1>Hello {{name}}!</h1>
    <p>This is a test.</p>
%else:
    <h1>Hello {{name.title()}}!</h1>
    <p>How are you?</p>
%end

%for i in range(0,10) :
    <p>Hello</p>
    <p>{{i}}:, Hello!</p>
%end