function [ X_new, ite ] = update_patterns( W, X, ite_lim )

if nargin<3 
    ite_lim = 1000;
end

converged = false;
ite = 0;

while not(converged) && ite < ite_lim
    X_new = sign(X*W);
    converged = isequal(X_new, X);
    ite = ite +1;
    X = X_new;
end

end
