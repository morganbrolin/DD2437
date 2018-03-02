function [weight_matrix, ite] = weight_update_batch(X_train, learning_rate, ite_max)
% Update weight matrix during Hebbian Learning
% Detailed explanation goes here

X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);

%W = zeros(N,N);

%W = (1/N)*(X'*X);
%W = W - diag(diag(W));
W =  rand(1024,1024)- 0.5;
RandomW = W;

Xiold = sign(X*W);

%Xi = sign(X*W)+ X;
%Xiold = sign(X*W);
ska_intevanul = sum(sum(X-Xiold));




for i = 1: ite_max
    soma = sum(sum(abs(X-Xiold)'));
    W = ((Xiold)'*(Xiold));
    Xi = sign((Xiold)*W);
    Xi = ((Xi)'*(Xi))*Xi
    Xiold = (Xi+X);
    ite = Xiold;
    
    

end
ite = sum(sum(abs(X-Xi)')==0);




weight_matrix = W;

end

