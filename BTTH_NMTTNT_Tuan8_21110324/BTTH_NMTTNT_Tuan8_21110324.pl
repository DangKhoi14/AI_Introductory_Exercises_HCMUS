% Binh nuoc Y
BY(Y, Vy, Yc) :- (Y =:= 0
            ->  Yc =:= Vy,
                Yc =:= Y
            )

% Binh nuoc X
BX(X, Vx, Xc) :- (X =:= Vx
            ->  Xc =:= 0,
                Xc =:= X
            ).

% Do nuoc
infuse(Y, X, Vx, K, Xc1, Yc1) :- (Y =\= 0, X < Vx
                                ->  K =:= min(Y, Vx - x),
                                    Xc1 =:= X + K,
                                    Yc1 =:= Y - K).

% Bat dau thuat toan
start(Vy, Vx, Y, X, Yc, Xc, K) :-
    BY(Y, Vy, Yc);
    BX(X, Vx, Xc);
    infuse(Yc, Xc, Vx, K, Xc1, Yc1).

% Dung thuat toan khi x = y = z
stop(Vy, Vx, Y, X, Z, Yc, Xc, K) :-(X =:= Z, Y =:= Z),
    BY(Y, Vy, Yc);
    BX(X, Vx, Xc);
    infuse(Yc, Xc, Vx, K, Xc1, Yc1),
    stop(Vy, Vx, Y, X, Z, Yc, Xc, K).