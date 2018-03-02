
clear
close all
clc

%% Load pict.dat

A = importdata('pict.dat');
P = zeros(11,1024);

for i = 1: 1: length(A)
    if (i/1024) - floor(i/1024) == 0
        k = floor(i/1024);
    else 
        k = floor(i/1024)+1;
    end
    P(k,(i-(k-1)*1024)) = A(i);
end
X_train = rand(300,100);

learning_rate = 1;
ite_max = 5;
[weight_matrix, ite] = weight_update_batch(X_train, learning_rate, ite_max);
W = weight_matrix;
%X_test = [reshape(P10,[1, 1024])];


    
