function[W] = initialize_weights_3_6_sparse(X_train)
a = size(X_train);
P = a(1);
N = a(2);

p = sum(sum(X_train))*(1/(N*P));
X_train = X_train-p;
W = X_train'*X_train;
%W = rmdiag(W);
