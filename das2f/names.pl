nameof(ID,Name):-
    das_fact(name,ID,Name),
    \+ das_fact(color,ID,"red").
nameof(ID,"-"):-
    das_fact(name,ID,_),
    das_fact(color,ID,"red").
nameof(ID,ID):-
    \+ das_fact(name,ID,_),
    \+ das_fact(color,ID,"red").
