
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
ratioArray = [0];
Iarray = [0]
for i = 1:9
    bias = 0;
    bias = i*0.1-0.5 + biasoffset;
    X_train = sign(sign(rand(300,100)-bias)+1);
    ite_max = 10;
    [activity,stabel_patterns] = weight_update_seqdata_batch_sparse_p_plot(X_train, ite_max,bias)
     ratioArray = [ratioArray stabel_patterns];
    Iarray = [Iarray i];
end
figure(1)
plot(Iarray,ratioArray)
%X_test = [reshape(P10,[1, 1024])];


    
