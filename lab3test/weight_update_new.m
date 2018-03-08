function [weight_matrix, ite] = weight_update_new(X_train, learning_rate, ite_max)
% Update weight matrix during Hebbian Learning
% Detailed explanation goes here

X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);

W = zeros(N,N);

W = (X'*X);
Y = sign(X*W);
Yold = sign(X*W);


for i = 1: ite_max
    Y = sign(Yold*W);
    W = (Yold'*Yold);
    Yold = Y;
end




ite = 0;


weight_matrix = W;

end

