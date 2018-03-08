function [perchentage_match,X_out] = weight_update_batch(X_train, ite_max,W)


X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);

X_new = X;


%Xi = sign(X*W)+ X;
%Xiold = sign(X*W);
diference = 1;

converged = false;
X_out = X;
for i = 1: ite_max
    if converged
        break
    end
    X_new = sign((X_new)*(W)+X_new);
    X_out = X_new;
    converged = isequal(X_new, X);
  
    
    

end
perchentage_match = sum(sum(abs(X-X_new)')==0);






end
