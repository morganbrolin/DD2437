function [ X_new, iterations, energy ] = update_patterns1_E( W, X, Xp, ite_lim )

if nargin<4 
    ite_lim = 1000;
end

converged = false;
ite = 0;
iterations = [];
energy = [];

while not(converged) && ite < ite_lim
    X_new = sign(X*W);
    converged = isequal(X_new, Xp);
    ite = ite +1;
    X = X_new;
    iterations = [iterations; ite];
    E = -(X_new*W*X_new');
    energy = [energy; E];
end

end

