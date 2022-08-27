nameof(ID,Name):-
    das_fact(name,ID,Name),
    vertexisport(ID),
    \+ das_fact(color,ID,"red").
nameof(ID,"-"):-
    das_fact(name,ID,_),
    das_fact(color,ID,"red").
nameof(ID,ID):-
    diagram_fact(vertex,ID,_),
    \+ vertexisport(ID),
    \+ das_fact(color,ID,"red").
vertexisport(P):-
    das_fact(kind,P,ellipse).

