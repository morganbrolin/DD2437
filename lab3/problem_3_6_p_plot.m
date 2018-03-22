
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
ratioArray = [];
Iarray_bias = []
Iarray_activity = []
for i = 1:199
    bias = 0;
    bias = i*0.005-0.5 + biasoffset;
    X_train = sign(sign(rand(300,100)-bias)+1);
    ite_max = 10;
    [activity,stabel_patterns] = weight_update_seqdata_batch_sparse_p_plot(X_train, ite_max,bias);
     ratioArray = [ratioArray stabel_patterns];
    Iarray_bias = [Iarray_bias bias];
    Iarray_activity = [Iarray_activity activity];
end

figure(1)
subplot(2,1,1)
plot(Iarray_bias,ratioArray)
title('Sparse Patterns 3.6 bias')
xlabel('Bias') % x-axis label
ylabel('Capacity') % y-axis label
subplot(2,1,2)
plot(Iarray_activity,ratioArray)
title('Sparse Patterns 3.6 activity')
xlabel('activity') % x-axis label
ylabel('Capacity') % y-axis label
%X_test = [reshape(P10,[1, 1024])];



    
