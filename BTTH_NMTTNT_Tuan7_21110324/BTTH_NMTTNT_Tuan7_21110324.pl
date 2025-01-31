/* 21110324 - Lương Đăng khôi
1.
a) Dê là động vật ăn cỏ: 
	dv_an_co(De)
b) Chó sói là động vật hung dữ: 
	dv_hung_du(Chó sói)
c) Động vật hung dữ là động vật ăn thịt: 
	dv_hung_du(X) => dv_an_thit(X)
d) Động vật ăn thịt thì ăn thịt:
	dv_an_thit(X) => an(X, thit)
e) Động vật ăn cỏ thì ăn cỏ:
	dv_an_co(X) => an(X, co)
f) Động vật ăn thịt thì ăn các động vật ăn cỏ:
	dv_an_thit(X) => an(X, dv_an_co)
g) Động vật ăn thịt và động vật ăn cỏ đều uống nước:
	dv_an_thit(X), dv_an_co(Y) => uong(X, nuoc), uong(Y, nuoc)
h) Một động vật tiêu thụ cái mà nó uống hoặc cái mà nó ăn:
	tieu_thu(X, Y, Z) => an(X, Y), uong(X, Z)
*/

% 2. Chuyển các câu trên sang Prolog
dv_an_co(de).
dv_hung_du(cho_soi).
dv_an_thit(X) :- dv_hung_du(X).
dv_an_hung_du(X) :- dv_an_thit(X).
an(X, thit) :- dv_an_thit(X).
an(X, co) :- dv_an_co(X).
an(X, Y) :- dv_an_thit(X), dv_an_co(Y).
uong(X, nuoc) :- dv_hung_du(X); dv_an_co(X).
tieu_thu(X, Y, Z) :- uong(X, Y), an(X, Z).

% Trả lời câu hỏi:  có động vật hung dữ không và nó tiêu thụ cái gì?
?- (dv_hung_du(X) -> 
    tieu_thu(X, Y, Z), tieu_thu(X, Y, U), Z\=U,
    write('Dong vat hung du: '), writeln(X), 
    write('No tieu thu: '), write(Y), write(', '), write(Z), write(', '), writeln(U)
; 
    writeln('Khong co dong vat hung du')).