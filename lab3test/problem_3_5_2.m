
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
W = initialize_weights(X_train);
ite_max = 5;
weight_update_seqdata_batch(X_train, ite_max,W);

%X_test = [reshape(P10,[1, 1024])];


    
