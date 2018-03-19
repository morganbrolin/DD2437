function [ X_new, iterations, energy ] = update_patterns1_seq_E( W, X, ite_lim )

if nargin<4 
    ite_lim = 1000;
end

converged = false;
ite = 0;
iterations = [];
energy = [];
I = 1;

while  ite < ite_lim
    X_new = X;
    A = sign(X*W);
    for i = 1: length(A)
        if A(i) == 0
            A(i) = 1;
        end
    end
    X_new(I) = A(I);
    %converged = isequal(X_new, X);
    ite = ite +1;
    I = I + 1;
    I = I - floor(I/length(X_new))*length(X_new);
    X = X_new;
    iterations = [iterations; ite];
    E = -(X_new*W*X_new');
    energy = [energy; E];
end
end

