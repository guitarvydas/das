:- use_module(library(http/json)).
?- consult("fbhello.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das/das2f/shapes.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das/das2f/onSameDiagram.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das/das2f/inside.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das/das2f/names.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das/das2f/ports.pl").

q1(All):-
setof([A,B],das_fact(contains,A,B),All).


q2(Indirect):-
setof([C,D],das_fact(indirect_contains,C,D),Indirect).

q3(All,Indirect,Set):-
subtract(All,Indirect,Set).

query:-
    (
	q1(All),
	q2(Indirect),
	q3(All,Indirect,Set),
	json_write(user_output,Set,[width(128)])
    ;
	json_write(user_output,[],[width(128)])
        
    ).
