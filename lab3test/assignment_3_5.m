

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

P1 = reshape(P(1,:),[32 32]);
P2 = reshape(P(2,:),[32 32]);
P3 = reshape(P(3,:),[32 32]);
P4 = reshape(P(4,:),[32 32]);
P5 = reshape(P(5,:),[32 32]);
P6 = reshape(P(6,:),[32 32]);
P7 = reshape(P(7,:),[32 32]);
P8 = reshape(P(8,:),[32 32]);
P9 = reshape(P(9,:),[32 32]);
P10 = reshape(P(10,:),[32 32]);
P11 = reshape(P(11,:),[32 32]);

X_train =  [reshape(P1,[1, 1024]);reshape(P2,[1, 1024]);reshape(P3,[1, 1024]);reshape(P4,[1, 1024]);];
X_test = [reshape(P1,[1, 1024])];

W = initialize_weights(X_train);
%W = zeros(1024);
%W = add_memory(W3,X_train');
%[printo, updates] = retrieve_memory(W3, reshape(P,[1, 1024])', true, 10);






%net = newhop(X_train');
%W = net.LW{1,1};



ite_max = 3;

[ite,X_out] = weight_update_batch(X_test, ite_max,W);


%X_test = [reshape(P10,[1, 1024])];
figure(1)
%imagesc(reshape(printo, [32, 32]))
%imagesc(reshape(sign(P(1,:)*W), [32, 32]))

imagesc(reshape(X_out(1,:), [32, 32]))
figure(2)
imagesc(P1)

    