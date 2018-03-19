function [ X_out, ite ] = update_patterns_seq_rand( W, X, ite_lim )
a = size(X);
P = a(1);
N = a(2);
if nargin<3 
    ite_lim = 1000;
end

converged = false;
ite = 0;
X_new = X;
while not(converged) && ite < ite_lim
    ite = ite + 1;
    for i_nn = 1 : N
        x = 1:N;
        pos = randi(length(x));
        i_n = x(pos);
        sum_of_input = 0;
        for j_n = 1 : N
            sum_of_input = sum_of_input + X_new(:,j_n)*W(j_n,i_n);
            
        end
        X_new(:,i_n) = ( sum_of_input);
        X_new = sign(X_new);
    end
    converged = isequal(X_new, X);
    X_out = X_new;
    X = X_new;
end

end
