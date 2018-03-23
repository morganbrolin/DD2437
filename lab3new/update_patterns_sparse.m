function [ X_new, ite ] = update_patterns_sparse( W, X, ite_lim,bias )

if nargin<3 
    ite_lim = 1000;
end

converged = false;
ite = 0;

while not(converged) && ite < ite_lim
    theta = bias;
    X_new = 0.5+0.5*sign((X*W-theta));
    converged = isequal(X_new, X);
    ite = ite +1;
    X = X_new;
end

end