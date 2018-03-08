function [perchentage_match,X_out] = weight_update_batch(X_train, ite_max,W)


X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);

Xiold = X;


%Xi = sign(X*W)+ X;
%Xiold = sign(X*W);
diference = 1;


X_out = X;
for i = 1: ite_max
    if diference == 0
        break
    end
    Xiold = sign((Xiold)*(W)+Xiold);
    X_out = Xiold
    diference = sum(sum((X-Xiold)))
    
    

end
perchentage_match = sum(sum(abs(X-Xiold)')==0);






end

