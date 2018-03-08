
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
biasoffset = 0.5;
%bias can only have values -0.49999 to + 0.49999 and then plus 0.5(offset)
%    0.4 gives 10%  0.45 gives p = 5%   0.49 gives 1%
bias = 0;
bias = bias + biasoffset
X_train = sign(sign(rand(300,100)-bias)+1);
ite_max = 10;
activity = weight_update_seqdata_batch_sparse(X_train, ite_max,bias)

%X_test = [reshape(P10,[1, 1024])];


    
