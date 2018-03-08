x1=[-1 -1 1 -1 1 -1 -1 1];
x2=[-1 -1 -1 -1 -1 1 -1 -1];
x3=[-1 1 1 -1 -1 1 -1 1];



x1d=[ 1 -1 1 -1 1 -1 -1 1];
x2d=[ 1 1 -1 -1 -1 1 -1 -1];
x3d=[ 1 1 1 -1 1 1 -1 1];


X_train =  [x1;x2;x3];
%X_test = [x1d;x2d;x3d];
X_test = X_train;

W = initialize_weights(X_train);
[ite,X_out] = weight_update_batch(X_test, 2,W);
sum(sum(X_train - X_out)== 0)