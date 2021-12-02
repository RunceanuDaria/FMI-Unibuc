
plus(0, X, X).

minus(X, Y, Z) :-
    plus(Y, Z, X).

%!  mul(?X, ?Y, ?Z)

mul(0, _, 0).
mul(s(X), Y, Z) :-
    mul(X, Y, Z1),
    plus(Y, Z1, Z).


plus(X, s(X)).

adevarat.

fals :- \+ adevarat.