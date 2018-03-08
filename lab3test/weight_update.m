function [weight_matrix, ite] = weight_update(X_test, X_train, learning_rate, ite_max)
% Update weight matrix during Hebbian Learning
% Detailed explanation goes here

X  = X_train;
Xd = X_test;
etha = learning_rate;
a = size(X_train);
P = a(1);
N = a(2);

W = zeros(N,N);


W = (1/N)*X'*X;
Y = sign(X*W);
Yd = sign(Xd*W);
ite = 1;

while isequal(Yd,Y) == 0 && ite < ite_max
    delta_W = etha*(X'*Y);
    W = W + delta_W;
    Y = sign(X*W);
    Yd = sign(Xd*W);
    X = Y;
    ite = ite + 1;
end

weight_matrix = W;

end

