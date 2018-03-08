x1=[-1 -1 1 -1 1 -1 -1 1];
x2=[-1 -1 -1 -1 -1 1 -1 -1];
x3=[-1 1 1 -1 -1 1 -1 1];



x1d=[ 1 -1 1 -1 1 -1 -1 1];
x2d=[ 1 1 -1 -1 -1 1 -1 -1];
x3d=[ 1 1 1 -1 1 1 -1 1];


X_train =  [x1;x2;x3];
X_test = [x2d];

W = initialize_weights(X_train);
[match,X_out] = weight_update_seq(X_test, 10,W);
X_out;
binary_vector = [-1,1];
for i = 1:8
random_vector_one(i) = binary_vector(randi(2));

end
random_vector_one
W = initialize_weights(X_train);
[shit,X_out] = weight_update_seq(random_vector_one, 2,W);
X_out
sum(sum(X_out-random_vector_one))