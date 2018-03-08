function [weight_matrix, X_out] = weight_update_new(X_train, learning_rate, ite_max)
% Update weight matrix during Hebbian Learning
% Detailed explanation goes here

X  = X_train;
etha = learning_rate;
a = size(X_train);
P = a(1);
N = a(2);

W = zeros(N,N);

for i = 1: 1: P
    W_pat = (1/N)*(X(i,:)'*X(i,:));
    W = W + W_pat;
end

Xp = X_train;
Y = sign(X*W);

ite = 1;

 while isequal(Y,Xp) == 0 && ite < ite_max
     %this should fix it but it doesnt make a difference
     
     for i = 1: 1: P
        Y = sign(X*W);
     end
     
     Y = sign(Xp*W);
     X_out = Y
     ite = ite + 1;
 end
 
 weight_matrix = W;
 
end