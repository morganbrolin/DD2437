function [ite,X_out] = weight_update_seq(X_train, ite_max,W)


X  = X_train;
a = size(X_train);
P = a(1);
N = a(2);

converged = 1;


X_out = X;
X_new = X_train;
for i = 1: ite_max
    if converged == 0
        break
    end
    X_new = sign(X_new);
    for i_n = 1 : N
        X_new = sign(X_new);
        sum_of_input = 0;
        for j_n = 1 : N
            sum_of_input = sum_of_input + X_new(:,j_n)*W(j_n,i_n);
            
        end
        %en=size((X_train(:,i_n)))
        %tvo = size((X_train(i_n,:)))
        X_new(:,i_n) = (X_new(:,i_n)+X_new(:,i_n)+ sum_of_input);
        X_new = sign(X_new);
    end
    X_out = X_new;
    converged = isequal(X_new, X);
    
    

end
ite = sum(sum(abs(X-X_new)')==0);





end
