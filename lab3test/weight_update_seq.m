function [ite,X_out] = weight_update_seq(X_train, ite_max,W)


X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);


Xiold = X;

%RandomW = W;

%Xi = sign(X*W)+ X;
%Xiold = sign(X*W);
diference = 1;


X_out = X;
Y = X_train;
for i = 1: ite_max
    if diference == 0
        break
    end
    Y = sign(Y);
    for i_n = 1 : N
        Y = sign(Y);
        sum_of_input = 0;
        for j_n = 1 : N
            sum_of_input = sum_of_input + Y(:,j_n)*W(j_n,i_n);
            
        end
        %en=size((X_train(:,i_n)))
        %tvo = size((X_train(i_n,:)))
        Y(:,i_n) = (Y(:,i_n)+Y(:,i_n)+ sum_of_input);
        Y = sign(Y);
    end
    X_out = Y;
    diference = sum(sum(X-Y));
    
    

end
ite = sum(sum(abs(X-Xiold)')==0);





end

