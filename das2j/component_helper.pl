hasport(R):-
    das_fact(contains,R,P),
    isport(P),
    !.

isport(P):-
    das_fact(kind,P,ellipse).

hasnoparent(R):-
    das_fact(kind,R,rectangle),
    \+ das_fact(contains,_,R).

inputs(R,Inputs):-
    setof(In, inputof(R,In), Inputs),!.
inputs(_,[]).

inputof(R,In):-
    das_fact(kind,R,rectangle),
    das_fact(direction,InputID,input),
    das_fact(direct_contains,R,InputID),
    nameof(InputID,In).
    
%% nameof(ID,Name):-
%%     das_fact(name,ID,Name).
nameof(ID,ID).

outputs(R,Outputs):-
    setof(In, outputof(R,In), Outputs),!.
outputs(_,[]).

outputof(R,Out):-
    das_fact(kind,R,rectangle),
    das_fact(direction,OutputID,output),
    das_fact(direct_contains,R,OutputID),
    nameof(OutputID,Out).


children(R,Children):-setof(Child,childof(R,Child),Children),!.
children(_,[]).

childof(R,nk{name:Child,kind:Kind}):-
    das_fact(kind,R,rectangle),
    das_fact(kind,ChildID,rectangle),
    das_fact(direct_contains,R,ChildID),
    iscomponent(ChildID),
    nameof(ChildID,Child),
    kindof(ChildID,Kind).

iscomponent(X):-
    das_fact(kind,X,rectangle),
    hasport(X),
    \+ iscode(X).

iscode(X):-
    issynccode(X).

issynccode(X):-
    das_fact(kind,X,rectangle),
    \+ hasport(X),
    das_fact(color,X,"red").

kindof(ID,K):-
    das_fact(kindtype,ID,K).

