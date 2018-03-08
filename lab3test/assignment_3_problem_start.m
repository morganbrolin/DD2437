
clear
close all
clc

%% Enter memory patterns

% Training Pattern
x1 = [-1 -1 1 -1 1 -1 -1 1];
x2 = [-1 -1 -1 -1 -1 1 -1 -1];
x3 = [-1 1 1 -1 -1 1 -1 1];

X_train = [x1; x2; x3];

% New patterns which are the distorted version of the original patterns
x1d = [1 -1 1 -1 1 -1 -1 1];
x2d = [1 1 -1 -1 -1 1 -1 -1];
x3d = [1 1 1 -1 1 1 -1 1];

X_test = [x1d; x2d; x3d];

learning_rate = 1;
ite_max = 100;

[weight_matrix, ite] = weight_update(X_test, X_train, learning_rate, ite_max);
W = weight_matrix;
N = ite;
    
y1d = sign(x1d*W);
y2d = sign(x2d*W);
y3d = sign(x3d*W);

