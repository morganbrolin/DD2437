function[W] = initialize_weights(X_train)
W = X_train'*X_train;
W;
%W = rmdiag(W);
